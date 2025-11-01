# 🤖 LangGraph Multi-Agent System

<div align="center">

![LangGraph](https://img.shields.io/badge/LangGraph-1.0.2-blue)
![Python](https://img.shields.io/badge/Python-3.9+-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red)
![Groq](https://img.shields.io/badge/Groq-Free-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

**A production-ready multi-agent system built with LangGraph 1.0, featuring intelligent research automation through coordinated AI agents.**

[Features](#-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Examples](#-usage-examples) • [Contributing](#-contributing)

</div>

---

<div align="center">

### ☕ Support This Project

If you find this project helpful, consider buying me a coffee to support continued development! ☕✨

<a href="https://buymeacoffee.com/mahendramedapati" target="_blank">
  <img src="Images/1_CEZSIxeYr6PCxsN6Gr38MQ.png" alt="Buy Me A Coffee" width="200">
</a>

</div>

---

## 📖 Table of Contents

1. [Overview](#-overview)
2. [Features](#-features)
3. [Architecture](#-architecture)
4. [Installation](#-installation)
5. [Quick Start](#-quick-start)
6. [Configuration](#-configuration)
7. [Usage Examples](#-usage-examples)
8. [Project Structure](#-project-structure)
9. [API Reference](#-api-reference)
10. [Advanced Usage](#-advanced-usage)
11. [Testing](#-testing)
12. [Troubleshooting](#-troubleshooting)
13. [Performance Tips](#-performance-tips)
14. [Deployment](#-deployment)
15. [Contributing](#-contributing)
16. [License](#-license)

---

## 🎯 Overview

The **LangGraph Multi-Agent System** is a comprehensive framework for building intelligent multi-agent applications. It demonstrates how multiple AI agents can work together in coordinated workflows to accomplish complex research and analysis tasks.

### Key Highlights

- **🆓 Free Tier**: Uses Groq's free API with Llama models
- **🚀 Fast**: Optimized workflows for quick responses
- **🎨 Beautiful UI**: Modern Streamlit interface
- **📊 Production Ready**: Comprehensive error handling, logging, and testing
- **🔧 Extensible**: Easy to add new agents and tools
- **📚 Well Documented**: Extensive documentation and examples

### What This System Does

This system demonstrates a complete research automation pipeline where multiple specialized agents collaborate to:

1. **Research** trending topics and gather information
2. **Collect** detailed data from multiple sources
3. **Analyze** patterns, sentiment, and market implications
4. **Write** comprehensive reports and summaries

---

## 🌟 Features

### 🎯 Dual Agent Systems

#### Single Agent System
- **Purpose**: Fast, efficient workflows for simple tasks
- **Use Case**: Quick research queries, simple summaries
- **Features**:
  - Direct tool access
  - Simple prompt-based execution
  - Fast response times
  - Perfect for testing and development

#### Multi-Agent System
- **Purpose**: Complex, hierarchical workflows with specialized teams
- **Use Case**: Comprehensive research, detailed analysis
- **Features**:
  - Hierarchical agent coordination
  - Specialized agent teams
  - State management across agents
  - Comprehensive reporting

### 👥 Specialized Agent Teams

#### 🔬 Research Team
- **ResearchAgent**: Gathers trending topics and creates overviews
  - Uses Groq's Llama models
  - Fetches trending topics
  - Creates concise overviews
  - Fast and efficient

- **DataCollectorAgent**: Collects detailed information from multiple sources
  - Searches for relevant articles
  - Aggregates data from multiple sources
  - Formats information for analysis

#### 📊 Analysis Team
- **AnalystAgent**: Analyzes trends and patterns
  - Detects common patterns
  - Provides key insights
  - Identifies market implications
  - Highlights emerging trends

- **SentimentAnalyzer**: Analyzes sentiment of findings
  - Keyword-based sentiment analysis
  - Confidence scoring
  - Positive/negative signal detection

#### ✍️ Writing Team
- **WriterAgent**: Creates professional final reports
  - Executive summaries
  - Structured reports
  - Actionable insights
  - Professional formatting

- **EditorAgent**: Edits and refines content
  - Improves conciseness
  - Enhances professionalism
  - Strengthens recommendations

### 🛠️ Powerful Tools

All agents have access to a comprehensive toolkit:

#### Search Tools
- **`fetch_trending_topics`**: Discovers trending tech topics
  - Configurable timeframe (day, week, month)
  - Limit results
  - Returns list of topics

- **`search_articles`**: Searches for articles about specific topics
  - Topic-based search
  - Configurable max results
  - Returns articles with metadata

#### Data Processing Tools
- **`process_data`**: Processes and transforms data
  - Filtering
  - Sorting
  - Grouping operations

- **`summarize_text`**: Summarizes long text content
  - Extractive summarization
  - Configurable max length

#### Analysis Tools
- **`analyze_sentiment`**: Analyzes sentiment of text
  - Sentiment classification
  - Confidence scoring
  - Positive/negative signals

- **`detect_patterns`**: Detects common patterns in data
  - Keyword frequency analysis
  - Pattern identification
  - Trend detection

### 🎨 Beautiful UI Features

- **Modern Interface**: Clean, intuitive Streamlit UI
- **Real-time Progress**: Visual progress tracking during execution
- **Tabbed Results**: Organized results in multiple tabs
  - Final Report
  - Research Notes
  - Analysis Results
  - Source Articles
- **Execution History**: Track previous executions
- **Export Capabilities**: Download reports as Markdown
- **Configurable Settings**: Advanced options in sidebar

### ⚙️ Production Ready Features

- **Error Handling**: Comprehensive error handling throughout
- **Logging**: Extensive logging with Loguru
  - Console and file logging
  - Configurable log levels
  - Automatic log rotation
- **Configuration Management**: Environment-based settings
- **Testing**: Unit and integration tests included
- **Documentation**: Comprehensive documentation

---

## 🏗️ Architecture

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│              Streamlit Frontend (app.py)                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  User Interface: Task Input, Results Display        │   │
│  │  Configuration: System Type, Task Settings          │   │
│  │  Progress Tracking: Real-time Updates              │   │
│  └─────────────────────────────────────────────────────┘   │
└───────────────────┬─────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
   ┌────▼────┐            ┌──────▼──────┐
   │ Single  │            │   Multi-    │
   │ Agent   │            │   Agent     │
   │Workflow │            │  Workflow   │
   │         │            │             │
   │ ┌────┐  │            │  ┌────────┐ │
   │ │Agent│  │            │  │Research│ │
   │ └────┘  │            │  │ Agent  │ │
   │    │    │            │  └───┬────┘ │
   │    │    │            │      │      │
   └────┼────┘            │  ┌───▼────┐ │
        │                 │  │Collect │ │
        └────────┬────────┘  │ Agent  │ │
                 │           └───┬────┘ │
                 │               │      │
        ┌────────┴───────────────┴──────┘
        │
   ┌────▼────────────────────────────┐
   │      Agent Base Layer            │
   │  ┌──────────────────────────┐   │
   │  │  Research Agents         │   │
   │  │  Analysis Agents         │   │
   │  │  Writing Agents          │   │
   │  └──────────────────────────┘   │
   └────┬─────────────────────────────┘
        │
   ┌────▼────────────────────────────┐
   │      Tools Layer                 │
   │  ┌──────────────────────────┐   │
   │  │  Search Tools            │   │
   │  │  Data Processing Tools    │   │
   │  │  Analysis Tools           │   │
   │  └──────────────────────────┘   │
   └────┬─────────────────────────────┘
        │
   ┌────▼────────────────────────────┐
   │      LLM Providers               │
   │  ┌──────────────────────────┐   │
   │  │  Groq (Llama Models)     │   │
   │  │  Google (Gemini)         │   │
   │  │  Anthropic (Claude)      │   │
   │  └──────────────────────────┘   │
   └──────────────────────────────────┘
```

### Multi-Agent Workflow Detailed Flow

```
┌─────────────────────────────────────────────────────────┐
│                    User Task Input                       │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │  Research Agent       │
         │  • Fetch topics       │
         │  • Create overview    │
         └───────────┬───────────┘
                     │ State: research_notes, topics
                     ▼
         ┌───────────────────────┐
         │ Data Collector Agent  │
         │  • Search articles    │
         │  • Collect data       │
         └───────────┬───────────┘
                     │ State: articles, detailed_data
                     ▼
         ┌───────────────────────┐
         │   Analyst Agent       │
         │  • Detect patterns   │
         │  • Analyze findings  │
         │  • Extract insights  │
         └───────────┬───────────┘
                     │ State: analysis_results, patterns
                     ▼
         ┌───────────────────────┐
         │   Writer Agent        │
         │  • Create report      │
         │  • Format output      │
         └───────────┬───────────┘
                     │ State: final_report
                     ▼
         ┌───────────────────────┐
         │    Final Report       │
         │  • Executive Summary │
         │  • Key Developments  │
         │  • Strategic Insights│
         │  • Recommendations   │
         └───────────────────────┘
```

### Single Agent Workflow Flow

```
User Task
    │
    ▼
┌───────────────────────┐
│  Single Agent         │
│  with Tools Access    │
└───────────┬───────────┘
            │
    ┌───────┴───────┐
    │               │
    ▼               ▼
┌──────────┐   ┌──────────┐
│ Tools:   │   │ LLM:     │
│ • fetch  │   │ Groq     │
│ • search │   │ Llama    │
│ • analyze│   │ Models   │
└────┬─────┘   └────┬─────┘
     │              │
     └──────┬───────┘
            │
            ▼
    ┌───────────────┐
    │  Summary      │
    │  Report       │
    └───────────────┘
```

---

## 🚀 Installation

### Prerequisites

Before installing, ensure you have:

- **Python 3.9 or higher** (Python 3.10 recommended)
- **pip** package manager
- **Git** (for cloning the repository)
- **Groq API Key** (free at https://console.groq.com)

### Step-by-Step Installation

#### Step 1: Clone the Repository

```bash
# Clone the repository
git clone <your-repo-url>
cd langgraph-multi-agent-system

# Or if you have the project locally, navigate to it
cd D:\github  # or your project directory
```

#### Step 2: Set Up Virtual Environment

**Using Conda (Recommended):**

```bash
# Create conda environment with Python 3.10
conda create -n github python=3.10 -y

# Activate the environment
conda activate github
```

**Using venv:**

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

#### Step 3: Install Dependencies

```bash
# Upgrade pip first
pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt
```

**Expected output:**
```
Successfully installed langgraph-1.0.2 langchain-1.0.3 ...
```

#### Step 4: Get Your Groq API Key

1. Visit **https://console.groq.com**
2. Sign up for a free account (or log in if you have one)
3. Navigate to **API Keys** section
4. Click **Create API Key**
5. Copy your API key (you'll need it in the next step)

#### Step 5: Configure Environment Variables

**Create `.env` file:**

```bash
# Windows PowerShell
echo GROQ_API_KEY=your_groq_api_key_here > .env

# Linux/Mac
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
```

**Or manually create `.env` file:**

Create a file named `.env` in the project root with:

```env
# Required: Groq API Key (get free key at https://console.groq.com)
GROQ_API_KEY=your_groq_api_key_here

# Optional: Google API Key (if you want to use Google models)
GOOGLE_API_KEY=your_google_api_key_here

# Optional: Anthropic API Key (if you want to use Claude models)
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Optional: LangSmith for monitoring
LANGCHAIN_TRACING_V2=false
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=langgraph-multi-agent

# Application Settings (Optional)
LOG_LEVEL=INFO
MAX_RETRIES=3
TIMEOUT_SECONDS=30
```

**⚠️ Important:** Replace `your_groq_api_key_here` with your actual Groq API key!

#### Step 6: Verify Installation

```bash
# Test imports
python -c "from langchain_groq import ChatGroq; print('✅ Groq installed')"
python -c "import streamlit; print('✅ Streamlit installed')"
python -c "from config.settings import settings; print(f'✅ Settings loaded: {settings.default_model}')"
```

---

## ⚡ Quick Start

### Running the Application

```bash
# Make sure you're in the activated environment
conda activate github  # or your venv

# Run the Streamlit app
streamlit run app.py
```

**Expected output:**
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
```

Open **http://localhost:8501** in your browser.

### First-Time Usage

1. **Open the application** in your browser (http://localhost:8501)

2. **Configure in Sidebar:**
   - Select **Agent System**: Choose "Single Agent" or "Multi-Agent"
   - Enter your **Task**: Type your research task or select a preset

3. **Click "🚀 Execute"** button

4. **View Results**: 
   - Single Agent: See results directly
   - Multi-Agent: Explore results in tabs (Report, Research Notes, Analysis, Sources)

### Example Tasks to Try

**Single Agent:**
- "Research trending topics in AI"
- "Summarize recent developments in machine learning"
- "Find articles about LangGraph"

**Multi-Agent:**
- "Analyze the latest trends in AI agents and LangGraph"
- "Research and analyze developments in quantum computing"
- "Create a comprehensive report on LLM deployment strategies"

---

## ⚙️ Configuration

### Environment Variables

Complete list of environment variables:

| Variable | Description | Required | Default | Example |
|----------|-------------|----------|---------|---------|
| `GROQ_API_KEY` | Groq API key for Llama models | ✅ **Yes** | - | `gsk_...` |
| `GOOGLE_API_KEY` | Google AI API key | No | - | `AIza...` |
| `ANTHROPIC_API_KEY` | Anthropic API key | No | - | `sk-ant-...` |
| `LOG_LEVEL` | Logging level | No | `INFO` | `DEBUG`, `INFO`, `WARNING` |
| `MAX_RETRIES` | Maximum retry attempts | No | `3` | `5` |
| `TIMEOUT_SECONDS` | Request timeout | No | `30` | `60` |
| `LANGCHAIN_TRACING_V2` | Enable LangSmith tracing | No | `false` | `true` |
| `LANGCHAIN_API_KEY` | LangSmith API key | No | - | - |
| `LANGCHAIN_PROJECT` | LangSmith project name | No | `langgraph-multi-agent` | - |

### Model Configuration

Models are configured in `config/settings.py`:

```python
# Default models (can be changed in settings.py)
default_model: str = "llama-3.3-70b-versatile"  # Primary model
cheap_model: str = "llama-3.1-8b-instant"        # Fast model
fast_model: str = "gemini-2.0-flash-exp"         # Google model
```

**Available Groq Models:**

- `llama-3.3-70b-versatile` - Best quality, comprehensive
- `llama-3.1-70b-versatile` - High quality alternative
- `llama-3.1-8b-instant` - Fast responses
- `mixtral-8x7b-32768` - Alternative option
- `gemma2-9b-it` - Fast alternative

### Changing Models

To use a different model, edit `config/settings.py`:

```python
# For example, use faster model
default_model: str = "llama-3.1-8b-instant"
```

Or set via environment variable:

```bash
# In .env file
DEFAULT_MODEL=llama-3.1-8b-instant
```

---

## 📖 Usage Examples

### Example 1: Basic Single Agent Usage

```python
from workflows.single_agent import create_single_agent_system

# Create the system
system = create_single_agent_system()

# Execute a task
result = system.invoke({
    "task": "Research trending topics in AI and machine learning",
    "messages": []
})

# Display result
print(result["result"])
```

### Example 2: Multi-Agent Workflow

```python
from workflows.multi_agent import create_multi_agent_system

# Create the system
system = create_multi_agent_system()

# Execute comprehensive analysis
result = system.invoke({
    "current_task": "Analyze the latest developments in AI agents and create a report",
    "messages": [],
    "research_notes": "",
    "trending_topics": [],
    "articles": [],
    "analysis_results": "",
    "patterns": [],
    "final_report": "",
    "next_agent": "researcher",
    "status": "started"
})

# Access different parts of the result
print("Final Report:")
print(result["final_report"])

print("\nResearch Notes:")
print(result["research_notes"])

print("\nTrending Topics:")
for topic in result["trending_topics"]:
    print(f"- {topic}")
```

### Example 3: Using Individual Agents

```python
from agents.research_agents import ResearchAgent, DataCollectorAgent
from agents.analysis_agents import AnalystAgent
from agents.writing_agents import WriterAgent

# Initialize agents
researcher = ResearchAgent()
collector = DataCollectorAgent()
analyst = AnalystAgent()
writer = WriterAgent()

# Execute workflow step by step
state = {"current_task": "Research AI trends"}

# Step 1: Research
state = researcher.execute(state)
print(f"Research complete: {len(state['trending_topics'])} topics found")

# Step 2: Collect data
state = collector.execute(state)
print(f"Data collected: {len(state['articles'])} articles")

# Step 3: Analyze
state = analyst.execute(state)
print("Analysis complete")

# Step 4: Write report
state = writer.execute(state)
print("\nFinal Report:")
print(state["final_report"])
```

### Example 4: Using Tools Directly

```python
from tools.search_tools import fetch_trending_topics, search_articles
from tools.analysis_tools import analyze_sentiment, detect_patterns

# Fetch trending topics
topics = fetch_trending_topics.invoke({
    "timeframe": "week",
    "limit": 10
})
print(f"Found {len(topics)} trending topics")

# Search for articles on a topic
articles = search_articles.invoke({
    "topic": "AI Agents",
    "max_results": 5
})
print(f"Found {len(articles)} articles")

# Analyze sentiment
sentiment = analyze_sentiment.invoke({
    "text": "This is a revolutionary technology that will change everything!"
})
print(f"Sentiment: {sentiment['sentiment']} (score: {sentiment['score']})")

# Detect patterns
patterns = detect_patterns.invoke({
    "data": topics
})
print(f"Detected {len(patterns)} patterns")
```

### Example 5: Custom Agent Configuration

```python
from agents.base import BaseAgent

# Create a custom agent with specific configuration
class CustomAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Custom Agent",
            model_name="llama-3.1-8b-instant",  # Use faster model
            temperature=0.5,  # Lower temperature for more focused output
            use_google=False  # Use Groq
        )
    
    def execute(self, state):
        # Your custom logic here
        result = self.invoke("Your prompt here")
        return {"result": result}

# Use the custom agent
agent = CustomAgent()
state = agent.execute({"task": "Your task"})
```

---

## 📁 Project Structure

```
langgraph-multi-agent-system/
│
├── 📄 Configuration Files
│   ├── .env.example              # Environment variables template
│   ├── .gitignore               # Git ignore rules
│   ├── requirements.txt         # Python dependencies
│   ├── README.md                # This comprehensive documentation
│   ├── SETUP.md                 # Detailed setup instructions
│   ├── API_KEYS_SETUP.md        # API keys setup guide
│   ├── MIGRATION_TO_GROQ.md     # Migration documentation
│   ├── run.sh                   # Linux/Mac run script
│   └── run.bat                  # Windows run script
│
├── 📂 config/                    # Configuration module
│   ├── __init__.py              # Module exports
│   └── settings.py               # Application settings & configuration
│
├── 📂 utils/                      # Utility functions
│   ├── __init__.py              # Module exports
│   ├── logger.py                 # Logging configuration with Loguru
│   └── helpers.py                # Helper functions (format, extract, retry, etc.)
│
├── 📂 tools/                       # LangChain tools
│   ├── __init__.py              # Tool exports
│   ├── search_tools.py          # Search & discovery tools
│   │   ├── fetch_trending_topics
│   │   └── search_articles
│   ├── data_tools.py             # Data processing tools
│   │   ├── process_data
│   │   └── summarize_text
│   └── analysis_tools.py         # Analysis tools
│       ├── analyze_sentiment
│       └── detect_patterns
│
├── 📂 agents/                      # Agent implementations
│   ├── __init__.py              # Agent exports
│   ├── base.py                   # Base agent class
│   ├── research_agents.py        # Research team agents
│   │   ├── ResearchAgent
│   │   └── DataCollectorAgent
│   ├── analysis_agents.py        # Analysis team agents
│   │   ├── AnalystAgent
│   │   └── SentimentAnalyzer
│   └── writing_agents.py         # Writing team agents
│       ├── WriterAgent
│       └── EditorAgent
│
├── 📂 workflows/                  # LangGraph workflows
│   ├── __init__.py              # Workflow exports
│   ├── single_agent.py          # Single agent workflow
│   └── multi_agent.py            # Multi-agent workflow
│
├── 📂 tests/                       # Test suite
│   ├── __init__.py              # Test module
│   ├── test_agents.py           # Agent unit tests
│   └── test_workflows.py        # Workflow integration tests
│
├── 📂 logs/                        # Application logs (auto-created)
│   └── app_YYYY-MM-DD.log       # Daily log files
│
└── 📱 app.py                       # Streamlit frontend application
```

### File Descriptions

**Configuration Files:**
- `.env.example`: Template for environment variables
- `requirements.txt`: All Python dependencies with versions

**Core Modules:**
- `config/settings.py`: Centralized configuration management
- `utils/logger.py`: Logging setup with file and console output
- `utils/helpers.py`: Reusable utility functions

**Tools:**
- `tools/search_tools.py`: Search and discovery functionality
- `tools/data_tools.py`: Data processing and summarization
- `tools/analysis_tools.py`: Sentiment analysis and pattern detection

**Agents:**
- `agents/base.py`: Base class for all agents with common functionality
- `agents/research_agents.py`: Agents for gathering information
- `agents/analysis_agents.py`: Agents for analyzing data
- `agents/writing_agents.py`: Agents for creating reports

**Workflows:**
- `workflows/single_agent.py`: Simple single-agent workflow
- `workflows/multi_agent.py`: Complex multi-agent coordination

**Frontend:**
- `app.py`: Complete Streamlit UI with all features

---

## 🔧 API Reference

### BaseAgent Class

The foundation for all agents in the system.

```python
class BaseAgent(ABC):
    """Base class for all agents."""
    
    def __init__(
        self,
        name: str,
        model_name: str = None,
        temperature: float = 0.7,
        use_google: bool = False
    ):
        """
        Initialize agent.
        
        Args:
            name: Agent name
            model_name: LLM model to use (default from settings)
            temperature: Model temperature (0.0-1.0)
            use_google: Use Google models instead of Groq
        """
    
    @abstractmethod
    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute agent's main task.
        
        Args:
            state: Current workflow state
            
        Returns:
            Updated state dictionary
        """
    
    def invoke(self, prompt: str) -> str:
        """
        Invoke the model with a prompt.
        
        Args:
            prompt: Text prompt for the model
            
        Returns:
            Model response as string
        """
```

### Research Agents

#### ResearchAgent

```python
class ResearchAgent(BaseAgent):
    """Agent specialized in gathering trending information."""
    
    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Gather trending topics and create overview.
        
        Returns:
            {
                "research_notes": str,
                "trending_topics": List[str],
                "next_agent": str
            }
        """
```

#### DataCollectorAgent

```python
class DataCollectorAgent(BaseAgent):
    """Agent specialized in gathering detailed information."""
    
    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Collect detailed data about topics.
        
        Returns:
            {
                "research_notes": str,
                "articles": List[Dict],
                "next_agent": str
            }
        """
```

### Analysis Agents

#### AnalystAgent

```python
class AnalystAgent(BaseAgent):
    """Agent specialized in analyzing trends and patterns."""
    
    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze research findings.
        
        Returns:
            {
                "analysis_results": str,
                "patterns": List[str],
                "next_agent": str
            }
        """
```

### Writing Agents

#### WriterAgent

```python
class WriterAgent(BaseAgent):
    """Agent specialized in creating final reports."""
    
    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create final report.
        
        Returns:
            {
                "final_report": str,
                "next_agent": "END"
            }
        """
```

### Tools API

#### fetch_trending_topics

```python
@tool
def fetch_trending_topics(
    timeframe: str = "week",
    limit: int = 5
) -> List[str]:
    """
    Fetch trending tech topics.
    
    Args:
        timeframe: Time period (day, week, month)
        limit: Maximum number of topics
    
    Returns:
        List of trending topic names
    """
```

#### search_articles

```python
@tool
def search_articles(
    topic: str,
    max_results: int = 3
) -> List[Dict[str, str]]:
    """
    Search for articles about a specific topic.
    
    Args:
        topic: Topic to search for
        max_results: Maximum number of articles
    
    Returns:
        List of article dictionaries with:
        - title: str
        - url: str
        - summary: str
        - source: str
        - date: str
    """
```

#### analyze_sentiment

```python
@tool
def analyze_sentiment(text: str) -> Dict[str, Any]:
    """
    Analyze sentiment of text content.
    
    Args:
        text: Text to analyze
    
    Returns:
        {
            "sentiment": str,  # "positive", "negative", "neutral", "mixed"
            "score": int,      # 0-100
            "confidence": int,  # 0-100
            "positive_signals": int,
            "negative_signals": int
        }
    """
```

---

## 🚀 Advanced Usage

### Custom Workflow Creation

Create your own workflow by extending the base classes:

```python
from langgraph.graph import StateGraph, END
from agents.base import BaseAgent

class CustomAgent(BaseAgent):
    def execute(self, state):
        # Your custom logic
        result = self.invoke(state.get("prompt", ""))
        return {"result": result, "next_agent": "end"}

def create_custom_workflow():
    workflow = StateGraph(YourState)
    
    def custom_node(state):
        agent = CustomAgent()
        return agent.execute(state)
    
    workflow.add_node("custom", custom_node)
    workflow.set_entry_point("custom")
    workflow.add_edge("custom", END)
    
    return workflow.compile()
```

### Adding New Tools

```python
from langchain_core.tools import tool

@tool
def my_custom_tool(param1: str, param2: int = 5) -> str:
    """
    Description of what this tool does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    """
    # Your tool logic here
    return "result"
```

Then import and use in workflows:

```python
from tools.my_tools import my_custom_tool

agent = create_react_agent(
    model=model,
    tools=[my_custom_tool, ...]
)
```

### Custom State Management

```python
from typing import TypedDict, Annotated, List
import operator

class CustomState(TypedDict):
    messages: Annotated[List, operator.add]
    custom_field: str
    data: Dict[str, Any]
```

### Error Handling Best Practices

```python
try:
    result = agent.execute(state)
except Exception as e:
    logger.error(f"Agent error: {e}")
    return {
        "error": str(e),
        "next_agent": "END"
    }
```

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_agents.py -v

# Run with coverage
pytest tests/ --cov=. --cov-report=html

# Run specific test
pytest tests/test_agents.py::test_research_agent_initialization -v
```

### Writing Tests

Example test structure:

```python
import pytest
from agents.research_agents import ResearchAgent

@pytest.fixture
def mock_state():
    return {
        "current_task": "Test task",
        "trending_topics": []
    }

def test_research_agent(mock_state):
    agent = ResearchAgent()
    result = agent.execute(mock_state)
    
    assert "research_notes" in result
    assert "trending_topics" in result
```

---

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. API Key Not Found

**Problem:**
```
⚠️ API keys not configured! Please set GROQ_API_KEY in .env file
```

**Solutions:**
- ✅ Verify `.env` file exists in project root
- ✅ Check that `GROQ_API_KEY=your_key` is in the file (no spaces around `=`)
- ✅ Ensure no quotes around the key: `GROQ_API_KEY="key"` ❌
- ✅ Correct format: `GROQ_API_KEY=key` ✅
- ✅ Restart Streamlit after changing `.env`

#### 2. Module Not Found Errors

**Problem:**
```
ModuleNotFoundError: No module named 'langchain_groq'
```

**Solutions:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade

# Or install specific package
pip install langchain-groq
```

#### 3. Import Errors

**Problem:**
```
ImportError: cannot import name 'ChatGroq' from 'langchain_groq'
```

**Solutions:**
- ✅ Update package: `pip install --upgrade langchain-groq`
- ✅ Check Python version: `python --version` (should be 3.9+)
- ✅ Verify conda environment is activated

#### 4. Port Already in Use

**Problem:**
```
Port 8501 is already in use
```

**Solutions:**
```bash
# Option 1: Use different port
streamlit run app.py --server.port 8502

# Option 2: Kill existing process (Windows)
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# Option 2: Kill existing process (Linux/Mac)
lsof -ti:8501 | xargs kill -9
```

#### 5. API Rate Limit Errors

**Problem:**
```
Rate limit exceeded
```

**Solutions:**
- ✅ Wait a few minutes and retry
- ✅ Check your Groq API quota
- ✅ Use a different model (smaller models have higher limits)
- ✅ Implement retry logic (already included)

#### 6. Model Not Found

**Problem:**
```
Model not found: llama-3.3-70b-versatile
```

**Solutions:**
- ✅ Check available models: https://console.groq.com/docs/models
- ✅ Update model name in `config/settings.py`
- ✅ Use alternative models like `llama-3.1-70b-versatile`

#### 7. Logging Issues

**Problem:**
Logs not appearing or file permission errors

**Solutions:**
```bash
# Check logs directory exists
mkdir -p logs

# Check permissions
chmod 755 logs

# Enable debug logging in .env
LOG_LEVEL=DEBUG
```

### Debug Mode

Enable detailed logging:

```bash
# In .env file
LOG_LEVEL=DEBUG

# Or in Streamlit sidebar
Enable "Verbose Logging" checkbox
```

Check logs:

```bash
# View latest log
tail -f logs/app_$(date +%Y-%m-%d).log

# Or on Windows
Get-Content logs\app_$(Get-Date -Format "yyyy-MM-dd").log -Tail 50 -Wait
```

---

## ⚡ Performance Tips

### 1. Model Selection

- **For Speed**: Use `llama-3.1-8b-instant`
- **For Quality**: Use `llama-3.3-70b-versatile`
- **For Balance**: Use `llama-3.1-70b-versatile`

### 2. Temperature Settings

- **Lower (0.2-0.5)**: More focused, deterministic
- **Medium (0.5-0.7)**: Balanced creativity
- **Higher (0.7-1.0)**: More creative, varied

### 3. Batch Processing

Process multiple tasks in parallel:

```python
from concurrent.futures import ThreadPoolExecutor

tasks = ["Task 1", "Task 2", "Task 3"]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(process_task, tasks))
```

### 4. Caching

Enable Streamlit caching for expensive operations:

```python
@st.cache_data
def expensive_operation(input_data):
    # Your expensive computation
    return result
```

### 5. Optimization Tips

- ✅ Use single agent for simple tasks (faster)
- ✅ Use multi-agent for complex analysis (better quality)
- ✅ Limit article searches to reduce API calls
- ✅ Cache frequent queries
- ✅ Use appropriate model sizes for tasks

---

## 🚢 Deployment

### Local Deployment

Already covered in Quick Start section.

### Streamlit Cloud Deployment

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Deploy to Streamlit Cloud:**
   - Visit https://streamlit.io/cloud
   - Sign in with GitHub
   - Click "New app"
   - Select repository and branch
   - Set main file: `app.py`
   - Add secrets:
     - `GROQ_API_KEY`: Your Groq API key

3. **Access your app:**
   - Your app will be available at `https://your-app.streamlit.app`

### Docker Deployment

**Create `Dockerfile`:**

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Build and run:**
```bash
docker build -t langgraph-multi-agent .
docker run -p 8501:8501 --env-file .env langgraph-multi-agent
```

### Environment Variables in Production

**Never commit `.env` file!** Use:
- Streamlit Cloud secrets
- Docker environment variables
- Cloud provider secrets management
- CI/CD pipeline secrets

---

## 🤝 Contributing

We welcome contributions! Here's how to contribute:

### Development Setup

```bash
# Fork the repository
git clone <your-fork-url>
cd langgraph-multi-agent-system

# Create feature branch
git checkout -b feature/amazing-feature

# Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black flake8 mypy

# Make your changes
# ... edit files ...

# Run tests
pytest tests/ -v

# Format code
black .

# Check linting
flake8 .

# Commit changes
git commit -m "Add amazing feature"

# Push to branch
git push origin feature/amazing-feature

# Open Pull Request
```

### Contribution Guidelines

1. **Code Style**: Follow PEP 8, use Black for formatting
2. **Testing**: Add tests for new features
3. **Documentation**: Update README and docstrings
4. **Commits**: Write clear commit messages
5. **PRs**: Provide description of changes

### Areas for Contribution

- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🧪 Additional tests
- 🎨 UI/UX enhancements
- 🚀 Performance optimizations
- 🔧 New tools and agents

---

## 📝 License

This project is licensed under the **MIT License**.

See `LICENSE` file for details.

---

## 🙏 Acknowledgments

- **LangGraph**: https://github.com/langchain-ai/langgraph
- **LangChain**: https://github.com/langchain-ai/langchain
- **Streamlit**: https://streamlit.io/
- **Groq**: https://groq.com/ (Free tier for Llama models)
- **Loguru**: https://github.com/Delgan/loguru

---

## 📞 Support & Resources

### Documentation

- **Setup Guide**: See `SETUP.md` for detailed setup instructions
- **API Keys Setup**: See `API_KEYS_SETUP.md` for API configuration
- **Migration Guide**: See `MIGRATION_TO_GROQ.md` for migration details

### Getting Help

1. **Check Documentation**: Read through this README and other docs
2. **Troubleshooting**: See [Troubleshooting](#-troubleshooting) section
3. **Issues**: Open an issue on GitHub
4. **Questions**: Check existing issues and discussions

### Useful Links

- **Groq Console**: https://console.groq.com
- **LangGraph Docs**: https://langchain-ai.github.io/langgraph/
- **Streamlit Docs**: https://docs.streamlit.io/
- **LangChain Docs**: https://python.langchain.com/

---

## 🎯 Use Cases

### Business Intelligence

- **Market Research**: Analyze industry trends and competitor information
- **Business Reports**: Generate comprehensive business analysis reports
- **Strategic Planning**: Research and analyze market opportunities

### Content Creation

- **Research Articles**: Create well-researched articles on topics
- **Blog Posts**: Generate blog content with research backing
- **Reports**: Create detailed reports with citations

### Research & Analysis

- **Academic Research**: Gather and analyze research information
- **Trend Analysis**: Identify and analyze emerging trends
- **Sentiment Analysis**: Analyze public sentiment on topics

### Education

- **Study Materials**: Generate comprehensive study guides
- **Research Assistance**: Help with research projects
- **Learning Resources**: Create educational content

---

## 🚀 Roadmap

Future enhancements planned:

- [ ] Real API integrations (Google Search, Twitter, Reddit)
- [ ] Database storage for research history
- [ ] Advanced analytics and visualization
- [ ] Multi-language support
- [ ] Agent performance metrics
- [ ] Custom agent builder UI
- [ ] Export to PDF and Word formats
- [ ] API endpoint for programmatic access
- [ ] Advanced caching strategies
- [ ] Agent orchestration improvements

---

## 📊 Project Statistics

- **Total Files**: 28+
- **Python Files**: 22
- **Test Files**: 2
- **Documentation Files**: 5
- **Agent Classes**: 6
- **Tools**: 6
- **Workflows**: 2

---

## ✅ Checklist for New Users

Use this checklist to get started:

- [ ] Python 3.9+ installed
- [ ] Repository cloned
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Groq API key obtained
- [ ] `.env` file created with `GROQ_API_KEY`
- [ ] Application runs successfully (`streamlit run app.py`)
- [ ] Tested single agent workflow
- [ ] Tested multi-agent workflow
- [ ] Read through documentation

---

## 🎓 Learning Resources

### Understanding Multi-Agent Systems

1. **LangGraph Documentation**: Learn about agent workflows
2. **LangChain Tutorials**: Understand agent concepts
3. **Groq Documentation**: Learn about available models

### Best Practices

1. Start with simple tasks using single agent
2. Progress to multi-agent for complex workflows
3. Experiment with different models and temperatures
4. Monitor API usage and costs
5. Use appropriate logging levels

---

## ❓ Frequently Asked Questions (FAQ)

### General Questions

#### Q: Do I need multiple API keys?
**A:** No! Only `GROQ_API_KEY` is required. All agents are configured to use Groq by default. Other API keys (Google, Anthropic) are optional.

#### Q: Is Groq really free?
**A:** Yes! Groq offers a generous free tier. You can get started immediately without any payment. Check https://console.groq.com for current limits.

#### Q: Can I use this without the Streamlit UI?
**A:** Absolutely! You can use the workflows and agents directly in Python code. The Streamlit UI is just a convenient interface.

#### Q: What Python version do I need?
**A:** Python 3.9 or higher is required. Python 3.10 is recommended for best compatibility.

#### Q: How fast is the system?
**A:** Response times depend on:
- Model selection (faster models like `llama-3.1-8b-instant` are quicker)
- Task complexity (single agent is faster than multi-agent)
- Network speed
- Typically: Single agent (10-30s), Multi-agent (30-90s)

### Technical Questions

#### Q: Can I customize agents?
**A:** Yes! All agents inherit from `BaseAgent`. You can:
- Create custom agents by extending `BaseAgent`
- Modify existing agents
- Change model parameters (temperature, model name)
- Add new tools and capabilities

#### Q: How do I add new tools?
**A:** 
1. Create a tool using `@tool` decorator in `tools/` directory
2. Add it to the appropriate `__init__.py`
3. Import and use in workflows or agents

Example:
```python
from langchain_core.tools import tool

@tool
def my_new_tool(param: str) -> str:
    """Tool description."""
    return f"Result: {param}"
```

#### Q: How do I change the model?
**A:** You have multiple options:
1. Edit `config/settings.py` and change `default_model`
2. Set environment variable: `DEFAULT_MODEL=llama-3.1-8b-instant`
3. Override in agent initialization

#### Q: Can I run this offline?
**A:** No, this requires internet connection for API calls to Groq and other services.

### Troubleshooting Questions

#### Q: Why am I getting rate limit errors?
**A:** Groq has rate limits on free tier. Solutions:
- Wait a few minutes and retry
- Use smaller models (they have higher limits)
- Reduce request frequency

#### Q: The app crashes on startup. What should I do?
**A:** 
1. Verify all dependencies are installed: `pip install -r requirements.txt`
2. Check your `.env` file exists and has `GROQ_API_KEY`
3. Ensure Python version is 3.9+
4. Check logs in `logs/` directory for errors

#### Q: How do I enable debug logging?
**A:** Set in `.env` file:
```env
LOG_LEVEL=DEBUG
```

Or in Streamlit sidebar, check "Verbose Logging".

### Deployment Questions

#### Q: Can I deploy this to production?
**A:** Yes! The system is production-ready. See [Deployment](#-deployment) section for:
- Streamlit Cloud deployment
- Docker deployment
- Custom server deployment

#### Q: Is it safe to commit my `.env` file?
**A:** **NO!** Never commit `.env` file with API keys. Always use:
- `.gitignore` (already configured)
- Environment secrets in deployment platforms
- Secure secret management services

#### Q: How do I scale this?
**A:** For scaling:
- Use faster models for high-volume requests
- Implement caching for repeated queries
- Use load balancing for multiple instances
- Consider database storage for history

### Feature Questions

#### Q: Can I use real search APIs instead of simulated data?
**A:** Yes! Modify `tools/search_tools.py` to integrate:
- Google Custom Search API
- Serper API
- Bing Search API
- Reddit API
- Twitter API

#### Q: How do I add database storage?
**A:** Add database integration:
```python
# Example with SQLite
import sqlite3

def save_result(result):
    conn = sqlite3.connect('results.db')
    # Save logic here
    conn.close()
```

#### Q: Can I export to other formats?
**A:** Yes! Currently supports Markdown. You can add:
- PDF export (using `reportlab` or `fpdf`)
- Word export (using `python-docx`)
- JSON export (already possible)
- HTML export (using templates)

---

## 🔐 Security Best Practices

### API Key Security

1. **Never commit `.env` file**
   ```bash
   # .gitignore already includes .env
   # Verify: git check-ignore .env
   ```

2. **Use environment variables in production**
   ```bash
   # Docker
   docker run -e GROQ_API_KEY=your_key ...
   
   # Kubernetes
   kubectl create secret generic api-keys --from-env-file=.env
   ```

3. **Rotate API keys regularly**
   - Update keys every 90 days
   - Revoke old keys when rotating
   - Use different keys for dev/prod

4. **Limit API key permissions**
   - Use read-only keys when possible
   - Set appropriate rate limits
   - Monitor usage regularly

### Code Security

1. **Validate all inputs**
   ```python
   def validate_task(task: str) -> bool:
       if not task or len(task) > 1000:
           return False
       return True
   ```

2. **Sanitize user inputs**
   - Escape special characters
   - Validate data types
   - Limit input lengths

3. **Use secure connections**
   - Always use HTTPS in production
   - Validate SSL certificates
   - Don't store sensitive data in logs

### General Security

1. **Keep dependencies updated**
   ```bash
   pip list --outdated
   pip install --upgrade <package>
   ```

2. **Review third-party code**
   - Audit dependencies
   - Check for known vulnerabilities
   - Use `pip-audit` tool

3. **Monitor for anomalies**
   - Track API usage patterns
   - Alert on unusual activity
   - Log security events

---

## 📈 Performance Benchmarks

### Response Times (Approximate)

| Workflow Type | Model | Average Time | Notes |
|--------------|-------|--------------|-------|
| Single Agent | llama-3.1-8b-instant | 10-20s | Fastest option |
| Single Agent | llama-3.3-70b-versatile | 20-40s | Better quality |
| Multi-Agent | llama-3.1-8b-instant | 40-70s | Fast multi-agent |
| Multi-Agent | llama-3.3-70b-versatile | 60-120s | Best quality |

*Times may vary based on network, API load, and task complexity*

### Resource Usage

- **Memory**: ~200-500MB (depending on model and workflow)
- **CPU**: Minimal (most work done via API)
- **Network**: Moderate (API calls to Groq)
- **Storage**: ~50MB (application + dependencies)

### Optimization Tips

1. **Use caching** for repeated queries
2. **Batch operations** when possible
3. **Choose appropriate models** for task complexity
4. **Limit article searches** to reduce API calls
5. **Use single agent** for simple tasks

---

## 🔄 Version History

### Version 1.0.0 (Current)
- ✅ Initial release
- ✅ Single and multi-agent workflows
- ✅ Complete agent teams (Research, Analysis, Writing)
- ✅ Comprehensive tool suite
- ✅ Streamlit UI with all features
- ✅ Full documentation
- ✅ Migration to Groq from OpenAI
- ✅ Production-ready error handling
- ✅ Logging system
- ✅ Test suite

### Planned Features (v1.1.0)
- 🔲 Real API integrations
- 🔲 Database storage
- 🔲 Advanced analytics
- 🔲 PDF/Word export
- 🔲 API endpoints
- 🔲 Performance metrics

---

## 📚 Quick Reference Guide

### Essential Commands

```bash
# Setup
conda create -n github python=3.10 -y
conda activate github
pip install -r requirements.txt

# Configuration
echo GROQ_API_KEY=your_key > .env

# Run
streamlit run app.py

# Test
pytest tests/ -v

# Check logs
tail -f logs/app_$(date +%Y-%m-%d).log
```

### Key Files to Modify

| File | Purpose | When to Modify |
|------|---------|----------------|
| `config/settings.py` | Model configuration | Change models or defaults |
| `agents/base.py` | Agent base class | Customize agent behavior |
| `tools/*.py` | Tools | Add new tools |
| `workflows/*.py` | Workflows | Create custom workflows |
| `.env` | Environment variables | Add API keys, change settings |

### Common Customizations

**Change default model:**
```python
# In config/settings.py
default_model: str = "llama-3.1-8b-instant"
```

**Change agent temperature:**
```python
# In agent __init__
super().__init__(name="Agent", temperature=0.3)
```

**Add new tool:**
```python
# In tools/my_tools.py
from langchain_core.tools import tool

@tool
def my_tool(param: str) -> str:
    """Tool description."""
    return result
```

---

## 🎬 Getting Started Video Tutorial

*(Add link to tutorial video if available)*

### Step-by-Step Visual Guide

1. **Installation** (2 minutes)
   - Clone repository
   - Create environment
   - Install dependencies

2. **Configuration** (1 minute)
   - Get Groq API key
   - Create `.env` file
   - Verify setup

3. **First Run** (1 minute)
   - Start Streamlit
   - Configure task
   - Execute workflow

4. **Customization** (5 minutes)
   - Modify agents
   - Add tools
   - Create workflows

---

## 🌍 Internationalization

Currently, the system is English-only. To add support for other languages:

1. **Translate UI elements** in `app.py`
2. **Add language detection** in tools
3. **Support multilingual models** (when available)
4. **Translate prompts** in agents

*Multi-language support planned for future versions*

---

## 📊 System Requirements

### Minimum Requirements

- **OS**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python**: 3.9 or higher (3.10 recommended)
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 1GB free space
- **Network**: Internet connection required

### Recommended Requirements

- **OS**: Latest stable version
- **Python**: 3.10 or 3.11
- **RAM**: 8GB or more
- **Storage**: 2GB free space
- **Network**: Stable broadband connection
- **CPU**: Modern multi-core processor

---

## 🔗 Integration Examples

### Integrate with Other Services

#### Add Slack Notifications

```python
import requests

def notify_slack(message: str):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    requests.post(webhook_url, json={"text": message})
```

#### Add Email Reports

```python
import smtplib
from email.mime.text import MIMEText

def send_email_report(report: str, recipient: str):
    msg = MIMEText(report)
    msg['Subject'] = 'Research Report'
    msg['To'] = recipient
    # Send email logic
```

#### Save to Database

```python
import sqlite3

def save_to_db(result: dict):
    conn = sqlite3.connect('results.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO results (report, timestamp) VALUES (?, ?)",
        (result['final_report'], datetime.now())
    )
    conn.commit()
    conn.close()
```

---

## 🏆 Best Practices

### Code Organization

1. **Follow the existing structure**
   - Agents in `agents/`
   - Tools in `tools/`
   - Workflows in `workflows/`
   - Utils in `utils/`

2. **Use type hints**
   ```python
   def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
       ...
   ```

3. **Add docstrings**
   ```python
   def my_function(param: str) -> str:
       """
       Description of function.
       
       Args:
           param: Description of param
       
       Returns:
           Description of return value
       """
   ```

### Workflow Design

1. **Start simple** - Use single agent first
2. **Iterate** - Build up to multi-agent
3. **Test thoroughly** - Test each component
4. **Document changes** - Update README as you modify

### Error Handling

1. **Always catch exceptions**
   ```python
   try:
       result = agent.execute(state)
   except Exception as e:
       logger.error(f"Error: {e}")
       return {"error": str(e)}
   ```

2. **Provide meaningful errors**
3. **Log errors appropriately**
4. **Don't expose sensitive information**

---

**Last Updated**: January 2025  
**Version**: 1.0.0  
**Status**: ✅ Production Ready

---

## 🚀 Want to Master More AI?

**Subscribe to my YouTube channel** for in-depth tutorials, hands-on coding sessions, and the latest AI insights! 📺✨

**👆 Hit that subscribe button and ring the notification bell to never miss cutting-edge content!**

---

## 🔗 Let's Connect & Collaborate!

I'm passionate about sharing knowledge and building amazing AI solutions. Let's connect:

### 📱 Social Media & Professional Links

| Platform | Link | Description |
|----------|------|-------------|
| 🐙 **GitHub** | [@MahendraMedapati27](https://github.com/MahendraMedapati27) | Check out my latest projects and code repositories |
| 💼 **LinkedIn** | [Mahendra Medapati](https://www.linkedin.com/in/mahendra-medapati-429239289/) | Connect for professional discussions and industry insights |
| 🐦 **X (Twitter)** | [@MahendraM27](https://x.com/MahendraM27) | Follow for updates, thoughts, and discussions on AI |
| 📧 **Email** | [mahendramedapati.r469@gmail.com](mailto:mahendramedapati.r469@gmail.com) | Reach out directly for inquiries or collaboration |

### ☕ Support This Project

If you find this project helpful, consider **buying me a coffee** to support continued development! ☕✨

<div align="center">

<a href="https://buymeacoffee.com/mahendramedapati" target="_blank">
  <img src="Images/1_CEZSIxeYr6PCxsN6Gr38MQ.png" alt="Buy Me A Coffee" width="300">
</a>

<br>

<a href="https://buymeacoffee.com/mahendramedapati" target="_blank">
  <strong>☕ Buy Me a Coffee</strong>
</a>

</div>

---

<div align="center">

**⭐ If you find this project helpful, please star it on GitHub! ⭐**

Made with ❤️ using LangGraph 1.0 & Groq

[Report Bug](https://github.com/MahendraMedapati27/langgraph-multi-agent-system/issues) • [Request Feature](https://github.com/MahendraMedapati27/langgraph-multi-agent-system/issues) • [Documentation](SETUP.md)

</div>
