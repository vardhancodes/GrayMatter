# 🧠 GrayMatter

> **A multi-agent AI research system that searches the live web, reads relevant sources, generates structured research reports, and evaluates the generated output.**

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Agentic%20AI-green)
![OpenAI](https://img.shields.io/badge/LLM-OpenAI-black?logo=openai)
![Tavily](https://img.shields.io/badge/Search-Tavily-orange)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?logo=streamlit)
![BeautifulSoup](https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

# 📌 Overview

**GrayMatter** is a multi-agent AI research system built with **Python, LangChain, OpenAI, Tavily, BeautifulSoup, Requests, and Streamlit**.

The project is designed around a simple idea:

> Instead of asking a single language model to answer a research question from its internal knowledge, divide the research workflow into specialized components and give different agents specific responsibilities.

The system performs research in multiple stages:

```text
User Research Topic
        ↓
Search Agent
        ↓
Live Web Search
        ↓
Reader Agent
        ↓
Web Page Extraction
        ↓
Research Context
        ↓
Writer Chain
        ↓
Structured Research Report
        ↓
Critic Chain
        ↓
Report Evaluation
