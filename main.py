from public import get_public_challenge
from client import mint
from verifier import verify

if __name__ != '__main__':
    exit(0)

hash_function, service, work, desired_token = get_public_challenge()
print(desired_token)
x, i = mint(hash_function, service, work, desired_token)
print(f'Found x: {x} in {i} attempts')
print(f'To what does "service + x" hash? {hash_function(service + x)}')
verify_result = verify(hash_function, service, work, desired_token, x)
print(f'Verification result: {verify_result}')
