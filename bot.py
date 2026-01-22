import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TELEGRAM_TOKEN = "YOUR_ACTU8319657690:AAEHsOOQqrcmriSHWLkYqC4K5wI2ZPxmBt8AL_TOKEN"
AI_API_KEY = "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"

def call_ai_model(system_prompt: str, user_message: str) -> str:
    headers = {
        "Authorization": f"Bearer {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}",
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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Research Assistant Bot. Use /paper /summary /idea /jp to begin.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    system = "You are a helpful research assistant for a student in swarm robotics in Japan."
    reply = call_ai_model(system, user_text)
    await update.message.reply_text(reply)

async def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Webhook setup
    PORT = int(os.environ.get("PORT", 8443))
    await app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url="https://research-bot-1.onrender.com"
    )

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()

