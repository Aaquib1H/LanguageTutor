import os

# Get the API key from an environment variable
API_KEY = os.getenv('OPENAI_API_KEY')

# Check if the API key was provided
if not API_KEY:
    raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable.")

# Now, you can use this API_KEY in your application as needed
