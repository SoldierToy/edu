from collections import namedtuple

Tokens = namedtuple('Tokens', ['access_token', 'refresh_token'])


def create(a, b):
    Tokens.access_token = a
    Tokens.refresh_token = b

    return Tokens


token_1 = create(2, 4)
token_2 = create(8, 9)

print(token_1 == token_2)
from collections import namedtuple

Tokens = namedtuple('Tokens', ['access_token', 'refresh_token'])

def create(a, b):
    Tokens.access_token = a
    Tokens.refresh_token = b

    return Tokens

token_1 = create(2, 4)
token_2 = create(8, 9)

print(token_1.refresh_token)
print(token_2.refresh_token)
print(token_1 == token_2)