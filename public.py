default_hash_function = hash
default_service = 'opm'
default_work = 3
desired_token_character = '1'

def get_public_challenge(
        hash_function=default_hash_function,
        service=default_service,
        work=default_work,
):
    desired_token = desired_token_character * work
    return hash_function, service, work, desired_token
