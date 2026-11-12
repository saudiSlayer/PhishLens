# PhishLens – Email Phishing Analysis & Triage Tool

# Overview

PhishLens is a Python-based email analysis tool designed to identify potential phishing indicators and assist with initial security triage.

The tool examines email sender information, subject lines, message content and URLs. It assigns a risk score based on configured indicators, categorises the email by severity and provides an analyst recommendation.

The project demonstrates basic phishing analysis techniques and how automated detection rules can support a security analyst's initial investigation.

# Features

- **Sender Analysis:** Compares sender and reply-to email domains to identify mismatches.
- **Suspicious Language Detection:** Identifies configured urgency and credential-related phrases.
- **URL Detection:** Searches email content for HTTP and HTTPS links.
- **Insecure Link Detection:** Flags unencrypted HTTP links.
- **Risk Scoring:** Assigns a score out of 100 based on detected indicators.
- **Severity Classification:** Categorises emails as LOW, MEDIUM, HIGH or CRITICAL.
- **Analyst Recommendations:** Provides suggested actions based on the assigned severity.
- **Email Triage:** Processes multiple sample emails and displays individual analysis results.

# Technologies Used

- Python 3
- JSON
- Regular Expressions (`re`)
- URL Parsing (`urllib.parse`)
- Git and GitHub

# Project Structure

```text
PhishLens/
│
├── data/
│   ├── sample_emails.json
│   └── screenshots/
│       ├── critical_priority.png
│       ├── high_priority.png
│       ├── overview.png
│       └── [additional screenshots]
│
├── src/
│   └── analyzer.py
│
├── .gitignore
└── README.md
```

# How the Analysis Works

PhishLens processes each email using a set of predefined detection rules.

# 1. Sender and Reply-To Analysis

The tool extracts the sender and reply-to domains and compares them. If they do not match, the email receives 25 risk points.

# 2. Suspicious Language Detection

The analyzer searches the email subject and body for configured phrases, including:

- urgent
- immediately
- expires today
- account will be suspended
- verify your password
- confirm your credentials

Each matching phrase adds 10 points to the risk score.

# 3. URL Analysis

Regular expressions are used to identify URLs in the email content.

Detected URLs add 10 points each, up to a maximum of 20 points.

The tool also checks whether any detected URL uses HTTP rather than HTTPS. An unencrypted HTTP link adds another 15 points.

# 4. Risk Scoring and Severity

The total score is capped at 100.

| Risk Score | Severity |
|---|---|
| 0–24 | LOW |
| 25–49 | MEDIUM |
| 50–74 | HIGH |
| 75–100 | CRITICAL |

Each severity level has a corresponding analyst recommendation.

#  Installation and Usage

# Requirements

- Python 3
- Git

The project uses Python's standard library and does not require additional third-party packages.

# Clone the Repository

```bash
git clone https://github.com/saudiSlayer/PhishLens.git
```

Navigate into the project directory:

```bash
cd PhishLens
```

# Run the Analyzer

From the main project directory, execute:

```bash
python3 src/analyzer.py
```

The program loads the sample emails from `data/sample_emails.json`, analyses each email and displays its findings, risk score, severity and analyst recommendation.

# Example Results

The sample dataset contains three emails representing different risk levels.

| Email ID | Result | Risk Score |
|---|---|---:|
| EMAIL-001 | LOW | 0/100 |
| EMAIL-002 | CRITICAL | 100/100 |
| EMAIL-003 | HIGH | 65/100 |

# Screenshots

The following screenshots demonstrate the tool's output:

- **Overview:** Displays the analysis of the sample email collection.
- **Critical Priority:** Demonstrates an email receiving a CRITICAL severity rating.
- **High Priority:** Demonstrates an email receiving a HIGH severity rating.

Screenshots are available in `data/screenshots/`.

# Limitations

PhishLens uses predefined detection rules and should be treated as an initial triage aid rather than a definitive phishing detection system.

Current limitations include:

- It does not verify sender authenticity through SPF, DKIM or DMARC.
- It does not check URLs against external threat intelligence services.
- It does not analyse email attachments.
- It does not perform dynamic analysis or sandbox suspicious links.
- Its detection results depend on the configured phrases and rules.

A high risk score indicates suspicious characteristics, not confirmed malicious activity.

# Future Improvements

Potential improvements include:

- Integration with threat intelligence services.
- SPF, DKIM and DMARC analysis.
- Attachment inspection.
- More advanced URL and domain analysis.
- Exportable investigation reports.
- A graphical user interface for analysts.

# Skills Demonstrated

- Python programming and automation.
- Email security and phishing analysis.
- Regular expression pattern matching.
- URL inspection and parsing.
- Security risk scoring and classification.
- Basic incident triage and analyst reporting.
- Git and GitHub project management.
