elapsed = 12 * 60 * 60  # 12 hours in seconds
seconds_in_minute = 60
seconds_in_hour = 60 * seconds_in_minute
seconds_in_day = 24 * seconds_in_hour
seconds_in_week = 7 * seconds_in_day

if elapsed < seconds_in_minute:
    magnitude = 'seconds'
elif elapsed < seconds_in_hour:
    magnitude = 'minutes'
elif elapsed < seconds_in_day:
    magnitude = 'hours'
elif elapsed < seconds_in_week:
    magnitude = 'days'
else:
    magnitude = 'weeks'
    
print(magnitude)