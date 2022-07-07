from _import import *


class Filelist_window:

    def choose_dir(self):
        self.disable_next_button()
        folder = tk.filedialog.askdirectory()
        self.update_filelist([folder])

    def enable_next_button(self, evt):
        self.GButton_69['state'] = 'normal'

    def disable_next_button(self):
        self.GButton_69['state'] = 'disabled'

    # to change file list values
    def update_filelist(self, folderlist: list):
        self.GListBox_923.delete(first=0)
        for folder in folderlist:
            list_dir = os.listdir(folder)
            for file in list_dir:
                if(file.endswith('.csv')):                                      # filter out csv files
                    self.GListBox_923.insert(
                        END, folder + "\\" + file)                                       # update window

    def __init__(self, root):

        root.title("Choose File..")
        root.state("normal")
        width = 587
        height = 340
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.GListBox_923 = tk.Listbox(root)
        self.GListBox_923["bg"] = "#ffffff"
        self.GListBox_923["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GListBox_923["font"] = ft
        self.GListBox_923["fg"] = "#333333"
        self.GListBox_923["justify"] = "left"
        self.GListBox_923.place(x=10, y=20, width=448, height=309)
        self.GListBox_923["listvariable"] = "lb"
        self.GListBox_923["selectmode"] = "single"

        self.GListBox_923.bind('<<ListboxSelect>>',
                               self.enable_next_button)         # event handling

        self.open_icon = tk.PhotoImage(file=r'res\import.png')
        GButton_68 = tk.Button(root, image=self.open_icon)
        GButton_68["bg"] = "#efefef"
        GButton_68["fg"] = "#000000"
        GButton_68["image"] = self.open_icon
        GButton_68["justify"] = "center"
        GButton_68.place(x=490, y=60, width=58, height=48)

        GButton_68["command"] = self.choose_dir             # event handling

        self.next_icon = tk.PhotoImage(file=r'res\next.png')
        self.GButton_69 = tk.Button(root, image=self.next_icon)
        self.GButton_69["bg"] = "#efefef"
        self.GButton_69["fg"] = "#000000"
        self.GButton_69["image"] = self.next_icon
        self.GButton_69["justify"] = "center"
        self.GButton_69["state"] = "disabled"
        self.GButton_69.place(x=490, y=190, width=58, height=48)
        self.GButton_69["command"] = root.quit


# Starter function
def Show_Filelist_window(filelist: list):
    root = tk.Tk()
    filelist_window = Filelist_window(root)
    filelist_window.update_filelist(filelist)
    root.mainloop()
    return root, filelist_window.GListBox_923.selection_get()
