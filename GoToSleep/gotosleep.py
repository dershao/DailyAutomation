import time, datetime, sys
from selenium import webdriver

#video reminding you to go to sleep
LINK = "https://www.youtube.com/watch?v=Udj-o2m39NA"

#length of video; used to quit web browser when video is done
LENGTH = 287

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
	seconds = today.second

	return {'day': day, 'month': month, 'year': year, 'hour': hour, 'minute': minute, 'seconds': seconds}

def getTargetTime():
	"""
	Get the target time to notify that it's about time to sleep.

	"""

	#default sleep time: 11:00 PM 

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
			print("Invalid format - setting sleep time to 11:00 PM")

	return {'hour': hour, 'minute' : minute}

def GOTOSLEEP():
	"""
	Everything has lead to this moment. Go to sleep.

	Opens YouTube video telling you to go to sleep.

	"""

	browser = webdriver.Firefox()
	browser.get(LINK)
	time.sleep(LENGTH)
	browser.quit()


def main():

	date = getCurrentTime()
	targetTime = getTargetTime();

	hoursUntilSleep = targetTime['hour'] - date['hour']
	minutesUntilSleep = targetTime['minute'] - date['minute']
	secondsUntilSleep = date['seconds'];
	totalTimeInSeconds = hoursUntilSleep * 60 * 60 + minutesUntilSleep * 60 - secondsUntilSleep;

	if (totalTimeInSeconds > 0):
		
		print("Thread sleeping for: " + str(totalTimeInSeconds) + ". You better be getting ready to sleep.")

		#thread sleeps until time to notify sleeping time
		time.sleep(totalTimeInSeconds)

	GOTOSLEEP()
	
if __name__ == "__main__":
	main()