import pywhatkit
import schedule
import datetime
import time

# Group ID - Replace with your actual group ID from invite link
group_id = "YOUR_GROUP_ID"

# 📅 Message scheduler
def send_wsr_message(message):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 1
    pywhatkit.sendwhatmsg_to_group(group_id, message, hour, minute)

# ✅ Thursday reminder
def thursday_reminder():
    message = (
        "👋 Hey team, just a friendly reminder to prepare your WSR updates today. "
        "Please keep them crisp and clear so we can all be aligned tomorrow! 😊"
    )
    send_wsr_message(message)

# ✅ Friday reminders (with escalating urgency, still polite)
def friday_morning_reminder():
    message = (
        "🌅 Good morning team! Please take a few minutes to fill out your WSR sheet. "
        "The sooner the better — thank you! 🙏"
    )
    send_wsr_message(message)

def friday_afternoon_reminder():
    message = (
        "⏰ Friendly afternoon nudge! Don’t forget to update your WSR if you haven’t already. "
        "Helps everyone stay in sync. 👍"
    )
    send_wsr_message(message)

def friday_final_reminder():
    message = (
        "🚨 Last call for WSR updates! Please fill it out before EOD. "
        "Let’s wrap up the week with clarity and alignment. Thanks a ton! 📝✨"
    )
    send_wsr_message(message)

# 🗓️ Schedule jobs
schedule.every().friday.at("00:36").do(thursday_reminder)        # Thursday evening
schedule.every().friday.at("09:30").do(friday_morning_reminder)    # Friday morning
schedule.every().friday.at("13:00").do(friday_afternoon_reminder)  # Friday afternoon
schedule.every().friday.at("17:00").do(friday_final_reminder)      # Friday evening

print("✅ WSR reminder bot is now running... Leave this terminal open!")

# 🌀 Keep it running
while True:
    schedule.run_pending()
    time.sleep(10)
