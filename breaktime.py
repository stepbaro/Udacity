import webbrowser
import time

total_breaks = 3
break_count = 0
print ("This program started at "+time.ctime())

while (break_count<total_breaks):
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=OGWhjojt5dw")
	break_count = break_count + 1
#	print ("Number of breaks - "+break_count)