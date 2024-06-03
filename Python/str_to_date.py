import datetime, sys

str_dt = 'May 30 2024 03:00PM'
days = 1
params = sys.argv
if len(params) > 2:
    str_dt = params[1]
    days = int(params[2])
  
# Function to convert string to datetime 
def convert(date_time): 
    format = '%b %d %Y %I:%M%p'
    datetime_str = datetime.datetime.strptime(date_time, format) 
  
    return datetime_str 
  
# Function to add days to target date 
def add_days(date_time, days_to_add): 
    return date_time + datetime.timedelta(days=days_to_add) 

print(f"args = {params} str_dt = {str_dt}, days = {days}")
dt = convert(str_dt)
print(dt) 
print(type(dt))
print(add_days(dt, days))