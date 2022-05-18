import time

timer_name = input('What is the name of the timer? \n')
time_file = "%s.timer" %timer_name
f = open(time_file, "w")
time.sleep(2)
timer = input('How long do you want the time to be? \n in seconds only \n')
f.write(timer)
f.close()

time.sleep(2)
print("New timer created called \n", timer_name)
