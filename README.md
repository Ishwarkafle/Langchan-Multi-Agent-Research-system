# 🧠 LangChain Multi-Agent Research System

A sophisticated AI-powered research system that leverages multiple autonomous agents to conduct comprehensive research, analyze content, and generate insightful reports on any topic.

## ✨ Features

- **Multi-Agent Architecture**: Coordinated team of specialized AI agents for different research tasks
  - 🔍 **Search Agent**: Performs web searches using Tavily API to gather recent information
  - 📖 **Read/Scrape Agent**: Extracts and processes content from URLs with multiple fallback strategies
  - ✍️ **Writer Agent**: Generates well-structured, comprehensive research reports
  - 🎯 **Critic Agent**: Provides feedback and quality assurance on generated content

- **Intelligent Content Extraction**: Multiple extraction strategies (BeautifulSoup, Trafilatura, Readability) for reliable content scraping
- **Web Interface**: Interactive Streamlit dashboard for easy interaction with the research system
- **LLM-Powered**: Uses Groq's fast inference for real-time research and analysis
- **Structured Reports**: Generates comprehensive reports with introductions, key findings, and conclusions

## 🛠️ Tech Stack

- **LLM & Frameworks**:
  - LangChain (>=0.2.0) - AI agent orchestration framework
  - LangChain Groq - Groq LLM integration
  - ChatGroq - Fast inference LLM model

- **Web Tools**:
  - Tavily API - Reliable web search tool
  - BeautifulSoup4 - HTML/XML parsing
  - Trafilatura - Content extraction
  - Readability-lxml - Web article extraction
  - Requests - HTTP client

- **Frontend**:
  - Streamlit - Interactive web interface

- **Utilities**:
  - Python-dotenv - Environment variable management
  - Rich - Terminal formatting

## 📋 Requirements

- Python 3.13+
- Conda (recommended)
- API Keys:
  - Groq API Key (for LLM access)
  - Tavily API Key (for web search)

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd Langchan-Multi-Agent-Research-system
```

### Step 2: Create Virtual Environment
```bash
conda create -n langmultiagent python=3.13 -y
conda activate langmultiagent
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

## 💻 Usage

### Option 1: Command Line Interface
Run the research pipeline directly:
```bash
python main.py
```

This will execute a research topic and display:
- Research findings from search results
- Scraped content from relevant sources
- Final comprehensive research report
- Critique and feedback on the report

**Example output**: Research report on "Latest Nepal Floods News"

### Option 2: Web Interface (Streamlit)
Launch the interactive dashboard:
```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501` and:
- Enter your research topic
- View real-time research progress
- Read generated reports in an interactive format
- Access search results and scraped content

## 📁 Project Structure

```
Langchan-Multi-Agent-Research-system/
├── main.py                 # CLI entry point for research pipeline
├── app.py                  # Streamlit web interface
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── LICENSE                # Project license
└── src/
    ├── __init__.py
    ├── agents/
    │   ├── __init__.py
    │   └── agents.py       # Multi-agent definitions (search, read, writer, critic)
    ├── tools/
    │   ├── __init__.py
    │   └── tools.py        # Tool definitions (web_search, scrape_url)
    └── pipeline/
        ├── __init__.py
        └── pipeline.py     # Research pipeline orchestration
```

## 🔧 Core Components

### Agents (`src/agents/agents.py`)
- **Search Agent**: Finds relevant web resources using Tavily
- **Read Agent**: Extracts meaningful content from URLs
- **Writer Chain**: Composes structured research reports
- **Critic Chain**: Reviews and provides feedback on reports

### Tools (`src/tools/tools.py`)
- **web_search()**: Searches the web and returns titles, URLs, and snippets (top 5 results)
- **scrape_url()**: Extracts clean, readable content from web pages using multiple strategies

### Pipeline (`src/pipeline/pipeline.py`)
Orchestrates the workflow:
1. Search for relevant information
2. Scrape and process content
3. Generate comprehensive report
4. Provide critical feedback

## 📊 Example Usage

```python
from src.pipeline import run_research_pipeline

# Run research on any topic
topic = "Latest Nepal Floods News"
result = run_research_pipeline(topic)

# Access results
print(result["final_report"])      # Complete research report
print(result["critique"])          # Critical feedback
```

## 🔑 API Keys

### Groq API
1. Visit [console.groq.com](https://console.groq.com)
2. Create an account and get your API key
3. Add to `.env` file as `GROQ_API_KEY`

### Tavily API
1. Visit [tavily.com](https://tavily.com)
2. Sign up and obtain your API key
3. Add to `.env` file as `TAVILY_API_KEY`

## 🎯 Use Cases

- **Research & Analysis**: Comprehensive topic research and analysis
- **News Monitoring**: Stay updated on specific topics or events
- **Content Creation**: Generate well-researched content quickly
- **Competitive Analysis**: Research market trends and competitors
- **Decision Support**: Gather information for informed decision-making

## ⚙️ Configuration

### Customizing Research Parameters
Edit `src/agents/agents.py` to adjust:
- LLM temperature (0 = deterministic, 1 = creative)
- Model selection (currently: `openai/gpt-oss-20b`)
- System prompts for different agents

### Report Structure
Modify the writer prompt in `agents.py` to customize report format

## 🐛 Troubleshooting

**Issue**: "API Key not found"
- **Solution**: Ensure `.env` file is created and keys are set correctly

**Issue**: "Connection error from Tavily"
- **Solution**: Check your Tavily API key and internet connection

**Issue**: Slow content extraction
- **Solution**: The system tries multiple extraction methods; this is normal for some websites

## 📝 License

See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues and enhancement requests.

## 📧 Contact & Support

For questions or support, please reach out through the repository issues section.

---

**Built with ❤️ using LangChain, Groq, and Streamlit**