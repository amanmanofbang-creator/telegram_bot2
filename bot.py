import os
import telebot
import random
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Render will inject your token securely
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# --- Updated Data Banks (10 questions each) ---
NDA_QUESTIONS = [
    "What is the derivative of sin(x^2)?",
    "Who was the first recipient of the Oscar Award?",
    "Which layer of the atmosphere reflects radio waves?",
    "In which year was the Quit India Movement launched?",
    "What is the value of log(1)?",
    "Which river is known as the 'Sorrow of Bihar'?",
    "What is the SI unit of power?",
    "Name the fundamental rights guaranteed by the Indian Constitution.",
    "Who wrote the book 'Discovery of India'?",
    "Which planet is known as the Red Planet?"
]

AFCAT_QUESTIONS = [
    "Find the odd one out: Car, Bicycle, Truck, Bus.",
    "What is the capital of Uzbekistan?",
    "What is a synonym for the word 'Vibrant'?",
    "If the code for 'APPLE' is 'BQQMF', what is the code for 'ORANGE'?",
    "Who was the first woman Air Marshal of the IAF?",
    "Which sport is associated with the term 'Deuce'?",
    "What is the chemical name of common salt?",
    "What is the antonym of 'Zenith'?",
    "Which state is the largest producer of tea in India?",
    "Who was the first Indian to travel into space?"
]

CDS_QUESTIONS = [
    "Mention the types of writs issued by the Supreme Court or High Court.",
    "Who was the Governor-General of India during the 1857 revolt?",
    "Which article of the Constitution provides for the Election Commission?",
    "Name the boundary line between India and China.",
    "What is the tenure of a member of the Rajya Sabha?",
    "Which element is used in the lead of a pencil?",
    "Who is known as the 'Grand Old Man of India'?",
    "What is the full form of NITI Aayog?",
    "Which is the highest mountain peak in India?",
    "When did the First Battle of Panipat take place and who were the combatants?"
]

SSB_QUESTIONS = [
    "Tell name of 5 planets?",
    "Tell me about your participation in extra-curricular activities in school/college.",
    "How do you contribute to your household chores daily?",
    "What are three qualities you like about your best friend?",
    "How exactly did you prepare for this SSB interview?",
    "Describe a real-life situation where you showed personal initiative.",
    "What was best day of your life?",
    "Tell me about your relationship with your siblings and parents.",
    "What is your opinion on current international relations regarding India?",
    "If you are not selected this time, what is your specific backup plan?"
]

# --- Step 1: Start Command & New Menu ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup(row_width=2)
    btn_nda = InlineKeyboardButton("NDA Questions", callback_data="btn_nda")
    btn_afcat = InlineKeyboardButton("AFCAT Questions", callback_data="btn_afcat")
    btn_cds = InlineKeyboardButton("CDS Questions", callback_data="btn_cds")
    btn_ssb = InlineKeyboardButton("SSB Questions", callback_data="btn_ssb")
    
    markup.add(btn_nda, btn_afcat, btn_cds, btn_ssb)
    
    bot.send_message(
        message.chat.id, 
        "Welcome to NDA, CDS, AFCAT and SSB preparation Preparation Bot.\n\nSelect a category below to begin your practice.", 
        reply_markup=markup
    )

# --- Step 2: Handle Updated Button Clicks ---
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    bot.answer_callback_query(call.id)
    
    if call.data == "btn_nda":
        question = random.choice(NDA_QUESTIONS)
        bot.send_message(call.message.chat.id, f"NDA Practice Question:\n\n{question}\n\nType your answer below.")
        
    elif call.data == "btn_afcat":
        question = random.choice(AFCAT_QUESTIONS)
        bot.send_message(call.message.chat.id, f"AFCAT Practice Question:\n\n{question}\n\nType your answer below.")
        
    elif call.data == "btn_cds":
        question = random.choice(CDS_QUESTIONS)
        bot.send_message(call.message.chat.id, f"CDS Practice Question:\n\n{question}\n\nType your answer below.")
        
    elif call.data == "btn_ssb":
        question = random.choice(SSB_QUESTIONS)
        bot.send_message(call.message.chat.id, f"SSB Interview Question:\n\n{question}\n\nPractice answering out loud or type it below.")

# --- Step 3: Handle User Text Input & Prompt Next ---
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
    print("Updated Preparation Bot is starting...")
    bot.infinity_polling()




# import os
# import telebot
# import random
# import threading
# from http.server import BaseHTTPRequestHandler, HTTPServer
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# # Render will inject your token securely
# TOKEN = os.environ.get('BOT_TOKEN')
# bot = telebot.TeleBot(TOKEN)

# # --- Data Banks ---
# WAT_WORDS = [
#     "CHALLENGE", "COURAGE", "INITIATIVE", "DISCIPLINE", "COUNTRY", 
#     "RESPONSIBILITY", "SUCCESS", "FAILURE", "SACRIFICE", "LEADER"
# ]

# SRT_SITUATIONS = [
#     "He was going for an important interview and his cycle punctured on the way. He...",
#     "During a train journey at night, he noticed a thief jumping out of the moving train with a passenger's bag. He...",
#     "His team was losing the football match and only 5 minutes were left. He...",
#     "He is appointed as the captain of a team that is known to be undisciplined. He...",
#     "While returning home late at night, he was surrounded by four armed men. He...",
#     "A fire breaks out in his neighborhood building. He...",
#     "He has to submit a project tomorrow but his laptop crashes. He...",
#     "During a trek, his friend twists his ankle and cannot walk. He...",
#     "He finds a wallet loaded with cash and ID cards on the road. He...",
#     "His exams are approaching and his neighbors are playing loud music. He..."
# ]

# INTERVIEW_QUESTIONS = [
#     "Tell me about your educational background starting from 10th standard.",
#     "What are your strengths and weaknesses?",
#     "How do you spend your spare time and weekends?",
#     "Who is your role model and why?",
#     "Why do you want to join this profession?",
#     "Tell me about a time you faced a major failure and how you overcame it.",
#     "How do you handle disagreements with your friends or colleagues?",
#     "What are your future plans if you are not selected this time?",
#     "Tell me about your daily routine.",
#     "Describe a situation where you showed leadership qualities."
# ]

# SD_PROMPT = (
#     "Self Description Test (SD):\n\n"
#     "Write down the following 5 paragraphs in your notebook:\n"
#     "1. What your parents think of you.\n"
#     "2. What your teachers or employers think of you.\n"
#     "3. What your friends think of you.\n"
#     "4. What you think of yourself.\n"
#     "5. What qualities you would like to improve."
# )

# # --- Step 1: Start Command & Menu ---
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     markup = InlineKeyboardMarkup(row_width=2)
#     btn_wat = InlineKeyboardButton("WAT Practice", callback_data="btn_wat")
#     btn_srt = InlineKeyboardButton("SRT Practice", callback_data="btn_srt")
#     btn_sd = InlineKeyboardButton("Self Description", callback_data="btn_sd")
#     btn_int = InlineKeyboardButton("Interview Questions", callback_data="btn_int")
    
#     markup.add(btn_wat, btn_srt, btn_sd, btn_int)

#     bot.send_message(
#         message.chat.id, 
#         "Welcome to the Interview Preparation Bot.\n\nNow you can prepare for your SSB interview and written exams like NDA, CDS, and AFCAT for free. To get a free, detailed assessment of all SSB interview-related tests, download the 'AI SSB' app.\n\nTo download the app, either search 'AI SSB' on the Google Play Store or click this link: https://play.google.com/store/apps/details?id=com.newpromax.bookandpen29349\n\nSelect a test from the menu below.", 
#         reply_markup=markup,
#         disable_web_page_preview=True 
#     )
    
#     # bot.send_message(
#     #     message.chat.id, 
#     #     "Welcome to the Interview Preparation Bot.\n\nSelect a test from the menu below to begin your practice.", 
#     #     reply_markup=markup
#     # )

# # --- Step 2: Handle Button Clicks ---
# @bot.callback_query_handler(func=lambda call: True)
# def handle_query(call):
#     bot.answer_callback_query(call.id)
    
#     if call.data == "btn_wat":
#         word = random.choice(WAT_WORDS)
#         bot.send_message(call.message.chat.id, f"Your WAT word is: {word}\n\nType your sentence below.")
        
#     elif call.data == "btn_srt":
#         situation = random.choice(SRT_SITUATIONS)
#         bot.send_message(call.message.chat.id, f"Situation:\n{situation}\n\nType your reaction below.")
        
#     elif call.data == "btn_sd":
#         bot.send_message(call.message.chat.id, SD_PROMPT)
        
#     elif call.data == "btn_int":
#         question = random.choice(INTERVIEW_QUESTIONS)
#         bot.send_message(call.message.chat.id, f"Interview Question:\n{question}\n\nPractice speaking your answer out loud.")

# # --- Step 3: Handle User Text Input ---
# @bot.message_handler(func=lambda message: True)
# def handle_text(message):
#     bot.send_message(
#         message.chat.id,
#         "To get a free detailed assessment, download the 'AI SSB' app from the Google Play Store. Join over 8,000 aspirants already preparing for free for the SSB interview and written exams like NDA, CDS, and AFCAT!\n\nSearch 'AI SSB' on the Google Play Store or click this direct link: https://play.google.com/store/apps/details?id=com.newpromax.bookandpen29349",
#         disable_web_page_preview=True 
#     )
#     # bot.send_message(
#     #     message.chat.id,
#     #     "Response recorded.\n\nTo practice another question, tap /start to open the main menu again."
#     # )

# # --- Dummy Web Server for Render Hosting ---
# class DummyHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()
#         self.wfile.write(b"Bot is running active")

#     def do_HEAD(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()

# def run_dummy_server():
#     port = int(os.environ.get("PORT", 10000))
#     server = HTTPServer(('0.0.0.0', port), DummyHandler)
#     server.serve_forever()

# if __name__ == "__main__":
#     threading.Thread(target=run_dummy_server, daemon=True).start()
#     print("Comprehensive SSB Bot is starting...")
#     bot.infinity_polling()
