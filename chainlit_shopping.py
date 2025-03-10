import chainlit as cl
from crews.shopping_crew.shopping_crew import ShoppingCrew
import json
import uuid
from typing import Optional

# Store user session data
user_sessions = {}

@cl.on_chat_start
async def on_chat_start():
    # Generate a unique session ID
    session_id = str(uuid.uuid4())
    
    # Initialize session data
    user_sessions[session_id] = {
        "current_step": "category",
        "category": None,
        "requirements": None,
        "budget": None
    }
    
    # Store session ID in user session
    cl.user_session.set("session_id", session_id)
    
    # Send welcome message
    await cl.Message(
        content="""👋 Welcome to your AI Shopping Assistant! 🛍️

I'm here to help you find the perfect products. Let's start by selecting a category.

Available categories:
1. Electronics
2. Fashion
3. Home & Kitchen
4. Books
5. Sports & Outdoors
6. Other

Please type the category you're interested in:"""
    ).send()

@cl.on_message
async def main(message: cl.Message):
    # Get session ID from user session
    session_id = cl.user_session.get("session_id")
    if not session_id:
        session_id = str(uuid.uuid4())
        cl.user_session.set("session_id", session_id)
    
    session = user_sessions.get(session_id, {
        "current_step": "category",
        "category": None,
        "requirements": None,
        "budget": None
    })
    
    if session["current_step"] == "category":
        # Store the category and ask for budget
        session["category"] = message.content
        session["current_step"] = "budget"
        
        await cl.Message(
            content=f"""Great! You're interested in {message.content}. 
            
Please select your budget range:
1. Under $50
2. $50 - $200
3. $200 - $500
4. $500 - $1000
5. Over $1000
6. Flexible

Type your budget range:"""
        ).send()
        
    elif session["current_step"] == "budget":
        # Store the budget and ask for requirements
        session["budget"] = message.content
        session["current_step"] = "requirements"
        
        await cl.Message(
            content=f"""Perfect! Now, please tell me your specific requirements.

You can include:
1. Must-have features
2. Preferred brands
3. Number of items
4. Specific preferences

Type your requirements:"""
        ).send()
        
    elif session["current_step"] == "requirements":
        # Store requirements and start the shopping process
        session["requirements"] = message.content
        session["current_step"] = "processing"
        
        # Send a "thinking" message
        await cl.Message(
            content="""🔍 Analyzing your requirements and searching for the best products...
            
This may take a few moments while I:
1. Research products in your category
2. Compare prices across retailers
3. Analyze customer reviews
4. Generate personalized recommendations"""
        ).send()
        
        try:
            # Initialize shopping crew
            shopping_crew = ShoppingCrew()
            
            # Execute the shopping process
            result = shopping_crew.crew().kickoff(
                inputs={
                    "category": session["category"],
                    "requirements": session["requirements"],
                    "budget": session["budget"]
                }
            )
            
            # Format and send the results
            await cl.Message(
                content=f"""✨ Here are your personalized shopping recommendations:

```
{result.raw}
```

What would you like to do next?
1. Start a new search
2. Refine current requirements
3. Compare prices for specific products
4. Get detailed review analysis

Type your choice:"""
            ).send()
            
            # Reset the session for new searches
            session["current_step"] = "category"
            
        except Exception as e:
            await cl.Message(
                content=f"""❌ I apologize, but I encountered an error while processing your request.
                
Please try again with your product category. Error: {str(e)}

Type 'retry' to start over:"""
            ).send()
            session["current_step"] = "category"
    
    # Update session data
    user_sessions[session_id] = session

if __name__ == "__main__":
    print("To run this app, use the command:")
    print("  chainlit run chainlit_shopping.py -w") 