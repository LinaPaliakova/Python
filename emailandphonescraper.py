import re
from data import text

phone_num = re.compile(r'((?:\(?\d{3}?\)?[-\s]?)?(?:\d{3})-(?:\d{4})(?:\s?x\d+)?(?:ext\.\s)?(?:\d+)?)')
regex_email=re.compile(r'((?:\w+)@(?:\w+)\.(?:\w+))')


numbers = re.findall(phone_num, text)
emails = re.findall(regex_email, text)
all_together = numbers + emails
print(*all_together, sep="\n")
