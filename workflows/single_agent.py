"""
Single Agent Workflow
"""
from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from config.settings import settings
from tools.search_tools import fetch_trending_topics, search_articles
from tools.analysis_tools import analyze_sentiment
from utils.logger import get_logger
import operator

logger = get_logger(__name__)

class SingleAgentState(TypedDict):
    """State for single agent workflow."""
    messages: Annotated[List, operator.add]
    task: str
    result: str

def create_single_agent_system():
    """
    Create a simple single-agent research system.
    
    Returns:
        Compiled LangGraph application
    """
    logger.info("Creating single agent system")
    
    # Create the agent with tools
    model = ChatGroq(
        model=settings.default_model,
        temperature=0.7,
        groq_api_key=settings.groq_api_key
    )
    
    agent = create_react_agent(
        model=model,
        tools=[
            fetch_trending_topics,
            search_articles,
            analyze_sentiment
        ]
    )
    
    # Define the workflow
    def process_task(state: SingleAgentState):
        """Process the task using the agent."""
        logger.info("Single agent processing task")
        
        task = state.get('task', 'Research trending tech topics')
        
        prompt = f"""You are a research assistant. Complete this task:

{task}

Use the available tools to:
1. Fetch trending topics
2. Search for relevant articles
3. Analyze the sentiment

Then provide a concise summary (200-300 words)."""
        
        try:
            response = agent.invoke({
                "messages": [{"role": "user", "content": prompt}]
            })
            
            result = response["messages"][-1].content
            
            return {
                "result": result,
                "messages": [{"role": "assistant", "content": result}]
            }
        
        except Exception as e:
            logger.error(f"Single agent error: {str(e)}")
            return {
                "result": f"Error: {str(e)}",
                "messages": [{"role": "assistant", "content": f"Error: {str(e)}"}]
            }
    
    # Build the graph
    workflow = StateGraph(SingleAgentState)
    workflow.add_node("process", process_task)
    workflow.set_entry_point("process")
    workflow.add_edge("process", END)
    
    return workflow.compile()

