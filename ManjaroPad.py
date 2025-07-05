import tkinter as tk
import os.path
print("File Directory")
inputOfUser = input()
targetDetected = ''
if os.path.exists(inputOfUser):
    targetDetected = open(inputOfUser, "r+")
else:
    targetDetected = open(inputOfUser, "x+")
ReadingVal = targetDetected.read()
window = tk.Tk()
window.config(bg="#1e1e2f")
window.title("ManJaro Pad")
window.geometry("400x460")
DirectoryBox = tk.Text(window,bg="#2e2e3e", fg="#ffffff", insertbackground="white",width=2, height=1)
TextBox = tk.Text(window, bg="#2e2e3e", fg="#ffffff", insertbackground="white",width=50, height=20)
TextBox.pack(pady=20)
TextBox.insert(1.0, ReadingVal)
buttonFrame = tk.Frame(window)
buttonFrame.pack(padx=2)

def save():
    targetDetected.seek(0)
    targetDetected.truncate(0)
    targetDetected.write(TextBox.get(1.0, tk.END))
    targetDetected.flush()
    print("saved")

saveButton = tk.Button(buttonFrame,text="Save", bg="#4e4e6f", fg="white", activebackground="#606080", command=save, width=15, height=1,)
saveButton.grid(row=0,column=0)
window.mainloop()
