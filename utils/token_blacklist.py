BLACKLIST_TOKENS = set()

def add_to_blacklist(token:str):
    BLACKLIST_TOKENS.add(token)
def is_token_blacklisted(token : str) -> bool :
    return token in BLACKLIST_TOKENS    