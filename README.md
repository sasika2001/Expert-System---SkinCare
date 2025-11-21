<h1>🧴 Skin Care Expert System</h1>

<h2>🩵 Project Overview</h2>
<p>The <strong>Skin Care Expert System</strong> is an AI-powered recommendation system that provides <strong>personalized skincare advice</strong> and <strong>product suggestions</strong> based on user inputs such as <strong>skin type</strong>, <strong>skin issues</strong>, and <strong>price range</strong>.  
It uses <strong>rule-based reasoning (Experta)</strong> and <strong>Groq LLM</strong> to generate intelligent, human-like skincare advice.</p>

<blockquote>
 <em>Example:</em><br>
If a user selects <strong>“Oily Skin”</strong> and <strong>“Acne”</strong>, the system suggests suitable cleansers, moisturizers, and serums while offering professional guidance on skincare routines.
</blockquote>

<h2> Key Features</h2>
<ul>
  <li> Takes <strong>user input</strong> (skin type, issues, budget)</li>
  <li> Uses <strong>Experta</strong> for expert reasoning and rule-based decisions</li>
  <li> Integrates <strong>Groq LLM</strong> to generate personalized skincare advice</li>
  <li> Provides skincare product recommendations based on condition</li>
  <li> User-friendly and easy to extend</li>
  <li> Includes a planned Phase 2 for automatic skin issue detection from facial images</li>
</ul>

<h2> System Workflow</h2>
<ol>
  <li>User enters:
    <ul>
      <li><strong>Skin Type</strong> → Oily, Dry, or Normal</li>
      <li><strong>Skin Issue</strong> → Acne, Pimples, Blackheads, etc.</li>
      <li><strong>Price Range</strong> → Normal or Best</li>
    </ul>
  </li>
  <li>Expert system applies <strong>rules (Experta)</strong> to determine suitable skincare products.</li>
  <li>The system then calls <strong>Groq LLM</strong> to generate <strong>personalized advice</strong>.</li>
  <li>Results (products + advice) are displayed to the user.</li>
</ol>

<h2>Technologies Used</h2>
<table>
<tr><th>Category</th><th>Tools / Libraries</th></tr>
<tr><td>Programming Language</td><td>Python 3.10</td></tr>
<tr><td>Expert System Engine</td><td>Experta</td></tr>
<tr><td>AI Assistant</td><td>Groq LLM</td></tr>
<tr><td>Environment Variables</td><td>python-dotenv</td></tr>
<tr><td>Data Handling</td><td>pandas, csv</td></tr>
<tr><td>Date & Time</td><td>datetime</td></tr>
<tr><td>Interface</td><td>Console + Streamlit UI</td></tr>
<tr><td>IDE</td><td>VS Code</td></tr>
</table>

<h2> Project Folder Structure</h2>
<pre>
SkinCareExpertSystem/
│
├── skincare_expert_system.py   # Main Python script (core logic)
├── ui.py                       # Streamlit UI version
├── skincare_knowledge.csv      # Contains skincare rules and products
├── user_history.csv            # Stores past user queries & results
├── requirements.txt            # Dependencies list
├── .env                        # Groq API key (to be created)
└── README.md                   # Project documentation
</pre>

<h2>Installation & Setup (Windows)</h2>

<h3>1. Clone or Download the Project</h3>
<pre><code>git clone https://github.com/yourusername/skincare-expert-system.git
cd skincare-expert-system
</code></pre>

<h3>2. Open Command Prompt or PowerShell</h3>
<p>Press <strong>Windows + R</strong>, type <code>cmd</code>, and press Enter.<br>
Then navigate to your project folder (example):</p>
<pre><code>cd C:\Users\<YourUserName>\Desktop\SkinCareExpertSystem
</code></pre>

<h3>3. Create a Virtual Environment</h3>
<pre><code>python -m venv venv
</code></pre>

<h3>4. Activate the Virtual Environment</h3>
<pre><code>venv\Scripts\activate
</code></pre>
<p>If activated successfully, you’ll see:</p>
<pre><code>(venv) C:\Users\YourName\Desktop\SkinCareExpertSystem&gt;
</code></pre>

<h3>5. Install Required Libraries</h3>
<p>If you have a <code>requirements.txt</code> file:</p>
<pre><code>pip install -r requirements.txt
</code></pre>
<p>If not, install manually:</p>
<pre><code>pip install experta groq python-dotenv pandas streamlit
</code></pre>

<h3>6. Set Up Environment Variables</h3>
<p>Create a <code>.env</code> file in the project folder and add your Groq API key:</p>
<pre><code>GROQ_API_KEY=your_api_key_here
</code></pre>

<h2> How to Run the Project</h2>

<h3> Option 1 — Console Version</h3>
<pre><code>python skincare_expert_system.py
</code></pre>

<h3> Option 2 — Streamlit Web UI</h3>
<pre><code>streamlit run ui.py
</code></pre>
<p>This will automatically open a local web app in your browser, usually at <code>http://localhost:8501</code>.</p>

<p>Then enter:</p>
<ul>
  <li>Skin type</li>
  <li>Skin issue</li>
  <li>Price range</li>
</ul>

<p>Results include:</p>
<ul>
  <li> Recommended products</li>
  <li> Personalized skincare advice</li>
  <li> History saved to <code>user_history.csv</code></li>
</ul>

<h2> Example Output</h2>
<p><strong>Input Example:</strong></p>
<pre><code>Skin Type: Oily
Skin Issue: Acne
Price Range: Best
</code></pre>

<p><strong>Output Example:</strong></p>
<pre><code>Recommended Products:
- Cleanser: CeraVe Foaming Facial Cleanser
- Moisturizer: Neutrogena Hydro Boost Gel
- Serum: The Ordinary Niacinamide 10% + Zinc 1%

AI Advice:
"Since you have oily and acne-prone skin, use a gentle cleanser twice daily.
Avoid heavy creams and use a lightweight, oil-free moisturizer."
</code></pre>

<h2> Future Improvements</h2>
<ul>
  <li>Stage 2: Automatically detect skin type & issues from facial images using CNN + OpenCV</li>
  <li>Stage 3: Mobile app version using Flutter or React Native</li>
  <li>Stage 4: Connect to a skincare product API for live recommendations</li>
</ul>

<h2> Author</h2>
<p><strong>Sasika Sewmini</strong><br>
University of Moratuwa — 3rd Year Undergraduate<br>
<a href="https://www.linkedin.com/in/sasika-sewmini-dp-829535351">LinkedIn Profile</a><br>
Email: <a href="mailto:dpsasikapeiris@gmail.com">dpsasikapeiris@gmail.com</a></p>

<p>⭐ If you like this project, give it a star on GitHub!</p>
