# AI Shopping Assistant 🛍️

An intelligent shopping assistant powered by CrewAI and Chainlit that helps users find the perfect products based on their requirements, budget, and preferences.

## Features ✨

- **Smart Product Research**: Find products based on detailed requirements and preferences
- **Price Comparison**: Compare prices across different retailers
- **Review Analysis**: Get insights from customer reviews
- **Budget Planning**: Stay within your budget while finding the best value
- **Interactive UI**: User-friendly interface built with Chainlit
- **Multi-Agent System**: Powered by CrewAI for comprehensive product analysis

## Prerequisites 📋

- Python 3.8 or higher
- Google Gemini API key
- Required Python packages (listed in requirements.txt)

## Installation 🚀

1. Clone the repository:
```bash
git clone <your-repository-url>
cd shopping_agent
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

4. Create a `.env` file in the project root and add your Google Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage 💡

1. Start the Chainlit interface:
```bash
chainlit run shopping_agent/src/shopping_agent/chainlit_shopping.py -w
```

2. Open your browser and navigate to `http://localhost:8000`

3. Follow the interactive prompts to:
   - Select a product category
   - Specify your budget
   - Provide your requirements
   - Get personalized recommendations

## Project Structure 📁

```
shopping_agent/
├── src/
│   └── shooping_agent/
│       ├── chainlit_shopping.py    # Main Chainlit interface
│       ├── crews/
│       │   └── shopping_crew/      # Shopping crew implementation
│       └── tools/                  # Custom tools for product research
├── .chainlit/                      # Chainlit configuration
├── requirements.txt                # Project dependencies
└── README.md                       # This file
```

## Tools 🔧

The project includes several specialized tools:

- **ProductSearchTool**: Searches for products based on requirements
- **PriceComparisonTool**: Compares prices across retailers
- **ReviewAnalysisTool**: Analyzes customer reviews
- **BudgetCalculatorTool**: Helps with budget planning

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- [CrewAI](https://github.com/joaomdmoura/crewAI) for the multi-agent framework
- [Chainlit](https://github.com/Chainlit/chainlit) for the UI components
- [Google Gemini](https://ai.google.dev/) for the language model 
