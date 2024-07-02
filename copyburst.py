import pyperclip
import keyboard
import time

clipboard = []
    
previous_text = ""  # Store the previous clipboard text to detect changes

def monitor_clipboard():
    global previous_text
    while True:
        current_text = pyperclip.paste()
        if current_text != previous_text:
            previous_text = current_text
            if current_text.strip():
                clipboard.append(current_text)
                print("copied: ")
                print(current_text)
                print("\n")
        time.sleep(0.5)

def paste():
    if clipboard:
        paste_text = clipboard.pop(0)
        print("pasted: ")
        print(paste_text)
        print("\n")
        keyboard.write(paste_text)
    else:
        print('Clipboard is empty!!!')


def remove_latest():
    if clipboard:
        removed_text = clipboard.pop()
        print('Removed latest from clipboard:')
        print(removed_text)
        print("\n")
    else:
        print('Clipboard is empty!!!')
        
        
def clear_clipboard():
    global clipboard
    clipboard = []
    print('Clipboard cleared.')

def main():

    # Setup hotkeys
    keyboard.add_hotkey('ctrl+alt+v', paste)
    keyboard.add_hotkey('ctrl+alt+x', clear_clipboard)
    keyboard.add_hotkey('ctrl+alt+z', remove_latest)

    print("Clipboard Manager running.")
    print("Press CTRL+C to exit.")
    print("\n")
    
    # Start clipboard monitoring
    try:
        monitor_clipboard()
    except KeyboardInterrupt:
        pyperclip.copy("")
        print("Shuting down clipboard manager...")

if __name__ == "__main__":
    main()
    