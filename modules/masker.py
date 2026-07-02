import re


def mask_email(email):

    username, domain = email.split("@")

    if len(username) <= 3:
        masked = username[0] + "*" * (len(username) - 1)
    else:
        masked = username[:3] + "*" * (len(username) - 3)

    return masked + "@" + domain


def mask_phone(phone):

    digits = re.sub(r"\D", "", phone)

    if len(digits) >= 10:
        return digits[:5] + "*" * (len(digits) - 5)

    return phone


def mask_pan(pan):

    if len(pan) == 10:
        return pan[:3] + "*****" + pan[-2:]

    return pan


def mask_aadhaar(aadhaar):

    digits = re.sub(r"\D", "", aadhaar)

    if len(digits) == 12:
        return digits[:4] + " **** " + digits[-4:]

    return aadhaar


def mask_credit_card(card):

    digits = re.sub(r"\D", "", card)

    if len(digits) >= 16:
        return "**** **** **** " + digits[-4:]

    return card


def mask_text(text, detections):

    masked = text

    for email in detections.get("email", []):
        masked = masked.replace(email, mask_email(email))

    for phone in detections.get("phone", []):
        masked = masked.replace(phone, mask_phone(phone))

    for pan in detections.get("pan", []):
        masked = masked.replace(pan, mask_pan(pan))

    for aadhaar in detections.get("aadhaar", []):
        masked = masked.replace(aadhaar, mask_aadhaar(aadhaar))

    for card in detections.get("credit_card", []):
        masked = masked.replace(card, mask_credit_card(card))

    return masked