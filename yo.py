from google import genai

API='AIzaSyCdx7oSFOXW2ZFfKbHLZwhfSUc2OrPeBOM'

client = genai.Client(api_key=API)
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works"
)
print(response.text)