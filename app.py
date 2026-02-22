import streamlit as st

st.set_page_config(page_title="RealityCheck AI", page_icon="💀", layout="centered")

# ---------- Minimal Clean Styling ----------
st.markdown("""
    <style>
    body {
        background-color: #ffffff;
    }
    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
    }
    .subtitle {
        text-align: center;
        color: #555;
        margin-bottom: 30px;
    }
    .result-box {
        padding: 25px;
        border-radius: 15px;
        background-color: #f5f5f7;
        text-align: center;
        margin-top: 20px;
    }
    .premium-box {
        padding: 20px;
        border-radius: 12px;
        background-color: #000000;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("<div class='main-title'>💀 RealityCheck AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Think you're the main character? Let's measure that.</div>", unsafe_allow_html=True)

# ---------- Questions ----------
questions = [
    "You imagine future success interviews in your head.",
    "You believe you're more capable than most people around you.",
    "You think failure is usually due to external factors.",
    "You expect big success without consistent boring effort.",
    "You assume people are secretly impressed by you.",
    "You mentally plan luxury purchases before earning the money.",
    "You think you're just 'waiting for your big break.'",
    "You believe rules don't fully apply to you.",
    "You compare yourself to billionaires often.",
    "You think your life could be a Netflix series."
]

scores = []

st.write("Rate each statement from 1 (Strongly Disagree) to 5 (Strongly Agree)")

for q in questions:
    score = st.slider(q, 1, 5, 3)
    scores.append(score)

# ---------- Calculate Result ----------
if st.button("Reveal My Delusion Score"):

    total_score = sum(scores)
    percentage = int((total_score / 50) * 100)

    st.markdown("---")

    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.header(f"🧠 Delusion Score: {percentage}%")

    if percentage <= 20:
        title = "🧊 Reality Anchor"
        desc = "You are painfully grounded. Possibly too grounded."
    elif percentage <= 40:
        title = "🙂 Optimistic Human"
        desc = "Healthy ambition. Slight delusion. Manageable."
    elif percentage <= 60:
        title = "😏 Controlled Delusion"
        desc = "You believe in yourself… aggressively."
    elif percentage <= 80:
        title = "🎬 Cinematic Main Character"
        desc = "You definitely hear background music when you walk."
    else:
        title = "🚀 Founder Syndrome"
        desc = "You’ve already planned your billionaire documentary."

    st.subheader(title)
    st.write(desc)

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------- Premium Section ----------
    st.markdown("### 🔓 Unlock Full Brutal Analysis — $3")

    st.markdown(
        """
        <a href="https://vennyverse4.gumroad.com/l/xztkm" target="_blank">
            <button style="
                padding: 14px 28px;
                background-color: black;
                color: white;
                font-size: 16px;
                border-radius: 10px;
                border: none;
                cursor: pointer;">
                Unlock Premium 🔥
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <div style="text-align:center; margin-top:10px; color:gray;">
    Premium includes: Deep personality breakdown, blind spots, future projection & brutal honesty mode.
    </div>
    """, unsafe_allow_html=True)