# 🤖 AI Meeting Summarizer

An AI-powered web application that automatically **summarizes meeting transcripts and extracts action items**.
Users can upload meeting notes or files and instantly receive a **concise summary, action items, and a downloadable PDF report**.

---

## 🚀 Features

* 📝 **AI-powered summarization** of meeting transcripts
* 📂 **Upload text files** or paste meeting notes
* ✅ **Automatic action item extraction**
* 📄 **Download meeting summary as a PDF**
* 🗂 **Meeting history storage using SQLite**
* 📊 **Dashboard with meeting statistics**

---

## 🛠 Tech Stack

* **Python**
* **Flask** – Web framework
* **Hugging Face Transformers** – AI text summarization
* **SQLite** – Local database for storing meetings
* **FPDF** – PDF report generation
* **HTML / CSS** – Frontend templates

---

## 📂 Project Structure

```
ai-meeting-summarizer
│
├── app.py
├── summarizer.py
├── action_items.py
├── file_processor.py
├── pdf_generator.py
├── database.py
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   └── history.html
│
├── static/
│
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/KhushiRaghav1/ai-meeting-summarizer.git
```

Navigate into the project folder:

```
cd ai-meeting-summarizer
```

Create a virtual environment:

```
python3 -m venv venv
```

Activate it:

Mac/Linux:

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask server:

```
python app.py
```

Open in your browser:

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

Add screenshots of the app here.

Example sections:

* Homepage
* Summary output
* Dashboard
* Meeting history

---

## 📌 Future Improvements

* 🎤 Audio meeting transcription
* ☁️ Cloud database support
* 📧 Email summary reports
* 📊 Advanced analytics dashboard
* 👥 Multi-user authentication

---

## 👩‍💻 Author

**Khushi Raghav**

GitHub:
https://github.com/KhushiRaghav1

---

## ⭐ If you like this project

Give it a **star ⭐ on GitHub** to support the project!
