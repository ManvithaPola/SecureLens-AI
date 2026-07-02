import os
from dotenv import load_dotenv
from google import genai

from modules.rag import search_vector_store

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ---------------------------------------------
# Question Intent Keywords
# ---------------------------------------------

LOOKUP_WORDS = [
    "how many",
    "list",
    "show",
    "display",
    "count",
    "present",
    "detected",
    "found",
    "available",
]

ADVICE_WORDS = [
    "protect",
    "secure",
    "security",
    "encrypt",
    "recommend",
    "recommendation",
    "prevent",
    "mitigate",
    "risk",
    "best practice",
    "best practices",
    "how can",
    "how should",
    "why",
    "explain",
]


def ask_document(question, detections, risk):

    q = question.lower().strip()

    is_lookup = any(word in q for word in LOOKUP_WORDS)
    is_advice = any(word in q for word in ADVICE_WORDS)

    # ==================================================
    # FACTUAL LOOKUP QUESTIONS
    # ==================================================

    if is_lookup:

        # ---------------- Email ----------------

        if "email" in q:

            emails = detections.get("email", [])

            if emails:
                return (
                    f"{len(emails)} email address(es) detected.\n\n"
                    + "\n".join(emails)
                )

            return "No email addresses were detected."

        # ---------------- Phone ----------------

        if "phone" in q or "mobile" in q or "contact" in q:

            phones = detections.get("phone", [])

            if phones:
                return (
                    f"{len(phones)} phone number(s) detected.\n\n"
                    + "\n".join(phones)
                )

            return "No phone numbers were detected."

        # ---------------- PAN ----------------

        if "pan" in q:

            pans = detections.get("pan", [])

            if pans:
                return "Detected PAN Number(s):\n\n" + "\n".join(pans)

            return "No PAN numbers were detected."

        # ---------------- Aadhaar ----------------

        if "aadhaar" in q or "aadhar" in q:

            aadhaar = detections.get("aadhaar", [])

            if aadhaar:
                return "Detected Aadhaar Number(s):\n\n" + "\n".join(aadhaar)

            return "No Aadhaar numbers were detected."

        # ---------------- Credit Card ----------------

        if "credit" in q or "card" in q:

            cards = detections.get("credit_card", [])

            if cards:
                return "Detected Credit Card(s):\n\n" + "\n".join(cards)

            return "No credit card numbers were detected."

        # ---------------- Bank ----------------

        if "bank" in q or "account" in q:

            accounts = detections.get("bank_account", [])

            if accounts:
                return "Detected Bank Account(s):\n\n" + "\n".join(accounts)

            return "No bank account numbers were detected."

        # ---------------- Password ----------------

        if "password" in q:

            passwords = detections.get("password", [])

            if passwords:
                return "Detected Password(s):\n\n" + "\n".join(passwords)

            return "No passwords were detected."

        # ---------------- API Keys ----------------

        if "api" in q or "token" in q or "key" in q:

            api_keys = []

            for field in [
                "aws_access_key",
                "github_token",
                "google_api_key",
                "jwt_token",
            ]:
                api_keys.extend(detections.get(field, []))

            if api_keys:
                return "Detected API Keys/Tokens:\n\n" + "\n".join(api_keys)

            return "No API Keys or Tokens were detected."

        # ---------------- Risk ----------------

        if "risk" in q:

            return (
                f"Risk Level : {risk['risk_level']}\n"
                f"Risk Score : {risk['risk_score']}"
            )

    # ==================================================
    # AI + RAG
    # ==================================================

    retrieved_chunks = search_vector_store(question, k=5)

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are SecureLens AI, an expert Cybersecurity and Compliance Assistant.

Below is the relevant information retrieved from the uploaded document.

Document Context:

{context}

User Question:

{question}

Instructions:

- If the user is asking for cybersecurity advice, remediation,
security recommendations, compliance guidance, or best practices,
use BOTH the uploaded document and your cybersecurity expertise.

- If the user refers to detected information such as an email,
phone number, API key, password, PAN, Aadhaar, etc.,
assume it exists in the uploaded document if it is present in the
document context and provide appropriate security advice.

- Do NOT simply repeat detected values unless the user explicitly asks.

- Keep your response concise, professional and practical.

- Answer naturally like a cybersecurity assistant.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception:

        return (
            "The AI service is temporarily unavailable. "
            "Please try again after a few moments."
        )