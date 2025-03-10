from typing import Type, List
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class ReviewAnalysisInput(BaseModel):
    """Input schema for ReviewAnalysisTool."""
    product_name: str = Field(..., description="The name of the product to analyze reviews for")
    category: str = Field(..., description="The category of the product")

class ReviewAnalysisTool(BaseTool):
    name: str = "Review Analysis Tool"
    description: str = (
        "A tool to analyze product reviews and provide insights about the product's "
        "strengths, weaknesses, and overall customer satisfaction."
    )
    args_schema: Type[BaseModel] = ReviewAnalysisInput

    def _run(self, product_name: str, category: str) -> str:
        try:
            # In a real implementation, you would fetch and analyze reviews from various sources
            # For now, we'll return a mock response
            return f"""Review Analysis for {product_name} in {category}:

Overall Rating: 4.5/5 (based on 1,234 reviews)

Key Strengths:
1. Excellent build quality
2. Great performance
3. User-friendly interface
4. Good battery life
5. Responsive customer support

Common Complaints:
1. Price is slightly high
2. Initial setup could be easier
3. Some users reported minor software bugs

Customer Satisfaction Trends:
- 85% of customers would recommend this product
- 92% of customers are satisfied with the purchase
- Average rating has increased by 0.2 points in the last 3 months

Most Recent Reviews:
1. "Excellent product, worth every penny!" (5/5)
2. "Great features but a bit expensive" (4/5)
3. "Perfect for my needs" (5/5)"""
        except Exception as e:
            return f"Error analyzing reviews: {str(e)}" 