import google.generativeai as genai
import gradio as gr
import os

# Configure API key for Google Generative AI
genai.configure(api_key="AIzaSyDvpSGZ5YEjX8gY_2FE-8CBopO9G9Bn2xE")

# Function to generate content using Gemini model
def chatbot(input):
    model = genai.GenerativeModel("gemini-1.5-flash")  # Use the specific model name
    response = model.generate_content(input)
    return response.text

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Gemini AI Chatbot")
    
    # Input box for user message
    with gr.Row():
        chatbot_input = gr.Textbox(label="Chat with AI", placeholder="Ask anything...", lines=7)
    
    # Output box for bot's reply
    chatbot_output = gr.Textbox(label="Bot's Reply", placeholder="Bot's response will appear here")
    
    # Button to submit user input and generate response
    submit_button = gr.Button("Submit")
    
    # Link the submit button to the chatbot function
    submit_button.click(fn=chatbot, inputs=chatbot_input, outputs=chatbot_output)

# Launch the Gradio interface
demo.launch(share=True)
