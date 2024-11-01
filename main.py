import ttkbootstrap as ttk
from ttkbootstrap import Window
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import DateEntry
import jdatetime
from datetime import datetime



def convert_to_jalali():
    gregorian_date_str = date_entry.entry.get()
    if not gregorian_date_str:
        result_label.config(text="Please select a date")
        return

    gregorian_date = datetime.strptime(gregorian_date_str, "%m/%d/%Y")
    jalali_date = jdatetime.date.fromgregorian(date=gregorian_date)

    # Format the Jalali date nicely
    formatted_date = f"{jalali_date.year}/{jalali_date.month}/{jalali_date.day}"
    result_label.config(text=f"Solar date: {formatted_date}", font=("Helvetica", 12))


window = Window(title="Date Convertor App",iconphoto="images/calendar.png", themename="superhero")
window.geometry("500x200")
window.resizable(False, False)

date_entry = DateEntry(window, width=30, bootstyle=SUCCESS)
date_entry.pack(pady=20)

convert_button = ttk.Button(window, text="Convert", command=convert_to_jalali,bootstyle = DANGER)
convert_button.pack(pady=10)

result_label = ttk.Label(window, text="", bootstyle=SUCCESS)
result_label.pack(pady=10)

window.mainloop()
