# 🧠 GrayMatter

> **A multi-agent AI research system that searches the web, reads relevant sources, generates structured research reports, and critiques the final output.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Agentic%20AI-green)](https://www.langchain.com/)
[![OpenAI](https://img.shields.io/badge/LLM-OpenAI-black?logo=openai)](https://openai.com/)
[![Tavily](https://img.shields.io/badge/Search-Tavily-orange)](https://tavily.com/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?logo=streamlit)](https://streamlit.io/)

---

## 🔎 What is GrayMatter?

GrayMatter is a **multi-agent AI research system** inspired by modern deep-research workflows.

Instead of asking a single LLM to answer a question from its existing knowledge, GrayMatter divides the research process into specialized components:

```text
User Topic
    ↓
Search Agent
    ↓
Find relevant web sources
    ↓
Reader Agent
    ↓
Extract useful information
    ↓
Writer Chain
    ↓
Generate structured report
    ↓
Critic Chain
    ↓
Evaluate the report
