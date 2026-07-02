"""
Keyword and Context-Based Sensitive Information Detection
"""

CONFIDENTIAL_KEYWORDS = [

    "confidential",
    "internal use only",
    "restricted",
    "classified",
    "proprietary",
    "trade secret",
    "non disclosure",
    "client confidential",
    "company confidential",
    "official use only",
    "do not distribute",
    "for internal circulation"

]

PASSWORD_KEYWORDS = [

    "password",
    "passwd",
    "pwd",
    "passcode",
    "secret",
    "secret key",
    "api secret"

]

API_KEYWORDS = [

    "api key",
    "access key",
    "aws secret",
    "aws access key",
    "google api key",
    "github token",
    "jwt token",
    "bearer token",
    "private key",
    "client secret"

]


def detect_keywords(text):

    text_lower = text.lower()

    results = {
        "confidential_information": [],
        "password_context": [],
        "api_key_context": []
    }

    for keyword in CONFIDENTIAL_KEYWORDS:

        if keyword in text_lower:
            results["confidential_information"].append(keyword)

    for keyword in PASSWORD_KEYWORDS:

        if keyword in text_lower:
            results["password_context"].append(keyword)

    for keyword in API_KEYWORDS:

        if keyword in text_lower:
            results["api_key_context"].append(keyword)
    
    for key in results:
        results[key] = sorted(list(set(results[key])))
    return results