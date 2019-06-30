from datetime import datetime

def display_timestamp():
    current_dt = datetime.now()
    dt_string = current_dt.strftime("%d-%m-%Y %I:%M %p")
    print("Hi, current date and time is",dt_string,end="")
    print(".")

if __name__=="__main__":
    display_timestamp()