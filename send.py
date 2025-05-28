import requests
import json

def send_whatsapp_message(message, number, BEARER_API_KEY):
    url = 'https://graph.facebook.com/v22.0/520773607795648/messages'
    headers = {
        'Authorization': f'Bearer {BEARER_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        'messaging_product': 'whatsapp',
        'to': number,
        'type': 'text',
        'text': {
            'body': message
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print('Message sent successfully.')
    else:
        print(f'Failed to send message. Status code: {response.status_code}')
        print(f'Response: {response.text}')