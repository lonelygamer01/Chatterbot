import tkinter as tk
from tkinter import ttk
import random
import time
import threading
from PIL import Image, ImageTk
from constants import *
from tts_stt import *

def main_ui():
    global loading_screen
    loading_screen.destroy()
    # Set up the main window
    root = tk.Tk()
    root.title("E.V.E.")
    root.geometry("500x700")  # Adjust dimensions as needed
    root.configure(bg="black")

    img = Image.open("EVE_pfp.png")  # Replace with your image path
    img = img.resize((320, 450))
    photo = ImageTk.PhotoImage(img)
    img_label = tk.Label(root, image=photo)
    img_label.pack(pady=10)

    # Equalizer section
    equalizer_frame = tk.Frame(root, bg="black")
    equalizer_frame.pack(pady=20)

    bars = []
    num_bars = 26  # Total number of bars (must be an odd number for symmetry)
    max_height = 130  # Max height of the tallest bar
    base_width = 3  # Width of each bar
    spacing = 5  # Spacing between bars

    

    listening_thread = threading.Thread(target=live_speech_to_text_google)
    listening_thread.daemon = True
    listening_thread.start()

    center_index = num_bars // 2
    def init_speaking_bars():
        for i in range(num_bars):
            distance_from_center = abs(center_index - i)
            initial_height = max_height * ((center_index - distance_from_center + 1) / (center_index + 1))

            bar = tk.Canvas(equalizer_frame, width=base_width, height=200, bg="black", highlightthickness=0)
            bar.create_rectangle(0, 100 - initial_height/2, base_width, 100 + initial_height/2, fill="white", tags="level")
            bar.grid(row=0, column=i, padx=spacing)
            bars.append((bar, initial_height))
    def init_not_speaking_bars():
        for i in range(num_bars):
            distance_from_center = abs(center_index - i)
            initial_height = 5 * ((center_index - distance_from_center + 1) / (center_index + 1))

            bar = tk.Canvas(equalizer_frame, width=base_width, height=200, bg="black", highlightthickness=0)
            bar.create_rectangle(0, 100 - initial_height/2, base_width, 100 + initial_height/2, fill="white", tags="level")
            bar.grid(row=0, column=i, padx=spacing)
            bars.append((bar, initial_height))
    def speaking():
        for bar, initial_height in bars:
            # Use a random height around the initial height
            fluctuation = random.uniform(0.5, 1.5)  # Adjust range for more or less movement
            level = initial_height * fluctuation
            
            # Update the bar height dynamically around a center line
            bar.coords("level", 0, 100 - level/2, base_width, 100 + level/2)
        root.after(80, speaking)  # Adjust speed by changing the delay
    def update_equalizer(active):
        if active:
            init_speaking_bars()
            speaking()
        else:
            init_not_speaking_bars()
    update_equalizer(equalizer_active)
    root.mainloop()


def loading_ui():
    global loading_screen
    loading_screen = tk.Tk()
    loading_screen.title("Loading Eve...")
    loading_screen.geometry("330x380")

    img = Image.open("EVE_logo.png")
    img = img.resize((300, 300))
    photo = ImageTk.PhotoImage(img)
    img_label = tk.Label(loading_screen, image=photo)
    img_label.pack(pady=10)

    progress = ttk.Progressbar(loading_screen, orient="horizontal", length=200, mode="indeterminate")
    progress.pack(pady=20)
    progress.start()
    loading_screen.after(5000, main_ui)
    loading_screen.mainloop()

loading_ui()
