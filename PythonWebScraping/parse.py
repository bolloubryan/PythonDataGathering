import json
  
# Opening JSON file
f = open('azure_platform_native_security_controls.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list

techniques = {}

for i in data['techniques']:
	tactic = i["tactic"]
	if tactic not in techniques:
		techniques[tactic] = 0
		for control in i["metadata"]:
			for keys in control.keys():
				if control[keys] == "control":
					techniques[tactic] +=1
	else :
		for control in i["metadata"]:
			for keys in control.keys():
				if control[keys] == "control":
					techniques[tactic] +=1
# Closing file

print(techniques)

f.close()

# C:\Users\bollouballs\Desktop\Masters\799 Paper\Primary>python parse.py
# {'discovery': 66, 'credential-access': 166, 'defense-evasion': 225, 'persistence': 205, 'privilege-escalation': 181, 'initial-access': 84, 'collection': 59, 'resource-development': 7, 'reconnaissance': 21, 'command-and-control': 66, 'lateral-movement': 58, 'execution': 58, 'exfiltration': 31, 'impact': 60}