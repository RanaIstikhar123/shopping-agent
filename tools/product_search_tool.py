from typing import Type, List
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class ProductSearchInput(BaseModel):
    """Input schema for ProductSearchTool."""
    query: str = Field(..., description="The search query for products")
    category: str = Field(..., description="The category of products to search for")
    max_results: int = Field(default=5, description="Maximum number of results to return")

class ProductSearchTool(BaseTool):
    name: str = "Product Search Tool"
    description: str = (
        "A tool to search for products using the Amazon Product API. "
        "It can find products based on category and search query, "
        "returning details like title, price, and ratings."
    )
    args_schema: Type[BaseModel] = ProductSearchInput

    def _run(self, query: str, category: str, max_results: int = 5) -> str:
        try:
            # In a real implementation, you would use the Amazon Product API
            # For now, we'll return a mock response
            return f"""Found {max_results} products in {category} matching '{query}':
            
1. Product 1
   - Title: {query} Premium Model
   - Price: $299.99
   - Rating: 4.5/5
   - Reviews: 128

2. Product 2
   - Title: {query} Standard Model
   - Price: $199.99
   - Rating: 4.2/5
   - Reviews: 95

3. Product 3
   - Title: {query} Basic Model
   - Price: $149.99
   - Rating: 4.0/5
   - Reviews: 75"""
        except Exception as e:
            return f"Error searching for products: {str(e)}" 