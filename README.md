# Python Password Strength Checker

## Overview
A configurable password security checker written in Python. This project explores password security principles, password validation and secure authentication practices

The project is being developed as part of my cybersecurity learning and portfolio development

### Development status
**Current version 1.1 (in development)**

- Completed: Initial password checker and JSON configuration
- In progress: NIST aligned validation and passphrase support
- Planned: Entropy estimation, breached password detection and automated testing

### Key Concepts explored
- Python programming and modular code design
- JSON configuration management
- Password security principles
- Dictonary handling and object attributes
- Password validation and common password detection
- Secure authentication practices

## Features
- Configurable minimum and maximum password lengths
- Common password dectection using a local password wordlist
- JSON based configuration
- Modular configuration management using Python's `SimpleNamespace`

## How it Works

Passwords are assessed against a set of configurable security rules

Configuration settings are stored in `config.json` and are loaded by `config.py`. Thee seperation of configuration fils from program logic allows users to edit configuration setting without altering the main Python program

### Configuration
The `config.json` file allows users to customise settings such as:
- Minimum password length
- Maximum password length

### Common password detection
The application checks passwords against a local password wordlist of 10,000 commonly used passwords

This wordlist is sourced from SecLists

## Requirements
- Python 3.x
- No external Python liberies are required for the current implementation

## Instalation
Clone the repository:

`git clone https://github.com/andyinfosec/password-checker.git`

Navigate to project directory

`cd password-checker`

Run application

`python3 password-checker` 

## Limitations
- Password strength estimation: The application uses predefined validation criteria rather than an advanced password strength estimation algorithm. It does not currently calculate entropy or estimate resistance to cracking
- Common password wordlist: The application compares passwords to a locally stored wordlist of 10,000 common passwords. This wordlist may not include newer, comprimised, or context specific passwords
- No breached password detection: The application does not currently check if a password has appearead in known data breaches
- Pattern recognition: Dectection of repeated characters, predictable sequences and common password patterns is limited
- No contextual analysis: The application does not currently identify passwords containing personal information, usernames, or other context-specific terms
- Configuration validation: Some parts of configuration validation and error handling are still being developed
- No automated testing: The application does not have an automated test suite.

## Planned improvements
- Breached password detection using the Have I Been Pwned Password API
- Add support for passphrases
- Addidtional password validation checks
- Password strength estimation
- Improved error handling and configuration validation
- Automated unit testing

## Disclamer
This project is developed for educational purposes. It is not a replacement for professional passsword security tools or password managers.

## Licence
This project is built and maintained under the MIT licence. See `licence.md` for details

## Resources
- SecLists - Password Wordlists
	- Source: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt
