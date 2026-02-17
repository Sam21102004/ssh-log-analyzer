import re

# Open log file
file = open("SSH_logs.txt", "r")

ip_count = {}
total_failed = 0

for line in file:
    if "Failed password" in line:
        total_failed += 1

        # Extract IP address (works for IPv4 and IPv6)
        parts = line.split("from ")
        if len(parts) > 1:
            ip_part = parts[1]
            ip = ip_part.split(" ")[0]

            if ip in ip_count:
                ip_count[ip] += 1
            else:
                ip_count[ip] = 1

file.close()

# Print results
print("\nTotal Failed Login Attempts:", total_failed)

print("\nFailed Attempts Per IP:")
for ip in ip_count:
    print(ip, ":", ip_count[ip])

print("\nSuspicious IPs (More than 5 attempts):")
found = False

for ip in ip_count:
    if ip_count[ip] > 5:
        print("Suspicious IP:", ip, "| Attempts:", ip_count[ip])
        found = True

if not found:
    print("No suspicious activity detected.")
