import pywhatkit
import datetime

# ✅ Replace with your actual number including country code
phone_number = "YOUR_PHONE_NUMBER"  # <-- YOUR phone number

# ✅ Your test message
message = "🔥 Test message: This is Siddharth's automated bot."

# 🔁 Send the message 1 minute from now
now = datetime.datetime.now()
hour = now.hour
minute = now.minute + 1

print(f"Scheduling message to {phone_number} at {hour}:{minute}...")

