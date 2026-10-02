\# PhishLens — Email Phishing Triage Tool



\## Overview



PhishLens is a Python-based email phishing triage tool designed to simulate basic Security Operations Centre (SOC) analyst workflows.



The application analyses synthetic email data, identifies configured phishing indicators, calculates a heuristic risk score, assigns a severity level, and provides an analyst recommendation.



This project is being developed as part of a cybersecurity portfolio, with a focus on email threat analysis and security alert triage.



\## Features



\- Sender and reply-to domain mismatch detection

\- Urgency and credential-related language detection

\- URL extraction and counting

\- Unencrypted HTTP link detection

\- Risk scoring from 0 to 100

\- Severity classification

\- Analyst recommendations based on severity

\- JSON-based email input



\## Technologies



\- Python

\- JSON

\- Regular Expressions

\- `urllib.parse`



\## Project Structure



```text

phishlens/

├── data/

│   └── sample\_emails.json

├── investigations/

├── reports/

├── screenshots/

│   ├── overview.png

│   ├── critical\_priority.png

│   └── high\_priority.png

├── src/

│   └── analyzer.py

├── tests/

├── README.md

└── .gitignore

```



\## Application Demonstration



\### PhishLens Overview



The application processes email records and displays its findings, risk scores, severity classifications, and analyst recommendations.



!\[PhishLens Overview](screenshots/overview.png)



\### Critical Priority Detection



This example demonstrates an email receiving a critical risk classification based on multiple configured indicators.



!\[Critical Priority Alert](screenshots/critical\_priority.png)



\### High Priority Detection



This example demonstrates how the application identifies suspicious email characteristics and recommends further analyst review.



!\[High Priority Alert](screenshots/high\_priority.png)



\## Detection Methodology



PhishLens evaluates email records using a set of rule-based indicators.



Each detected indicator contributes to a heuristic risk score, which is capped at 100.



| Risk Score | Severity |

|---|---|

| 0–24 | LOW |

| 25–49 | MEDIUM |

| 50–74 | HIGH |

| 75–100 | CRITICAL |



The application generates an analyst recommendation based on the resulting severity.



\## Running the Application



From the project root directory, run:



```powershell

python src/analyzer.py

```



\## Sample Data



The project uses synthetic email records stored in JSON format.



The sample dataset is intended for controlled testing and demonstration.



\## Limitations



PhishLens currently uses rule-based detection rather than machine learning or external threat intelligence.



The risk score is a heuristic indicator, not a definitive probability that an email is malicious.



Legitimate emails may trigger certain rules, while sophisticated phishing emails may evade the configured indicators.



Analyst review and additional context remain necessary.



\## Future Development



\- Expand phishing detection rules

\- Improve URL and domain analysis

\- Implement automated test cases

\- Generate structured investigation reports

\- Improve risk scoring and explainability

\- Introduce MITRE ATT\&CK references where applicable

\- Develop a graphical interface

\- Explore threat intelligence integration



\## Disclaimer



PhishLens is an educational cybersecurity project intended for controlled testing and portfolio demonstration.



All included email data is synthetic.



