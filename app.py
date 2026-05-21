import streamlit as st


st.set_page_config(
    page_title="AI Code Review Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Code Review Agent")
st.caption("The Humility Agent — Confidence-Aware Code Reviews")

# Sidebar
st.sidebar.header("Settings")
confidence_threshold = st.sidebar.slider(
    "Confidence Threshold",
    min_value=0,
    max_value=100,
    value=75
)

# Repository Input
st.header("Repository Input")

st.info(
    """
Paste a GitHub repository URL and run an AI-powered
code review with confidence-aware insights.
"""
)

repo_url = st.text_input(
    "Enter GitHub Repository URL",
    placeholder="https://github.com/user/repository"
)

analyze_button = st.button("Analyze Repository")

if analyze_button:

    if not repo_url:
        st.warning("Please enter a repository URL.")

    else:
        st.success("Repository analysis started!")

        # Placeholder metrics
        st.subheader("Repository Metrics")

        col1, col2, col3 = st.columns(3)

        col1.metric("Files Analyzed", 19)
        col2.metric("Functions Reviewed", 22)
        col3.metric("Issues Found", 7)

        # High Confidence Section
        st.subheader("✅ Actionable Insights")

        st.info(
            """
            Example Issue:
            Performance issue in auth.py

            Confidence: 88%
            Severity: Medium
            """
        )

        # Low Confidence Section
        with st.expander("⚠ Verify This (Low Confidence Findings)"):

            st.warning(
                """
                Example Issue:
                Possible security issue

                Confidence: 48%
                Human verification recommended.
                """
            )