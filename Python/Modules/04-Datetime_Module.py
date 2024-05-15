from datetime import date  #import "date" class from "datetime" module
from datetime import datetime
from datetime import timedelta

today = date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())    #Return day of the week, where Monday == 0 ... Sunday == 6.
print(today.isoweekday()) #Return day of the week, where Monday == 1 ... Sunday == 7.
#day,month,year -> attributes / weekday(),isoweekday() -> methods

past_history = date(2000,12,16)
print(past_history)
print(past_history.isoweekday())

elapsed_time = today - past_history
print(elapsed_time)

elapsed_years = elapsed_time.days / 365.25
print("Age : ",elapsed_years)


#datetime
now = datetime.now()
print(now)
print(now.strftime("%d-%m-%Y  %A"))            #using datetime by object
print(datetime.strftime(today,"%d-%m-%Y  %A")) #using datetime directly


#timedelta
now = datetime.now()
tdelta = timedelta(days=7,hours=5)
print("After 7 days and 5 hours later : ",now + tdelta)

future_time = now + tdelta
elapsed_time = future_time - now
print("Elapsed time: ", elapsed_time)
#print("Elapsed time : ",tdelta-now)  ->error (not supported)

