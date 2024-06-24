import pyperclip
from collections import deque

class ClipboardManager:
    def __init__(self):
        self.clipboard_queue = deque()

    def copy_to_clipboard(self, text):
        self.clipboard_queue.append(text)
        pyperclip.copy(text)
        print(f"Copied: {text}")

    def paste_from_clipboard(self):
        if self.clipboard_queue:
            text = self.clipboard_queue.popleft()
            pyperclip.copy(text)
            print(f"Pasted: {text}")
            return text
        else:
            print("Clipboard is empty")
            return None

    def clear_clipboard(self):
        self.clipboard_queue.clear()
        pyperclip.copy("")
        print("Clipboard cleared")

    def remove_latest(self):
        if self.clipboard_queue:
            removed_text = self.clipboard_queue.pop()
            print(f"Removed latest copied text: {removed_text}")
        else:
            print("Clipboard is empty")
