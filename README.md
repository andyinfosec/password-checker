# Python Password Strength Checker

## Overview
This is a Python-based password strength checker used to assess password security against common password weaknesses.

The program takes a user entered password and measures it against a set of security criteria, giving an overall password strength, a score (out of 8) and also provides feedback on potential weaknesses and suggestions on how to improve password security. The program also performs a check against a local database of 10,000 commonly used passwords.

I devoped this project as part of my personal cybersecurity learning and portfolio building.

## Features
- Checks password length
- Checks for uppercase and lowercase letters
- Checks for numerical characters
- Checks for special characters
- Compares password to local database of 10,000 commonly used passwords
- Identifies passwords that are commonly used and could be vunerable
- Gives feedback on password strength

## How It Works
The program takes in a user input. Users either enter a password they want to check or 'q' which exits the program. The While loop handles the input and allows for users to keep checking passwords if the input is not provided to quit the program. The While loop calls the function `feedback()`, which takes in `password` as a parameter.

The `feedback()` function calls two other functions before returning feedback to the user.

`check_common()` is a function used to compare the user entered password to the list of 10,000 commonly used passwords.

1. `with open('10k-most-common.txt', 'r') as f:` opens the text file containing the passwords in read mode
2. Each password is on a seperate line, `f.read()` would store all the contents in `common`. `splitlines()` iterates through the file line by line and stores a single password in `common` to be checked
3. `if password in common:` If the user enter password matches a password found in the list, the function returns the boolean value `True`, else it will return `False`

`check_strength()` takes in `password` as a parameter. The function is used to asses the strength of a password and assign it a score. By default, `score` is set to 0.

1. `length = len(password)` variable `length` is declared and initilised with the length of the users enterd password
2. `upper = any(c.isupper() for c in password)` checks the contents of password for any uppercase letters. If password contains any, the value of `upper` is true
	- `lower = any(c.islower() for c in password)` checks the contents of password for any uppercase letters. If password contains any, the value of `lower` is true
	-  `special = any(c in string.punctuation for c in password)` checks the contents of password for any special characters using Python's `string` library, imported at the top of the program. If password contains any, the value of `special` is true
	- `upper = any(c.isdigit() for c in password)` checks the contents of password for any numbers. If password contains any, the value of `number` is true
3. `characters = [upper, lower, special, number]` is an array of boolean values, with true being equal to 1, and false equal to zero
4. `score += 1` if the length surpasses one of the milestone targets (8,12,16,20) a point is added. Each milestone adds an additional point, so a password over 20 characters is awarded 4 points
5. `score += sum(characters)` adds the values from the boolean array together and adds it to `score`
6. `return "Weak", score` returns overall strength and score based on value of `score` on a scale of `"Weak"`, `"Okay"`, `"Better"`, and `"Strong"`

In the `feedback()` function,  `if check_common(password):` will return a warning to the user if their entered password is in the list of common passwords, if not, the program continues

1. `strength, score = check_strength(password) ` when called, the strength and score values are calculated and stored for the users enterd password
2. `feedback = f"\n| Strength: {strength} | Score: {score}/7\n"` appends `feedback` with `strength` and `score`
3. `if strength !="Strong":` if the password is strong, there is no feedback to be given. a full score of 8 means all of the criteria have been ment. if the password isnt strong then `feedback` is appened with suggestions
	- `-Password too short. Make sure  passwords are 8 characters or more in length\n"` if password length is less than 8 characters
	- `-Include upper case letters (A, B, C, ect)\n"` if password contains no uppercase letters
	- `-Include lower case letters (a, b, c, ect)\n"` if password contains no lowercase letters
	- `-Include special characters (@, #, !, ect)\n"` if password contains no special characters
	- `-Include numbers  (1, 2, 3, ect)\n"` if password contains no numbers
4. `return feedback` appened feedback is returned and printed to console

## Limitaions
There are a few limitations to the program in its current verrsion. The main one being that database of 10,000 passwords doesnt identify every weak or common passwords. It also cannot identify comprimised passwords.

Some of the other limitations:
- Common password database may not contain newer passwords
- Passwords may still be predictable even if they are not in the database
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
