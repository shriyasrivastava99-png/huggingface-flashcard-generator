🤗 Hugging Face Flashcard Generator

A simple Generative AI-based flashcard generator built using **Python** and the **Hugging Face API**.

It takes a study topic or text as input and uses an AI model from Hugging Face to generate useful question-and-answer flashcards for quick learning and revision.

## ✨ Features

* 🤖 AI-generated flashcards
* 📝 Generate questions and answers from a topic or text
* 📚 Useful for study and revision
* ⚡ Simple and lightweight Python application
* 🤗 Uses Hugging Face API
* 🔐 API token is stored securely using environment variables

## 🛠️ Technologies Used

* **Python**
* **Hugging Face API**
* **Python-dotenv**

## 📂 Project Structure

```text
huggingface-flashcard/
│
├── app.py
├── README.md
└── .gitignore
```

> `venv/` is used locally for the Python environment and is not uploaded to GitHub.

## ⚙️ How It Works

```text
User enters a topic/text
        ↓
Python application
        ↓
Hugging Face API
        ↓
AI generates flashcards
        ↓
Questions and answers are displayed
```

## 🚀 How to Run

### 1. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 2. Install required packages

```bash
pip install -r requirements.txt
```

### 3. Add Hugging Face Token

Create a `.env` file and add:

```text
HF_TOKEN=your_hugging_face_token
```

Do not upload the `.env` file to GitHub.

### 4. Run the application

```bash
python app.py
```

## 🔒 Security

The Hugging Face API token is stored in an environment variable and should never be exposed or committed to GitHub.

The `.gitignore` file excludes:

```text
.env
venv/
__pycache__/
```

## 🎯 Purpose

This project demonstrates how **Generative AI and the Hugging Face API can be used with Python to create an AI-powered educational tool for generating study flashcards.**
