from datetime import date, timedelta
yesterday=date.today()-timedelta(1)
today=date.today()
tomorrow=date.today()+timedelta(1)
print('Yesterday is', yesterday)
print('Today is', today)
print('Tomorrow is', tomorrow)