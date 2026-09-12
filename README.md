# 🧪 GrayMatter-Graph — Autonomous Multi-Agent Deep Research Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Orchestration-LangGraph-orange.svg)](https://python.langchain.com/docs/langgraph/)
[![Model](https://img.shields.io/badge/LLM-OpenAI%20%2F%20Gemini-green.svg)](https://platform.openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**GrayMatter-Graph** is an autonomous, stateful multi-agent deep research platform built using **LangGraph**, **LangChain**, and **Python**. Inspired by high-precision systems engineering, it replaces basic single-prompt LLM wrappers with a non-linear Directed Acyclic Graph (DAG) state machine.

The system orchestrates specialized agents—**Planner**, **Search Researcher**, **Synthesizer**, and **Fact-Checking Critic**—to perform multi-step web and academic research, aggregate findings with inline citations, and dynamically eliminate hallucinations through iterative reflection loops.

---

## 🏛️ System Architecture & Workflow

Unlike standard linear pipelines, GrayMatter-Graph manages research as a stateful graph execution flow where nodes represent autonomous agent roles and edges govern conditional routing:

```text
                     ┌────────────────────────┐
                     │      User Prompt       │
                     └───────────┬────────────┘
                                 │
                                 ▼
                     ┌────────────────────────┐
                     │     Planner Agent      │
                     │  (Deconstructs Query)  │
                     └───────────┬────────────┘
                                 │
                                 ▼
                     ┌────────────────────────┐
                     │  Search Agent Node(s)  │
                     │  (Tavily / Serper API) │
                     └───────────┬────────────┘
                                 │
                                 ▼
                     ┌────────────────────────┐
                     │    Synthesis Agent     │
                     │ (Builds Draft & Links) │
                     └───────────┬────────────┘
                                 │
                                 ▼
                     ┌────────────────────────┐
                     │  Fact-Checking Critic  │
                     └───────────┬────────────┘
                                 │
                   Are Facts Grounded & Complete?
                   ┌─────────────┴─────────────┐
               NO  │                           │ YES
                   ▼                           ▼
    ┌─────────────────────────────┐   ┌─────────────────────────┐
    │ Re-query & Search Loop      │   │ Output Final Markdown   │
    │ (Self-Corrective Reflection)│   │ Deep Research Report    │
    └─────────────────────────────┘   └─────────────────────────┘
