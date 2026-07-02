# 🔒 SecureLens AI

### AI-Powered Cybersecurity & Compliance Document Analyzer

SecureLens AI is an intelligent cybersecurity assistant that automatically analyzes uploaded documents for sensitive information, evaluates compliance risks, generates AI-powered security reports, performs document masking, supports OCR for image-based documents, and enables natural language interaction through Retrieval-Augmented Generation (RAG).

The system combines traditional pattern matching, OCR, vector search, and Generative AI to help organizations identify confidential information and improve document security before sharing or storing files.

---

# 🚀 Live Demo

**Public Deployment:**  
👉 https://securelens-ai-production.up.railway.app 

---

# 🎯 Project Objective

Organizations frequently share resumes, contracts, reports, invoices, identity documents, and confidential files without realizing that they may contain personally identifiable information (PII) or sensitive credentials.

SecureLens AI aims to:

- Detect confidential and sensitive information
- Assess cybersecurity and compliance risks
- Generate AI-powered compliance reports
- Protect sensitive information through masking
- Allow users to ask questions about uploaded documents using AI
- Support both text-based and scanned documents

---

# ✨ Features

### 📄 Multi-format Document Support

- PDF Documents
- TXT Files
- CSV Files
- Image Files (PNG, JPG, JPEG) using OCR

---

### 🔍 Sensitive Data Detection

Automatically detects:

- Email Addresses
- Phone Numbers
- PAN Numbers
- Aadhaar Numbers
- Credit Card Numbers
- Employee IDs
- Bank Account Numbers
- IFSC Codes
- API Keys
- GitHub Tokens
- JWT Tokens
- Passwords
- Confidential Keywords

---

### 🤖 AI Compliance Report

Google Gemini generates:

- Compliance observations
- Security risks
- Recommended actions
- Executive summary

---

### 📊 Risk Classification

Documents are automatically classified into:

- Low Risk
- Medium Risk
- High Risk

based on detected sensitive information.

---

### 💬 AI Compliance Chatbot (RAG)

Users can ask questions like:

- Summarize this document
- How many emails are present?
- List all sensitive information
- What security risks exist?
- What should I improve?

The chatbot combines:

- Retrieval-Augmented Generation (RAG)
- FAISS Vector Database
- Sentence Transformers
- Google Gemini

---

### 🔐 Data Masking

Automatically masks sensitive information such as:

```
Email:
john****@gmail.com

Phone:
98******21

PAN:
ABCDE****F
```

---

### 🖼 OCR Support

Image-based documents are processed using EasyOCR.

Example:

- Aadhaar Card
- Identity Cards
- Scanned Documents

---

# 💼 Use Cases

- Resume Security Analysis
- Employee Document Screening
- Compliance Audits
- Secure Document Sharing
- HR Verification
- Identity Document Analysis
- Cybersecurity Assessments
- Data Privacy Compliance

---

# ✅ Advantages

- Detects sensitive information automatically
- Reduces accidental data exposure
- AI-generated cybersecurity insights
- Supports scanned image documents
- Interactive AI assistant
- Easy-to-use web interface
- Fast semantic document search
- Privacy-aware document masking

---

# 🏗 System Architecture

```
                User
                  │
                  ▼
        Upload Document
                  │
                  ▼
        Document Parser
       (PDF / TXT / CSV / OCR)
                  │
                  ▼
     Sensitive Data Detection
      (Regex + Keywords)
                  │
                  ▼
      Risk Classification
                  │
                  ▼
       AI Compliance Report
        (Google Gemini)
                  │
                  ▼
      FAISS Vector Database
                  │
                  ▼
    RAG AI Compliance Chatbot
                  │
                  ▼
        Data Masking Module
                  │
                  ▼
          User Dashboard
```

---

# 🧠 AI / ML Approach Used

SecureLens AI combines multiple AI techniques to provide intelligent document analysis.

### 1. OCR

EasyOCR extracts text from image-based documents.

---

### 2. Sensitive Data Detection

Regex-based detection identifies structured information including:

- Emails
- Phone Numbers
- PAN
- Aadhaar
- Credit Cards
- API Keys
- Passwords

Keyword-based detection identifies confidential terminology.

---

### 3. Risk Assessment

Each detected entity is assigned a weighted score.

Overall document risk is classified into:

- Low
- Medium
- High

---

### 4. Retrieval-Augmented Generation (RAG)

The uploaded document is:

- Split into chunks
- Embedded using Sentence Transformers
- Stored in a FAISS vector database

When the user asks a question:

- Relevant document chunks are retrieved
- Sent to Google Gemini
- Gemini generates context-aware responses

---

### 5. AI Compliance Report

Google Gemini analyzes:

- Compliance observations
- Security risks
- Recommendations
- Executive summary

---

# 💻 Tech Stack

## Frontend

- HTML5
- CSS3
- JavaScript
- Tailwind CSS

---

## Backend

- Flask
- Python

---

## AI / ML

- Google Gemini API
- Sentence Transformers
- FAISS
- EasyOCR

---

## Libraries

- pdfplumber
- pandas
- NumPy
- python-dotenv

---

## Deployment

- Railway

---

# 📸 Output Screens

Include screenshots of:

- Home Page

```
screenshots/home.png
```

---

- Document Upload

```
screenshots/upload.png
```

---

- Sensitive Information Detection

```
screenshots/detection.png
```

---

- AI Compliance Report

```
screenshots/report.png
```

---

- AI Chatbot

```
screenshots/chatbot.png
```

---

- Data Masking

```
screenshots/masking.png
```

---

# ⚠ Challenges Faced

During development, several technical challenges were encountered:

- Extracting text from scanned image documents.
- Improving sensitive data detection accuracy while minimizing false positives.
- Implementing Retrieval-Augmented Generation (RAG) for document-specific question answering.
- Managing large AI dependencies such as EasyOCR and Sentence Transformers.
- Optimizing deployment due to memory constraints on cloud hosting platforms.
- Designing a responsive and intuitive cybersecurity dashboard.
- Ensuring AI responses remain context-aware and document-specific.

---

# 🚀 Future Improvements

- Multi-document support
- PDF download of masked documents
- Automatic document redaction
- Compliance support for GDPR, HIPAA, ISO 27001, PCI-DSS
- User authentication
- Document history dashboard
- Batch document analysis
- Cloud storage integration
- Role-based access control
- Real-time compliance monitoring
- AI-powered policy recommendation engine

---

# ⚙ Installation & Local Setup

## 1. Clone the Repository

```bash
git clone https://github.com/ManvithaPola/SecureLens-AI.git

cd SecureLens-AI
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create Gemini API Key

Visit:

https://aistudio.google.com/app/apikey

Create a free Gemini API Key.

---

## 5. Create a `.env` File

Inside the project root create:

```
.env
```

Add:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 6. Run the Application

```bash
python app.py
```

The application will start at:

```
http://127.0.0.1:5000
```

---

# 📁 Project Structure

```
SecureLens-AI/

│── app.py
│── requirements.txt
│── README.md
│── .env
│
├── modules/
│      parser.py
│      detector.py
│      classifier.py
│      chat.py
│      rag.py
│      summarizer.py
│      masker.py
│      keyword_detector.py
│      ocr.py
│
├── templates/
│
├── uploads/
│
└── screenshots/
```

---

# 👩‍💻 Author

**Manvitha Pola**

Artificial Intelligence & Machine Learning Engineer


---

# 📜 License

This project is intended for educational and research purposes.
