from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Twilio client
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)
twilio_phone = os.getenv('TWILIO_PHONE_NUMBER')

@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle incoming WhatsApp messages"""
    incoming_msg = request.values.get('Body', '').lower()
    sender = request.values.get('From')
    
    # Create response
    resp = MessagingResponse()
    
    # Simple command handling
    if 'hello' in incoming_msg:
        resp.message('Hi there! 👋 How can I help you today?')
    elif 'help' in incoming_msg:
        resp.message('Available commands:\n- hello\n- help\n- status')
    elif 'status' in incoming_msg:
        resp.message('🟢 Bot is online and working!')
    else:
        resp.message('I didn\'t understand that. Type "help" for available commands.')
    
    return str(resp)

@app.route('/send-message', methods=['POST'])
def send_message():
    """Send a message to a WhatsApp user"""
    data = request.json
    to_number = data.get('to')
    message_text = data.get('message')
    
    if not to_number or not message_text:
        return {'error': 'Missing "to" or "message" field'}, 400
    
    try:
        message = client.messages.create(
            from_=twilio_phone,
            body=message_text,
            to=f'whatsapp:{to_number}'
        )
        return {'success': True, 'sid': message.sid}, 200
    except Exception as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
