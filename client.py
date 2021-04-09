import random

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
def get_random_string():
    character_count = random.randint(5, 10)
    return ''.join(random.choice(characters) for i in range(character_count))

def mint(hash_function, service: str, work: int, desired_token: str) -> str:
    i = 1
    while (True):
        x = get_random_string()
        hashed_result = str(hash_function(service + x))
        token = hashed_result[:work]
        
        if token == desired_token:
            return x, i
        
        if i % 100000 == 0:
            print(f'{i} guesses so far.')
        i += 1
        