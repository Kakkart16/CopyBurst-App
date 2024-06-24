import keyboard
import pyperclip
from clipboard_manager import ClipboardManager

def main():
    manager = ClipboardManager()

    def copy_action():
        try:
            selected_text = pyperclip.paste()
            if selected_text:
                manager.copy_to_clipboard(selected_text)
        except Exception as e:
            print(f"Error copying text: {e}")

    def paste_action():
        try:
            manager.paste_from_clipboard()
        except Exception as e:
            print(f"Error pasting text: {e}")

    def clear_action():
        try:
            manager.clear_clipboard()
        except Exception as e:
            print(f"Error clearing clipboard: {e}")

    def remove_latest_action():
        try:
            manager.remove_latest()
        except Exception as e:
            print(f"Error removing latest copied text: {e}")

    # Hotkeys
    keyboard.add_hotkey('ctrl+alt+c', copy_action)
    keyboard.add_hotkey('ctrl+alt+v', paste_action)
    keyboard.add_hotkey('ctrl+alt+x', clear_action)
    keyboard.add_hotkey('ctrl+alt+z', remove_latest_action)

    # Keep the script running to listen for hotkeys
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Clipboard manager stopped.")

if __name__ == "__main__":
    main()
