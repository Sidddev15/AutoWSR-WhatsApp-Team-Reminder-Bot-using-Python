# 🛎️ autoWSR: WhatsApp Team Reminder Bot using Python

A simple yet effective Python automation script that sends WhatsApp group messages on a set schedule to remind team members to update their Weekly Status Report (WSR).

## ✨ Features

- ✅ Scheduled WSR reminders on Thursdays and Fridays
- ⏰ Friday reminders escalate politely throughout the day
- 📆 Uses `schedule` module for flexible timing
- 💬 Sends messages to WhatsApp groups via `pywhatkit`

---

## 🧰 Tech Stack

- Python 3
- [pywhatkit](https://pypi.org/project/pywhatkit/)
- schedule
- datetime

---

## ⚙️ How It Works

1. Opens WhatsApp Web via browser
2. Sends a pre-written message to a specified group ID at the scheduled time
3. Stays idle between reminders (can run in the background)

---

## 🔁 Reminder Flow

| Day       | Time   | Message Type                     |
|-----------|--------|----------------------------------|
| Thursday  | 6:30PM | WSR heads-up reminder            |
| Friday    | 9:30AM | Friendly morning ping            |
| Friday    | 1:00PM | Afternoon follow-up              |
| Friday    | 5:00PM | Last call reminder before EOD    |

---
## Screenshots

![image](https://github.com/user-attachments/assets/0fe78fcb-9fe8-4838-82f7-d40590c8cd4a)

![image](https://github.com/user-attachments/assets/6fb91d7a-2acb-480c-b7d9-1239f8240296)

![image](https://github.com/user-attachments/assets/d8eb0409-eb4d-42c2-a8cc-bb8420a4d5dd)

![image](https://github.com/user-attachments/assets/34ecab26-94af-4e6c-b840-6ce474ddc43c)

---

## 🛠 Installation

```bash
# Clone this repo
git clone https://github.com/yourusername/autoWSR.git
cd autoWSR

# Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  # on Windows

# Install dependencies
pip install pywhatkit schedule
