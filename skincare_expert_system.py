from experta import *
from groq import Groq
from dotenv import load_dotenv
import os
import pandas as pd
import csv
from datetime import datetime

# -------------------------
# ✅ LOAD ENV AND INIT AI
# -------------------------
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

# -------------------------
# ✅ LOAD SKINCARE KNOWLEDGE CSV
# -------------------------
knowledge_df = pd.read_csv("skincare_knowledge.csv")

# -------------------------
# ✅ NORMALIZE SKIN TYPE
# -------------------------
def normalize_skin_type(text):
    if not text:
        return "unknown"
    t = text.lower().strip()
    if "comb" in t and "oily" in t:
        return "combination-oily"
    if "comb" in t and "dry" in t:
        return "combination-dry"
    if "comb" in t:
        return "combination"
    if "oily" in t:
        return "oily"
    if "dry" in t:
        return "dry"
    if "sens" in t:
        return "sensitive"
    return "unknown"

# -------------------------
# ✅ NORMALIZE ISSUE / SYNONYMS
# -------------------------
ISSUE_MAPPING = {
    "pimples": "acne",
    "whiteheads": "acne",
    "breakouts": "acne",
    "dark spots": "pigmentation",
    "melasma": "pigmentation",
    "rough skin": "texture",
    "uneven texture": "texture",
    "flaky": "dryness",
    "irritation": "redness",
    "under-eye bags": "dark_circles",
    "fine lines": "early_aging",
    "wrinkles": "early_aging",
    "oily skin": "oiliness",
    "shiny skin": "oiliness",
    "sensitive skin": "sensitivity"
}

def normalize_issue(issue):
    return ISSUE_MAPPING.get(issue.strip().lower(), issue.strip().lower())

# -------------------------
# ✅ FACT DEFINITIONS
# -------------------------
class UserProfile(Fact):
    skin_type = Field(str)
    issue = Field(str)

class FollowUp(Fact):
    details = Field(dict)

# -------------------------
# ✅ FOLLOW-UP QUESTIONS
# -------------------------
PREDEFINED_QUESTIONS = {
    "acne": [
        "What is your age ?",
        "Did you use bleaching creams? (yes/no)",
        "How long have you had acne? (weeks/months/years)",
        "Are you stressed frequently? (yes/no)",
        "Do you use heavy makeup? (yes/no)",
        "Does acne worsen during periods? (yes/no/not sure)"
    ],
    "dryness": [
        "What is your age ?"
        "Do you wash face with hot water? (yes/no)",
        "Do you use exfoliants? (yes/no)",
        "How many times do you wash face per day?",
        "Do you drink enough water? (yes/no)"
        "Do you use moisturizers regularly? (yes/no)"
    ],
    "blackheads": [
        "What is your age ?",
        "Do you use oil-based products? (yes/no)",
        "How often do you exfoliate? (never/weekly/daily)",
        "Is your T-zone oily? (yes/no)",
        "Do you have large pores? (yes/no)"
    ],
    "redness": [
        "What is your age ?",
        "Does skin burn after applying products? (yes/no)",
        "Do you react to fragrances? (yes/no)",
        "Do you use sunscreen daily? (yes/no)",
        "Do you have rosacea symptoms? (yes/no/not sure)"
    ]
}

def get_followup_questions(issue_category):
    # Return predefined questions if available
    if issue_category in PREDEFINED_QUESTIONS:
        return PREDEFINED_QUESTIONS[issue_category]
    # Otherwise, generate generic questions
    return [
        f"How long have you had {issue_category}?",
        "Do you use any skincare products currently? (yes/no)",
        "Do you have sensitive skin? (yes/no)",
        "Do you follow any skincare routine? (yes/no)"
    ]

# -------------------------
# ✅ DEFAULT RECOMMENDATION
# -------------------------
DEFAULT_RECOMMENDATION = """
✅ General Skincare Recommendations:
- Use a gentle cleanser
- Apply sunscreen daily
- Avoid over-exfoliating
- Maintain hydration
"""

# -------------------------
# ✅ GET EXPERT RECOMMENDATION FROM CSV
# -------------------------
def get_recommendation(issue, skin_type):
    issue = issue.lower()
    matched = knowledge_df[
        knowledge_df['keywords'].str.contains(issue, case=False, na=False)
    ]
    if not matched.empty:
        filtered = matched[matched['skin_type'].str.contains(skin_type, case=False, na=False)]
        if filtered.empty:
            filtered = matched[matched['skin_type'].str.contains("all", case=False, na=False)]
        rec = ""
        for _, row in filtered.iterrows():
            rec += f"✅ {row['issue_category'].capitalize()}:\n"
            rec += f"- Ingredients: {row['ingredients']}\n"
            rec += f"- Products: {row['product']}\n\n"
        return rec.strip()
    return DEFAULT_RECOMMENDATION

# -------------------------
# ✅ LOG USER INTERACTIONS
# -------------------------
def log_interaction(user_skin_type, issue, followup_answers, expert_recommendation, ai_advice):
    with open("user_history.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(),
            user_skin_type,
            issue,
            followup_answers,
            expert_recommendation.replace("\n", ";"),
            ai_advice.replace("\n", ";")
        ])

# -------------------------
# ✅ EXPERT SYSTEM ENGINE
# -------------------------
class SkincareExpert(KnowledgeEngine):

    def __init__(self):
        super().__init__()
        self.recommendations = ""
        self.ai_advice = ""

    # Generic rule for any issue
    @Rule(UserProfile(issue=MATCH.issue), FollowUp(details=MATCH.details))
    def generic_rule(self, issue, details):
        skin_type = self.facts[1]['skin_type']
        self.recommendations = get_recommendation(issue, skin_type)
        self.ask_ai(issue, details)

    # AI Call
    def ask_ai(self, issue, details):
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are a skincare expert."},
                    {
                        "role": "user",
                        "content": (
                            f"Skin issue: {issue}\n"
                            f"User details: {details}\n"
                            "Give a personalised skincare routine using only ingredients, no brand names."
                        )
                    }
                ]
            )
            self.ai_advice = response.choices[0].message.content

        except Exception as e:
            self.ai_advice = f"⚠️ AI Error: {e}"
