import streamlit as st

from ingestion.cloner import clone_repository
from ingestion.file_discovery import get_python_files
from parser.ast_parser import extract_code_chunks

from outputs.json_export import export_to_json
from outputs.csv_export import export_to_csv
from outputs.markdown_export import export_to_markdown

from agent.review_pipeline import run_review_pipeline


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

analyze_button = st.button(
    "Analyze Repository"
)


if analyze_button:

    if not repo_url:
        st.warning(
            "Please enter a repository URL."
        )

    else:
        try:
            with st.spinner(
                "Analyzing repository..."
            ):

                # Clone repo
                repo_path = clone_repository(
                    repo_url,
                    "analyzed_repo"
                )

                # Discover files
                python_files = (
                    get_python_files(
                        repo_path
                    )
                )

                total_chunks = 0
                all_chunks = []

                # Parse AST
                for file in python_files:

                    chunks = (
                        extract_code_chunks(
                            file
                        )
                    )

                    total_chunks += (
                        len(chunks)
                    )

                    all_chunks.extend(
                        chunks
                    )

                # Review pipeline
                review_results = (
                    run_review_pipeline(
                        all_chunks
                    )
                )

            st.success(
                "Repository analysis complete!"
            )

            # Metrics
            st.subheader(
                "Repository Metrics"
            )

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
            st.subheader(
                "Files Analyzed"
            )

            for file in python_files[:10]:
                st.write(file)

            # AST Preview
            st.subheader(
                "Code Structure Preview"
            )

            preview_chunks = (
                all_chunks[:10]
            )

            for chunk in preview_chunks:

                with st.expander(
                    f"{chunk['type'].title()}: "
                    f"{chunk['name']}"
                ):

                    st.write(
                        f"**File:** "
                        f"{chunk['file']}"
                    )

                    st.write(
                        f"**Lines:** "
                        f"{chunk['start_line']}"
                        f" - "
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

            # High confidence reviews
            st.subheader(
                "✅ Actionable Insights"
            )

            high_confidence = [
                c
                for c in review_results[
                    "comments"
                ]
                if not c["verify"]
            ]

            if high_confidence:

                for review in (
                    high_confidence
                ):

                    st.success(
                        f"""
Issue:
{review['issue']}

File:
{review['file']}

Confidence:
{review['final_confidence']}%
"""
                    )

            else:
                st.info(
                    "No high confidence "
                    "issues found."
                )

            # Low confidence reviews
            with st.expander(
                "⚠ Verify This "
                "(Low Confidence Findings)"
            ):

                low_confidence = [
                    c
                    for c in review_results[
                        "comments"
                    ]
                    if c["verify"]
                ]

                if low_confidence:

                    for review in (
                        low_confidence
                    ):

                        st.warning(
                            f"""
Issue:
{review['issue']}

File:
{review['file']}

Confidence:
{review['final_confidence']}%
"""
                        )

                else:
                    st.info(
                        "No low confidence "
                        "findings."
                    )

            # Export section
            st.subheader(
                "Download Results"
            )

            json_file = (
                export_to_json(
                    review_results
                )
            )

            csv_file = (
                export_to_csv(
                    review_results
                )
            )

            md_file = (
                export_to_markdown(
                    review_results
                )
            )

            col1, col2, col3 = (
                st.columns(3)
            )

            with open(
                json_file,
                "rb"
            ) as file:

                col1.download_button(
                    "Download JSON",
                    file,
                    file_name=json_file
                )

            with open(
                csv_file,
                "rb"
            ) as file:

                col2.download_button(
                    "Download CSV",
                    file,
                    file_name=csv_file
                )

            with open(
                md_file,
                "rb"
            ) as file:

                col3.download_button(
                    "Download Markdown",
                    file,
                    file_name=md_file
                )

        except Exception as e:
            st.error(f"Error: {e}")