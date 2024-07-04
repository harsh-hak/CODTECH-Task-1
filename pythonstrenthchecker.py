import re
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def password_strength_checker(password):
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append(f"{Fore.RED}Password is too short! It should be at least 8 characters long.")

    # Check for uppercase, lowercase, digits, and special characters
    if not re.search(r'[A-Z]', password):
        feedback.append(f"{Fore.RED}Password should include at least one uppercase letter.")

    if not re.search(r'[a-z]', password):
        feedback.append(f"{Fore.RED}Password should include at least one lowercase letter.")

    if not re.search(r'\d', password):
        feedback.append(f"{Fore.RED}Password should include at least one digit.")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append(f"{Fore.RED}Password should include at least one special character.")

    if not feedback:
        return f"{Fore.GREEN}Your password is strong!", True
    else:
        return "\n".join(feedback), False

def main():
    print(f"{Fore.CYAN}Welcome to the Password Strength Checker!")
    print(f"{Fore.CYAN}Your password should meet the following criteria:")
    print(f"{Fore.YELLOW}1. At least 8 characters long")
    print(f"{Fore.YELLOW}2. At least one uppercase letter (A-Z)")
    print(f"{Fore.YELLOW}3. At least one lowercase letter (a-z)")
    print(f"{Fore.YELLOW}4. At least one digit (0-9)")
    print(f"{Fore.YELLOW}5. At least one special character (e.g., !@#$%^&*)")

    while True:
        password = input(f"\n{Fore.CYAN}Please enter a password to check: ")
        result, is_strong = password_strength_checker(password)
        print(result)

        if is_strong:
            print(f"{Fore.GREEN}Congratulations! Your password is strong.")
            break
        else:
            print(f"{Fore.RED}Please try again.")

if __name__ == "__main__":
    main()
