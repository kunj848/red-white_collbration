"""
Console/Terminal Version: Instagram Account Manager using Python Dictionary

Task:
- Take username and password from user.
- Store username as key and password as value in a dictionary.
- If a user tries to create an account with an already existing username,
  show a proper error message (handling duplicate keys).
"""

def main():
    # Dictionary to store username -> password
    instagram_users = {}

    print("=" * 50)
    print("      INSTAGRAM ACCOUNT MANAGER (DICTIONARY)")
    print("=" * 50)

    while True:
        print("\n--- MENU ---")
        print("1. Create New Account (Sign Up)")
        print("2. Log In")
        print("3. View All Accounts (Dictionary)")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            print("\n--- CREATE NEW ACCOUNT ---")
            username = input("Enter Instagram Username: ").strip()

            # Check if username is empty
            if not username:
                print("❌ Error: Username cannot be empty!")
                continue

            # Check for duplicate key in dictionary
            if username in instagram_users:
                print(f"❌ Error: Username '{username}' already exists!")
                print("   Duplicate keys are not allowed. Please choose a different username.")
                continue

            password = input("Enter Password: ").strip()
            if not password:
                print("❌ Error: Password cannot be empty!")
                continue

            # Store username as key and password as value
            instagram_users[username] = password
            print(f"✅ Success: Account created successfully for '{username}'!")

        elif choice == choice == "2":
            print("\n--- LOGIN ---")
            username = input("Enter Username: ").strip()
            password = input("Enter Password: ").strip()

            # Verify username and password in dictionary
            if username not in instagram_users:
                print(f"❌ Error: Username '{username}' does not exist!")
            elif instagram_users[username] != password:
                print("❌ Error: Incorrect password!")
            else:
                print(f"✅ Login successful! Welcome, @{username}!")

        elif choice == "3":
            print("\n--- REGISTERED ACCOUNTS DICTIONARY ---")
            if not instagram_users:
                print("No accounts registered yet. The dictionary is empty: {}")
            else:
                print(f"Current Dictionary: {instagram_users}\n")
                print(f"{'Username (Key)':<20} | {'Password (Value)':<20}")
                print("-" * 43)
                for user, pwd in instagram_users.items():
                    print(f"{user:<20} | {pwd:<20}")

        elif choice == "4":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
