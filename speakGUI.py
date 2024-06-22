from tkinter import *
from speak_func import speakTheSentence
from googletrans import  LANGCODES

# star the loop
root = Tk()
root.geometry("400x250")
root.resizable(0,0)
root.config(background="blue")

def showText():
    USER_TEXT = userText.get()
    if USER_TEXT == "":
        speakTheSentence("apko khuchh likhna parega tabhi to mai bolungi, nahito pata chala mene kuchh ulta sidha bol diya tab to mere source code ko delete kar doge", LANGCODES[language.get()])
        root.destroy()
    speakTheSentence(USER_TEXT, LANGCODES[language.get()])
    userText.set("")
    root.destroy()

# Dropdown menu options
options = LANGCODES.keys()

# datatype of menu text
language = StringVar()

# initial menu text
language.set("Select language")


userText = StringVar()
Label(root, text="Translator",bg="blue",fg='white' ,font="cascadia 20 bold").pack()
Entry(root, textvariable=userText, width=30, font="cascadia 15").pack(pady=10)
# Create Dropdown menu
drop = OptionMenu( root , language, *options )
drop.pack()
Button(root, text='Speak', font='cascadia 10 bold', command=showText, bg="blue", fg='white',padx=7, pady=5, border=4, relief='raised').pack(pady=10)


# end of the loop
root.mainloop()