from typing import List, Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QueryPlanner:
    """
    Agentic Query Planner for decomposing complex RAG inquiries.
    Determines whether a query needs multi-hop retrieval or decomposition.
    """
    def __init__(self, model: Any):
        """
        Args:
            model: An initialized LLM client (e.g., LangChain OpenAI wrapper).
        """
        self.model = model

    def decompose(self, query: str) -> List[str]:
        """
        Analyzes a user query and breaks it into atomic sub-questions.
        
        Args:
            query: The original user input.
            
        Returns:
            A list of sub-queries for independent retrieval.
        """
        logger.info(f"Decomposing query: {query}")
        
        # Simplified logic: In production, this would be an LLM call with a specific prompt
        # Prompt: "Decompose this query into sub-questions if complex: {query}"
        
        if "and" in query.lower() or "compare" in query.lower():
            # Mock decomposition for demonstration
            sub_queries = [
                f"Identify key data points for the first entity in: {query}",
                f"Identify key data points for the second entity in: {query}"
            ]
            return sub_queries
        
        return [query]

    def should_search_web(self, query: str) -> bool:
        """
        Heuristic to determine if external search is required.
        """
        real_time_keywords = ["latest", "current", "today", "stock price"]
        return any(k in query.lower() for k in real_time_keywords)

    def route_query(self, query: str) -> str:
        """
        Routes query to specific expert chains (e.g., Financial, Technical, Legal).
        """
        # Logic for domain-specific routing
        return "GENERAL"
