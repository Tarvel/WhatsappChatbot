# WhatsappChatbot using Flask + Google Gemini

A Flask-based webhook that connects to the WhatsApp Cloud API to receive incoming messages, uses Google Gemini to generate AI-powered responses, and sends them back via WhatsApp.

---

## 📌 Features

- ✅ WhatsApp Cloud API integration
- 🤖 AI responses powered by Google Gemini API
- 📬 Automated message replies in real time
- 🔒 Environment variable support using `python-dotenv`
- 🧪 Webhook verification endpoint

---

## 🔧 Stack

- Python
- Flask
- WhatsApp Cloud API (via Meta Graph API)
- Google Gemini (Generative Language API)
- dotenv

---

## 🚀 How It Works

1. User sends a message to your connected WhatsApp number.
2. WhatsApp forwards the message to your Flask webhook.
3. Flask sends the message content to Google Gemini for processing.
4. Gemini generates a natural-language reply.
5. Flask sends the reply back to the user via WhatsApp.

---


