# 🧠 GrayMatter — Autonomous Multi-Agent Deep Research Platform

> **A modular multi-agent AI research platform that autonomously discovers live web sources, synthesizes multi-document technical context, drafts rigorous structured research papers, and evaluates output quality.**

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-1.x%20Agentic%20AI-green)
![OpenAI](https://img.shields.io/badge/LLM-OpenAI%20GPT--4o-black?logo=openai)
![Tavily](https://img.shields.io/badge/Search-Tavily%20%2B%20Fallback-orange)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?logo=streamlit)
![BeautifulSoup](https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

## 🏛️ Multi-Agent Architecture & State Propagation

```text
               USER TOPIC
                   │
                   ▼
┌────────────────────────────────────────────────────────┐
│                  01. SEARCH AGENT                      │
│        (LLM + Tavily Web Search Tool Calling)          │
└──────────────────┬─────────────────────────────────────┘
                   │ Emits search snippets & discovery URLs
                   ▼
┌────────────────────────────────────────────────────────┐
│             STATE: ['search_results']                  │
└──────────────────┬─────────────────────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────────────────────┐
│                  02. READER AGENT                      │
│     (Evaluates URL Credibility + Scrape Worker)        │
└──────────────────┬─────────────────────────────────────┘
                   │ Extracts clean article bodies (strips ads/scripts)
                   ▼
┌────────────────────────────────────────────────────────┐
│             STATE: ['scraped_content']                 │
└──────────────────┬─────────────────────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────────────────────┐
│                  03. WRITER CHAIN                      │
│        (Structured Synthesis & Citation Mapping)       │
└──────────────────┬─────────────────────────────────────┘
                   │ Formats deep markdown report with executive summary
                   ▼
┌────────────────────────────────────────────────────────┐
│                 STATE: ['report']                      │
└──────────────────┬─────────────────────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────────────────────┐
│                  04. CRITIC CHAIN                      │
│      (Autonomous Peer Review & 10-Point Scoring)       │
└──────────────────┬─────────────────────────────────────┘
                   │ Scores strengths, gaps, & recommendations
                   ▼
┌────────────────────────────────────────────────────────┐
│            STATE: ['feedback'] + EXPORT                │
│    (Interactive Streamlit HUD / Downloadable .md)      │
└────────────────────────────────────────────────────────┘
```

---

## 🔄 End-to-End Execution Sequence Flow

```text
User / Streamlit UI           Search Agent               Reader Agent             Writer Chain             Critic Chain
        │                           │                          │                        │                        │
        │── Submit Topic ──────────>│                          │                        │                        │
        │                           │── Query Live Tavily/DDG ─│                        │                        │
        │                           │<── Returns 5 Snippets ───│                        │                        │
        │<── Step 1 Complete ───────│                          │                        │                        │
        │                                                      │                        │                        │
        │── Select Best Sources ──────────────────────────────>│                        │                        │
        │                                                      │── HTTP Scrape Body ────│                        │
        │                                                      │── BeautifulSoup Parse ─│                        │
        │<── Step 2 Complete ──────────────────────────────────│                        │                        │
        │                                                                               │                        │
        │── Assemble Context (Search + Raw Scrapes) ───────────────────────────────────>│                        │
        │                                                                               │── Synthesize Sections  │
        │<── Step 3 Complete (Structured Report Generated) ─────────────────────────────│                        │
        │                                                                                                        │
        │── Pass Generated Report for Peer Review ──────────────────────────────────────────────────────────────>│
        │                                                                                                        │── Evaluate Claims
        │<── Step 4 Complete (Score, Strengths, Verdict Returned) ───────────────────────────────────────────────│
```

---

## 🤖 The Four Specialized Agents

1. **🔍 Search Agent (`build_search_agent`):** Queries live search indices using Tavily / Web API to identify authoritative, high-signal technical documentation and news.
2. **📄 Reader Agent (`build_reader_agent`):** Dispatches scraper workers to parse clean body text from top discovery URLs, stripping tracking cookies, styling boilerplate, and ads.
3. **✍️ Writer Chain (`build_writer_chain`):** Synthesizes extracted primary source material into an exhaustive, structured report featuring an Executive Summary, Detailed Analysis, Strategic Implications, and Source Citations.
4. **🧐 Critic Chain (`build_critic_chain`):** Subject matter peer reviewer that grades the report on a 1-10 numerical scale, itemizing key strengths, factual blindspots, and recommended improvements.

---

## 🛠️ Resilient Dual-Layer Architecture

* **Zero-Crash Initialization:** LLM and client bindings are lazily resolved. The UI launches seamlessly without hard crashes if environment variables have not yet been exported.
* **Built-In Search Fallbacks:** If `TAVILY_API_KEY` is not provided or rate limits are reached, the system falls back to DuckDuckGo discovery, keeping research workflows functional.
* **Interactive UI Settings:** Configure OpenAI keys, Tavily keys, and select target models (`gpt-4o-mini`, `gpt-4o`, `gpt-4-turbo`) directly inside the Streamlit sidebar.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10, 3.11, or 3.12
* OpenAI API Key (required for LLM agents)
* Tavily API Key (optional, enhances live search depth)

---

### 1. Clone the repository
```bash
git clone https://github.com/vardhancodes/GrayMatter.git
cd GrayMatter
```

### 2. Set up virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables (Optional)
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```
*(Note: You can also enter API keys directly in the Streamlit application sidebar).*

---

### 4. Run the Streamlit Web Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501` to use the interactive research command center.

---

### 5. Run via Command-Line Pipeline
```bash
python pipeline.py
```

---

## 📁 Repository Structure

```text
GrayMatter/
├── app.py              # Modern dark-mode Streamlit interactive research dashboard
├── agents.py           # Agent factories (Search, Reader, Writer Chain, Critic Chain)
├── pipeline.py         # Sequential CLI orchestrator pipeline
├── tools.py            # Tavily live search, fallback web discovery, & page scrapers
├── requirements.txt    # Project dependencies
└── README.md           # Architecture and usage documentation
```

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
