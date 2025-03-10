from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from typing import List
from shooping_agent.tools.product_search_tool import ProductSearchTool
from shooping_agent.tools.price_comparison_tool import PriceComparisonTool
from shooping_agent.tools.review_analysis_tool import ReviewAnalysisTool
from shooping_agent.tools.budget_calculator_tool import BudgetCalculatorTool

@CrewBase
class ShoppingCrew:
    """Shopping Assistant Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            google_api_key=os.getenv("GEMINI_API_KEY"),
            temperature=0.7,
            convert_system_message_to_human=True
        )
        
        # Initialize tools
        self.product_search_tool = ProductSearchTool()
        self.price_comparison_tool = PriceComparisonTool()
        self.review_analysis_tool = ReviewAnalysisTool()
        self.budget_calculator_tool = BudgetCalculatorTool()

    @agent
    def product_researcher(self) -> Agent:
        """Creates an agent that researches products and their specifications."""
        return Agent(
            role="Product Research Specialist",
            goal="Find and analyze products based on user requirements",
            backstory="""You are an expert product researcher with years of experience 
            in analyzing product specifications, features, and customer reviews. 
            You have a keen eye for detail and can identify the best products that 
            match customer requirements.""",
            tools=[self.product_search_tool, self.review_analysis_tool],
            llm=self.llm
        )

    @agent
    def price_analyst(self) -> Agent:
        """Creates an agent that analyzes prices and finds the best deals."""
        return Agent(
            role="Price Analysis Expert",
            goal="Find the best deals and analyze price-to-value ratios",
            backstory="""You are a skilled price analyst who specializes in finding 
            the best deals and determining if products provide good value for money. 
            You have extensive experience in price comparison and market analysis.""",
            tools=[self.price_comparison_tool, self.budget_calculator_tool],
            llm=self.llm
        )

    @agent
    def shopping_advisor(self) -> Agent:
        """Creates an agent that provides personalized shopping recommendations."""
        return Agent(
            role="Shopping Advisor",
            goal="Provide personalized shopping recommendations",
            backstory="""You are a professional shopping advisor with expertise in 
            understanding customer needs and providing tailored recommendations. 
            You excel at balancing features, price, and quality to suggest the 
            perfect products.""",
            tools=[self.product_search_tool, self.price_comparison_tool, self.review_analysis_tool],
            llm=self.llm
        )

    @task
    def research_products(self, category: str, requirements: str) -> Task:
        """Task to research products based on user requirements."""
        return Task(
            description=f"""Research products in the {category} category that match 
            the following requirements: {requirements}. 
            Use the product search tool to find relevant products and the review analysis tool 
            to understand customer feedback. Focus on finding products that best match the user's needs.""",
            agent=self.product_researcher
        )

    @task
    def analyze_prices(self, products: List[str], budget: float) -> Task:
        """Task to analyze prices of the researched products."""
        return Task(
            description=f"""Analyze the prices of the following products: {products}. 
            Use the price comparison tool to find the best deals across different retailers.
            Use the budget calculator tool to ensure recommendations stay within the user's budget of ${budget}.
            Determine the price-to-value ratio for each product.""",
            agent=self.price_analyst
        )

    @task
    def make_recommendations(self, research: str, price_analysis: str) -> Task:
        """Task to provide final recommendations based on research and price analysis."""
        return Task(
            description=f"""Based on the product research: {research} 
            and price analysis: {price_analysis}, provide personalized shopping 
            recommendations. Consider the best balance of features, price, and quality.
            Use all available tools to provide comprehensive recommendations that include:
            1. Product details and features
            2. Price comparisons
            3. Review analysis
            4. Budget considerations""",
            agent=self.shopping_advisor
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Shopping Assistant Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            planning=True,
            planner=self.llm
        ) 