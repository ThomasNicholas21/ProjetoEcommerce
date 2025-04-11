def get_file_name(instance, filename):
    name = instance.user.username.lower().replace(' ', '-')
    return f'profile_pictures/{name}/{filename}'
