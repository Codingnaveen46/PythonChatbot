# Python Streamlit Chatbot

Simple chatbot app built with:
- `streamlit`
- `langchain`
- `langchain_openai`
- `langchain_core`
- `python-dotenv`

## Setup

1. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your OpenAI key:
```bash
cp .env.example .env
```
Then set `OPENAI_API_KEY` in `.env`.

4. Run the app:
```bash
streamlit run app.py
```
