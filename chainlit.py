import chainlit as cl
import sys
import os
from main import PoemFlow

# Ensure required dependencies are installed
try:
    import chainlit
except ImportError:
    print("Chainlit is not installed. Please install it using: pip install chainlit")
    sys.exit(1)

@cl.on_chat_start
async def on_chat_start():
    # Set the welcome message
    await cl.Message(
        content="""👋 Welcome to the AI Poem Generator! 🎨

This chatbot specializes in creating unique and creative poems. Here's how to use it:

1. Simply type 'generate poem' to create a new poem
2. Each poem will be unique and randomly generated
3. The bot will create poems about CrewAI in different styles

To get started, type 'generate poem' and let the creativity flow! ✨
"""
    ).send()

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content.strip().lower()
    
    if user_input == "generate poem":
        # Send a "thinking" message
        await cl.Message(content="🤔 Creating your masterpiece...").send()
        
        print("Generating a poem...")
        poem_flow = PoemFlow()
        poem_flow.kickoff()
        
        # Read the generated poem
        try:
            with open("poem.txt", "r", encoding="utf-8") as f:
                poem = f.read()
            await cl.Message(content=f"✨ Here's your poem:\n\n```\n{poem}\n```\n\nType 'generate poem' to create another one!").send()
        except FileNotFoundError:
            await cl.Message(content="❌ Oops! Poem generation failed. Please try again.").send()
    else:
        await cl.Message(content="🎯 To create a new poem, please type 'generate poem'").send()

if __name__ == "__main__":
    print("To run this app, use the command:")
    print("  chainlit run chainlit.py -w")

