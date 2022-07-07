from _import import *
from reader import EMAIL, NAME, parse_credentials


class Email_Client:
    Mail_status = "Mail Log :-"

    def email(self, mailing_list: list):
        USERNAME, PASSWORD = parse_credentials()

        for Student in mailing_list:
            sent_from = 'Teacher'

            # compose email
            msg = MIMEMultipart('alternative')
            msg['Subject'] = 'Attendance shortage notification'
            msg['From'] = 'College'
            e_mail_file = open(r'res\email_body.txt', 'r')
            email_body = e_mail_file.read(1000)
            msg['to'] = Student[NAME]
            sent_to = Student[EMAIL]

            status_str = '\nSending email to {} : {}'.format(
                Student[NAME], Student[EMAIL])
            print(status_str)
            self.Mail_status += status_str

            part_plain = MIMEText(email_body, 'plain')
            msg.attach(part_plain)

            with smtplib.SMTP('smtp.gmail.com', 587) as SERVER:
                SERVER.starttls()
                SERVER.login(USERNAME, PASSWORD)
                SERVER.sendmail(sent_from, sent_to, msg.as_string())

                status_str = '\nSent email'
                self.Mail_status += status_str
                print(status_str)

    def __init__(self, root):
        # setting title
        root.title("Mailing")
        # setting window size
        width = 586
        height = 340
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.MailStatus_923 = tk.Text(root)
        self.MailStatus_923["bg"] = "#ffffff"
        self.MailStatus_923["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.MailStatus_923["font"] = ft
        self.MailStatus_923["fg"] = "#ff5050"
        self.MailStatus_923.place(x=10, y=20, width=448, height=309)
        self.MailStatus_923["setgrid"] = "False"

        self.back_icon = tk.PhotoImage(file=r'res\back.png')
        Mail_btn = tk.Button(root, image=self.back_icon)
        Mail_btn["bg"] = "#efefef"
        Mail_btn["fg"] = "#000000"
        Mail_btn["justify"] = "center"
        Mail_btn["image"] = self.back_icon
        Mail_btn["text"] = ""
        Mail_btn.place(x=490, y=190, width=58, height=48)
        Mail_btn["command"] = root.quit


def Show_Mailing_window(mailing_list: list):
    root = tk.Tk()
    Mail_Window = Email_Client(root)
    Mail_Window.email(mailing_list)
    Mail_Window.MailStatus_923.insert(END, Mail_Window.Mail_status)
    root.mainloop()
    return root
