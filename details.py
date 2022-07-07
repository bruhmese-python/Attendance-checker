from _import import *
import reader


class Student_data:
    def date_difference(self, _date):
        endDate = datetime.now()
        delta = endDate - _date
        return delta.days

    def attendance_roll_percentile(self, attendance, total):
        return (attendance / total) * 100

    def update_list(self, items):
        self.GListBox_Data.delete(0, END)
        [self.GListBox_Data.insert(END, '{}\t\t{}\t\t{}\t\t{}'.format(
            record[reader.ID], record[reader.NAME], record[reader.EMAIL], record[reader.ATTENDANCE])) for record in items]

    def filter_list(self):
        self.filtered_items = list()
        for record in self.items:

            # filter out students short on attendance
            if(self.attendance_roll_percentile(int(record[reader.ATTENDANCE]), self.date_difference(reader.parse_date(self.start_date))) < self.percentile_bar):
                self.filtered_items.append(record)

        self.update_list(self.filtered_items)
        self.GButton_mail["state"] = "normal"

    def __init__(self, root):
        root.title("Student - data")
        width = 586
        height = 340
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.GListBox_Data = tk.Listbox(root)
        self.GListBox_Data["bg"] = "#ffffff"
        self.GListBox_Data["borderwidth"] = "1px"
        self.GListBox_Data["fg"] = "#333333"
        self.GListBox_Data["justify"] = "left"
        self.GListBox_Data.place(x=10, y=20, width=448, height=309)
        self.GListBox_Data["listvariable"] = "lb"
        self.GListBox_Data["selectmode"] = "single"
        self.GListBox_Data["setgrid"] = "False"

        self.filter_icon = tk.PhotoImage(file="res\\filter.png")
        GButton_Filter = tk.Button(root, image=self.filter_icon)
        GButton_Filter["bg"] = "#efefef"
        GButton_Filter["fg"] = "#000000"
        GButton_Filter["image"] = self.filter_icon
        GButton_Filter["justify"] = "center"
        GButton_Filter.place(x=490, y=60, width=58, height=48)
        GButton_Filter["command"] = self.filter_list        # event handling

        self.next_icon = tk.PhotoImage(file=r'res\mail.png')
        self.GButton_mail = tk.Button(root, image=self.next_icon)
        self.GButton_mail["bg"] = "#efefef"
        self.GButton_mail["fg"] = "#000000"
        self.GButton_mail["image"] = self.next_icon
        self.GButton_mail["justify"] = "center"
        self.GButton_mail["state"] = "disabled"
        self.GButton_mail.place(x=490, y=190, width=58, height=48)
        self.GButton_mail["command"] = root.quit         # event handling


def Show_Details_window(filename, percentile_bar, start_date):
    root = tk.Tk()
    student_data = Student_data(root)
    student_data.items = reader.parse_csv(filename)
    student_data.percentile_bar, student_data.start_date = [
        float(percentile_bar), start_date]

    student_data.update_list(student_data.items)
    root.mainloop()
    return root, student_data.filtered_items
