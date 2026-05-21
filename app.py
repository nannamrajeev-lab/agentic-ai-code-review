import streamlit as st

from ingestion.cloner import clone_repository
from ingestion.file_discovery import get_python_files
from parser.ast_parser import extract_code_chunks


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

# Main UI
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
        try:
            with st.spinner("Analyzing repository..."):

                # Clone repo
                repo_path = clone_repository(
                    repo_url,
                    "analyzed_repo"
                )

                # Discover files
                python_files = get_python_files(repo_path)

                total_chunks = 0
                all_chunks = []

                # Parse AST
                for file in python_files:
                    chunks = extract_code_chunks(file)
                    total_chunks += len(chunks)
                    all_chunks.extend(chunks)

            st.success("Repository analysis complete!")

            # Metrics
            st.subheader("Repository Metrics")

            col1, col2 = st.columns(2)

            col1.metric(
                "Python Files",
                len(python_files)
            )

            col2.metric(
                "Functions / Classes",
                total_chunks
            )

            # Files analyzed
            st.subheader("Files Analyzed")

            for file in python_files[:10]:
                st.write(file)

            # AST Preview
            st.subheader("Code Structure Preview")

            preview_chunks = all_chunks[:10]

            for chunk in preview_chunks:

                with st.expander(
                    f"{chunk['type'].title()}: {chunk['name']}"
                ):

                    st.write(
                        f"**File:** {chunk['file']}"
                    )

                    st.write(
                        f"**Lines:** "
                        f"{chunk['start_line']} - "
                        f"{chunk['end_line']}"
                    )

                    st.write(
                        f"**Imports:** "
                        f"{', '.join(chunk['imports'][:5])}"
                    )

                    st.code(
                        chunk["code"][:600],
                        language="python"
                    )

            # Placeholder review sections
            st.subheader("✅ Actionable Insights")

            st.info(
                "LLM review results will appear here."
            )

            with st.expander(
                "⚠ Verify This (Low Confidence Findings)"
            ):
                st.warning(
                    "Low confidence findings will appear here."
                )

        except Exception as e:
            st.error(f"Error: {e}")