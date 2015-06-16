#Testscores.py (Lab 6) [Shane Roeseberg]

#Goal:
#1.) A histogram of average ACT scored with bins of size 1 between a score of 18 and 24.
#2.) A double bar chart that compares the composite ACT score with the total score of all 
#3 SAT tests for all 51 states/territories.
#3.) Produce the same chart as in part 2, but only for states in which less than 50% take 
#the ACT and more than 50% take the SAT. (There should be 21 states/terriroties like this.)

import matplotlib.pyplot as plt

with open("actsat.txt" , "r") as f:
	lines = f.readlines()

temps = []
for line in lines:
	cols = line.split()
	try:
		if len(cols) > 1:
			temps.append(float(cols[1]))
	except ValueError:
		pass

numbuckets = 1
binnumbers = range(0, numbuckets)
counts = []

for bucketno in binnumbers:
	bucket = []
	for temp in temps:
		if 18 + bucketno * 1 < temp < 18 + (bucketno + 1) * 1:
			bucket.append(temp)

	counts.append(len(bucket))

xlabels = []
for bucket in binnumbers:
	xlabels.append("{} to {}C" .format(18 + bucket * 1, 18 + (bucket + 1) * 1))

plt.bar(binnumbers, counts, align = "center")
plt.xticks(binnumbers, xlabels)
plt.xlabel("SAT Scores")
plt.ylabel("Grades")
plt.title("Average ACT scores")
plt.show()