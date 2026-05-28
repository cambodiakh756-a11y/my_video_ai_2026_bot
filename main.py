import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# លេខកូដសម្ងាត់ Bot របស់អ្នក
TOKEN = "TOKEN = "8817414744:AAFoYG9yeJlCunWICwexEl8fnZ4M..."
"

async def start(update: Update, context):
    await update.message.reply_text("សួស្តី! ខ្ញុំជា Bot ដែលរត់នៅលើ Render ២៤ ម៉ោង។ ខ្ញុំត្រៀមខ្លួនរួចរាល់ហើយ!")

async def reply(update: Update, context):
    user_text = update.message.text
    await update.message.reply_text(f"ខ្ញុំទទួលបានសារ៖ {user_text}")

# បង្កើត Web Server ក្លែងក្លាយដើម្បីកុំឱ្យ Render កាត់ផ្ដាច់ (បច្ចេកទេស Render)
class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), WebServer)
    server.serve_forever()

def main():
    # រត់ Web Server ក្នុង Thread ផ្សេង
    threading.Thread(target=run_web_server, daemon=True).start()

    # ដំណើរការ Telegram Bot
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    
    print("🤖 Bot is starting on Render...")
    app.run_polling()

if __name__ == "__main__":
    main()
