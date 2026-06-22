# 🔍 CogniTrace: AI-Powered Digital Forensics & Incident Response

## 1. Project Title
**CogniTrace** – AI-Powered Digital Forensics & Incident Response (DFIR) Assistant

---

## 2. Short Overview
CogniTrace is an intelligent security analysis platform that transforms raw network logs (CSV) into actionable threat intelligence. 

It leverages **Unsupervised Machine Learning (Isolation Forest)** to detect zero-day anomalies, **SHAP (Explainable AI)** to provide mathematical reasoning behind every alert, and a **Generative AI (LLM)** engine to auto-generate professional incident response reports with ranked suspects and containment playbooks. 

The entire system is accessible through a clean, enterprise-grade **Gradio** interface, designed to reduce incident response time from hours to seconds.

---

## 3. Problem or Challenge Addressed
This project directly tackles **Theme 5: Digital Forensics Mini-Lab** and addresses three critical industry gaps:

1. **Analyst Overwhelm**: Security teams face thousands of daily alerts. Our system prioritizes threats using a **Ranked Suspects** list, so analysts act on the biggest risk first.
2. **AI Trust Deficit**: Traditional ML models are "black boxes." Analysts cannot act on alerts they don't understand. CogniTrace uses **SHAP** to explain *which features* (e.g., packet size, port number) drove the anomaly score.
3. **Slow Response Time**: Writing incident reports is tedious. Our **Generative AI** automatically produces a structured report with severity ratings and immediate containment commands (e.g., `iptables` rules), bridging the gap between detection and action.

---

## 4. Tech Stack Used

| Category | Tools & Libraries |
| :--- | :--- |
| **Frontend / UI** | Gradio, HTML/CSS (Enterprise Light Theme) |
| **Machine Learning** | Scikit-learn (Isolation Forest), StandardScaler |
| **Explainability** | SHAP (Shapley Additive Explanations) |
| **Generative AI** | Hugging Face Transformers (microsoft/phi-2) |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly (Interactive charts), Matplotlib |
| **Environment** | Python 3.9+ |
| **Deployment** | Gradio `share=True` (public link for judging) |

---

## 5. Clear Setup and Run Instructions

### Prerequisites
- Python 3.9 or higher installed on your system.
- Git (to clone the repository).

### Step-by-Step Guide

**1. Clone the Repository**
```bash
git clone https://github.com/prasanna2056525/CogniTrace-AI-Powered-Digital-Forensics-Incident-Response-DFIR-Assistant-for-cybersecurity-analysts.git
cd CogniTrace

### Team Members
Prasanna Gautam
Bidya Sharan Adhikari

###  Important Usage Notes, Limitations, and Next Steps
Usage Notes
Input Format: The tool accepts .csv or .log files with a standard tabular structure. At least 2 numeric columns are required for the ML engine.

Auto-Processing: The system automatically detects timestamp columns, flags dangerous ports (e.g., 22, 3389, 4444), and creates behavioral features (IP frequency).

Offline Capability: The core ML and SHAP engines run entirely offline. The LLM (Phi-2) requires an internet connection for the first run to download the model weights (approx. 1.5GB).

Limitations
Data Size: The current implementation is optimized for logs up to 50,000 rows. Larger files may increase processing time.

LLM Availability: If the transformers library fails to load Phi-2 (due to network or memory constraints), the system automatically falls back to a structured template-based report—ensuring the demo never breaks.

Feature Scope: The SHAP explainer focuses on the top 3 anomalies to maintain speed. Full dataset explainability is a future enhancement.
