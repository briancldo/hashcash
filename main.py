from public import get_public_challenge
from client import mint

hash_function, service, work, desired_token = get_public_challenge()
x, i = mint(hash_function, service, work, desired_token)
print(f'Found x: {x} in {i} attempts')
print(f'To what does "service + x" hash? {hash_function(service + x)}')
