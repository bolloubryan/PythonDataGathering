import requests
import re



# Request the URL and gt all the html links
elasticurl = "https://www.elastic.co/guide/en/siem/guide/current/prebuilt-rules.html"
y = requests.get(elasticurl)
#tactic = re.findall("\<p\>Tactic\:\<\/p\>\n\<div class\=\"ulist itemizedlist\"\>\n\<ul class\=\"itemizedlist\"\>\n\<li class\=\"listitem\"\>\nName\:(.*?)\n", y.text)
ends = re.findall("\<td align\=\"left\" valign\=\"top\"\>\<p\>\<a class\=\"xref\" href\=\"(.*?)\"", y.text)

print(ends)

baseurl = "https://www.elastic.co/guide/en/siem/guide/current/"

techniques = {}

for end in ends:
	newurl = baseurl+end.split("\n")[0]
	x = requests.get(newurl)
	tactic = re.findall("\<p\>Tactic\:\<\/p\>\n\<div class\=\"ulist itemizedlist\"\>\n\<ul class\=\"itemizedlist\"\>\n\<li class\=\"listitem\"\>\nName\:(.*?)\n", x.text)
	print(newurl)
	print(tactic)
	for one in tactic:
		if one not in techniques:
			techniques[one] = 0
			techniques[one] +=1
		else :
			techniques[one] +=1
print(techniques)

#output
#{' Defense Evasion': 35, ' Persistence': 12, ' Privilege Escalation': 8, ' Execution': 26, ' Command and Control': 20, ' Lateral Movement': 7, ' Discovery': 7, ' Exfiltration': 6, ' Credential Access': 2, ' Initial Access': 8}