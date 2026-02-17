# SSH Log Analyzer (Python)

A Python-based SSH log analysis tool that detects failed login attempts and identifies potential brute-force attacks by analyzing authentication logs.


# Project Overview

-> The SSH Log Analyzer reads system authentication logs and extracts information related to failed SSH login attempts.

-> It helps in detecting suspicious IP addresses that may be attempting brute-force attacks.

-> This project demonstrates basic cybersecurity log analysis and blue-team monitoring concepts.

# Technologies Used

- Python 3
- File Handling
- String Processing
- Basic Pattern Matching

# Project Structure

ssh-log-analyzer/
│── log_analyzer.py
│── SSH_logs.txt
└── README.md

# How to Run the Project

1. Clone the Repository

-> git clone [https://github.com/yourusername/ssh-log-analyzer.git](https://github.com/Sam21102004/ssh-log-analyzer.git)

2. Go to Project Folder

-> cd ssh-log-analyzer

3. Run the Script

-> python3 log_analyzer.py

# How the Script Works

-> Opens the SSH log file.

-> Reads the file line by line.

-> Searches for lines containing "Failed password".

-> Extracts IPv4 and IPv6 addresses.

-> Counts failed login attempts per IP.

-> Flags IPs with more than 5 failed attempts as suspicious.

# Features
✔ Detects failed SSH login attempts
✔ Supports both IPv4 and IPv6
✔ Counts attempts per IP address
✔ Identifies potential brute-force attacks
✔ Simple and easy-to-understand code

# Output:

<img width="484" height="199" alt="Screenshot From 2026-02-17 23-20-41" src="https://github.com/user-attachments/assets/01c5fd52-840c-4ae6-a508-9b95ba0b7d41" />

# Learning Outcomes

- Understanding SSH authentication logs

- Detecting brute-force attack patterns

- Python file handling

- Basic cybersecurity monitoring







