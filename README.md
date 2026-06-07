# 🛡️ Enterprise AI Expense Auditor

**Built for the Microsoft Build AI Hackathon 2026**

## 🚀 The Problem
Manual expense auditing is a massive bottleneck for enterprise finance teams. It is slow, prone to human error, and often fails to catch subtle compliance violations or fraudulent claims.

## 💡 The Solution
The Enterprise AI Expense Auditor is an intelligent, scalable Multi-Agent system powered by the **Microsoft AI Stack**. It automates the ingestion, analysis, and approval/rejection of expense reports based on strict corporate policies.

### ⚙️ System Architecture (Multi-Agent Workflow)
We utilize **Microsoft AutoGen** to orchestrate a team of specialized AI agents:
1. **Admin Proxy:** Ingests the expense document and initiates the workflow.
2. **Finance Auditor Agent:** Scrutinizes expenses for anomalies, missing documentation, and potential fraud.
3. **Compliance Officer Agent:** Cross-references the Auditor's findings against corporate policies to make a final binding decision (Approve/Reject).

### 🛠️ Tech Stack
* **AI Orchestration:** Microsoft AutoGen
* **LLM Engine:** GPT-4o (via GitHub Models / Azure Inference API)
* **Frontend/UX:** Streamlit (For rapid prototyping and clean UX)
* **Language:** Python 3.x

## 💻 Setup & Installation (Local Development)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/build-ai-auditor.git](https://github.com/your-username/build-ai-auditor.git)
   cd build-ai-auditor