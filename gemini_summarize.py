import google.generativeai as genai

with open('googleapikey.txt', 'r') as f:
    GOOGLE_API_KEY = f.read()
    f.close()

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_summary(transcript):
    prompt = """Summarize and take notes on the following transcript from a lecture:
    
    """ + transcript
    response = model.generate_content(prompt)
    return response.text
