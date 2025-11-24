import re

mailpat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
numpat = re.compile("(0|91)?[7-9][0-9]{9}")

def valemail(email):
    return re.fullmatch(mailpat, email)

def valphone(phone):
    return numpat.match(phone)
