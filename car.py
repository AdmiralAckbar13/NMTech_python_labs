
class Car:
	def __init__(self,tire,engine):
		self.tire = tire
		self.engine = engine
		if self.tire.traction < self.engine.acceleration:
			self.engine.acceleration = (self.tire.traction + self.engine.acceleration)/2
	def travel_time(self, time):
		distance = 0
		for t in range(0,time):
			distance += self.engine.speed * self.tire.radius
			engine.calcEngineSpeed()
		return distance

	def travel_distance(self,distance):
		time = 0
		cur_distance = 0
		while cur_distance < distance:
			time+=1
			cur_distance+= self.engine.speed * self.tire.radius
			engine.calcEngineSpeed()
		return time
