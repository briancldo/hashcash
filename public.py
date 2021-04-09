hash_function = hash
service = 'opm'
work = 5
desired_token = '1' * work

def get_public_challenge():
    return hash_function, service, work, desired_token
