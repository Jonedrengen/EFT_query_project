# import tkinter to create GUI
import tkinter as tk

# create a window
GUI = tk.Tk()

print(tk.TkVersion)
# set the geometry of window
GUI.geometry("550x350")

# set the background color of GUI window
GUI.configure(background="blue")

# set the title of GUI window
GUI.title("test")

# run the GUI window
GUI.mainloop()