import string

# Checks to see if user password is commonly used. File is part of a collection on the SecLists github

def check_common(password):
    with open('10k-most-common.txt', 'r') as f:
        common = f.read().splitlines()
        if password in common:
            return True
        return False
   
# Assesses the strength of a users password by checking the length and combination of characters

def check_strength(password):
    score = 0
    length = len(password)

    # Looks for different character types 
    
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    special = any(c in string.punctuation for c in password)
    number = any(c.isdigit() for c in password)

    characters = [upper, lower, special, number] # Bool arr, If one or more characters of a type are present, value is True (1)

    # Adds points to running total if password length milestones are met

    if length > 8:
        score += 1
    if length > 12:
            score += 1
    if length > 16:
            score += 1
    if length > 20:
            score += 1

    score += sum(characters) # Adds one to score for each charater type included in password

    if score < 4:
        return "Weak", score
    elif score == 4:
        return "Okay", score
    elif 4 < score < 8:
        return "Better", score
    else:
        return "Strong", score 

# Calculates the overall strength of the password and provides feedback to user on how to improve

def feedback(password):
    if check_common(password): # Returns warning if identified in common password list
        return "Password identified in common list. Score: 0"

    strength, score = check_strength(password) # Returns the strength and score of given password
    feedback = f"\n| Strength: {strength} | Score: {score}/7\n"

    if strength !="Strong": # If password strength is not strong, suggestions are appened to feedback, then returned
        feedback += "Here are some suggestions to improve your password:\n"

        if len(password) < 8: 
            feedback += "   -Password too short. Make sure  passwords are 8 characters or more in length\n"
        if not any(c.isupper() for c in password):
            feedback += "   -Include upper case letters (A, B, C, ect)\n"
        if not any(c.islower() for c in password):
            feedback += "   -Include lower case letters (a, b, c, ect)\n"
        if not any(c in string.punctuation for c in password):
            feedback += "   -Include special characters (@, #, !, ect)\n"
        if not any(c.isdigit() for c in password):
            feedback += "   -Include numbers  (1, 2, 3, ect)\n"
                
user_input = input("Enter password or 'q' to quit: ")
print("\n")

while user_input != 'q':
    password = user_input
    print(feedback(password))
    user_input = input("Enter password or 'q' to quit: ")
    print("\n")
