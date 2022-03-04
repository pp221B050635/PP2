from datetime import datetime, date
def calc(date1, date2):
    timedelta=date2-date1
    return timedelta.days*24*3600+timedelta.seconds

date2=date.today()
date1=input(datetime.strftime('%Y/%m/%d  %H:%M:%S'))
print(calc(date1,date2))