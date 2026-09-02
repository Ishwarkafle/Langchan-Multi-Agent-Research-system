from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
from src.tools.tools import web_search, scrape_url

print("Loading environment variables...")
load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

# ======================
# 1. Search Agent
# ======================
def create_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )

# ======================
# 2. Read / Scrape Agent
# ======================
def create_read_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )

# ======================
# 3. Writer Chain
# ======================
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. You write clear, well-structured, and insightful reports."),
    ("human", """Please write a comprehensive research report on the following topic.

Topic: {topic}

Research Material:
{research}

Structure the report as:
1. Introduction
2. Key Findings (minimum 3-5 key points)
3. Conclusion
4. References

Be detailed, factual, and professional in your writing. Use the research provided to support your report.""")
])

writer_chain = writer_prompt | llm | StrOutputParser()

# ======================
# 4. Critic Chain
# ======================
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert researcher and critical reviewer. You provide constructive, professional, and detailed feedback."),
    ("human", """Please carefully review the following research report and provide constructive feedback.

Report:
{report}

Your feedback should focus on these aspects:
1. Clarity and coherence of the writing
2. Accuracy and relevance of the information
3. Organization and structure
4. Use of evidence and sources
5. Overall effectiveness

For each aspect:
- Give a score out of 10
- Give specific comments
- Suggest improvements

At the end, give an **Overall Score out of 10** and a short final recommendation.""")
])

critic_chain = critic_prompt | llm | StrOutputParser()