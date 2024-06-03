import datetime 
  
# Function to convert string to datetime 
def convert(date_time): 
    format = '%b %d %Y %I:%M%p'
    datetime_str = datetime.datetime.strptime(date_time, format) 
  
    return datetime_str 
    
date_time = 'May 30 2024 03:00PM'
dt = convert(date_time)
print(dt) 
print(type(convert(date_time)))
print(dt + datetime.timedelta(days=9))