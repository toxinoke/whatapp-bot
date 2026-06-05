# WhatsApp Bot Configuration

# Bot name
BOT_NAME = "WhatsApp Bot"

# Bot welcome message
WELCOME_MESSAGE = "Hello! Welcome to WhatsApp Bot. Type 'help' for available commands."

# Command responses
COMMANDS = {
    'hello': 'Hi there! 👋 How can I help you today?',
    'help': 'Available commands:\n- hello\n- help\n- status',
    'status': '🟢 Bot is online and working!',
}

# Default response for unknown commands
DEFAULT_RESPONSE = "I didn't understand that. Type 'help' for available commands."

# Server configuration
HOST = '0.0.0.0'
PORT = 5000
DEBUG = True
