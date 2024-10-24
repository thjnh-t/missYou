import tkinter as tk
import threading
import random
import time

messages = [
    ("I Miss You !", ("Comic Sans MS", 18, "bold"))
]

colors = ["white"]

def create_window(screen_width, screen_height):
    window = tk.Tk()
    
    window.geometry(f"210x50+{random.randint(0, screen_width-300)}+{random.randint(0, screen_height-100)}")
    window.title("Thông báo")
    
    message, font = random.choice(messages)
    fg_color = random.choice(colors)
    
    label = tk.Label(window, text=message, font=font, fg=fg_color, bg="#F8C7DA")
    label.pack(expand=True, fill='both')
    
    window.after(10000, window.destroy)
    window.mainloop()

def create_multiple_windows(num):
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()  
    
    for _ in range(num):
        t = threading.Thread(target=create_window, args=(screen_width, screen_height))
        t.start()
        time.sleep(0.03) 

if __name__ == "__main__":
    create_multiple_windows(200)
