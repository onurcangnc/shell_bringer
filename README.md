# ShellBringer

![Main Image](mainScreen.png)

## Introduction
ShellBringer is a Python script designed for penetration testers. It facilitates the creation and management of reverse shell payloads, automating listener setup across multiple platforms.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Dependencies](#dependencies)
5. [Configuration](#configuration)
6. [Examples](#examples)
7. [Troubleshooting](#troubleshooting)
8. [Contributors](#contributors)
9. [License](#license)

## Installation
To install ShellBringer, follow these steps:

1. Ensure Python 3.6+ is installed on your system.

2. Clone the repository:
   ```bash
   git clone https://github.com/onurcangnc/shell_bringer.git

3. Install required Python packages:
   ```bash
   pip install -r requirements.txt

## Usage
To start using ShellBringer, run the following command in your terminal:

   ```python
    python3 shellbringer.py

Follow the interactive prompts to generate reverse shells or start a listener.

## Dependencies
ShellBringer requires the following Python libraries:

- pyfiglet (Used for creating ASCII art text banners)
- colorama (Used for adding color and style to the text printed in the terminal.)
- ipaddress (Used for validating IPv4 addresses)
- platform (Used to detect the operating system)
- subprocess (Used for spawning new processes)
- ctypes (Used to interact with the Windows API, specifically for checking and requesting administrator privileges)
- sys (Used to interact with interpreter to exit the program)
- time (Delay of 2 seconds when exiting the script)


## Features
*Multi-OS Support:* Compatible with Linux, macOS, and Windows.
*Interactive CLI:* User-friendly command line interface for ease of use.
*Dynamic Payload Generation:* Supports multiple types of reverse shells.
*Listener Automation:* Simplifies the process of setting up listeners with netcat/ncat.

## Configuration

As it has shown above, the script has several library dependencies. Besides, you should configure it according to your operating system.

###Linux
    - rlwrap is not a built-in command in many Linux distros. That's why you should install it.
    
    1. Debian/Ubuntu-based systems:

    ```bash
    sudo apt-get update
    sudo apt-get install rlwrap
    ```

    2. Red Hat-based systems (Fedora, CentOS, RHEL):

    ```bash
    sudo dnf install rlwrap  # For Fedora
    sudo yum install rlwrap  # For CentOS/RHEL
    ```

    3. Arch Linux  

    ```bash
    sudo pacman -Sy rlwrap
    ```

    4. openSUSE
    ```bash
    sudo zypper install rlwrap
    ```

    - DO NOT FORGET TO CHECK THE WHETHER YOU HAVE 'NETCAT' or not
    
    ```bash
    which nc
    ```

###Windows
    - As you know Windows operating system does not support netcat directly. Therefore, we have another alternative for that.
      Ncat is a modern reimplementation of the classic Netcat (nc) tool. Shell-Bringer only supports that listener.

1. *Using Nmap Installer:*
    1. Download Nmap for Windows:
     - Visit the official Nmap download page at https://nmap.org/download.html and download the Windows installer.
    2. Run the Installer:
     - Run the downloaded Nmap installer (.exe file) and follow the on-screen instructions.
    3. Select Components:
     - During the installation process, ensure that you select the option to install Ncat along with Nmap. The installer usually provides checkboxes for components like Ncat, Zenmap, etc.
    4. Complete Installation:
     - Complete the installation by following the prompts. Once done, Ncat will be installed on your system.

2. *Using Chocolatey (Package Manager for Windows):*
    1. Install Chocolatey (if not already installed):
        - Open an elevated Command Prompt (run as administrator) and run the following command:

    ```powershell
    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    ```

    2. Install Nmap (including Ncat) via Chocolatey:
        - After Chocolatey is installed, you can install Nmap with the following command:

        ```powershell
        choco install nmap
        ```

    3. Verify Installation:
        - After installation, verify that Nmap and Ncat are installed by running nmap --version and ncat --version in Command Prompt or PowerShell.

###MacOS
    1. *Install Homebrew (if not already installed):*
        - Open Terminal and run the following command to install Homebrew:

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

    2. *Install Nmap (includes Ncat) using Homebrew:*
        - Once Homebrew is installed, you can install Nmap, which includes Ncat, by running:

    ```bash
    brew install nmap
    ```

    3. *Verify Installation:*
    After installation is complete, you can verify that Nmap and Ncat are installed by running:

    ```bash
    nmap --version
    ```

    ```bash
    ncat --version
    ```

##Example Runs

###Windows (Some uncompatible UI issues because of the unsupported CLI)

![Windows Image](powershell.gif)

![Windows Image2](commandPrompt.gif)


###Kali Linux

![Kali Image](kali.gif)


###macOS
![macOS Image](powershell.gif)