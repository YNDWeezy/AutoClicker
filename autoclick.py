import threading
import time
import pyautogui
import keyboard
import winsound


autoclick_enabled = False
exit_program = False  

# Fonction d'autoclick
def autoclick():
    global exit_program
    while not exit_program:
        if autoclick_enabled:
            pyautogui.click()  # Effectue un clic
        time.sleep(0.1)  


def notify(message):
    print(f"*** {message} ***") 
    winsound.Beep(1000, 500)  # Émet un bip sonore (1000 Hz pendant 500 ms)

# Fonction pour gérer l'appui sur la touche 'X'
def toggle_autoclick():
    global autoclick_enabled
    # Basculer l'état d'autoclick
    autoclick_enabled = not autoclick_enabled
    if autoclick_enabled:
        notify("Autoclick activé")  # Notification d'activation
    else:
        notify("Autoclick désactivé")  # Notification de désactivation


autoclick_thread = threading.Thread(target=autoclick)
autoclick_thread.daemon = True 
autoclick_thread.start()


keyboard.add_hotkey('x', toggle_autoclick)


def exit_program_fn():
    global exit_program
    exit_program = True
    notify("Programme terminé")
    time.sleep(0.5)  
    exit()

keyboard.add_hotkey('esc', exit_program_fn)

keyboard.wait('esc')