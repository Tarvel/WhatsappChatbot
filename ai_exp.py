import requests, json

def generate_ai_explanation(text_body, AI_API_KEY):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-thinking-exp-01-21:generateContent?key={AI_API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": text_body
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 1.5,
            "topK": 64,
            "topP": 0.95,
            "maxOutputTokens": 3000,
            "responseMimeType": "text/plain"
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        response_data = response.json()
        try:
            text = response_data['candidates'][0]['content']['parts'][0]['text']
            return text
        except (KeyError, IndexError) as e:
            print('Error extracting text:', e)
    else:
        print(f'Failed to generate content. Status code: {response.status_code}')
        print('Response:', response.text)
