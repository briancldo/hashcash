def verify(hash_function, service, work, desired_token, x):
    hashed_result = str(hash_function(service + x))
    token = hashed_result[:work]
    return token == desired_token