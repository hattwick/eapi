# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import calendar

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    month = datetime.date.today().month
    year = datetime.date.today().year
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(datetime.datetime.now())
    print (calendar.month(year,month))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
