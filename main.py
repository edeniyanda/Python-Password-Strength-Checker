import string

def check_password_strength(password: str) -> int:
    """Returns a score indicating the strength of the password.
    A higher score means the password is stronger.
    """
    
    global x
    score = 0
    x = 0
    # Check if the password contains at least one character from each required character class
    if any(c.isupper() for c in password):
        score += 1
        x = 1
    if any(c.islower() for c in password):
        score += 1
        x += 1
    if any(c.isdigit() for c in password):
        score += 1
        x += 1
    if any(c in string.punctuation for c in password):
        score += 1
        x += 1
    
    if x < 4:
        return score
    
    # Check if the password is long enough
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if len(password) >= 20:
        score += 1
  
    return score

def check_password(password: str) -> None:
    """Checks the password for various issues and prints a message indicating its strength."""
    # Read the list of common passwords from the file
    with open("common.txt", "r") as f:
        common_passwords = set(f.read().splitlines())

    # Check if the password is too common
    if password in common_passwords:
        print("Password is too common. Your password strength is 0.")
        return

    # Check the password strength
    score = check_password_strength(password)
    if score == 0:
        print ("Password is too weak")
        if x < 4:
            print ("Password must contain at least an uppercase letter, lowercase letter, special character and at least one digit")
    elif score == 1:
        print("Password is weak.")
        if x < 4:
            print ("Password must contain at least an uppercase letter, lowercase letter, special character and at least one digit")
    elif score == 2:
        print("Password is average.")
        if x < 4:
            print ("Password must contain at least an uppercase letter, lowercase letter, special character and at least one digit")
    elif score == 3:
        print("Password is not that strong.")
        if x < 4:
            print ("Password must contain at least an uppercase letter, lowercase letter, special character and at least one digit")
    elif score == 4:
        print("Password is not that strong.")
        if x < 4:
            print ("Password must contain at least an uppercase letter, lowercase letter, special character and at least one digit")
    else:
        print("Password is extremely strong.")

while True:
    password = input("Enter password: ")
    check_password(password)
