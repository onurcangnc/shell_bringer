import os
import re
import platform
import subprocess
import pyfiglet
import sys
import ctypes
import ipaddress
import time
from colorama import Fore, Style

from rev_shell_commands import ReverseShellCommands

# Constants
DEFAULT_PORT_MIN = 1
DEFAULT_PORT_MAX = 65535

def detect_os() -> str:
    """Detects the operating system and returns its name."""
    system = platform.system()
    if system == 'Linux':
        return "Linux"
    elif system == 'Darwin':
        return "macOS"
    elif system == 'Windows':
        return "Windows"
    else:
        return "Unknown"

def validate_ip(ip: str) -> bool:
    """Validates an IPv4 address and printing error message."""
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        print("Invalid IP address. Please try again.")
        return False

def start_netcat_listener(port: int, os_type: str, rev_shell: str, ip_version: str) -> None:
    """Starts a netcat listener based on the operating system."""
    if os_type == 'Linux':
        use_rlwrap = input("Use netcat with rlwrap? (y/n): ").lower()
        if use_rlwrap == 'y':
            subprocess.Popen(["rlwrap", "nc", "-lvnp", str(port)])
        else:
            subprocess.Popen(["nc", "-lvnp", str(port)])
    elif os_type == 'macOS':
        subprocess.Popen(["ncat", "-lvnp", str(port)])
    elif os_type == 'Windows':
        # Request administrator privileges
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            print("This script requires administrator privileges. Restarting with elevated permissions...")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit(0)
        
        ncat_path = r"C:\Program Files (x86)\Nmap\ncat.exe"  # Replace with the actual path to ncat
        subprocess.Popen([ncat_path, "-lvnp", str(port)])

def print_reverse_shell_types(rev_shell_commands: ReverseShellCommands) -> None:
    """Prints available reverse shell commands with colors."""
    print(highlight_text("\nAvailable reverse shell commands:", color=Fore.LIGHTYELLOW_EX, style=Style.BRIGHT))
    for index, (key, value) in enumerate(rev_shell_commands.list_commands().items(), start=1):
        print(highlight_text(f"{index}. ", color=Fore.LIGHTCYAN_EX, style=Style.BRIGHT) + highlight_text(value['name'], color=Fore.WHITE, style=Style.NORMAL))


def get_user_input(prompt: str, validate_func) -> str:
    """Gets user input and validates it, printing a custom message if input is invalid."""
    while True:
        try:
            user_input = input(prompt)
            if validate_func(user_input):
                return user_input
            else:
                print("Invalid input. Please try again.")
        except KeyboardInterrupt:
            print("\nKeyboard interrupt detected. Please try again.")


def highlight_text(text: str, color=Fore.WHITE, style=Style.NORMAL) -> str:
    """Highlights the text with specified color and style."""
    return f"{style}{color}{text}{Style.RESET_ALL}"

def print_contact_info() -> None:
    """Prints contact information from contact_info.txt."""
    with open('contact_info.txt', 'r') as file:
        social_media = file.read()

    print(highlight_text("\nContact:", color=Fore.LIGHTRED_EX, style=Style.BRIGHT))
    print(highlight_text("************************************", color=Fore.LIGHTYELLOW_EX, style=Style.NORMAL))
    print(highlight_text(social_media, color=Fore.GREEN, style=Style.BRIGHT))

def print_header() -> None:
    """Prints the header."""
    with open('header_ascii.txt', 'r') as file:
        ascii_banner = file.read()

    tool_banner = pyfiglet.figlet_format("SHELL BRINGER")

    print(highlight_text(ascii_banner, color=Fore.YELLOW, style=Style.BRIGHT))
    print(highlight_text(tool_banner, color=Fore.GREEN, style=Style.BRIGHT))
    print(highlight_text("Brand New Swiss Army Butterfly Knife!", color=Fore.RED, style=Style.NORMAL))
    print(highlight_text("Reverse Shell Generator + Listener", color=Fore.RED, style=Style.NORMAL))
    print(highlight_text("powered by Onurcan Genc\n", color=Fore.RED, style=Style.BRIGHT))
    print(highlight_text("************************************", color=Fore.YELLOW, style=Style.NORMAL))
    print_contact_info()
    os_type = detect_os()
    print(highlight_text("\nOS Detection:", color=Fore.LIGHTRED_EX, style=Style.BRIGHT), highlight_text(os_type, color=Fore.LIGHTGREEN_EX, style=Style.BRIGHT))
    print(highlight_text("************************************", color=Fore.YELLOW, style=Style.NORMAL))

def print_goodbye_message() -> None:
    goodbye_banner = pyfiglet.figlet_format("GOODBYE!")
    print(highlight_text("\n" + goodbye_banner, color=Fore.RED, style=Style.BRIGHT))
    print(highlight_text("************************************\n", color=Fore.YELLOW, style=Style.NORMAL))
    print(highlight_text("Thank you for using ShellBringer!", color=Fore.GREEN, style=Style.BRIGHT))
    time.sleep(1)

def get_shell_option(rev_shell_commands):
    """Get the shell option from user input."""
    shell_types = list(rev_shell_commands.list_commands().keys())
    while True:
        try:
            option = int(input(highlight_text("Enter the shell option:", color=Fore.WHITE, style=Style.NORMAL) + highlight_text("(0 to exit) ", color=Fore.LIGHTRED_EX, style=Style.BRIGHT)))
            if option == 0:
                return -1
            elif option in range(1, len(shell_types) + 1):
                return option
            else:
                print("Invalid option. Please choose again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main() -> None:
    """Main function to run the script."""
    print_header()

    rev_shell_commands = ReverseShellCommands()

    while True:
        print(highlight_text("\n1. ", color=Fore.LIGHTRED_EX, style=Style.BRIGHT), "List all available reverse shell types")
        print(highlight_text("0. ", color=Fore.LIGHTRED_EX, style=Style.BRIGHT), "Exit\n")

        choice = get_user_input(highlight_text("Enter your choice ", color=Fore.RED, style=Style.BRIGHT) + highlight_text("(0-1): ", color=Fore.RED, style=Style.BRIGHT), lambda x: x in ['0', '1'])

        if choice == "0":
            print_goodbye_message()
            break
        elif choice == "1":
            print_reverse_shell_types(rev_shell_commands)  # Print the list again when requested
            option = get_shell_option(rev_shell_commands)

            if option == -1:
                print_goodbye_message()
                break

            shell_types = list(rev_shell_commands.list_commands().keys())
            if option not in range(1, len(shell_types) + 1):
                print("Invalid option. Please choose again.")
                continue

            shell_type = shell_types[option - 1]
            ip_version = input("Enter '4' for IPv4 or '6' for IPv6: ")
            while ip_version not in ['4', '6']:
                print("Invalid IP version. Please choose IPv4 or IPv6.")
                ip_version = input("Enter '4' for IPv4 or '6' for IPv6: ")

            ip = get_user_input(highlight_text("Enter your IP address: ", color=Fore.LIGHTRED_EX, style=Style.BRIGHT), validate_ip)
            port = get_user_input(highlight_text(f"Enter the port number ({DEFAULT_PORT_MIN}-{DEFAULT_PORT_MAX}): ", color=Fore.LIGHTRED_EX, style=Style.BRIGHT), lambda x: x.isdigit() and DEFAULT_PORT_MIN <= int(x) <= DEFAULT_PORT_MAX)

            command = rev_shell_commands.get_command(shell_type, port, ip)
            if command:
                print(highlight_text("\nPrepared payload(s):\n", color=Fore.LIGHTRED_EX, style=Style.BRIGHT))
                for i, command in enumerate(command, start=1):
                    print(highlight_text(f"{i}. ", color=Fore.LIGHTCYAN_EX, style=Style.BRIGHT) + highlight_text(command, color=Fore.WHITE, style=Style.NORMAL), "\n")
            else:
                print("\nInvalid option. Please choose again.\n")

            start_listener = input("\nStart listener? (y/n): ").lower()
            if start_listener == 'y':
                print(highlight_text("\nStarting listener...", color=Fore.LIGHTRED_EX, style=Style.BRIGHT))
                print(highlight_text("Press Ctrl+C to exit the listener.\n", color=Fore.LIGHTRED_EX, style=Style.BRIGHT))
                start_netcat_listener(int(port), detect_os(), command, ip_version)

if __name__ == "__main__":
    main()


