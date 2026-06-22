import streamlit as st

# Page Title
st.set_page_config(page_title="AI Medical Assistant")

st.markdown("""
<h1 style="
text-align:center;
font-size:60px;
font-weight:bold;
background: linear-gradient(90deg, #1976D2, #42A5F5);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
text-shadow: 2px 2px 5px rgba(0,0,0,0.2);
margin-bottom:10px;
">
🩺 AI Medical Assistant
</h1>

<p style="
text-align:center;
font-size:20px;
color:#555555;
margin-top:-10px;
margin-bottom:30px;
">
Ask general health-related questions and receive AI-generated guidance.
</p>
""", unsafe_allow_html=True)

# User Input
query = st.text_area(
    "Describe your symptoms or ask a health question:",
    height=200
)

# Button
if st.button("Get Advice"):

    query = query.lower()

    if "fever" in query or "cold" in query:
        advice = """
### Medical Guidance

I'm here to provide helpful information. Based on your symptoms:

**1. General Information**
A fever and cold are usually caused by a viral infection.

**2. Self-Care**
- Drink plenty of water
- Take enough rest
- Eat nutritious food

**3. Seek Medical Attention If**
- Fever lasts more than 3 days
- Difficulty breathing
- Severe weakness

**Disclaimer**
This is not a medical diagnosis. Consult a healthcare professional.
"""

    elif "headache" in query:
        advice = """
### Medical Guidance

**Possible Causes**
- Stress
- Dehydration
- Lack of sleep

**Suggestions**
- Drink water
- Rest in a quiet room
- Avoid excessive screen time

**Seek Medical Help If**
- Severe headache
- Vision problems
- Frequent headaches
"""

    else:
        advice = """
### Medical Guidance

Your symptoms could not be identified clearly.

Please provide more details such as:
- Fever
- Cough
- Headache
- Body pain
- Sore throat
"""

    st.markdown(advice) 