import requests
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TELEGRAM_TOKEN = "PASTE_YOUR_NEW_TOKEN_HERE"
AI_API_KEY = "PASTE_YOUR_AI_KEY_HERE"

def call_ai_model(system_prompt: str, user_message: str) -> str:
    headers = {
        "Authorization": f"Bearer " + AI_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "model": "your-model-name",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    }
    response = requests.post("https://api.your-llm-provider.com/v1/chat/completions",
                             json=payload, headers=headers)
    return response.json()["choices"][0]["message"]["content"].strip()

async def start(update, context):
    await update.message.reply_text("Welcome to Research Assistant Bot. Use /paper /summary /idea /jp to begin.")

async def handle_message(update, context):
    user_text = update.message.text
    system = "You are a helpful research assistant for a student in swarm robotics in Japan."
    reply = call_ai_model(system, user_text)
    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
