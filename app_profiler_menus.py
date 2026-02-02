import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="William's Portfolio", layout="wide")

# ---- Global styling (colors + spacing) ----
st.markdown(
    """
    <style>
      /* Page layout */
      .main .block-container {
        padding-top: 2.2rem;
        padding-bottom: 2.2rem;
        max-width: 1200px;
      }

      /* Sidebar */
      div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0b1020 0%, #101827 100%);
        border-right: 1px solid rgba(255, 255, 255, 0.08);
      }
      div[data-testid="stSidebar"] * {
        color: #e5e7eb !important;
      }
      div[data-testid="stSidebar"] .stRadio > div {
        padding: 0.25rem 0.25rem 0.75rem 0.25rem;
      }

      /* Typography */
      h1, h2, h3 {
        letter-spacing: -0.02em;
      }

      /* Card styling */
      .card {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.10);
        border-radius: 18px;
        padding: 18px 18px 14px 18px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.18);
      }
      .kicker {
        font-size: 0.85rem;
        opacity: 0.8;
        margin-bottom: 0.25rem;
      }
      .value {
        font-size: 1.05rem;
        font-weight: 600;
        line-height: 1.2;
      }
      .muted {
        opacity: 0.9;
      }
      .hr {
        height: 1px;
        background: rgba(255,255,255,0.10);
        margin: 0.8rem 0;
      }

      /* Links */
      a {
        color: #38bdf8 !important;
        text-decoration: none;
      }
      a:hover {
        text-decoration: underline;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Profile", "Education🎓", "Experience💼", "Contact📞"],
)

# Sections based on menu selection
if menu == "Profile":
    st.title("Profile")

    # Collect basic information
    name = "William Mohlahlane"
    field = "Conputer Science"
    institution = "University of the Western Cape"

    # Display basic profile information (same content, nicer layout)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            f"""
            <div class="card">
              <div class="kicker">Name</div>
              <div class="value">{name}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f"""
            <div class="card">
              <div class="kicker">Field</div>
              <div class="value">{field}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            f"""
            <div class="card">
              <div class="kicker">Institution</div>
              <div class="value">{institution}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

    st.subheader("About Me")
    st.markdown(
        """
        <div class="card">
          <div class="muted">
            I am a highly motivated and adaptable student who thrives in new environments and embraces challenges head-on. I have a strong passion for learning, quickly picking up new skills and continuously pushing myself to grow. Reliable, curious, and people-focused, I bring energy, commitment, and a willingness to go the extra mile in everything I do.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Skills💡")
    st.markdown(
        """
        <div class="card">
          <div class="muted">
            <ul style="margin-top: 0.2rem; margin-bottom: 0.2rem;">
              <li>Programming Languages: Python, Java, C++</li>
              <li>Web Development: HTML, CSS, JavaScript</li>
              <li>Data Analysis: Pandas, NumPy, Matplotlib</li>
              <li>Version Control: Git, GitHub</li>
              <li>Problem-Solving and Critical Thinking</li>
            </ul>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif menu == "Education🎓":
    st.title("Education🎓")

    st.markdown(
        """
        <div class="card">
          <div class="kicker">Matric</div>
          <div class="value">Zonkizizwe Secondary School</div>
          <div class="kicker">Jan 2021 - Nov 2021</div>
          <div class="hr"></div>
          <div class="kicker">BSc Computer Sciences[cum laude]</div>
          <div class="value">University of the Western Cape</div>
            <div class="kicker">Feb 2022 - Nov 2025</div>
          <div class="hr"></div>
          <div class="kicker">BSc(hons) Computer Science</div>
          <div class="value">University of the Western Cape</div>
            <div class="kicker">Feb 2026 - Present</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif menu == "Experience💼":
    st.title("Experience💼")

    st.markdown(
        """
        <div class="card">
          <div class="kicker">Mathematics tutor</div>
          <div class="value">University of the Western Cape </div>
          <div class="kicker">Feb 2025 - Nov 2025</div>
          <div class="hr"></div>
          <div class="kicker">CHPC SCC - Participant</div>
          <div class="value">CHPC Student Cluster Competition, Counsil for Scientific  and Industrial Research (CSIR)</div>
            <div class="kicker">Jun 2024 - Dec 2024</div>
          <div class="hr"></div>
          <div class="kicker">UWC IT Society mentor</div>
          <div class="value">University of the Western Cape IT Society</div>
          <div class="kicker">Jul 2025 - Nov 2025</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif menu == "Contact📞":
    # Add a contact section
    st.header("Contact Information📞")
    email = "mohlahlanewilliam@gmail.com"
    linkedin = "www.linkedin.com/in/william-mohlahlane-004977343"
    github = "https://github.com/mohhlahlanewilliam"

    # Same content, just styled + clickable where possible
    st.markdown(
        f"""
        <div class="card">
          <ul style="margin-top: 0.2rem; margin-bottom: 0.2rem;">
            <li>You can reach me at <a href="mailto:{email}">{email}</a>.</li>
            <li>My linkedin profile: <a href="https://{linkedin}">{linkedin}</a></li>
            <li>My GitHub profile: <a href="{github}">{github}</a></li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
