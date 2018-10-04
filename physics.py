import math
import tkinter as tk #may need to make uppercase t

print("Welcome to the physics problem solver!")

root = tk.Tk()

text = ["Fe", "Fg", "ΔV", "|E|"]

def command_():
	print(var.get())

var = tk.StringVar()

def choose():
	print("YESSSS")
	if var.get() == 1:
		print(var.get() + "chosen!")

i = 0
for x in range(0, 4):
	RB1 = tk.Radiobutton(root, text=text[i], padx=20, variable=var, command=command_, value=i).pack(anchor=tk.W)
	i += 1

A = tk.Button(root, text="Choose", command=choose())

A.pack()
root.mainloop()