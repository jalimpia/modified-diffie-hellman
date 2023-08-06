import secrets
def generate_token(n):
    result = secrets.token_urlsafe(n)
    return int.from_bytes(result,"big")
   

print(generate_token(20))