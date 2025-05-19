# 🛡️ Compliance Monitoring Agent

**A modular, agentic AI tool for automating log analysis and compliance reporting.**

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![AI-Powered](https://img.shields.io/badge/AI-GPT--4-powered-critical)

---

## ✨ Overview

The Compliance Monitoring Agent is a lightweight, agentic AI system that scans system logs for security anomalies and compliance risks using GPT-4. Designed for IT teams, consultants, and SMBs, it enables fast, auditable reporting with minimal overhead.

---

## ⚙️ Features

- ✅ Automated detection of brute-force login attempts
- ✅ GPT-4 powered log summarization and risk classification
- ✅ Modular and easy to extend
- ✅ Secure email dispatch of weekly reports
- ✅ Full audit log for transparency

---

## 🧱 Architecture

```
[Log File] → [Suspicion Filter] → [LLM Analysis] → [Report Generator] → [Email Dispatcher]
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/compliance-monitoring-agent
cd compliance-monitoring-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root:

```env
LOG_FILE=sample_logs/server_log.csv
EMAIL_SENDER=your_email@example.com
EMAIL_RECIPIENT=recipient_email@example.com
SMTP_SERVER=smtp.example.com
SMTP_PASSWORD=your_password
OPENAI_API_KEY=your_openai_api_key
```

### 4. Run the Agent

```bash
python main.py
```

---

## 📊 Sample Output

```
Compliance Monitoring Report
==============================

Suspicious Log Entries:
2025-05-19 08:31:08 | jdoe | LOGIN | 192.168.1.101 | FAILED | Account temporarily locked
2025-05-19 08:32:15 | admin | LOGIN | 10.0.0.5 | FAILED | Unauthorized access attempt

Summary:
Multiple failed login attempts detected from 192.168.1.101. Admin login failed from suspicious IP. Risk: Medium. Recommend IP block and MFA enforcement.
```

---

## 🔒 Security & Privacy

- All credentials are stored in `.env` (excluded from version control).
- GPT-4 queries are stateless and logged for audit.
- No persistent storage of sensitive data.

---

## 🧠 Powered By

- [Python](https://www.python.org/)
- [LangChain](https://www.langchain.com/)
- [OpenAI](https://platform.openai.com/docs)
- [pandas](https://pandas.pydata.org/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## 🧭 Roadmap

- [ ] Add support for log rotation and archiving
- [ ] Integrate with Slack/Teams for real-time alerts
- [ ] Add HTML/PDF report output
- [ ] Dashboard UI (web-based)

---

## 👤 Author

Matthew Monroe  
Cybersecurity Consultant & Software Architect  
🌐 https://vektas.com  
📧 matthew@vektas.com  

---

## 📄 License

[MIT License](LICENSE)
