current_time = '18.29.01'
hours = int(current_time[:2])
minutes = int(current_time[3:5])
seconds = int(current_time[6:])
total_seconds = hours*3600 + minutes*60 + seconds
print("Total_seconds: %d" % total_seconds)

