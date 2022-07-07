from _import import *
import filelist
import reader
import details
import mail

# read config file
[percentile_bar, start_date, path1, path2] = reader.parse_cfg()
while(True):
    WINDOW_1, WINDOW_1_RETURN = filelist.Show_Filelist_window([path1, path2])
    WINDOW_1.destroy()

    WINDOW_2, WINDOW_2_RETURN = details.Show_Details_window(
        WINDOW_1_RETURN, percentile_bar, start_date)
    WINDOW_2.destroy()

    WINDOW_3 = mail.Show_Mailing_window(WINDOW_2_RETURN)
    WINDOW_3.destroy()
