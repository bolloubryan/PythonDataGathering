import re
  
f = open('WeightedSurvey.txt')
  
data = f.readlines()


counter = 0
for line in data:
	if(re.match("\+",line)):
		print(line)
	arrays[counter] = 

arrays = [{},{},{}]

print(arrays)

f.close()