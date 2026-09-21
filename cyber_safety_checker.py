def password_safety():
    print("\n🔐 PASSWORD SAFETY")
    print("------------------")

    password = input("Enter a password to check: ")

    length_ok = len(password) >= 12
    upper_ok = any(c.isupper() for c in password)
    lower_ok = any(c.islower() for c in password)
    number_ok = any(c.isdigit() for c in password)
    special_ok = any(not c.isalnum() for c in password)

    score = sum([length_ok, upper_ok, lower_ok, number_ok, special_ok])

    print("\nPassword Check:")

    print("✓ 12 or more characters" if length_ok else "✗ Use at least 12 characters")
    print("✓ Uppercase letter" if upper_ok else "✗ Add an uppercase letter")
    print("✓ Lowercase letter" if lower_ok else "✗ Add a lowercase letter")
    print("✓ Number" if number_ok else "✗ Add a number")
    print("✓ Special character" if special_ok else "✗ Add a special character")

    if score == 5:
        print("\nPassword Strength: STRONG 💪")
    elif score >= 3:
        print("\nPassword Strength: MEDIUM ⚠️")
    else:
        print("\nPassword Strength: WEAK ❌")


def phishing_awareness():
    print("\n🎣 PHISHING AWARENESS")
    print("----------------------")
    print("• Don't click suspicious links.")
    print("• Check the sender's email address.")
    print("• Never share OTPs or passwords.")
    print("• Be careful with urgent messages.")


def cyber_safety_tips():
    print("\n🛡️ CYBER SAFETY TIPS")
    print("---------------------")
    print("• Use strong and unique passwords.")
    print("• Enable two-factor authentication.")
    print("• Keep your software updated.")
    print("• Avoid using public Wi-Fi for sensitive activities.")
    print("• Never share personal information with strangers online.")


print("================================")
print("     🛡️ CYBER SAFETY CHECKER")
print("================================")

print("\n1. Password Safety")
print("2. Phishing Awareness")
print("3. Cyber Safety Tips")

choice = input("\nChoose an option (1-3): ")

if choice == "1":
    password_safety()
elif choice == "2":
    phishing_awareness()
elif choice == "3":
    cyber_safety_tips()
else:
    print("\n❌ Invalid choice. Please choose 1, 2, or 3.")
