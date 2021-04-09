hash_function = hash
service = 'opm'
work = 5

def get_public_challenge():
    return {
        'hash_function': hash_function,
        'service': service,
        'work': work
    }
