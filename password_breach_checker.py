'''
To use:
-python password_breach_checker.py -e <path to lastpassexport.csv>
-python password_breach_checker.py -f <path to file, one password per line>
-python password_breach_checker.py -p <single password>
'''


import csv
import requests
import hashlib
import argparse

# Parses the CSV file from LastPass into a de-duped list
def parseLastPassExport(path):
	passes = set() # use a set for unique values
	with open(path) as f:
		reader = csv.DictReader(f)
		data = [r for r in reader] # parse the CSV using list comprehension
	for p in data: # for every row in the CSV, 
		passes.add(p['password']) # grab the password and add it to a set()
	return list(passes) # cast the set() to a list for ease of use
	

def checkPassword(p):
	apiUrl = 'https://api.pwnedpasswords.com/range/'
	fullHash =  hashlib.sha1(p).hexdigest().upper() #hash the whole password
	hashFirstFive = fullHash[:5] # pull first 5 for API call
	hashLast=fullHash[5:] # pull the rest for checking it against the returned values
	req = requests.get(apiUrl+hashFirstFive) # send the API call
	suffixes = req.text.split('\r\n') # split the results on newlines
	for suffix in suffixes: # for every suffix, 
		if hashLast in suffix: # if the last part of the hash is in the suffix, 
			print "Password compromised -> ", p # print it out
			

parser = argparse.ArgumentParser(description="Check passwords against cred dumps.")
parser.add_argument('-e', help="Path to LastPass data export")
parser.add_argument('-f', help="Path to file with passwords, one per line")
parser.add_argument('-p', help="single password to check")

if __name__ == "__main__":
	args = parser.parse_args()
	if args.e:
		passes = parseLastPassExport(args.e)
		for pw in passes:
			checkPassword(pw)
	elif args.f:
		with open(args.f) as f:
			passes = f.read().split()
			for pw in passes:
				checkPassword(pw)
	elif args.p:
		checkPassword(args.p)
	else:
		print "you done goofed!"
	