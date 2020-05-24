from tkinter import *
from webcam1 import fn1
    
def main_account_screen():
    main_screen = Tk()  # create a GUI window
    main_screen.geometry("900x600")  # set the configuration of GUI window
    main_screen.title("MUSIC  PLAYER")  # set the title of GUI window
    # create a Form label
    background_image = PhotoImage(file="bg.png")
    background_label = Label(main_screen, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    Label(text="SELECT  YOUR  CHOICE", bg="blue", width="300",padx=100, height="2", font=("Calibri", 20)).pack()
    Label(text="",height=10).pack()

   # create Login Button
    Button(text="START  CAMERA", height="2",font=("Bold",14), width="30",bg="green",command=fn1).pack()
    Label(text="").pack()

   # create a register button
    Button(text="EXIT", height="2",font=("Bold",14), width="30",bg="red",command=main_screen.destroy).pack()
    main_screen.configure(background='AntiqueWhite1')
    main_screen.mainloop()  # start the GUI AntiqueWhite1

main_account_screen()  # call the main_account_screen() function
