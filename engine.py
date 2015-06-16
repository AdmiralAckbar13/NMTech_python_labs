
class Engine:
	def __init__(self,maxSpeed, acceleration):
		self.maxSpeed = maxSpeed
		self.acceleration = acceleration
		self.speed = 0
	def calcEngineSpeed(self):
		self.speed = self.speed + self.acceleration(self.maxSpeed-self.speed)
