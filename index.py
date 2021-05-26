from tkinter import *

# frame design
frameBg = "#ff0000"
app = Tk()
app.geometry('600x300')
app.configure(bg=frameBg)
app.title("Youtube Video Downloader")
mainframe = Frame(app, bg=frameBg)
nameLabel = Label(mainframe, text="Youtube Video Downloader", bg=frameBg, font=("Times", "24", "bold"), fg="white")
nameLabel.pack(padx=20, pady=40)
entryLabel = Label(mainframe, text="Enter Video URL", bg=frameBg, font=("Times", "14", "bold"), fg="white")
entryLabel.pack(padx=20, pady=10)
urlEntry = Entry(mainframe, width=60)
urlEntry.pack(padx=20, pady=10)
downloadButton = Button(mainframe, text="Download", bg="white", font=("Times", "11", "bold"), fg=frameBg,
                        activebackground=frameBg, activeforeground="white", relief="flat", cursor="hand2")
downloadButton.pack(padx=20, pady=10)
mainframe.pack()
app.mainloop()
