import win32com.client

# 1. Create a list of names you want to give a shoutout to
names = ["Sahito", "Furqan", "Fiyana", "Sabeeqa", "Rubab"]

# 2. Open up the Windows text-to-speech engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# 3. Loop through each name and tell the speaker to speak out loud!
for name in names:
    message = f"Shoutout to {name}"
    print(message)  # This prints it on your screen
    speaker.Speak(message)  # This makes your laptop speak it out loud!