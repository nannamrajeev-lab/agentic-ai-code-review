# AI Code Review Agent

An agentic AI system that clones GitHub repositories, parses code using AST, and generates confidence-aware code review comments.

## Features

- GitHub repository cloning
- AST-based code parsing
- Function & class extraction
- Confidence-aware review pipeline
- Streamlit dashboard
- JSON / CSV / Markdown exports
- Responsible AI ("Verify This" low-confidence section)

## Tech Stack

- Python
- Streamlit
- GitPython
- OpenAI API
- Pydantic
- AST module

## Project Structure

```txt
agentic-ai/
│── agent/
│── ingestion/
│── parser/
│── schemas/
│── outputs/
│── temp_repos/
│── app.py
│── requirements.txt
│── README.md