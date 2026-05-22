# AI Code Review Agent

An agentic AI system that clones GitHub repositories, parses code using AST, and generates confidence-aware code review comments.

## Features

- GitHub repository cloning
- AST-based code parsing
- Confidence-aware AI code reviews
- Streamlit dashboard
- JSON / CSV / Markdown exports
- Responsible AI via confidence scoring
- Low-confidence **"Verify This"** section

---

## Tech Stack

- Python
- Streamlit
- GitPython
- OpenAI API (`gpt-4o-mini`)
- Python AST
- Pydantic
- Pandas

---

## Live Demo

Deployed on Streamlit Community Cloud.

---

## Project Structure

```txt
agentic-ai-code-review/
│── agent/
│── ingestion/
│── parser/
│── schemas/
│── outputs/
│── temp_repos/
│── app.py
│── requirements.txt
│── README.md
│── .env.example
```

---

## Installation

```bash
git clone https://github.com/nannamrajeev-lab/agentic-ai-code-review.git

cd agentic-ai-code-review

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## OpenAI API Key Setup

This project requires an OpenAI API key for **real AI code reviews**.

### Step 1: Create `.env`

Create a file named:

```txt
.env
```

in the project root.

### Step 2: Add API key

Paste:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

You can copy:

```txt
.env.example
```

and rename it to:

```txt
.env
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Workflow

```txt
GitHub Repository
→ Clone Repository
→ Discover Files
→ AST Parsing
→ Prompt Generation
→ LLM Review
→ Confidence Scoring
→ Dashboard Output
```

---

## Notes

- The application becomes fully functional after inserting a valid OpenAI API key.
- If API quota is unavailable, the system automatically falls back to mock reviews for demonstration purposes.
- The architecture remains identical to the production version.

---

## Responsible AI

Every generated review includes:

- Severity rating
- Confidence score (0–100%)
- Low-confidence segregation (`Verify This` section)

This demonstrates uncertainty-aware AI behavior and production-style epistemic humility.

---

## Deployment

Deployed using Streamlit Community Cloud.