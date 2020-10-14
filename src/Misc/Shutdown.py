import os, time, datetime
from win10toast import ToastNotifier

class Shutdown(object):
	""" """
	def __init__(self, mins=0):
		""" """
		self.clock = str(datetime.datetime.fromtimestamp(time.time()).strftime(r'%H:%M:%S'))
		self.mins = mins
		self.parser = ToastNotifier()
	
	def main(self):
		""" """
		if self.mins != 0:
			print(self.popup())
			time.sleep(self.mins)
			return os.system("shutdown -s -t 0")
		else:
			return os.system("shutdown -s -t 0")
	
	def popup(self):
		""" """
		return self.parser.show_toast("Shutdown", str(f"Time is now : {self.clock}\nSystem will power-off in {int(self.miins / 60)} minutes."), duration=50)
	
if __name__ == "__main__":
	try:
		mins = int(input("Enter minutes to shutdown : ")) * 60
		Shutdown(mins).main()
	except:
		Shutdown().main()