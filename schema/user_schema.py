def user_serializer(user):
    return {
        'id': user['key'],
        'first_name': user['first_name'],
        'last_name': user['last_name'],
        'email': user['email'],
        'password': user['password']
    }

def users_serializer(users):
    return [user_serializer(user) for user in users]