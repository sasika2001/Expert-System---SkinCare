import streamlit as st
from skincare_expert_system import (
    SkincareExpert,
    UserProfile,
    FollowUp,
    get_followup_questions,
    normalize_skin_type,
    normalize_issue,
    log_interaction
)
from PIL import Image

# -------------------------
# Page config
# -------------------------
st.set_page_config(page_title="AI Skincare Expert", layout="wide")

# -------------------------
# Custom CSS
# -------------------------
st.markdown("""
<style>
/* App background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to bottom right, #FFF3E0, #E0F7FA);
}

/* Card style */
.card {
    background-color: rgba(255, 255, 255, 0.95);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 4px 4px 20px rgba(0,0,0,0.25);
    margin-bottom: 25px;
}

/* Input fields */
input, textarea {
    font-size: 22px !important;
    border-radius: 12px;
    border: 2px solid #FF80AB;
    padding: 12px;
}

/* Buttons */
.stButton>button {
    font-size: 22px !important;
    background-color: #FF4081;
    color: white;
    border-radius: 12px;
    padding: 12px 35px;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #F50057;
}

/* Headings and text */
h1,h2,h3 { font-size: 36px !important; text-shadow: 1px 1px 3px #ffffff; }
p { font-size: 22px !important; }

/* Full-width top bar */
.top-bar {
    width: 100%;
    background: linear-gradient(to right, #FFCDD2, #E0F7FA);
    padding: 15px 30px;
    border-radius: 0 0 20px 20px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    color: #000;
    font-size: 28px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Full-width top bar
# -------------------------
st.markdown('<div class="top-bar">💆‍♀️ AI Skincare Expert System 🌿</div>', unsafe_allow_html=True)

# -------------------------
# Layout columns for input and images
# -------------------------
col1, col2 = st.columns([2, 1])

# -------------------------
# Right-hand images column
# -------------------------
with col2:
    try:
        serum_img = Image.open("images/serum.jpg")
        routine_img = Image.open("images/skincare_routine.jpg")
        bottle_img = Image.open("images/skincare_bottle.jpg")

        st.image(serum_img, caption="💧 Face Serum", width='stretch')
        st.image(routine_img, caption="🌸 Skincare Routine", width='stretch')
        st.image(bottle_img, caption="🧴 Skincare Bottle", width='stretch')
    except Exception as e:
        st.error(f"Error loading images: {e}")

# -------------------------
# Left-hand main UI column
# -------------------------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h1>💆‍♀️ SkinCare Expert System 🌿</h1>", unsafe_allow_html=True)
    st.markdown("<p>Answer the questions below to receive personalised skincare recommendations.</p>", unsafe_allow_html=True)

    # Skin type and main issue
    st.markdown("<h2>📝 Skin Information</h2>", unsafe_allow_html=True)
    raw_skin = st.text_input("Enter your skin type :")
    skin = normalize_skin_type(raw_skin)
    st.markdown(f"<p>Detected skin type → <b>{skin}</b></p>", unsafe_allow_html=True)

    issue = st.text_input("Enter your main skin issue :").strip().lower()
    if issue == "":
        st.warning("Please enter a skin issue.")
        st.stop()
    issue_category = normalize_issue(issue)

    # Follow-up questions
    st.markdown("<h2>🔍 More Details</h2>", unsafe_allow_html=True)
    questions = get_followup_questions(issue_category)
    answers = {}
    if len(questions) == 0:
        st.info("This issue has no predefined follow-up questions. AI will handle it.")
    else:
        for q in questions:
            answers[q] = st.text_input(q)

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# Full-width container for recommendations
# -------------------------
if st.button("Get Skincare Recommendations"):
    engine = SkincareExpert()
    engine.reset()
    engine.declare(UserProfile(skin_type=skin, issue=issue_category))
    engine.declare(FollowUp(details=answers))
    engine.run()

    # Log interaction
    log_interaction(
        user_skin_type=skin,
        issue=issue_category,
        followup_answers=answers,
        expert_recommendation=engine.recommendations,
        ai_advice=engine.ai_advice
    )

    # -------------------------
    # Display recommendations in full page
    # -------------------------
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("<h2>🌿 Expert System Recommendation</h2>", unsafe_allow_html=True)
        for line in engine.recommendations.split('\n'):
            line = line.strip()
            if line.startswith("- Ingredients:") or line.startswith("- Products:") or line.startswith("✅"):
                st.markdown(f"**{line}**")
            elif line != "":
                st.markdown(line)

        st.markdown("<h2>🤖 Personalised Advice</h2>", unsafe_allow_html=True)
        st.markdown(f"<p>{engine.ai_advice}</p>", unsafe_allow_html=True)
        st.success("💾 Your responses have been logged.")
        st.markdown('</div>', unsafe_allow_html=True)
