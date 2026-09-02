# 🎓 Complete Beginner's Guide to Multi-Agent Research System
## Learn Agentic AI By Understanding This Project

---

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [What is Agentic AI?](#2-what-is-agentic-ai)
3. [Project Structure Explained](#3-project-structure-explained)
4. [Understanding Imports](#4-understanding-imports)
5. [Deep Dive: agents.py](#5-deep-dive-agentspy)
6. [Deep Dive: pipeline.py](#6-deep-dive-pipelinepy)
7. [How Tools Work](#7-how-tools-work)
8. [Data Flow Between Agents](#8-data-flow-between-agents)
9. [Agent vs Chain](#9-agent-vs-chain)
10. [How to Run the Project](#10-how-to-run-the-project)
11. [Key Concepts You'll Learn](#11-key-concepts-youll-learn)
12. [Next Steps to Improve Your Skills](#12-next-steps-to-improve-your-skills)

---

## 1. Project Overview

### What Does This Project Do?

Imagine you want to research a topic like "Latest Nepal Floods News". Instead of manually:
1. Searching Google for information
2. Reading articles
3. Writing a summary
4. Getting someone to review your work

This project **automates all of it** using AI agents!

### The Simple Flow:
```
Your Question
    ↓
Search Agent (finds info) → Read Agent (reads articles) → Writer Agent (writes report) → Critic Agent (reviews it)
    ↓
Professional Report + Feedback
```

### Real-World Example:
Input: "What is the impact of AI on Education?"
Output: 
- Comprehensive research report
- Critique with scores and suggestions for improvement

---

## 2. What is Agentic AI?

### Traditional Programming vs. Agentic AI

**Traditional Programming:**
```
You write code → Code does exactly what you tell it → Result
```

**Agentic AI:**
```
You give AI a goal + tools → AI decides what to do → AI uses tools intelligently → Result
```

### Key Differences Explained:

| Aspect | Traditional Code | Agentic AI |
|--------|-----------------|-----------|
| **Control** | You control every step | AI decides the steps |
| **Flexibility** | Follow fixed rules | Adapt to different situations |
| **Tools** | No tools | Has tools to solve problems |
| **Decision Making** | None | AI makes decisions |

### What are Agents?

Think of an agent as **a smart robot** that:
1. **Understands a goal** ("Research this topic")
2. **Has tools** (Google search, website reader)
3. **Thinks independently** (decides which tools to use)
4. **Takes actions** (uses tools to gather info)
5. **Achieves the goal** (completes the task)

### Analogy:
A **regular function** is like a recipe: "Mix A + B = C"

An **agent** is like a chef: "Make something delicious" - the chef decides what ingredients to use and how to combine them.

---

## 3. Project Structure Explained

```
Langchan-Multi-Agent-Research-system/
│
├── main.py                    # Entry point (CLI version)
├── app.py                     # Web interface (Streamlit)
├── requirements.txt           # List of libraries needed
├── README.md                  # Project documentation
│
└── src/                       # Source code folder
    │
    ├── agents/
    │   ├── __init__.py        # (Tells Python this is a package)
    │   └── agents.py          # WHERE AGENTS ARE DEFINED
    │
    ├── tools/
    │   ├── __init__.py
    │   └── tools.py           # WHERE TOOLS ARE DEFINED
    │
    └── pipeline/
        ├── __init__.py
        └── pipeline.py        # WHERE EVERYTHING WORKS TOGETHER
```

### Breaking Down Each Part:

#### **src/agents/agents.py** - The Brain
- **Contains**: 4 different agents (Search, Read, Writer, Critic)
- **Purpose**: Defines how each agent behaves
- **Analogy**: Like defining different job titles (Detective, Journalist, Editor, Reviewer)

#### **src/tools/tools.py** - The Tools
- **Contains**: Functions that agents can use
- **Purpose**: Provides abilities like searching web, reading URLs
- **Analogy**: Like giving tools to workers (hammer for construction worker, pen for writer)

#### **src/pipeline/pipeline.py** - The Workflow
- **Contains**: The main process that runs all agents in order
- **Purpose**: Coordinates agents so they work together
- **Analogy**: Like a project manager organizing a team workflow

#### **main.py** - Simple Command Line
- **Purpose**: Simple way to run the system from terminal
- **Usage**: `python main.py`

#### **app.py** - Beautiful Web Interface
- **Purpose**: Allows non-technical people to use the system
- **Usage**: `streamlit run app.py`

---

## 4. Understanding Imports

Let's break down what each import does:

### In `agents.py`:

```python
from langchain.agents import create_agent
```
- **What**: Import function to create agents
- **From**: LangChain library
- **Why**: We need this to create our Search and Read agents
- **Think of it as**: Buying a "create agent kit" from a store

```python
from langchain_groq import ChatGroq
```
- **What**: Import the Groq AI model
- **What it does**: Connects to Groq's AI service (like OpenAI but faster)
- **Why**: This is our "brain" - the AI that powers everything
- **Think of it as**: Hiring a super smart consultant

```python
from langchain_core.prompts import ChatPromptTemplate
```
- **What**: Template for creating prompts
- **Example**: We use this to create the "Writer Prompt" and "Critic Prompt"
- **Why**: Keeps our prompts organized and reusable
- **Think of it as**: A form template ("Name: ___, Age: ___")

```python
from langchain_core.output_parsers import StrOutputParser
```
- **What**: Converts AI output to plain text
- **Why**: AI returns complex objects; we need simple text
- **Think of it as**: A translator that turns "complicated speech" into "simple text"

```python
from dotenv import load_dotenv
import os
```
- **What**: Loads secret keys from `.env` file
- **Why**: We can't put API keys in code (security risk)
- **Think of it as**: A safe where we store passwords

### In `tools.py`:

```python
from langchain.tools import tool
```
- **What**: Decorator to create tools for agents
- **Example**: We use `@tool` before `web_search()` function
- **Why**: Tells LangChain "this function is a tool agents can use"
- **Think of it as**: Putting a sign saying "agents can use this"

```python
import requests
```
- **What**: Allows us to make HTTP requests (get website data)
- **Why**: We need to download web pages
- **Think of it as**: A messenger that fetches things from the internet

```python
from tavily import TavilyClient
```
- **What**: Connection to Tavily search service
- **Why**: More reliable web search than Google (especially for news)
- **Think of it as**: Using a professional search company instead of DIY

```python
from bs4 import BeautifulSoup
from readability import Document
import trafilatura
```
- **What**: Tools to read and clean web pages
- **Why**: Web pages have ads, navigation, noise - these tools extract just the content
- **Think of it as**: Removing all the junk mail to find the actual letter

### In `pipeline.py`:

```python
from src.agents.agents import (
    create_search_agent,
    create_read_agent,
    writer_chain,
    critic_chain
)
```
- **What**: Importing our agents and chains
- **Why**: We need to use them in the pipeline
- **Think of it as**: Hiring different team members for your project

---

## 5. Deep Dive: agents.py

### Section 1: Setup & LLM

```python
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
from src.tools.tools import web_search, scrape_url

print("Loading environment variables...")
load_dotenv()
```

**What's happening:**
- Loading secrets from `.env` file
- If file has: `GROQ_API_KEY=xyz123`, then `os.getenv("GROQ_API_KEY")` returns `xyz123`

### The LLM (Large Language Model)

```python
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)
```

**Breaking this down:**

| Part | Meaning |
|------|---------|
| `ChatGroq` | Connects to Groq's AI service |
| `model="openai/gpt-oss-20b"` | Which AI model to use |
| `temperature=0` | How creative? (0=robotic, 1=creative) |

**Temperature Explained:**
- `temperature=0`: Always gives the same answer (deterministic)
- `temperature=0.5`: Somewhat varied
- `temperature=1`: Very creative and random

**Why `temperature=0`?** For research, we want facts, not creativity!

### Agent 1: Search Agent

```python
def create_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )
```

**What this does:**
1. **Creates an agent** that's powered by our LLM
2. **Gives it a tool**: web_search function
3. **Returns the agent** ready to use

**Think of it as:**
```
Creating a "Detective Agent"
- Power: ChatGroq AI
- Tools: Can search the web
```

**How it works when you use it:**
1. You tell it: "Search for 'Nepal Floods News'"
2. Agent thinks: "I need to search, I have web_search tool"
3. Agent uses: `web_search("Nepal Floods News")`
4. Returns: Titles, URLs, snippets

### Agent 2: Read/Scrape Agent

```python
def create_read_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )
```

**What this does:**
- Similar to Search Agent
- But with a different tool: `scrape_url`
- This agent's job: Read and extract content from URLs

**Think of it as:**
```
Creating a "Reader Agent"
- Power: ChatGroq AI
- Tools: Can read websites and extract content
```

**How it works:**
1. You give it: "Extract important info from [this URL]"
2. Agent thinks: "I need to read this website, I have scrape_url tool"
3. Agent uses: `scrape_url("https://...")`
4. Returns: Clean, readable content from the website

---

### Part 3: Writer Chain

Now we move from **Agents** to **Chains**. This is important!

```python
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
```

**Breaking it down:**

#### Step 1: Create a Prompt Template

```python
ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer..."),
    ("human", "Please write a comprehensive research report...")
])
```

This creates a template with two parts:
- **System message**: Tells the AI its role ("You are a research writer")
- **Human message**: The actual task with placeholders `{topic}` and `{research}`

#### Step 2: Chain them together

```python
writer_chain = writer_prompt | llm | StrOutputParser()
```

The `|` symbol means **pipe** (pass data through):

```
Template → LLM → Text Parser
  ↓         ↓        ↓
Formats   Thinks   Converts to
prompt    about    plain text
           it
```

**Visual Flow:**
```
Input: {"topic": "AI", "research": "...data..."}
  ↓
writer_prompt (adds system instructions)
  ↓
llm (ChatGroq thinks and generates response)
  ↓
StrOutputParser (converts to clean text)
  ↓
Output: "Comprehensive report about AI..."
```

### Part 4: Critic Chain

```python
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert researcher and critical reviewer..."),
    ("human", """Please carefully review the following research report...
    
Your feedback should focus on:
1. Clarity and coherence
2. Accuracy and relevance
3. Organization and structure
...etc...""")
])

critic_chain = critic_prompt | llm | StrOutputParser()
```

**Works exactly like Writer Chain:**
- Creates prompt template for a critic
- Pipes it through LLM
- Converts output to text

**Different purpose:**
- Writer: Creates reports
- Critic: Reviews and scores reports

---

## 6. Deep Dive: pipeline.py

The pipeline is where all agents work together. Let's break down each step:

### Complete Flow:

```python
def run_research_pipeline(topic: str) -> dict:
    print(f"\n🚀 Starting research pipeline for topic: {topic}\n")
    state = {}
```

**What's happening:**
- Function takes one input: `topic` (a string)
- Returns: A dictionary with all results
- `state = {}`: Empty dictionary to store all results as we go

### Step 1: Search Agent

```python
print("🔍 Search Agent working...")
search_agent = create_search_agent()

search_results = search_agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": f"Search the web for the latest news about: {topic}. Return titles, links and short summaries."
        }
    ]
})

state["search_results"] = search_results["messages"][-1].content
```

**Line by line:**

1. **`search_agent = create_search_agent()`**
   - Creates a fresh search agent (from agents.py)

2. **`search_agent.invoke({...})`**
   - "Invoke" means "run the agent"
   - Pass a message: "Search the web for..."
   - Agent thinks about this message and decides to use web_search tool

3. **`search_results["messages"][-1].content`**
   - `[-1]` means "last item" in the list
   - `.content` extracts the text
   - We get: List of search results with titles, URLs, snippets

4. **`state["search_results"] = ...`**
   - Store results for later use

**What Agent 1 produces:**
```
Title: Nepal Floods Worsen...
URL: https://news.com/...
Snippet: Heavy rains have caused flooding in...
----
Title: Thousands Evacuated...
URL: https://...
Snippet: Officials report...
```

### Step 2: Read/Scrape Agent

```python
print("📖 Read Agent working...")
read_agent = create_read_agent()

read_results = read_agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": f"From the following search results, extract the most important and detailed information about '{topic}':\n\n{state['search_results'][:3000]}"
        }
    ]
})

state["scraped_content"] = read_results["messages"][-1].content
```

**What's different:**
- Takes the search results from Step 1
- Asks: "Extract important information from these search results"
- Agent uses scrape_url to read the websites
- Returns clean, extracted content

**What Agent 2 produces:**
```
Nepal has experienced severe flooding with over 100 casualties.
The floods damaged infrastructure and displaced thousands...
Government response included setting up evacuation centers...
```

### Step 3: Writer Chain

```python
print("✍️  Writer Agent working...")

final_report = writer_chain.invoke({
    "topic": topic,
    "research": state["scraped_content"]
})

state["final_report"] = final_report
```

**What's happening:**
- Takes the topic and scraped content
- Passes to writer_chain (from agents.py)
- Writer prompt tells LLM: "You are a research writer"
- LLM writes a professional report
- Stores result in state

**What Writer produces:**
```
COMPREHENSIVE RESEARCH REPORT: Latest Nepal Floods News

1. INTRODUCTION
The recent floods in Nepal represent one of the worst natural disasters...

2. KEY FINDINGS
- Over 100 casualties reported
- Critical infrastructure damaged
- Thousands evacuated from affected areas
- Government declared emergency...

3. CONCLUSION
The Nepal floods demonstrate the need for better disaster preparedness...

4. REFERENCES
- Nepal News Agency report
- International Relief Organization statement...
```

### Step 4: Critic Chain

```python
print("🧐 Critic Agent working...")

critique = critic_chain.invoke({
    "report": state["final_report"]
})

state["critique"] = critique
```

**What's happening:**
- Takes the final report
- Passes to critic_chain
- Critic prompt tells LLM: "You are a critical reviewer"
- LLM reviews the report and provides feedback
- Stores critique

**What Critic produces:**
```
REPORT REVIEW & FEEDBACK

1. CLARITY AND COHERENCE: Score 8/10
   Comment: Well-written and easy to follow
   Suggestion: Add more statistics for impact

2. ACCURACY AND RELEVANCE: Score 9/10
   Comment: Information is current and accurate
   Suggestion: Include expert quotes for credibility

3. ORGANIZATION AND STRUCTURE: Score 8/10
   Comment: Good flow from intro to conclusion
   Suggestion: Add subsections to Key Findings

OVERALL SCORE: 8/10
RECOMMENDATION: Excellent report with minor improvements needed
```

### Final Return

```python
print("🎉 Pipeline finished!\n")
return state
```

**Returns dictionary with all results:**
```python
{
    "search_results": "...",
    "scraped_content": "...",
    "final_report": "...",
    "critique": "..."
}
```

---

## 7. How Tools Work

### What are Tools?

Tools are **functions that agents can use** to solve problems.

In this project:
- **Tool 1**: `web_search()` - Searches the web
- **Tool 2**: `scrape_url()` - Reads website content

### Tool 1: web_search()

```python
@tool
def web_search(query : str) -> str:
    """Search the web for recent and reliable information on a topic. 
    Returns Titles, URLs and snippets."""
    
    results = tavily.search(query=query, max_results=5)
    
    out = []
    for r in results['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )
    
    return "\n----\n".join(out)
```

**Breaking it down:**

1. **`@tool` decorator**
   - This `@tool` tells LangChain: "This function is a tool agents can use"
   - Without this, agents wouldn't know about it

2. **Input:** `query` (search term)
   - Example: "Nepal Floods News"

3. **Process:**
   - `tavily.search()` calls Tavily API with query
   - Tavily returns results with title, URL, content
   - We format each result nicely
   - Join all with separator `"----"`

4. **Output:** Formatted string with search results
   - ```
     Title: Nepal Floods Crisis
     URL: https://...
     Snippet: Heavy rains have...
     ----
     Title: Floods Worsen
     URL: https://...
     Snippet: Officials report...
     ```

**Why Tavily instead of Google?**
- Google is blocked for API access (protects their search)
- Tavily is designed for AI/agents
- Returns structured data perfect for AI
- Good for news and recent information

### Tool 2: scrape_url()

This is more complex. Let's break it down:

```python
@tool
def scrape_url(url: str) -> str:
    """
    Scrape and extract clean readable content from a URL.
    Uses multiple extraction strategies for better reliability.
    """
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/",
    }
```

**`headers` explained:**
- Many websites block robots/scrapers
- We send headers that make requests look like a real browser
- `User-Agent`: "I'm a real browser, not a bot"
- This is called "user-agent spoofing"

```python
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        html = response.text
```

**What's happening:**
1. `requests.get()`: Download the webpage
2. `headers=headers`: Send fake browser headers
3. `timeout=15`: Wait max 15 seconds
4. `response.raise_for_status()`: If error, stop here
5. `html = response.text`: Get the HTML code of the page

#### Strategy 1: Trafilatura

```python
        extracted = trafilatura.extract(html, include_comments=False, 
                                        include_tables=False)
        
        if extracted and len(extracted.strip()) > 200:
            cleaned = re.sub(r'\s+', ' ', extracted)
            return cleaned[:5000]
```

**What Trafilatura does:**
- Reads HTML
- Finds the main article content
- Removes ads, navigation, sidebar
- Returns just the important text

**Why this works best:**
- Specifically designed for articles/news
- Very reliable for that use case

**Check:** If we got something with >200 characters, return it

#### Strategy 2: Readability

```python
        doc = Document(html)
        clean_html = doc.summary()
        
        soup = BeautifulSoup(clean_html, "html.parser")
        
        for tag in soup(['script', 'style', 'nav', 'footer', 'header', 
                         'aside', 'form']):
            tag.decompose()
        
        text = soup.get_text(separator=" ", strip=True)
        
        if text and len(text.strip()) > 200:
            cleaned = re.sub(r'\s+', ' ', text)
            return cleaned[:5000]
```

**What Readability does:**
- Alternative method if Trafilatura fails
- Creates a summary of main content
- BeautifulSoup parses HTML
- Removes junk tags (script, style, nav, footer, etc.)
- Extracts plain text

**`tag.decompose()`:**
- Removes the tag from HTML
- Like deleting lines from a document

#### Strategy 3: Fallback

```python
        soup = BeautifulSoup(html, "html.parser")
        # ... remove junk tags ...
        text = soup.get_text(separator=" ", strip=True)
        
        if cleaned:
            return cleaned[:5000]
        
        return "Could not extract meaningful content from the page."
```

**Last resort:**
- Try basic HTML parsing
- If all else fails, return error message

#### Error Handling

```python
    except requests.exceptions.Timeout:
        return "Request timed out while scraping the URL."
    
    except requests.exceptions.HTTPError as e:
        return f"HTTP error occurred: {str(e)}"
    
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"
```

**Catches problems:**
- Website too slow → Timeout
- Website blocked us → HTTP error
- Anything else → Generic error

**Why this matters:** If one tool fails, the agent doesn't crash!

### How Agents Use Tools

When an agent has tools, LangChain does this:

1. **Agent receives task:** "Search for Nepal Floods"
2. **Agent thinks:** "I have web_search tool, let me use it"
3. **Agent decides:** Which tool to use and what parameters
4. **Agent calls:** `web_search("Nepal Floods News")`
5. **Tool returns:** Search results
6. **Agent receives:** Results back
7. **Agent thinks:** "Should I call another tool or return answer?"
8. **Agent returns:** Final answer to the user

---

## 8. Data Flow Between Agents

This is CRUCIAL for understanding Agentic AI!

### Visualization:

```
┌─────────────────────────────────────────────────────────────┐
│ PIPELINE STARTS: Topic = "Nepal Floods News"               │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: SEARCH AGENT                                        │
│ Input:  "Search the web for: Nepal Floods News"            │
│ Tool Used: web_search()                                     │
│ Output: Titles, URLs, snippets (5 results)                 │
│         (stored in state["search_results"])                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
                    ┌───────────────┐
                    │ state = {     │
                    │   "search_... │
                    │ }             │
                    └───────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 2: READ/SCRAPE AGENT                                   │
│ Input:  "Extract from these results:" + search_results     │
│ Tool Used: scrape_url()                                     │
│ Output: Clean content extracted from articles               │
│         (stored in state["scraped_content"])                │
└─────────────────────────────────────────────────────────────┘
                            ↓
                    ┌───────────────┐
                    │ state = {     │
                    │   "search_...,│
                    │   "scraped_...|
                    │ }             │
                    └───────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 3: WRITER CHAIN                                        │
│ Input:  topic + scraped_content                            │
│ Tool Used: None (just LLM thinking)                         │
│ Output: Full professional research report                   │
│         (stored in state["final_report"])                   │
└─────────────────────────────────────────────────────────────┘
                            ↓
                    ┌───────────────┐
                    │ state = {     │
                    │   "search_...,│
                    │   "scraped_...,
                    │   "final_...|
                    │ }             │
                    └───────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 4: CRITIC CHAIN                                        │
│ Input:  final_report                                        │
│ Tool Used: None (just LLM thinking)                         │
│ Output: Review, scores, suggestions                         │
│         (stored in state["critique"])                       │
└─────────────────────────────────────────────────────────────┘
                            ↓
            ┌───────────────────────────┐
            │ FINAL state = {           │
            │   "search_results": "...", │
            │   "scraped_content": "...",│
            │   "final_report": "...",   │
            │   "critique": "..."        │
            │ }                          │
            └───────────────────────────┘
                            ↓
        ┌──────────────────────────────────┐
        │ Returned to main.py or app.py    │
        │ User sees: Report + Critique     │
        └──────────────────────────────────┘
```

### Key Points About Data Flow:

1. **Sequential:** Agents run one after another, not parallel
   - Can't write report without content
   - Can't critique report without report

2. **Passing Data:** Each step uses previous results
   - Search → Read uses Search results
   - Write uses Read results
   - Critic uses Write results

3. **Stored in State:** Everything saved in dictionary
   - Easy to debug (see intermediate results)
   - Can return all results to user

4. **Building on Information:** Each step adds value
   - Search: Raw info
   - Read: Organized info
   - Write: Formatted info
   - Critic: Quality assurance

### Real Example with Data:

```
STEP 1 - Search Agent:
Input: "Search Nepal Floods"
↓
Uses: web_search("Nepal Floods")
↓
Output: [
  {Title: "Nepal Floods Crisis", URL: "...", Snippet: "Heavy rains..."},
  {Title: "Floods Worsen", URL: "...", Snippet: "Officials report..."},
  ...
]

STEP 2 - Read Agent:
Input: "Extract from these URLs:" + [list from above]
↓
Uses: scrape_url() multiple times
↓
Output: "Nepal experienced severe flooding today. Over 100 casualties
reported. Government declared emergency. More than 5000 people evacuated..."

STEP 3 - Writer Chain:
Input: 
  topic: "Nepal Floods News"
  research: "Nepal experienced severe flooding..." (from Step 2)
↓
Uses: ChatGroq LLM
↓
Output: "[PROFESSIONAL REPORT]
1. Introduction: Recent floods in Nepal...
2. Key Findings: - 100+ casualties
                - 5000+ evacuated
                - Infrastructure damaged
3. Conclusion: Need for disaster preparedness
4. References: ..."

STEP 4 - Critic Chain:
Input: "[PROFESSIONAL REPORT]" (from Step 3)
↓
Uses: ChatGroq LLM
↓
Output: "CRITIQUE:
1. Clarity: 8/10 - Well written but needs more stats
2. Accuracy: 9/10 - Information is current
3. Structure: 8/10 - Good flow
OVERALL: 8/10"
```

---

## 9. Agent vs Chain

This is a MAJOR concept!

### What's the Difference?

| Aspect | Agent | Chain |
|--------|-------|-------|
| **Has tools?** | YES | NO |
| **Makes decisions?** | YES | NO |
| **Can iterate?** | YES | NO |
| **Follows fixed path?** | NO | YES |
| **Complex tasks?** | ✓ Good | Simple only |

### Agent Explained:

An **Agent** is like a problem-solver with tools.

```python
search_agent = create_agent(
    model=llm,
    tools=[web_search]  # <-- Has a tool!
)
```

**How Agent Works:**

1. **Receives task:** "Search for Nepal Floods"
2. **Thinks:** "I need to search the web"
3. **Decides:** "I'll use my web_search tool"
4. **Executes:** Calls web_search("Nepal Floods")
5. **Gets result:** List of search results
6. **Decides next:** "I have answer, return it"
7. **Returns:** Results to user

**Agent has intelligence** - it decides which tools to use and when.

### Chain Explained:

A **Chain** is like a pipeline with fixed steps.

```python
writer_chain = writer_prompt | llm | StrOutputParser()
```

**How Chain Works:**

1. **Input data:** {"topic": "AI", "research": "..."}
2. **Step 1:** writer_prompt formats the input
3. **Step 2:** llm generates response (doesn't make decisions)
4. **Step 3:** StrOutputParser converts to text
5. **Output:** Professional text report

**Chain is sequential** - always same steps in same order.

### When to Use Each?

#### Use Agent for:
- Complex, multi-step problems
- Uncertain workflow (agent decides steps)
- Tasks needing tool selection
- Research, problem-solving
- **Example:** "Research this topic" (agent decides how)

#### Use Chain for:
- Well-defined processes
- Fixed workflow
- Simple transformations
- Text generation, translation
- **Example:** "Write a report from this data" (fixed process)

### In This Project:

```
AGENTS (have tools, make decisions):
├── Search Agent (decides to use web_search)
└── Read Agent (decides to use scrape_url)

CHAINS (fixed process, no tools):
├── Writer Chain (always: format → LLM → parse)
└── Critic Chain (always: format → LLM → parse)
```

### Conceptual Difference:

**Agent:**
```
Task → Agent thinks → "Which tool?" → Uses tool → Gets result → 
"Do I need more?" → Maybe uses another tool → Returns answer
```

**Chain:**
```
Input → Step1 → Step2 → Step3 → Output
(Always same steps)
```

---

## 10. How to Run the Project

### Prerequisites:

1. **Python 3.13+**
2. **API Keys:**
   - Groq API Key (from console.groq.com)
   - Tavily API Key (from tavily.com)

### Setup:

#### 1. Create Environment File

Create `.env` file in project root:
```
GROQ_API_KEY=your_groq_key_here
TAVILY_API_KEY=your_tavily_key_here
```

#### 2. Create Conda Environment

```bash
conda create -n langmultiagent python=3.13 -y
conda activate langmultiagent
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### Running It:

#### Option 1: Command Line

```bash
python main.py
```

**What happens:**
1. Runs research on "Latest Nepal Floods News"
2. Prints search results
3. Prints scraped content
4. Prints full report
5. Prints critique

#### Option 2: Web Interface

```bash
streamlit run app.py
```

**What happens:**
1. Opens browser at `http://localhost:8501`
2. Beautiful UI with:
   - Input field for topic
   - Example topics sidebar
   - Real-time progress
   - Formatted report display
   - Critique display

### Customizing:

#### Change Topic (CLI):

Edit `main.py`:
```python
topic = "Your topic here instead of Nepal Floods"
result = run_research_pipeline(topic)
```

#### Change Topic (Web):

Type in input box and click "Research"

#### Change AI Model:

Edit `src/agents/agents.py`:
```python
llm = ChatGroq(
    model="gpt-4-turbo",  # Change this
    temperature=0
)
```

#### Change Report Structure:

Edit `src/agents/agents.py`, modify writer_prompt:
```python
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are..."),
    ("human", """Please write report with:
    1. Summary
    2. Technical details
    3. Recommendations
    ...etc...""")
])
```

---

## 11. Key Concepts You'll Learn

### Concept 1: LLM (Large Language Model)

**What:** A neural network trained on massive text data

**Can:**
- Understand requests
- Generate text
- Make logical inferences
- Answer questions
- Write reports

**In project:** ChatGroq is our LLM

### Concept 2: Prompt Engineering

**What:** How you ask the LLM affects quality of output

**Example:**
```
Bad prompt: "Write something about Nepal"
Output: "Nepal is a country in Asia"

Good prompt: "Write a professional research report on Nepal Floods
with Introduction, Key Findings, and Conclusion sections. Include
specific statistics and ensure it's factual based on research material."
Output: [Professional, detailed report]
```

**In project:**
- Writer prompt tells LLM to write professionally
- Critic prompt tells LLM how to review

### Concept 3: Tool Use

**What:** LLM can call functions to accomplish tasks

**How:**
1. LLM decides it needs information
2. LLM calls a tool (web_search)
3. Tool returns information
4. LLM uses information to answer

**In project:**
- Search agent uses web_search tool
- Read agent uses scrape_url tool

### Concept 4: Agent Autonomy

**What:** Agents make decisions instead of humans

**Example:**
```
Human: "Research this topic"
Agent decides:
- Search for information (uses web_search)
- Read articles (uses scrape_url)
- Extract key info (processes text)
- Return results
```

### Concept 5: Orchestration

**What:** Coordinating multiple agents to work together

**In project:**
1. Pipeline orchestrates 4 agents/chains
2. Each completes its task
3. Results passed to next
4. Final output to user

### Concept 6: Streaming & Pipes

**What:** `|` symbol means pass data through

```python
writer_chain = writer_prompt | llm | StrOutputParser()
```

**Means:**
```
writer_prompt creates prompt
  ↓
llm processes it
  ↓
StrOutputParser converts to text
  ↓
Final output
```

### Concept 7: State Management

**What:** Keeping track of data through the process

**In project:**
```python
state = {}
state["search_results"] = "..."
state["scraped_content"] = "..."
state["final_report"] = "..."
state["critique"] = "..."
return state
```

### Concept 8: Error Handling

**What:** Gracefully handling problems

**In project:** `scrape_url()` has try-except blocks
- Timeouts handled
- HTTP errors handled
- Unknown errors handled
- Returns error message instead of crashing

### Concept 9: Multi-Agent Systems

**What:** Multiple AI agents collaborating

**In project:**
- Search Agent: Finds info
- Read Agent: Extracts content
- Writer: Formats nicely
- Critic: Quality checks

**Why useful:** Divide-and-conquer. Each agent specializes in one task.

### Concept 10: API Integration

**What:** Using external services

**In project:**
- Groq API: Provides AI/LLM
- Tavily API: Provides web search
- Local tools: Search, scrape, format

**Why useful:** Don't need to build everything from scratch

---

## 12. Next Steps to Improve Your Skills

### Level 1: Beginner (Understand Current Project)

**Task 1: Add a new Chain**
- Add a "Summarizer Chain" that creates 1-paragraph summary
- Use same pattern as Writer and Critic
- Update pipeline to use it

**Task 2: Modify Agent Behavior**
- Change temperature to 0.5 (make it more creative)
- Observe differences in output
- Try different models in Groq

**Task 3: Customize Prompts**
- Change writer prompt to write in different style
- Make critic provide different feedback
- Experiment with prompt engineering

### Level 2: Intermediate (Extend Project)

**Task 4: Add a Third Agent**
- Create a "Source Validator Agent"
- Job: Check if sources are reliable
- Use web_search tool to check source credibility

**Task 5: Add Parallel Agents**
- Currently agents run sequentially (one after another)
- Make multiple search/read agents run at same time
- Combine their results
- **Hint:** Use Python's asyncio

**Task 6: Add Memory**
- Remember previous research topics
- Reuse past results if same topic asked again
- Implement simple dictionary cache

**Task 7: Add Different Output Formats**
- Generate report as JSON
- Generate report as Markdown
- Generate report as PowerPoint structure

### Level 3: Advanced (Build New Systems)

**Task 8: Build a Debate System**
- Create two opposing agents
- Agent 1 argues for a position
- Agent 2 argues against
- Return both arguments

**Example:**
```
Topic: "Should AI be regulated?"
Agent 1: "Yes, AI needs strict regulations because..."
Agent 2: "No, regulations will slow innovation because..."
```

**Task 9: Build a Question-Answer System**
- User asks question
- Search Agent finds answers
- Read Agent extracts relevant parts
- Answer Agent formulates response
- Return answer with sources

**Task 10: Build a Comparison System**
- Compare two products/concepts
- Search for info on both
- Extract key features
- Create comparison table
- Return formatted comparison

**Task 11: Build a Fact-Checking System**
- User provides statement
- Search Agent looks for sources
- Verify/Refute Agent checks facts
- Return fact-check result with evidence

**Task 12: Add Web UI Improvements**
- Add chart showing agent progress
- Add download button for reports
- Add feedback feature
- Add export to PDF/Word

### Level 4: Expert (Production System)

**Task 13: Optimize Performance**
- Make agents run in parallel
- Cache search results
- Implement connection pooling
- Benchmark and profile

**Task 14: Add Error Recovery**
- If web_search fails, try different search
- If one URL fails, try next URL
- Implement retry logic
- Log all errors

**Task 15: Add Monitoring & Logging**
- Log every step with timestamps
- Track LLM token usage
- Track API costs
- Create analytics dashboard

**Task 16: Deploy to Cloud**
- Deploy app.py to Streamlit Cloud
- Or deploy to AWS/Google Cloud
- Set up CI/CD pipeline
- Monitor in production

**Task 17: Multi-Language Support**
- Add language detection
- Generate reports in multiple languages
- Allow user to select language

**Task 18: Advanced Agent Orchestration**
- Create "Manager Agent" that plans workflow
- Manager decides if research needed
- Manager decides if report needed
- Manager routes tasks to specialists

---

## Learning Path Recommendations

### Week 1: Understanding
1. Read this entire guide
2. Run the project with example topics
3. Modify prompts and observe changes
4. Play with temperature settings

### Week 2: Experimentation
1. Complete Task 1-3 (Level 1)
2. Add print statements to understand data flow
3. Draw diagrams of how data flows
4. Explain it to someone else

### Week 3: Extension
1. Complete Task 4-7 (Level 2)
2. Add new tools
3. Create new agents
4. Combine in new ways

### Week 4+: Specialization
1. Choose one area from Level 3-4
2. Deep dive into that area
3. Build something cool
4. Share with community

---

## Common Mistakes to Avoid

### Mistake 1: Forgetting API Keys
```python
# ❌ Wrong
llm = ChatGroq(model="...", api_key="my_key")

# ✓ Right
load_dotenv()
llm = ChatGroq(model="...")  # Loads from .env
```

### Mistake 2: Not Handling Errors
```python
# ❌ Wrong
content = scrape_url(url)  # Crashes if URL fails

# ✓ Right
try:
    content = scrape_url(url)
except:
    content = "Error scraping"
```

### Mistake 3: Over-engineering
```python
# ❌ Wrong - Too complex for beginners
# Create fancy async agents, complex caching, etc.

# ✓ Right - Start simple
# Get working version first
# Optimize later
```

### Mistake 4: Not Testing Incrementally
```python
# ❌ Wrong
# Build entire system, then test

# ✓ Right
# Test each agent separately
# Test each chain separately
# Test pipeline with simple example
# Gradually add complexity
```

### Mistake 5: Ignoring Temperature
```python
# ❌ Wrong - Using temperature=1 for research
llm = ChatGroq(model="...", temperature=1)

# ✓ Right - Using temperature=0 for facts
llm = ChatGroq(model="...", temperature=0)
```

---

## Glossary

| Term | Meaning |
|------|---------|
| **Agent** | AI with tools that makes decisions |
| **Chain** | Fixed pipeline of steps |
| **Tool** | Function an agent can call |
| **LLM** | Large Language Model (AI engine) |
| **Prompt** | Instructions to the AI |
| **Temperature** | Creativity level (0-1) |
| **Invoke** | Run/execute an agent |
| **State** | Stored data from process |
| **API** | Service provided by external company |
| **Token** | Unit of text for LLM |
| **Orchestration** | Coordinating multiple agents |
| **Streaming** | Passing data through steps |
| **Pipe** | Symbol `\|` meaning pass through |
| **Scraping** | Extracting data from websites |
| **Parser** | Converts one format to another |

---

## Practice Exercises

### Exercise 1: Data Flow Diagram
Draw a diagram showing how data flows through the pipeline. Include:
- Input topic
- Each agent/chain
- Outputs at each stage
- Final output

### Exercise 2: Explain to a Friend
Explain in 2-3 minutes to someone who doesn't know AI:
- What this project does
- Why it's useful
- How agents work

### Exercise 3: Modify and Test
1. Change search_agent to search for 3 results instead of 5
2. Run project
3. Observe changes
4. Document observations

### Exercise 4: Create Documentation
Write simple documentation for:
- How to set up project
- How to run it
- How to customize it
- Common errors and solutions

### Exercise 5: Performance Analysis
1. Time each step of pipeline
2. Which step is slowest?
3. Why might it be slow?
4. How could you optimize?

---

## Conclusion

You now understand:
1. ✓ What Agentic AI is
2. ✓ How this project works
3. ✓ How agents and chains differ
4. ✓ How tools enable agents
5. ✓ How data flows through system
6. ✓ How to run and modify project
7. ✓ What to learn next

### Next: Take Action!

The best way to learn is by **doing**. Pick one task from Level 1 and implement it. Don't wait for perfection!

Happy coding! 🚀

---

## Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Groq Console](https://console.groq.com)
- [Tavily API Docs](https://tavily.com/)
- [BeautifulSoup Tutorial](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Streamlit Docs](https://docs.streamlit.io/)

