from typing import Type, List
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class PriceComparisonInput(BaseModel):
    """Input schema for PriceComparisonTool."""
    product_name: str = Field(..., description="The name of the product to compare prices for")
    category: str = Field(..., description="The category of the product")

class PriceComparisonTool(BaseTool):
    name: str = "Price Comparison Tool"
    description: str = (
        "A tool to compare prices of products across different retailers. "
        "It provides price information from various sources to help find the best deal."
    )
    args_schema: Type[BaseModel] = PriceComparisonInput

    def _run(self, product_name: str, category: str) -> str:
        try:
            # In a real implementation, you would fetch prices from multiple retailers
            # For now, we'll return a mock response
            return f"""Price comparison for {product_name} in {category}:

1. Amazon
   - Price: $299.99
   - Shipping: Free
   - Total: $299.99
   - Stock: In Stock

2. Best Buy
   - Price: $319.99
   - Shipping: Free
   - Total: $319.99
   - Stock: In Stock

3. Walmart
   - Price: $309.99
   - Shipping: Free
   - Total: $309.99
   - Stock: In Stock

Best Price: Amazon at $299.99"""
        except Exception as e:
            return f"Error comparing prices: {str(e)}" 