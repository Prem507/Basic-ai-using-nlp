# 🔍 Searching Through PDFs — A Simple NLP Project

Most of us have faced this: a folder full of PDFs, and a simple question like *“What is the leave policy?”* — but no easy way to find the answer quickly.

This project is a small attempt to solve that.

It reads multiple PDF documents, breaks their text into words, and tries to find which documents are relevant to your question. It’s not “AI magic,” just a clean and honest use of basic NLP concepts — which makes it a great learning project too.

---

## 💡 What This Project Does

* Loads multiple PDF files from your system
* Extracts text from each document
* Takes a question as input from the user
* Breaks both the question and documents into words
* Finds overlapping words between them
* Shows a preview of documents that seem relevant

In short: **it helps you search documents using plain English questions.**

---

## ⚙️ How It Works (Without Jargon)

Think of it like this:

1. You ask a question
   → *“leave policy”*

2. The program splits it into words
   → `["leave", "policy"]`

3. It does the same for each PDF

4. Then it checks:

   > “Do these words appear in this document?”

5. If yes → it shows part of that document

Simple, direct, and surprisingly useful for small datasets.

---

## 🛠️ Tools Used

* **Python** – the base language
* **PyPDF2** – to read PDF files
* **NLTK** – to break text into words (tokenization)

---

## ▶️ Running the Project

### 1. Install dependencies

```bash
pip install PyPDF2 nltk
```

### 2. Run the script

```bash
python main.py
```

### 3. Ask your question

Example:

```
Ask Question: What is notice period?
```

---

## 📂 About the Data

This project works with multiple PDF files such as:

* Employee policies
* Office rules
* Travel guidelines
* Health check policies

You can replace them with your own documents — resumes, notes, books, anything.

---

## 📌 Example Output

```
Documents Loaded: 7

Ask Question: leave policy

Query Tokens: ['leave', 'policy']

Common Tokens: {'leave', 'policy'}

Relevant Section:
Employees are entitled to leave as per company policy...
```

---

## ⚠️ A Few Honest Limitations

This project is intentionally simple, so:

* It doesn’t understand meaning — only matches words
* It won’t rank results (just checks if something matches)
* Common words like “is”, “the” are not removed
* Matching is case-sensitive

So yes — it’s basic. But that’s also its strength as a learning step.

---

## 🚀 Where This Can Go Next

If you want to take this further (and you should), here’s the natural path:

* Clean text (lowercase, remove noise)
* Remove stopwords
* Apply stemming or lemmatization
* Use **TF-IDF + cosine similarity** (real ranking)
* Show exact matching sentences instead of document chunks
* Build a UI using Streamlit or Django

This project becomes much more powerful with just a few upgrades.

---

## 🎯 Why I Built This

To understand how machines can begin to “search” human language — not with heavy models, but with simple logic.

It’s a stepping stone toward:

* search engines
* chatbots
* document assistants

---

## 👨‍💻 Author

**Prem**
If you’re exploring NLP or building similar systems, this is a good place to start — and improve from.

---
