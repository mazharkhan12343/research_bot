
#TELEGRAM_TOKEN = "YOUR_ACTU8319657690:AAEHsOOQqrcmriSHWLkYqC4K5wI2ZPxmBt8AL_TOKEN"
#AI_API_KEY = "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"

import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TELEGRAM_TOKEN = "YOUR_TELYOUR_ACTU8319657690:AAEHsOOQqrcmriSHWLkYqC4K5wI2ZPxmBt8AL_TOKENEGRAM_TOKEN"
AI_API_KEY = "YOUR_AI_KEY"

def call_ai_model(system_prompt, user_message):
    headers = {
        "Authorization": f"Bearer {AI_gsk_tw4cEcPHkgfXEWP0OAPI_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    }
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        json=payload,
        headers=headers
    )
    return response.json()["choices"][0]["message"]["content"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is online and ready!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    system = "You are a helpful research assistant."
    reply = call_ai_model(system, user_text)
    await update.message.reply_text(reply)

async def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
