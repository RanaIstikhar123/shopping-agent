from typing import Type, List
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class BudgetCalculatorInput(BaseModel):
    """Input schema for BudgetCalculatorTool."""
    total_budget: float = Field(..., description="The total budget available")
    category: str = Field(..., description="The category of products to budget for")
    number_of_items: int = Field(..., description="Number of items to budget for")

class BudgetCalculatorTool(BaseTool):
    name: str = "Budget Calculator Tool"
    description: str = (
        "A tool to help calculate and manage shopping budgets. "
        "It provides recommendations for allocating budget across different products "
        "and suggests price ranges for each item."
    )
    args_schema: Type[BaseModel] = BudgetCalculatorInput

    def _run(self, total_budget: float, category: str, number_of_items: int) -> str:
        try:
            # Calculate price ranges
            max_per_item = total_budget / number_of_items
            min_per_item = max_per_item * 0.7  # 70% of max for flexibility
            
            return f"""Budget Analysis for {category} Shopping:

Total Budget: ${total_budget:.2f}
Number of Items: {number_of_items}

Recommended Price Ranges:
- Maximum per item: ${max_per_item:.2f}
- Minimum per item: ${min_per_item:.2f}

Budget Allocation Suggestions:
1. Primary Item (40%): ${max_per_item:.2f}
2. Secondary Items (30% each): ${min_per_item:.2f}

Tips for Staying Within Budget:
1. Look for items in the ${min_per_item:.2f} - ${max_per_item:.2f} range
2. Consider refurbished or open-box items for savings
3. Watch for sales and promotions
4. Compare prices across different retailers
5. Consider buying in bulk for better deals

Would you like me to search for specific products within these price ranges?"""
        except Exception as e:
            return f"Error calculating budget: {str(e)}" 