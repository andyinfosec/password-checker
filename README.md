# Python Password Strength Checker

## Overview
This is a Python-based password strength checker used to assess password security against common password weaknesses.

The program takes a user entered password and measures it against a set of security criteria, giving an overall password strength, a score (out of 8) and also provides feedback on potential weaknesses and suggestions on how to improve password security. The program also performs a check against a local wordlist of 10,000 commonly used passwords.

I devoped this project as part of my personal cybersecurity learning and portfolio building.

## Features
- Checks password length
- Checks for uppercase and lowercase letters
- Checks for numerical characters
- Checks for special characters
- Compares password to local wordlist of 10,000 commonly used passwords
- Identifies passwords that are commonly used and could be vunerable
- Gives feedback on password strength

## Limitaions
There are a few limitations to the program in its current verrsion. The main one being that wordlist of 10,000 passwords cannot identify every weak or common passwords. It also cannot identify comprimised passwords.

Some of the other limitations:
- Common password wordlist may not contain newer passwords
- Passwords may still be predictable even if they are not in the wordlist
- Character variety alone does not constitute a secure password
- The security criteria passwords are assessed to is basic
- the program does not currently search against breached-password databases

## Future improvements
- Integration with Have I Been Pwned Passwords database
- More advanced security criteria
- Improved dectection of common password patterns
- Additional password dictonaries
- Improve UI

## Resources
- SecLists - Password Wordlists
	- Source: https://github.com/danielmiessler/SecLists/blob/dbe00ff6dc7cd2d0efe2a2808ac80a8188cef8c3/Passwords/Common-Credentials/10k-most-common.txt
