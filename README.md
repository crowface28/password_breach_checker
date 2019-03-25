# password_breach_checker
Checks passwords against HaveIBeenPwned password database to see if they have ever been compromised in a leak.  

Plaintext passwords never leave your machine. 

https://codecrossroad.blogspot.com/2019/02/python-use-haveibeenpwned-api-to-check.html

**Warning: It will display compromised passwords to the screen.  Keep that head on a swivel!**


To export from LastPass:
  - Go to your Vault
  - Go to More Options
  - Go to Advanced
  - Go to Export
  - Copy/paste the text into a file

usage: password_breach_checker.py [-h] [-e E] [-f F] [-p P]

Check passwords against cred dumps.

optional arguments:
  -h, --help  show this help message and exit
  -e E        Path to LastPass data export
  -f F        Path to file with passwords, one per line
  -p P        single password to check
  
