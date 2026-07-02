import re

from modules.keyword_detector import detect_keywords

# ----------------------------------------------------
# Regex Patterns for Structured Sensitive Information
# ----------------------------------------------------

PATTERNS = {

    # -----------------------------
    # Personal Information
    # -----------------------------
    "email": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    "phone": r"(?:\+91[- ]?)?[6-9]\d{9}",
    "pan": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
    "aadhaar": r"\b\d{4}\s?\d{4}\s?\d{4}\b",
    "credit_card": r"\b(?:\d[ -]?){13,16}\b",

    # -----------------------------
    # Employee Information
    # -----------------------------
    "employee_id": r"\b(?:EMP|EMPLOYEE|ID)[-_ ]?\d+\b",

    # -----------------------------
    # Banking Information
    # -----------------------------
    "bank_account": r"\b\d{11,18}\b",
    "ifsc": r"\b[A-Z]{4}0[A-Z0-9]{6}\b",

    # -----------------------------
    # API Keys
    # -----------------------------
    "aws_access_key": r"AKIA[0-9A-Z]{16}",
    "github_token": r"ghp_[A-Za-z0-9]{36}",
    "google_api_key": r"AIza[0-9A-Za-z\\-_]{35}",
    "jwt_token": r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+",

    # -----------------------------
    # Passwords
    # -----------------------------
    "password": r"(?i)(?:password|passwd|pwd)\s*[:=]\s*\S+",
}


def detect_sensitive_data(text):
    """
    Detect structured sensitive information using
    Regex + Keyword Detection.
    """

    results = {}

    # -----------------------------------------
    # Regex Detection
    # -----------------------------------------
    for name, pattern in PATTERNS.items():

        matches = re.findall(pattern, text, re.IGNORECASE)

        results[name] = sorted(list(set(matches)))

    # -----------------------------------------
    # Keyword Detection
    # -----------------------------------------
    keyword_results = detect_keywords(text)

    results.update(keyword_results)

    return results