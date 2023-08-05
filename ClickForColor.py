import tkinter as tk
from tkinter import ttk, Toplevel
import pyperclip
from PIL import ImageGrab
from pynput import mouse, keyboard

class ColorPickerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Color Picker")
        self.geometry("250x200")
        
        self.is_active = tk.BooleanVar(self)
        self.is_active.set(False)
        
        ttk.Checkbutton(self, text="Activate", variable=self.is_active).pack(pady=10)
        
        self.color_display = tk.Canvas(self, width=100, height=50)
        self.color_display.pack(pady=5)
        
        self.label = ttk.Label(self, text="")
        self.label.pack(pady=10)

        ttk.Button(self, text="History", command=self.show_history).pack(pady=10)
        
        self.color_history = []
        
        # Only keyboard listener is required now
        self.keyboard_listener = keyboard.Listener(on_press=self.on_keypress)
        self.keyboard_listener.start()

    def on_keypress(self, key):
        try:
            # If F9 is pressed and the application is activated
            if key == keyboard.Key.f9 and self.is_active.get():
                x, y = mouse.Controller().position
                screen = ImageGrab.grab(bbox=(x, y, x+2, y+2))
                color = screen.getpixel((0, 0))
                hex_color = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
                self.label.config(text=hex_color)
                self.color_display.create_rectangle(0, 0, 100, 50, fill=hex_color, outline=hex_color)
                self.save_color(hex_color)
        except AttributeError:
            pass

    def save_color(self, color):
        if color:
            pyperclip.copy(color)
            self.color_history.append(color)
            if len(self.color_history) > 10:
                self.color_history.pop(0)

    def copy_to_clipboard(self, color):
        pyperclip.copy(color)

    def show_history(self):
        history_win = Toplevel(self)
        history_win.title("Color History")
        
        for color in self.color_history:
            frame = ttk.Frame(history_win)
            frame.pack(pady=2, padx=10, fill=tk.BOTH)

            label = ttk.Label(frame, text=color, background=color, foreground=self.text_color(color))
            label.pack(side=tk.LEFT, padx=10)
            
            btn = ttk.Button(frame, text="Copy", command=lambda c=color: self.copy_to_clipboard(c))
            btn.pack(side=tk.RIGHT)

    def text_color(self, bg_color):
        r, g, b = int(bg_color[1:3], 16), int(bg_color[3:5], 16), int(bg_color[5:7], 16)
        return 'white' if (r*0.299 + g*0.587 + b*0.114) < 186 else 'black'

if __name__ == "__main__":
    app = ColorPickerApp()
    app.mainloop()
