import os
import telebot
import random
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Render will inject your token securely
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# --- Data Banks ---
WAT_WORDS = [
    "CHALLENGE", "COURAGE", "INITIATIVE", "DISCIPLINE", "COUNTRY", 
    "RESPONSIBILITY", "SUCCESS", "FAILURE", "SACRIFICE", "LEADER"
]

SRT_SITUATIONS = [
    "He was going for an important interview and his cycle punctured on the way. He...",
    "During a train journey at night, he noticed a thief jumping out of the moving train with a passenger's bag. He...",
    "His team was losing the football match and only 5 minutes were left. He...",
    "He is appointed as the captain of a team that is known to be undisciplined. He...",
    "While returning home late at night, he was surrounded by four armed men. He...",
    "A fire breaks out in his neighborhood building. He...",
    "He has to submit a project tomorrow but his laptop crashes. He...",
    "During a trek, his friend twists his ankle and cannot walk. He...",
    "He finds a wallet loaded with cash and ID cards on the road. He...",
    "His exams are approaching and his neighbors are playing loud music. He..."
]

INTERVIEW_QUESTIONS = [
    "Tell me about your educational background starting from 10th standard.",
    "What are your strengths and weaknesses?",
    "How do you spend your spare time and weekends?",
    "Who is your role model and why?",
    "Why do you want to join this profession?",
    "Tell me about a time you faced a major failure and how you overcame it.",
    "How do you handle disagreements with your friends or colleagues?",
    "What are your future plans if you are not selected this time?",
    "Tell me about your daily routine.",
    "Describe a situation where you showed leadership qualities."
]

SD_PROMPT = (
    "Self Description Test (SD):\n\n"
    "Write down the following 5 paragraphs in your notebook:\n"
    "1. What your parents think of you.\n"
    "2. What your teachers or employers think of you.\n"
    "3. What your friends think of you.\n"
    "4. What you think of yourself.\n"
    "5. What qualities you would like to improve."
)

# --- Step 1: Start Command & Menu ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup(row_width=2)
    btn_wat = InlineKeyboardButton("WAT Practice", callback_data="btn_wat")
    btn_srt = InlineKeyboardButton("SRT Practice", callback_data="btn_srt")
    btn_sd = InlineKeyboardButton("Self Description", callback_data="btn_sd")
    btn_int = InlineKeyboardButton("Interview Questions", callback_data="btn_int")
    
    markup.add(btn_wat, btn_srt, btn_sd, btn_int)
    
    bot.send_message(
        message.chat.id, 
        "Welcome to the Interview Preparation Bot.\n\nSelect a test from the menu below to begin your practice.", 
        reply_markup=markup
    )

# --- Step 2: Handle Button Clicks ---
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    bot.answer_callback_query(call.id)
    
    if call.data == "btn_wat":
        word = random.choice(WAT_WORDS)
        bot.send_message(call.message.chat.id, f"Your WAT word is: {word}\n\nType your sentence below.")
        
    elif call.data == "btn_srt":
        situation = random.choice(SRT_SITUATIONS)
        bot.send_message(call.message.chat.id, f"Situation:\n{situation}\n\nType your reaction below.")
        
    elif call.data == "btn_sd":
        bot.send_message(call.message.chat.id, SD_PROMPT)
        
    elif call.data == "btn_int":
        question = random.choice(INTERVIEW_QUESTIONS)
        bot.send_message(call.message.chat.id, f"Interview Question:\n{question}\n\nPractice speaking your answer out loud.")

# --- Step 3: Handle User Text Input ---
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.send_message(
        message.chat.id,
        "Response recorded.\n\nTo practice another question, tap /start to open the main menu again."
    )

# --- Dummy Web Server for Render Hosting ---
class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Bot is running active")

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

def run_dummy_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), DummyHandler)
    server.serve_forever()

if __name__ == "__main__":
    threading.Thread(target=run_dummy_server, daemon=True).start()
    print("Comprehensive SSB Bot is starting...")
    bot.infinity_polling()
