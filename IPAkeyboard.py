import tkinter as tk
import pyperclip
import pyautogui

def click_key(key):
    # Copy the key to the clipboard
    pyperclip.copy(key)
    
    # Focus on the target application
    pyautogui.click()
    
    # Paste the clipboard contents (simulates a keyboard shortcut)
    pyautogui.hotkey("ctrl", "v")

# Create the main tkinter window
root = tk.Tk()
root.title("IPA Special Character Keyboard")

# Set window attributes to keep it on top
root.wm_attributes("-topmost", 1)

# Converting the unicode values of the IPA to characters
theta =chr(0x03B8)
eth = chr(0x00F0)
reversedR = chr(0x0279)
alveolartap = chr(0x027E)
voicelesspostalveolarFricative = chr(0x0283)
ezh = chr(658)
longN = chr(0x014B)
glottalstop = chr(0x0294)

# Define the characters
characters = [theta, eth, reversedR, alveolartap, voicelesspostalveolarFricative, ezh, longN, glottalstop]
row, col = 0, 0

# Create and place buttons for each key/character
for key in characters:
    button = tk.Button(root, text=key, width=5, height=2, command=lambda k=key: click_key(k))
    button.grid(row=row, column=col)
    col += 1
    if col > 2:
        col = 0
        row += 1

# Start the tkinter event loop
root.mainloop()
