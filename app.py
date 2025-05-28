from flask import Flask, request
import requests, json, os
from dotenv import load_dotenv
from send import send_whatsapp_message
from ai_exp import generate_ai_explanation

load_dotenv()

VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')
BEARER_API_KEY = os.getenv('BEARER_API_KEY')
AI_API_KEY = os.getenv('AI_API_KEY')

app = Flask(__name__)


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        return "Verification failed", 403

    data = request.get_json()
    print("Received payload:", json.dumps(data, indent=2)) 
    
    try:
        changes = data.get('entry', [{}])[0].get('changes', [{}])[0]
        value = changes.get('value', {})
        
        if 'messages' not in value or changes.get('field') != 'messages':
            return "OK - Non-message event", 200
            
        messages = value.get('messages', [{}])[0]
        contacts = value.get('contacts', [{}])[0]
        
        name = contacts.get('profile', {}).get('name', 'Unknown User')
        text_body = messages.get('text', {}).get('body', '')
        number = contacts.get('wa_id', None) or value.get('metadata', {}).get('phone_number_id', '')
        
        if not text_body or not number:
            return "OK - Missing required fields", 200

        message = generate_ai_explanation(text_body, AI_API_KEY)
        send_whatsapp_message(message, number, BEARER_API_KEY)
        return "OK", 200
        
    except Exception as e:
        print(f"Error processing webhook: {str(e)}")
        return "Error", 500

if __name__ == '__main__':
    app.run(debug=False)