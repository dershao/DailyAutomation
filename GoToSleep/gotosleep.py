import time, datetime, sys


def getCurrentTime():
	"""
	Create a datetime object of current time.

	"""
	today = datetime.datetime.now()
	year = today.year
	month = today.month
	day = today.day
	hour = today.hour
	minute = today.minute
	return {'day': day, 'month': month, 'year': year, 'hour': hour, 'minute': minute}	

def getTargetTime():
	"""
	Get the target time to notify that it's about time to sleep.

	"""

	#default sleep time: 11:00 PM EST

	DEFAULT_HOUR = 23
	DEFAULT_MINUTE = 0

	hour = DEFAULT_HOUR
	minute = DEFAULT_MINUTE
	ampm = ""

	#hardcoded format: hour minute AM/PM
	if (len(sys.argv) == 4):
		try:
			hour = int(sys.argv[1]) + (12 if sys.argv[3].lower() == "pm" else 0)
			minute = int(sys.argv[2])
		except ParseError:
			print("Invalid format.")

	return {'hour': hour, 'minute' : minute}

def main():

	date = getCurrentTime()
	targetTime = getTargetTime();

	hoursUntilSleep = targetTime['hour'] - date['hour']
	minutesUntilSleep = targetTime['minute'] - date['minute']
	totalTimeInSeconds = hoursUntilSleep * 60 * 60 + minutesUntilSleep * 60;

	print("Thread sleeping for: " + str(totalTimeInSeconds))

	#Thread sleeps until time to notify
	time.sleep(totalTimeInSeconds)

	print("GO TO SLEEP DEREK")
	#TODO: open web page that says go to sleep
	#TODO: higher accuracy by incoporating seconds as well
	
if __name__ == "__main__":
	main()
