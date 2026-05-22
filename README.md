# AI Code Review Agent

An **agentic AI system** that clones GitHub repositories, parses source code using **AST (Abstract Syntax Tree)**, and generates **confidence-aware code review comments** using LLM-based analysis.

The system follows a **Responsible AI approach** by exposing uncertainty through confidence scoring and a dedicated **"Verify This"** section for low-confidence findings.

---

## Features

✅ GitHub repository cloning  
✅ AST-based code parsing  
✅ Function & class extraction  
✅ Confidence-aware AI code reviews  
✅ Streamlit interactive dashboard  
✅ JSON / CSV / Markdown export support  
✅ Responsible AI via uncertainty handling  
✅ Low-confidence **"Verify This"** section  
✅ Graceful fallback mode if API quota is unavailable

---

## Tech Stack

- **Python**
- **Streamlit**
- **GitPython**
- **OpenAI API (`gpt-4o-mini`)**
- **Python AST**
- **Pydantic**
- **Pandas**

---

## Live Demo

Deployed using **Streamlit Community Cloud**.

Paste a GitHub repository URL and analyze the codebase directly.

---

## Project Structure

```txt
agentic-ai-code-review/
│── agent/
│   ├── confidence.py
│   ├── llm_client.py
│   ├── prompt_builder.py
│   └── review_pipeline.py
│
│── ingestion/
│   ├── cloner.py
│   └── file_discovery.py
│
│── parser/
│   └── ast_parser.py
│
│── outputs/
│   ├── csv_export.py
│   ├── json_export.py
│   └── markdown_export.py
│
│── schemas/
│── temp_repos/
│── app.py
│── requirements.txt
│── README.md
│── .env.example
```

---

# Quick Start Guide (Windows)

## Step 1: Open Terminal

Open:

- **PowerShell**
or
- **VS Code Terminal**

---

## Step 2: Clone Repository

```bash
git clone https://github.com/nannamrajeev-lab/agentic-ai-code-review

cd agentic-ai-code-review
```

---

## Step 3: Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 4: Activate Virtual Environment

```bash
.\venv\Scripts\activate
```

Expected terminal:

```txt
(venv) PS C:\path\to\agentic-ai-code-review>
```

---

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

Expected result:

```txt
Successfully installed ...
```

---

## Step 6: Add OpenAI API Key

Open the existing:

```txt
.env
```

file in the project root.

Replace the placeholder key with your own OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Save the file.

If the key is valid and has API quota,
the application will generate real AI code reviews.

## Step 7: Run Streamlit App

```bash
streamlit run app.py
```

Expected terminal output:

```txt
Local URL: http://localhost:8501
```

Open the URL in your browser.

---

## Step 8: Test Repository

Paste this repository into the app:

```txt
https://github.com/psf/requests
```

Click:

```txt
Analyze Repository
```

Expected behavior:

- Repository cloning
- Python file discovery
- AST parsing
- Code structure preview
- AI review generation (if API quota exists)
- Mock review fallback (if quota unavailable)
- JSON / CSV / Markdown downloads

---

## Step 9: Stop Streamlit

Press:

```txt
Ctrl + C
```

---

## Step 10: Deactivate Virtual Environment

```bash
deactivate
```

---

## Workflow

```txt
GitHub Repository
        ↓
Clone Repository
        ↓
Discover Python Files
        ↓
AST Parsing
        ↓
Prompt Generation
        ↓
LLM Review
        ↓
Confidence Scoring
        ↓
Dashboard Output
```

---

## Responsible AI Design

Every generated review contains:

- Severity rating
- Confidence score (**0–100%**)
- Reasoning
- Suggested fix

Low-confidence findings are automatically separated into:

```txt
Verify This
```

This demonstrates **uncertainty-aware AI behavior** and production-style **epistemic humility**.

---

## Notes

- The application becomes **fully functional** after inserting a valid OpenAI API key.
- If API quota is unavailable, the system automatically falls back to **mock reviews** for demonstration.
- The architecture remains identical to the production version.

---

## Customization

### Adjust Number of Review Insights

To improve performance and reduce API cost, the project has a limit to the number of code chunks analyzed[5].

You can change this manually in:

```txt
agent/review_pipeline.py
```

Look for a line 23 :

```python
 for chunk in chunks[:5]:
```

Increase the value to analyze more code sections.

Example:

```python
 for chunk in chunks[:15]:
```
 After changing the value save it( ctrl+S), run these commands in terminal ( either vs terminal or any other but keep using one terminal through the project customization):

1.git add .( space should be there between "and" and "." , press enter)
2.git commit -m "increase review scope"(press enter)
3.git push(press enter)

Now close the previous app which is loaded before the number change and revisit the app link(https://agentic-ai-code-review-fvqmaqtgkherzan7pkyvoq.streamlit.app/). 
Finally click on three dots on the right side of the link , and click on reboot. You can have customized insights.

Recommended values:

- `5` → Faster demo / lower API usage
- `10–20` → Balanced analysis
- `50+` → More comprehensive review (slower)

For large repositories, increasing this number may increase runtime and API usage.

## Deployment

Deployed using **Streamlit Community Cloud**.