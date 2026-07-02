import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_summary(text, detections, risk):

    prompt = f"""
You are SecureLens AI, an expert Cybersecurity, Privacy, and Compliance Assistant.

Your task is to analyze the uploaded document and generate a professional cybersecurity compliance report.

Document Information

Detected Sensitive Data:
{detections}

Risk Classification:
{risk}

Uploaded Document:
{text}

Instructions:

- Analyze the uploaded document carefully.
- Use both the document content and the detected sensitive information.
- Generate a concise, professional cybersecurity compliance report.
- Do NOT write long paragraphs.
- Use bullet points wherever applicable.
- Maximum 4 bullet points per section.
- Keep each bullet to one or two lines.
- Avoid repeating information.
- Mention if sensitive data types such as PAN, Aadhaar, Credit Card, API Keys, etc. are not found.
- Recommendations should be practical and actionable.
- The Executive Summary should be only 3–4 sentences.
- Do NOT generate tables.
- Do NOT include introductory or concluding statements.
- Return ONLY the report in Markdown.

Return the report in exactly this format:

# 📋 Compliance Observations

- Observation 1
- Observation 2
- Observation 3
- Observation 4

# ⚠️ Security Risks

- Risk 1
- Risk 2
- Risk 3
- Risk 4

# 🔒 Recommended Actions

- Recommendation 1
- Recommendation 2
- Recommendation 3
- Recommendation 4

# 📝 Executive Summary

Write a concise executive summary (3–4 sentences) highlighting:
- Overall document risk
- Sensitive information detected
- Key security concerns
- Recommended next steps
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text