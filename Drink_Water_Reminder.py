# This is for WINDOWS

import time
from plyer import notification
import win32com.client

while True:
    notification.notify(
        title = "Time to Drink Water!",
        message = "Hey! Please take a break and hydrate yourself to stay healthy.",
        app_icon = None, 
        timeout = 10       # The notification stays on screen for 10 seconds
    )

    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak("Hey! Time to drink water.")
    
    time.sleep(7200)       # Pause the script execution for 2 hour (7200 seconds)