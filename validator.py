import re


# Validates message name.
def name(val):
    if not val:
        return "Your name is required!"

    # Need more validators here

    return None


# Validates message content.
def content(val):
    if re.search(r'twilight', val, re.IGNORECASE):
        return "You can't talk about Twilight here!"

    if re.search(r'https?://', val, re.IGNORECASE):
        return "You can't post links!"

    # Need more validators here
    
    if len(val)>140:
        return "chillax bro its all like twitter up in here"

    return None