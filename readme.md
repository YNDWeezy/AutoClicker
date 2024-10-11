**AutoClicker with Keyboard Toggle**

This Python project is an autoclicker that allows users to simulate mouse clicks at regular intervals with simple keyboard controls. The script listens for keyboard events to toggle the autoclicker and provides both visual and auditory notifications when the autoclicker is activated or deactivated.

**Features**
Activate/Deactivate the autoclicker by pressing the X key.
Exit the program by pressing the ESC key.
Sound Notification: A beep sound when the autoclicker is toggled.
Threading: Runs on a separate thread to avoid blocking the main program and ensure responsive keyboard controls.

**How It Works**
Autoclicker Activation: When the user presses X, the program starts simulating mouse clicks at regular intervals (default 100ms). The user can stop the autoclicker by pressing X again.
Program Exit: The user can exit the program by pressing the ESC key, which stops the autoclicker thread and exits the application.
Requirements
Python 3.x

**The following Python libraries:**
pyautogui: For simulating mouse clicks.
keyboard: For capturing keyboard events.
winsound: For providing sound notifications (Windows only).