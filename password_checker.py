import re

def password_strength(password):
    strength = 0
    remarks = ""

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "Password should be at least 8 characters long.\n"

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks += "Add at least one uppercase letter.\n"

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks += "Add at least one lowercase letter.\n"

    # Check digits
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks += "Add at least one number.\n"

    # Check special characters
    if re.search(r"[@_!#$%^&*()<>?/\\|}{~:]", password):
        strength += 1
    else:
        remarks += "Add at least one special character.\n"

    if strength == 5:
        return "Strong Password 💪\nGreat Job!", remarks
    elif 3 <= strength < 5:
        return "Medium Password 🙂\nYou can improve it!", remarks
    else:
        return "Weak Password 😢\nMust improve!", remarks


if __name__ == "__main__":
    password = input("Enter your password: ")
    status, advice = password_strength(password)
    print("\nPassword Status:", status)
    if advice:
        print("\nSuggestions:\n", advice)
