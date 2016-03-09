import tkinter

class reddit_wallpaper_gui(tkinter.Frame):
    def __init__(self, master=None):
        self.subreddits = 'earthporn, spaceporn, wallpaper, skyporn, cityporn, abandonedporn'

        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.subredditLabel = tkinter.Label(self)
        self.subredditLabel['text'] = 'Subreddits:'
        self.subredditLabel.pack(padx='5px')
        self.subredditEntry = tkinter.Entry(self)
        self.subredditName = tkinter.StringVar()
        self.subredditName.set(self.subreddits)
        self.subredditEntry['textvariable'] = self.subredditName
        self.subredditEntry.pack(ipadx='100px', pady='5px')

        self.nsfwCheck = tkinter.Checkbutton(self)
        self.nsfwCheck.pack(after=self.subredditEntry)
        self.nsfwCheck['text'] = 'Allow NSFW?'
        self.nsfw = tkinter.BooleanVar()
        self.nsfw.set(False)
        self.nsfwCheck['variable'] = self.nsfw

        self.genButton = tkinter.Button(self)
        self.genButton['text'] = 'Save'
        #self.genButton['command'] = self.generate
        self.genButton.pack(padx='10px', pady='5px')

if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry('500x400')
    root.wm_title('Reddit Wallpaper')
    app = reddit_wallpaper_gui(root)
    app.mainloop()
