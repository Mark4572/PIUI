import tkinter as tk
import subprocess
import time
import datetime

def create_fullscreen_overlay():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')  # Set background color to black   
        
        
    # Create a frame to act as a taskbar
    taskbar = tk.Frame(root, bg='gray', height=150)
    taskbar.pack(side='bottom', fill='x')

    # Add a label to the taskbar
    def open_menu():
        menu = tk.Toplevel()
        menu.attributes('-fullscreen', True)
        menu.configure(bg='black')
        menu.bind('<Escape>', lambda e: menu.destroy())  # Exit fullscreen on Escape key press
        menu_label = tk.Label(menu, text="Menu", bg='black', fg='white', font=('Arial', 24))
        menu_label.pack()
        def shutdown():
            subprocess.run(["shutdown", "/s", "/t", "0"])

        def energy_saving_mode():
            subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState", "0", "1", "0"])

        shutdown_button = tk.Button(menu, text="Shut Down", bg='gray', fg='white', font=('Arial', 24), command=shutdown)
        shutdown_button.pack(pady=20)

        energy_saving_button = tk.Button(menu, text="Energy Saving Mode", bg='gray', fg='white', font=('Arial', 24), command=energy_saving_mode)
        energy_saving_button.pack(pady=20)
        
        close_button = tk.Button(menu, text="Close Menu", bg='gray', fg='white', font=('Arial', 24), command=menu.destroy)
        close_button.pack(pady=20)

        def open_explorer():
            explorer_process = subprocess.Popen(["explorer", "/root,C:\\Users\\Administrator\\OneDrive\\Programms\\PiUi\\Main\\SysData\\data\\"], shell=True)
            def prevent_close():
                try:
                    explorer_process.wait()
                except KeyboardInterrupt:
                    pass
            root.after(1, prevent_close)

        explorer_button = tk.Button(menu, text="Open Explorer", bg='gray', fg='white', font=('Arial', 24), command=open_explorer)
        explorer_button.pack(pady=20)
        menu.mainloop()


    taskbar_label = tk.Button(taskbar, text="PIUI", bg='gray', fg='Black', font=('Arial', 24), command=open_menu)
    taskbar_label.pack(side='left', padx=10)
    
    # Add an exit button to the taskbar
    exit_button = tk.Button(taskbar, text='Exit', bg='red', fg='white', font=('Arial', 24), command=root.destroy)
    exit_button.pack(side='right', padx=10)
    taskbar_label.pack(side='left', padx=10)
    root.bind('<Escape>', lambda e: root.destroy())  # Exit fullscreen on Escape key press
    def open_edge():
        subprocess.run(["start", "opera", "--start-fullscreen"], shell=True)
        root.overrideredirect(True)  # Hide the Windows taskbar

    edge_button = tk.Button(taskbar, text='Browser', bg='blue', fg='black', font=('Arial', 24), command=open_edge)
    edge_button.pack(side='left', padx=10)
    exit_button.pack(side='right', padx=10)

    # Add any additional widgets or functionality here
    # Set an image as the background
    background_image = tk.PhotoImage(file="C:\\Users\\Administrator\\Downloads\\Webpictures\\Taiga at Night.png")
    background_label = tk.Label(root, image=background_image)
    background_label.image = background_image  # Keep a reference to the image to prevent garbage collection
    background_label.place(relwidth=1, relheight=1)
    def lift_taskbar():
        taskbar.lift()  # Ensure the taskbar is above the background image
        root.after(100, lift_taskbar)  # Repeat every 100 milliseconds

    lift_taskbar()

    def update_clock():
        now = datetime.datetime.now().strftime("%H:%M:%S")
        clock_button.config(text=now)
        root.after(1000, update_clock)  # Update the clock every second

    clock_button = tk.Button(taskbar, text="", bg='gray', fg='white', font=('Arial', 24))
    clock_button.pack(side='right', padx=10)
    def open_clock_menu():
        clock_menu = tk.Toplevel()
        clock_menu.geometry("400x300+1550+720")  # Set the size of the clock menu window
        clock_menu.overrideredirect(True)  # Hide the window controls
        root.overrideredirect(True)  # Hide the Windows taskbar
        clock_menu.configure(bg='black')
        clock_menu.bind('<Escape>', lambda e: clock_menu.destroy())  # Exit on Escape key press
        clock_label = tk.Label(clock_menu, text= datetime.datetime.now().strftime("%H:%M:%S"), bg='black', fg='white', font=('Arial', 24))
        root.after(1000, clock_label)
        clock_label.pack()

        def close_clock_menu():
            clock_menu.destroy()

        close_button = tk.Button(clock_menu, text="Close Clock Menu", bg='gray', fg='white', font=('Arial', 24), command=close_clock_menu)
        root.after(1000, update_clock)  # Update the clock every second
        close_button.pack(pady=20)

    clock_button.config(command=open_clock_menu)
    update_clock()  # Start the clock update loop
    taskbar.lift()  # Ensure the taskbar is above the background image

    root.mainloop()  # Start the Tkinter event loop
        
if __name__ == "__main__":
    
    
    create_fullscreen_overlay()
    

    def update_clock():
        now = datetime.datetime.now().strftime("%H:%M:%S")
        clock_button.config(text=now)
        root.after(1000, update_clock)  # Update the clock every second

    clock_button = tk.Button(taskbar, text="", bg='gray', fg='white', font=('Arial', 24))
    clock_button.pack(side='right', padx=10)
    update_clock() # Start the clock update loop
    
    
def datetime():
        now = datetime.datetime.now().strftime("%H:%M:%S")
        time_button.config(text=now)
        root.after(1000, datetime)  # Update the clock every second
        
     
