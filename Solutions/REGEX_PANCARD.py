import re
def validate_pancard(pancard):
    pattern = "^[A-Z]{5}[0-9]{4}[A-Z]{1}$"
    result = re.search(pattern, pancard)
    if result:
        return "pan"
    else:
        return "not pan"


pancard = input()
print(validate_pancard(pancard))