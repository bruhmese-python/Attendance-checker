from _import import *

ID = 0
NAME = 1
EMAIL = 2
ATTENDANCE = 3


def parse_date(str_date):
    try:
        return datetime.strptime(str_date, '%d/%m/%Y %H:%M:%S.%f')
    except:
        messagebox.showinfo(
            message="error while parsing date")


def parse_credentials():
    try:
        config = configparser.ConfigParser()
        f = open('credentials.cfg', 'r')
        config.read_file(f)
        return [config['DEFAULT']['username'], config['DEFAULT']['password']]
    except:
        messagebox.showinfo(
            message="error while reading credentials ")


def parse_cfg():
    try:
        config = configparser.ConfigParser()
        f = open('init.cfg', 'r')
        config.read_file(f)
        return [config['DEFAULT']['percentile-bar'], config['DEFAULT']['start-date'], config['PATH']['path1'], config['PATH']['path2']]
    except:
        messagebox.showinfo(
            message="error while reading config file")


def parse_csv(filename):
    try:
        with open(filename) as file:
            data = csv.reader(file)
            return [row for row in data]
    except:
        messagebox.showinfo(
            message="error while reading CSV file")
