print("🛡️ Welcome to Cyber Safety Checker!")
print("-----------------------------------")

print("1. Password Safety")
print("2. Phishing Awareness")
print("3. Cyber Safety Tips")

choice = input("\nChoose an option (1-3): ")

if choice == "1":
    print("\n🔐 Password Safety Tips:")
    print("- Use at least 12 characters.")
    print("- Use uppercase and lowercase letters.")
    print("- Include numbers and symbols.")
    print("- Never share your password.")

elif choice == "2":
    print("\n🎣 Phishing Awareness:")
    print("- Don't click suspicious links.")
    print("- Check the sender's email address.")
    print("- Never share OTPs or passwords.")
    print("- Be careful with urgent messages.")

elif choice == "3":
    print("\n🛡️ Cyber Safety Tips:")
    print("- Keep your software updated.")
    print("- Use two-factor authentication.")
    print("- Avoid unknown downloads.")
    print("- Use secure Wi-Fi.")

else:
    print("\n❌ Invalid choice. Please choose 1, 2, or 3.")
