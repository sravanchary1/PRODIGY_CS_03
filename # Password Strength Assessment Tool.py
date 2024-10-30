# Password Strength Assessment Tool

import re

def assess_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    else:
        score += 1  # Add points for sufficient length

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should include at least one digit.")

    # Check for special characters
    if re.search(r'[@$!%*?&#]', password):
        score += 1
    else:
        feedback.append("Password should include at least one special character (@, $, !, %, *, ?, &, or #).")

    # Check for common patterns
    common_patterns = ["123", "password", "qwerty", "abc", "111", "000"]
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("Avoid common patterns like '123', 'password', 'abc', etc.")
    else:
        score += 1  # Points for avoiding common patterns

    # Check overall score and give a result
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, feedback

# Tool with loop for repeated assessment
while True:
    print("\n" + "="*40)
    print("### Password Strength Assessment Tool ###")
    print("="*40)
    
    password = input("\nEnter the password to assess (or type 'exit' to quit): ")
    if password.lower() == 'exit':
        print("Thank you for using the Password Strength Assessment Tool. Goodbye!")
        break

    strength, feedback = assess_password_strength(password)
    print(f"\nPassword Strength: {strength}")
    print("Feedback:")
    for item in feedback:
        print(f" - {item}")
    
    print("\n" + "="*40)
    input("Press Enter to try another password or type 'exit' to quit.")
