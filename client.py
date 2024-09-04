import google.generativeai as genai

API_KEY = "AIzaSyD7yR5UBY4UJjrDXoNFI_1X9k3qxJlFTi0" 
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("What is coding")
print(response.text)