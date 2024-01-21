from tkinter import *

window = Tk()
window.title('Poke ball')
window.resizable(False,False)
canvas = Canvas(window, width=500, height=500)

canvas.create_arc(0, 0, 500, 500,
                  fill='red',
                  extent=180,
                  width=10)
canvas.create_arc(0, 0, 500, 500,
                  fill='white',
                  start=180,
                  extent=180,
                  width=10)

canvas.create_oval(190, 190, 310, 310,
                   fill='white',
                   width=10)

canvas.pack()
window.mainloop()
