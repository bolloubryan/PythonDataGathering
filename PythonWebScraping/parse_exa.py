import json
  
# Opening JSON file
f = open('exabeam_mitre_map.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list

techniques = {}

for i in data['techniques']:
	tactic = i["tactic"]
	score = i["score"]
	if tactic not in techniques:
		techniques[tactic] = 0
		techniques[tactic] = techniques[tactic] + score
	else :
		techniques[tactic] = techniques[tactic] + score
# Closing file

print(techniques)

f.close()

# C:\Users\bollouballs\Desktop\Masters\799 Paper\Primary>python parse_exa.py
# {'lateral-movement': 276, 'initial-access': 442, 'command-and-control': 318, 'defense-evasion': 998, 'privilege-escalation': 615, 'persistence': 713, 'discovery': 191, 'credential-access': 228, 'execution': 361, 'exfiltration': 220, 'collection': 85, 'resource-development': 2, 'reconnaissance': 6, 'impact': 21}