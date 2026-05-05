# from telegram import Update, ReplyKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# import pymysql

# # ================= CONFIG =================
# TOKEN = "8775152874:AAHZrXjTMu-NHb-NsS_AYCugZw3ArbnDiQ4"

# DB_CONFIG = {
#     "host": "45.114.246.232",
#     "user": "root",
#     "password": "cia%23@08@#%OPD!@#",
#     "database": "dcdclive_30_2026"
# }

# # ================= DB CONNECTION =================
# def get_connection():
#     return pymysql.connect(**DB_CONFIG)

# # ================= MENU =================
# def start(update: Update, context: CallbackContext):
#     keyboard = [["1", "2"], ["3", "4"], ["5"]]
#     reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

#     message = """
# 👋 Welcome to DCDC - AI Powered Dialysis Assistant Bot

# Choose an option:

# 1️⃣ Total Patients Count  
# 2️⃣ Last Dialysis (by Patient ID)  
# 3️⃣ Branch List  
# 4️⃣ Total Billing Count (Last 30 Days)  
# 5️⃣ Contact Support  
# """
#     update.message.reply_text(message, reply_markup=reply_markup)

# # ================= HANDLER =================
# def handle_message(update: Update, context: CallbackContext):
#     text = update.message.text.strip()

#     if text == "1":
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute("SELECT COUNT(*) FROM dc_patient_billing")
#         count = cursor.fetchone()[0]

#         update.message.reply_text(f"👥 Total Patients: {count}")

#         conn.close()

#     elif text == "2":
#         update.message.reply_text("Enter Patient ID:")

#         context.user_data['awaiting_patient_id'] = True

#     elif context.user_data.get('awaiting_patient_id'):
#         patient_id = text

#         conn = get_connection()
#         cursor = conn.cursor()

#         query = """
#         SELECT MAX(billing_date)
#         FROM dc_patient_billing
#         WHERE patient_id = %s
#         """
#         cursor.execute(query, (patient_id,))
#         result = cursor.fetchone()[0]

#         if result:
#             update.message.reply_text(f"💉 Last Dialysis: {result}")
#         else:
#             update.message.reply_text("❌ No record found")

#         conn.close()
#         context.user_data['awaiting_patient_id'] = False

#     elif text == "3":
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute("SELECT branch_name FROM dc_branch LIMIT 5")
#         branches = cursor.fetchall()

#         msg = "🏥 Branch List:\n"
#         for b in branches:
#             msg += f"- {b[0]}\n"

#         update.message.reply_text(msg)

#         conn.close()

#     elif text == "4":
#         conn = get_connection()
#         cursor = conn.cursor()

#         query = """
#         SELECT COUNT(patient_id)
#         FROM dc_patient_billing
#         WHERE billing_date >= CURDATE() - INTERVAL 30 DAY
#         """
#         cursor.execute(query)
#         total = cursor.fetchone()[0]

#         update.message.reply_text(f"💰 Total Billing Count (30 days): ₹{total}")

#         conn.close()

#     elif text == "5":
#         update.message.reply_text("📞 Contact: +91-7982688701")

#     elif text.lower() in ["hi", "hello", "start"]:
#         start(update, context)

#     else:
#         update.message.reply_text(
#         "❌ Invalid input.\n\n👉 Please choose option 1–5 or type 'hi' to see menu."
#     )

# # ================= MAIN =================
# def main():
#     updater = Updater(TOKEN, use_context=True)
#     dp = updater.dispatcher

#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

#     updater.start_polling()
#     updater.idle()

# if __name__ == "__main__":
#     main()

# ------------- Updated ---------------------------------
# from telegram import Update, ReplyKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# import pymysql
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # ================= CONFIG =================
# TOKEN = os.getenv("BOT_TOKEN")

# DB_CONFIG = {
#     "host": os.getenv("DB_HOST"),
#     "user": os.getenv("DB_USER"),
#     "password": os.getenv("DB_PASSWORD"),
#     "database": os.getenv("DB_NAME")
# }

# # ================= DB CONNECTION =================
# def get_connection():
#     return pymysql.connect(**DB_CONFIG)

# # ================= MENU =================
# def start(update: Update, context: CallbackContext):
#     keyboard = [
#         ["1️⃣ Total Patients Count", "2️⃣ Last Dialysis (by Patient ID)"],
#         ["3️⃣ Top 5 Branches (by billing count)", "4️⃣ Total Billing Count (Last 30 Days)"],
#         ["5️⃣ Contact Support"]
#     ]
#     reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

#     message = """
#    👋 Welcome to DCDC - AI Powered Dialysis Assistant Bot

#     Choose an option:

# 1️⃣ Total Patients Count  
# 2️⃣ Last Dialysis (by Patient ID)  
# 3️⃣ Top 5 Branches (by Billing Count)
# 4️⃣ Total Billing Count(Last 30 Days)  
# 5️⃣ Contact Support  
# """
#     update.message.reply_text(message, reply_markup=reply_markup)

#     # Reset all states
#     context.user_data.clear()

# # ================= POST ACTION =================
# # def show_post_action(update):
# #     keyboard = [["1️⃣ Menu", "2️⃣ Exit"]]
# #     reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# #     update.message.reply_text(
# #         "🔁 What would you like to do next?",
# #         reply_markup=reply_markup
# #     )

# def show_post_action(update):
#     keyboard = [["🔄 Menu", "❌ Exit"]]
#     reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

#     update.message.reply_text(
#         "🔁 What would you like to do next?\n\n"
#         "🔄 Menu\n"
#         "❌ Exit",
#         reply_markup=reply_markup
#     )
# # ================= MAIN HANDLER =================
# ALLOWED_USERS = {8775152874}

# def handle_message(update: Update, context: CallbackContext):

#     if update.effective_user.id not in ALLOWED_USERS:
#         update.message.reply_text("❌ Unauthorized access")
#         return
     
#     text = update.message.text.strip()

#     # ================= HANDLE NEXT ACTION =================
#     # if context.user_data.get('awaiting_next_action'):
#     #     if text.startswith("1"):
#     #         context.user_data.clear()
#     #         start(update, context)
#     #         return
#     #     elif text.startswith("2"):
#     #         update.message.reply_text("👋 Thank you! Goodbye.")
#     #         context.user_data.clear()
#     #         return
#     #     else:
#     #         update.message.reply_text("❌ Please choose 1️⃣ or 2️⃣")
#     #         return

#     if context.user_data.get('awaiting_next_action'):

#      if text in ["🔄 Menu", "menu", "Menu"]:
#         context.user_data.clear()
#         start(update, context)
#         return

#      elif text in ["❌ Exit", "exit", "Exit"]:
#         update.message.reply_text("👋 Thank you! Goodbye.")
#         context.user_data.clear()
#         return

#      else:
#         update.message.reply_text("❌ Please choose 'Menu' or 'Exit'")
#         return
#     # ================= HANDLE PATIENT ID =================
#     if context.user_data.get('awaiting_patient_id'):
#         patient_id = text

#         try:
#             conn = get_connection()
#             cursor = conn.cursor()

#             query = """
#             SELECT MAX(billing_date)
#             FROM dc_patient_billing
#             WHERE patient_id = %s
#             """
#             cursor.execute(query, (patient_id,))
#             result = cursor.fetchone()[0]

#             if result:
#                 update.message.reply_text(f"💉 Last Dialysis: {result}")
#             else:
#                 update.message.reply_text("❌ No record found")

#             conn.close()

#         except Exception as e:
#             update.message.reply_text("⚠️ Error fetching data")

#         # Reset state
#         context.user_data['awaiting_patient_id'] = False

#         # Ask next step
#         show_post_action(update)
#         context.user_data['awaiting_next_action'] = True
#         return

#     # ================= GREETINGS =================
#     if text.lower() in ["hi", "hello", "start"]:
#         start(update, context)
#         return

#     # ================= MENU OPTIONS =================

#     # 1️⃣ Total Patients
#     if text.startswith("1"):
#         try:
#             conn = get_connection()
#             cursor = conn.cursor()

#             cursor.execute("SELECT COUNT(*) FROM dc_patient_billing")
#             count = cursor.fetchone()[0]

#             update.message.reply_text(f"👥 Total Patients: {count}")
#             conn.close()

#         except:
#             update.message.reply_text("⚠️ Error fetching data")

#         show_post_action(update)
#         context.user_data['awaiting_next_action'] = True
#         return

#     # 2️⃣ Last Dialysis
#     elif text.startswith("2"):
#         update.message.reply_text("🆔 Enter Patient ID:")
#         context.user_data['awaiting_patient_id'] = True
#         return

#     # 3️⃣ Top 5 Branches (by billing count)
#     elif text.startswith("3"):
#         try:
#             conn = get_connection()
#             cursor = conn.cursor()

#             cursor.execute("""SELECT branch_name, COUNT(patient_id)
#             AS patient_count FROM dc_patient_billing
#             GROUP BY branch_name ORDER BY patient_count DESC LIMIT 5""")
#             branches = cursor.fetchall()

#             msg = "🏥 Top 5 Branches by Billing Count:\n"
#             for b in branches:
#                 # msg += f"- {b[0]}\n"
#                 msg += f"- {b[0]} ({b[1]})\n"

#             update.message.reply_text(msg)
#             conn.close()

#         except:
#             update.message.reply_text("⚠️ Error fetching branches")

#         show_post_action(update)
#         context.user_data['awaiting_next_action'] = True
#         return

#     # 4️⃣ Billing Count(Last 30 Days)
#     elif text.startswith("4"):
#         try:
#             conn = get_connection()
#             cursor = conn.cursor()

#             query = """
#             SELECT COUNT(patient_id)
#             FROM dc_patient_billing
#             WHERE billing_date >= CURDATE() - INTERVAL 30 DAY
#             """
#             cursor.execute(query)
#             total = cursor.fetchone()[0]

#             update.message.reply_text(f"💰 Total Billing (30 days): ₹{total}")
#             conn.close()

#         except:
#             update.message.reply_text("⚠️ Error fetching billing data")

#         show_post_action(update)
#         context.user_data['awaiting_next_action'] = True
#         return

#     # 5️⃣ Support
#     elif text.startswith("5"):
#         update.message.reply_text("📞 Contact: +91-7982688701")

#         show_post_action(update)
#         context.user_data['awaiting_next_action'] = True
#         return

#     # ================= INVALID =================
#     else:
#         update.message.reply_text(
#             "❌ Invalid input.\n\n👉 Choose option or type 'hi' to see menu."
#         )

# # ================= MAIN =================
# def main():
#     print("🚀 Bot started...")

#     updater = Updater(TOKEN, use_context=True)
#     dp = updater.dispatcher

#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

#     updater.start_polling()
#     updater.idle()

# if __name__ == "__main__":
#     main()

# --------- API Access Script ----------------

# from telegram import Update, ReplyKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# from dotenv import load_dotenv
# import os
# import requests

# load_dotenv()

# TOKEN = os.getenv("BOT_TOKEN")
# BASE_URL = "http://127.0.0.1:5000"

# ALLOWED_USERS = {6244556529}

# # ================= MENU =================
# # def start(update: Update, context: CallbackContext):
# #     keyboard = [
# #         ["1️⃣ Total Patients", "2️⃣ Last Dialysis"],
# #         ["3️⃣ Top Branches", "4️⃣ Billing"],
# #         ["5️⃣ Support"]
# #     ]
# #     reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# #     update.message.reply_text(
# #         "👋 Welcome to Dialysis Bot\n\nChoose option:",
# #         reply_markup=reply_markup
# #     )

# #     context.user_data.clear()

# def start(update: Update, context: CallbackContext):
#     keyboard = [
#         ["1️⃣ Total Patients", "2️⃣ Last Dialysis"],
#         ["3️⃣ Top Branches", "4️⃣ Billing"],
#         ["5️⃣ Support"]
#     ]

#     reply_markup = ReplyKeyboardMarkup(
#         keyboard,
#         resize_keyboard=True,
#         one_time_keyboard=False
#     )

#     update.message.reply_text(
#         "👋 Welcome to DCDC - AI Powered Dialysis Assistant Bot\n\n"
#         "Choose an option:\n\n"
#         "1️⃣ Total Patients\n"
#         "2️⃣ Last Dialysis\n"
#         "3️⃣ Top Branches\n"
#         "4️⃣ Billing\n"
#         "5️⃣ Support\n\n"
#         "👉 You can type 1–5 or use buttons below.",
#         reply_markup=reply_markup
#     )

#     context.user_data.clear()

# # ================= POST ACTION =================
# def show_post_action(update):
#     keyboard = [["🔄 Menu", "❌ Exit"]]
#     reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

#     update.message.reply_text("🔁 What next?", reply_markup=reply_markup)

# # ================= HANDLER =================
# def handle_message(update: Update, context: CallbackContext):
#     print("User ID:", update.effective_user.id)
    
#     if update.effective_user.id not in ALLOWED_USERS:
#         update.message.reply_text("❌ Unauthorized")
#         return

#     text = update.message.text.strip()

#     # NEXT ACTION
#     if context.user_data.get('awaiting_next_action'):
#         if text.startswith("🔄"):
#             start(update, context)
#             return
#         elif text.startswith("❌"):
#             update.message.reply_text("👋 Goodbye")
#             context.user_data.clear()
#             return

#     # PATIENT ID
#     if context.user_data.get('awaiting_patient_id'):
#         patient_id = text

#         try:
#             res = requests.get(f"{BASE_URL}/last-dialysis/{patient_id}")
#             result = res.json()["last_dialysis"]

#             update.message.reply_text(f"💉 Last Dialysis: {result}")

#         except:
#             update.message.reply_text("⚠️ Error")

#         context.user_data['awaiting_patient_id'] = False
#         show_post_action(update)
#         context.user_data['awaiting_next_action'] = True
#         return

#     # GREETING
#     if text.lower() in ["hi", "hello", "start"]:
#         start(update, context)
#         return

#     # OPTIONS

#     if text.startswith("1"):
#         res = requests.get(f"{BASE_URL}/total-patients")
#         count = res.json()["total_patients"]

#         update.message.reply_text(f"👥 Total Patients: {count}")

#     elif text.startswith("2"):
#         update.message.reply_text("Enter Patient ID:")
#         context.user_data['awaiting_patient_id'] = True
#         return

#     elif text.startswith("3"):
#         res = requests.get(f"{BASE_URL}/top-branches")
#         data = res.json()["top_branches"]

#         msg = "🏥 Top Branches:\n"
#         for b in data:
#             msg += f"- {b['branch_name']} ({b['patient_count']})\n"

#         update.message.reply_text(msg)

#     elif text.startswith("4"):
#         res = requests.get(f"{BASE_URL}/billing")
#         total = res.json()["billing"]

#         update.message.reply_text(f"💰 Billing: {total}")

#     elif text.startswith("5"):
#         update.message.reply_text("📞 Support: +91-XXXXXXXX")

#     else:
#         update.message.reply_text("❌ Invalid input")
#         return

#     show_post_action(update)
#     context.user_data['awaiting_next_action'] = True

# # ================= MAIN =================
# def main():
#     print("🚀 Bot started...")

#     updater = Updater(TOKEN, use_context=True)
#     dp = updater.dispatcher

#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

#     updater.start_polling()
#     updater.idle()

# if __name__ == "__main__":
#     main()

# ------ API Secured ----------
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv
import os
import requests

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
# BASE_URL = "http://127.0.0.1:5000"
BASE_URL = "https://telegram-dialysis-chatbot.onrender.com"
API_KEY = os.getenv("API_KEY")

HEADERS = {"x-api-key": API_KEY}

ALLOWED_USERS = {6244556529}

# ================= MENU =================
def start(update: Update, context: CallbackContext):
    keyboard = [
        ["1️⃣ Total Billing Count", "2️⃣ Last Dialysis (by patient id)"],
        ["3️⃣ Top 5 Branches (by billing count)", "4️⃣ Last 30 days Billing Count"],
        ["5️⃣ Contact Support"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    update.message.reply_text(
        "👋 Welcome to DCDC - AI Powered Dialysis Assistant Bot\n\n"
        "Choose an option:\n\n"
        "1️⃣ Total Billing Count\n"
        "2️⃣ Last Dialysis (by Patient id)\n"
        "3️⃣ Top 5 Branches (by Billing Count)\n"
        "4️⃣ Last 30 Days Billing Count\n"
        "5️⃣ Contact Support\n\n"
        "👉 Type 1–5 OR use buttons",
        reply_markup=reply_markup
    )

    context.user_data.clear()

# ================= POST ACTION =================
def show_post_action(update):
    keyboard = [["🔄 Menu", "❌ Exit"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    update.message.reply_text(
        "🔁 What next?\n\n"
        "👉 Type 'menu' to go back\n"
        "👉 Type 'exit' to quit",
        reply_markup=reply_markup
    )

# ================= HANDLER =================
def handle_message(update: Update, context: CallbackContext):

    print("User:", update.effective_user.id, "| Msg:", update.message.text)

    if update.effective_user.id not in ALLOWED_USERS:
        update.message.reply_text("❌ Unauthorized access")
        return

    text = update.message.text.strip().lower()

    # NEXT ACTION
    if context.user_data.get('awaiting_next_action'):
        if text in ["menu", "🔄 menu"]:
            start(update, context)
            return
        elif text in ["exit", "❌ exit"]:
            update.message.reply_text("👋 Goodbye")
            context.user_data.clear()
            return
        else:
            update.message.reply_text("❌ Type 'menu' or 'exit'")
            return

    # PATIENT ID
    if context.user_data.get('awaiting_patient_id'):
        patient_id = text

        try:
            res = requests.get(f"{BASE_URL}/last-dialysis/{patient_id}", headers=HEADERS)
            result = res.json().get("last_dialysis")

            update.message.reply_text(f"💉 Last Dialysis: {result}")

        except:
            update.message.reply_text("⚠️ Error fetching data")

        context.user_data['awaiting_patient_id'] = False
        show_post_action(update)
        context.user_data['awaiting_next_action'] = True
        return

    # GREETING
    if text in ["hi", "hello", "start"]:
        start(update, context)
        return

    # OPTIONS
    try:
        if text.startswith("1"):
            res = requests.get(f"{BASE_URL}/total-patients", headers=HEADERS)
            update.message.reply_text(f"👥 Total Patients: {res.json()['total_patients']}")

        elif text.startswith("2"):
            update.message.reply_text("🆔 Enter Patient ID:")
            context.user_data['awaiting_patient_id'] = True
            return

        elif text.startswith("3"):
            res = requests.get(f"{BASE_URL}/top-branches", headers=HEADERS)
            data = res.json()["top_branches"]

            msg = "🏥 Top Branches:\n"
            for b in data:
                msg += f"- {b['branch_name']} ({b['patient_count']})\n"

            update.message.reply_text(msg)

        elif text.startswith("4"):
            res = requests.get(f"{BASE_URL}/billing", headers=HEADERS)
            update.message.reply_text(f"💰 Billing: {res.json()['billing']}")

        elif text.startswith("5"):
            update.message.reply_text("📞 Contact: +91-XXXXXXXX")

        else:
            update.message.reply_text("❌ Invalid input")
            return

    except:
        update.message.reply_text("⚠️ API error")

    show_post_action(update)
    context.user_data['awaiting_next_action'] = True

# ================= MAIN =================
def main():
    print("🚀 Bot started...")

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()