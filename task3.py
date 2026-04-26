# Task 3: Extract Email Addresses from a Text File

import re

# Open input file
file = open("data.txt", "r")
text = file.read()
file.close()

# Find email addresses
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Save emails to output file
out = open("emails.txt", "w")

for email in emails:
    out.write(email + "\n")

out.close()

print("Email addresses extracted successfully!")
print("Saved in emails.txt")