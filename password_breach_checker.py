import csv
import requests
import hashlib

# Parses the CSV file from LastPass into a de-duped list
def parseLastPassExport():
 passes = set() # use a set for unique values
 with open('c:\\users\\user\\desktop\\lastPassExport.csv') as f:
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
   

passes = parseLastPassExport()
for pw in passes:
 checkPassword(pw)
