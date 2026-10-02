
import json
import re
from urllib.parse import urlparse

DATA_FILE = "data/sample_emails.json"

URGENT_PHRASES = [
    "urgent",
    "immediately",
    "expires today",
    "account will be suspended",
    "avoid losing access",
    "verify your password",
    "confirm your credentials"
]


def load_emails():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_domain(email_address):
    if "@" not in email_address:
        return ""

    return email_address.rsplit("@", 1)[1].lower()


def get_recommendation(severity):
    recommendations = {
        "CRITICAL": (
            "Prioritise investigation. Do not interact with links. "
            "Follow the organisation's phishing response procedure."
        ),
        "HIGH": (
            "Escalate for analyst review. Inspect sender details "
            "and URLs without opening suspicious links."
        ),
        "MEDIUM": (
            "Review sender authenticity and inspect links "
            "before taking action."
        ),
        "LOW": (
            "No immediate escalation indicated by configured rules. "
            "Review further if additional context becomes available."
        )
    }

    return recommendations[severity]


def analyze_email(email):
    findings = []
    score = 0

    sender_domain = get_domain(email["sender"])
    reply_domain = get_domain(email["reply_to"])

    text = (
        email["subject"] + " " + email["body"]
    ).lower()

    # Sender and reply-to mismatch
    if sender_domain != reply_domain:
        findings.append("Sender and reply-to domains do not match")
        score += 25

    # Urgency and credential-related language
    for phrase in URGENT_PHRASES:
        if phrase in text:
            findings.append(
                f"Urgency or credential-related phrase: '{phrase}'"
            )
            score += 10

    # URL detection
    urls = re.findall(r"https?://[^\s\"']+", text)

    if urls:
        findings.append(f"Email contains {len(urls)} URL(s)")
        score += min(len(urls) * 10, 20)

    # Unencrypted HTTP links
    for url in urls:
        if urlparse(url).scheme.lower() == "http":
            findings.append("Unencrypted HTTP link detected")
            score += 15
            break

    score = min(score, 100)

    if score >= 75:
        severity = "CRITICAL"
    elif score >= 50:
        severity = "HIGH"
    elif score >= 25:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    recommendation = get_recommendation(severity)

    return {
        "email_id": email["id"],
        "sender": email["sender"],
        "subject": email["subject"],
        "score": score,
        "severity": severity,
        "findings": findings,
        "recommendation": recommendation
    }


def display_result(result):
    print("\n========================================")
    print("             PHISHING TRIAGE")
    print("========================================")

    print(f"Email ID: {result['email_id']}")
    print(f"Sender: {result['sender']}")
    print(f"Subject: {result['subject']}")

    print(f"\nRisk Score: {result['score']}/100")
    print(f"Severity: {result['severity']}")

    print("\nFindings:")

    if result["findings"]:
        for finding in result["findings"]:
            print(f"  - {finding}")
    else:
        print("  - No configured indicators detected")

    print("\nAnalyst Recommendation:")
    print(f"  {result['recommendation']}")

    print("----------------------------------------")


def main():
    emails = load_emails()

    print("\n=== PHISHLENS: EMAIL TRIAGE ===")

    for email in emails:
        result = analyze_email(email)
        display_result(result)


if __name__ == "__main__":
    main()
