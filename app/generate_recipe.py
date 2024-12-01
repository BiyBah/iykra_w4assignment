import google.generativeai as genai
import os
from dotenv import load_dotenv

def generate_recipe(user_text):
    system_instruction = f"""
    You are a food expert, helping people get the ingredients and how to make food based on food name input by user.
    Your response must be concise, accurate and fill the (...) on this template:
    Food name: 
    ...
    Ingredients: 
    ...
    How to make: 
    ...

    If the user doesn't provide a food name, ignore the template above, apologize and ask them to provide one.
    """
    
    # Load environment variables
    # gemini_api_key = 'AIzaSyAlbj87lJSG7qeTzdy7lqkvwinFdjoZyc8'
    
    # if not gemini_api_key:
    #     return {"error": "API key not found. Please set the GOOGLE_API_KEY in the .env file."}
    
    genai.configure(api_key='AIzaSyAlbj87lJSG7qeTzdy7lqkvwinFdjoZyc8')

    # Check if the user has provided input
    if not user_text or len(user_text.strip()) < 1:
        return {"error": "Please provide a food name"}

    # Set up the generative model
    model = genai.GenerativeModel("gemini-1.5-flash-8b",
                                 generation_config=genai.types.GenerationConfig(
                                     temperature=0.0,
                                     max_output_tokens=200
                                 ),
                                 system_instruction=system_instruction)

    try:
        # Generate the content
        response = model.generate_content([user_text])
        return {
            "AI response": response.text.strip() if hasattr(response, 'text') else "No response from AI"
        }
    except Exception as e:
        return {
            "error": str(e)
        }
