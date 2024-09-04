import google.generativeai as genai

API_KEY = <API_KEY>
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("What is coding")
print(response.text)
