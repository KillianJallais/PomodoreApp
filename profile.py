from timer import RepetedTimer

class Profile:
	TRAVAIL = "t"
	PAUSE = "p"

	def __init__(self, nbrExercice: int, tempExercice: int, tempPause: int, timeLabel, titleLabel, updateFrame):
		self.nbrExercice = nbrExercice

		self.tempExercice = tempExercice * 60 #donné en minute mais convertie en seconde
		self.tempPause = tempPause * 60 #donné en minute mais convertie en seconde

		self.timer = None

		self.nbrTimers = self.nbrExercice*2 - 1

		self.initProfile(timeLabel, titleLabel, updateFrame)

	def initProfile(self, timeLabel, titleLabel, updateFrame) -> None:
		self.timer = RepetedTimer(self.tempExercice, Profile.TRAVAIL, timeLabel, titleLabel, updateFrame)
		temp = self.timer

		for i in range(1, self.nbrTimers):
			if i%2 == 0:
				temp.next = RepetedTimer(self.tempExercice, Profile.TRAVAIL, timeLabel, titleLabel, updateFrame)
			else:
				temp.next = RepetedTimer(self.tempPause, Profile.PAUSE, timeLabel, titleLabel, updateFrame)

			temp = temp.next

	def getTimeLeft(self) -> str:
		return self.timer.getTimeLeft()

	def start(self) -> None:
		self.timer.start()

	def stop(self):
		self.timer.stop()