# -----------------------------
# Risk Weights
# -----------------------------

RISK_WEIGHTS = {
    "email": 2,
    "phone": 3,
    "employee_id": 4,
    "pan": 8,
    "aadhaar": 10,
    "credit_card": 10,
    "bank_account": 8,
    "ifsc": 5,
    "password": 10,
    "aws_access_key": 10,
    "github_token": 10,
    "google_api_key": 10,
    "jwt_token": 10,
    "confidential_information": 7,
    "password_context": 8,
    "api_key_context": 9,
}


def classify_risk(detections):

    score = 0

    detected_categories = []

    for data_type, matches in detections.items():
        count = len(matches)

        if count > 0:
            detected_categories.append(data_type)

            score += count * RISK_WEIGHTS.get(data_type, 0)

    # -----------------------------
    # Risk Level
    # -----------------------------

    if score <= 8:
        level = "Low"

    elif score <= 20:
        level = "Medium"

    else:
        level = "High"

    return {"risk_score": score, "risk_level": level, "categories": detected_categories}
