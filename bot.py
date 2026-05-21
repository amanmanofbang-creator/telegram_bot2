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
    "Name 5 planets in our solar system.",
    "Tell me about your participation in extra-curricular activities in school/college.",
    "How do you contribute to your household chores daily?",
    "What are three qualities you like about your best friend?",
    "How exactly did you prepare for this SSB interview?",
    "Describe a real-life situation where you showed personal initiative.",
    "What was the best day of your life?",
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
    
    welcome_text = (
        "Welcome to the NDA, CDS, AFCAT, and SSB Preparation Bot.\n\n"
        "To get detailed assessments related to your SSB interview and comprehensive study "
        "notes for the NDA, CDS, and AFCAT written exams, download the 'AI SSB' app from the Google Play Store.\n\n"
        "To get this app either search 'AI SSB' on google play store or click here to download from google play store: https://play.google.com/store/apps/details?id=com.newpromax.bookandpen29349&hl=en_IN\n\n"
        "Select a category below to begin your practice."
    )
    
    bot.send_message(
        message.chat.id, 
        welcome_text, 
        reply_markup=markup,
        disable_web_page_preview=False
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
    response_text = (
        "Response recorded.\n\n"
        "To get detailed assessments of this response and comprehensive study "
        "notes for the SSB, NDA, CDS, and AFCAT written exams, download the 'AI SSB' app from the Google Play Store.\n\n"
        "To get this app either search 'AI SSB' on google play store or click here to download from google play store: https://play.google.com/store/apps/details?id=com.newpromax.bookandpen29349&hl=en_IN\n\n"
        "To practice another question, tap /start to open the main menu again."
    )
    
    bot.send_message(
        message.chat.id,
        response_text,
        disable_web_page_preview=False
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









# Below is the case code for appr
# import os
# import telebot
# import random
# import threading
# from http.server import BaseHTTPRequestHandler, HTTPServer
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# # Render will inject your token securely
# TOKEN = os.environ.get('BOT_TOKEN')
# bot = telebot.TeleBot(TOKEN)

# # --- Updated Data Banks (10 questions each) ---
# NDA_QUESTIONS = [
#     "What is the derivative of sin(x^2)?",
#     "Who was the first recipient of the Oscar Award?",
#     "Which layer of the atmosphere reflects radio waves?",
#     "In which year was the Quit India Movement launched?",
#     "What is the value of log(1)?",
#     "Which river is known as the 'Sorrow of Bihar'?",
#     "What is the SI unit of power?",
#     "Name the fundamental rights guaranteed by the Indian Constitution.",
#     "Who wrote the book 'Discovery of India'?",
#     "Which planet is known as the Red Planet?"
# ]

# AFCAT_QUESTIONS = [
#     "Find the odd one out: Car, Bicycle, Truck, Bus.",
#     "What is the capital of Uzbekistan?",
#     "What is a synonym for the word 'Vibrant'?",
#     "If the code for 'APPLE' is 'BQQMF', what is the code for 'ORANGE'?",
#     "Who was the first woman Air Marshal of the IAF?",
#     "Which sport is associated with the term 'Deuce'?",
#     "What is the chemical name of common salt?",
#     "What is the antonym of 'Zenith'?",
#     "Which state is the largest producer of tea in India?",
#     "Who was the first Indian to travel into space?"
# ]

# CDS_QUESTIONS = [
#     "Mention the types of writs issued by the Supreme Court or High Court.",
#     "Who was the Governor-General of India during the 1857 revolt?",
#     "Which article of the Constitution provides for the Election Commission?",
#     "Name the boundary line between India and China.",
#     "What is the tenure of a member of the Rajya Sabha?",
#     "Which element is used in the lead of a pencil?",
#     "Who is known as the 'Grand Old Man of India'?",
#     "What is the full form of NITI Aayog?",
#     "Which is the highest mountain peak in India?",
#     "When did the First Battle of Panipat take place and who were the combatants?"
# ]

# SSB_QUESTIONS = [
#     "Tell name of 5 planets?",
#     "Tell me about your participation in extra-curricular activities in school/college.",
#     "How do you contribute to your household chores daily?",
#     "What are three qualities you like about your best friend?",
#     "How exactly did you prepare for this SSB interview?",
#     "Describe a real-life situation where you showed personal initiative.",
#     "What was best day of your life?",
#     "Tell me about your relationship with your siblings and parents.",
#     "What is your opinion on current international relations regarding India?",
#     "If you are not selected this time, what is your specific backup plan?"
# ]

# # --- Step 1: Start Command & New Menu ---
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     markup = InlineKeyboardMarkup(row_width=2)
#     btn_nda = InlineKeyboardButton("NDA Questions", callback_data="btn_nda")
#     btn_afcat = InlineKeyboardButton("AFCAT Questions", callback_data="btn_afcat")
#     btn_cds = InlineKeyboardButton("CDS Questions", callback_data="btn_cds")
#     btn_ssb = InlineKeyboardButton("SSB Questions", callback_data="btn_ssb")
    
#     markup.add(btn_nda, btn_afcat, btn_cds, btn_ssb)
    
#     bot.send_message(
#         message.chat.id, 
#         "Welcome to NDA, CDS, AFCAT and SSB preparation Preparation Bot.\n\nSelect a category below to begin your practice.", 
#         reply_markup=markup
#     )

# # --- Step 2: Handle Updated Button Clicks ---
# @bot.callback_query_handler(func=lambda call: True)
# def handle_query(call):
#     bot.answer_callback_query(call.id)
    
#     if call.data == "btn_nda":
#         question = random.choice(NDA_QUESTIONS)
#         bot.send_message(call.message.chat.id, f"NDA Practice Question:\n\n{question}\n\nType your answer below.")
        
#     elif call.data == "btn_afcat":
#         question = random.choice(AFCAT_QUESTIONS)
#         bot.send_message(call.message.chat.id, f"AFCAT Practice Question:\n\n{question}\n\nType your answer below.")
        
#     elif call.data == "btn_cds":
#         question = random.choice(CDS_QUESTIONS)
#         bot.send_message(call.message.chat.id, f"CDS Practice Question:\n\n{question}\n\nType your answer below.")
        
#     elif call.data == "btn_ssb":
#         question = random.choice(SSB_QUESTIONS)
#         bot.send_message(call.message.chat.id, f"SSB Interview Question:\n\n{question}\n\nPractice answering out loud or type it below.")

# # --- Step 3: Handle User Text Input & Prompt Next ---
# @bot.message_handler(func=lambda message: True)
# def handle_text(message):
#     bot.send_message(
#         message.chat.id,
#         "Response recorded.\n\nTo practice another question, tap /start to open the main menu again."
#     )

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
#     print("Updated Preparation Bot is starting...")
#     bot.infinity_polling()

