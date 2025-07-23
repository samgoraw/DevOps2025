import re

text = "contact me at sam.gourav19@gmail.com or sam.gourav88@hotmail.com"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern,text)
print(emails)
