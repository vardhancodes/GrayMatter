import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url

load_dotenv()

def get_llm(api_key: str = None, model: str = "gpt-4o-mini", temperature: float = 0.0) -> ChatOpenAI:
    """Return a ChatOpenAI model instance, picking up api_key from arg or environment."""
    key = api_key or os.getenv("OPENAI_API_KEY")
    if not key or not key.strip():
        # Provide placeholder key so initialization does not throw at configuration time;
        # actual API invocation will surface a direct user prompt if unset.
        key = "sk-placeholder-key-for-init"
    return ChatOpenAI(
        model=model,
        temperature=temperature,
        api_key=key.strip()
    )

# 1st agent: Search Agent
def build_search_agent(llm_instance: ChatOpenAI = None, api_key: str = None, model: str = "gpt-4o-mini"):
    model_to_use = llm_instance or get_llm(api_key=api_key, model=model, temperature=0.0)
    return create_agent(
        model=model_to_use,
        tools=[web_search]
    )

# 2nd agent: Reader Agent
def build_reader_agent(llm_instance: ChatOpenAI = None, api_key: str = None, model: str = "gpt-4o-mini"):
    model_to_use = llm_instance or get_llm(api_key=api_key, model=model, temperature=0.0)
    return create_agent(
        model=model_to_use,
        tools=[scrape_url]
    )

# Writer prompt & builder
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured, comprehensive and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction & Executive Summary
- Key Findings & In-Depth Analysis (minimum 3-4 thoroughly explained points)
- Strategic Implications / Future Outlook
- Conclusion
- Cited Sources (list all URLs and sources found in the research)

Be detailed, factual, and maintain high analytical rigor."""),
])

def build_writer_chain(llm_instance: ChatOpenAI = None, api_key: str = None, model: str = "gpt-4o-mini"):
    model_to_use = llm_instance or get_llm(api_key=api_key, model=model, temperature=0.2)
    return writer_prompt | model_to_use | StrOutputParser()

# Critic prompt & builder
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp, constructive, and uncompromising research critic. Evaluate reports for rigor, clarity, and factual completeness."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact structured format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

Actionable Recommendations:
- ...

One line verdict:
..."""),
])

def build_critic_chain(llm_instance: ChatOpenAI = None, api_key: str = None, model: str = "gpt-4o-mini"):
    model_to_use = llm_instance or get_llm(api_key=api_key, model=model, temperature=0.0)
    return critic_prompt | model_to_use | StrOutputParser()

# Backwards compatibility handles
class LazyChainProxy:
    def __init__(self, builder):
        self._builder = builder
        self._instance = None

    def invoke(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._builder()
        return self._instance.invoke(*args, **kwargs)

    def __or__(self, other):
        if self._instance is None:
            self._instance = self._builder()
        return self._instance | other

writer_chain = LazyChainProxy(build_writer_chain)
critic_chain = LazyChainProxy(build_critic_chain)
