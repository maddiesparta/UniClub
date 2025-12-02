from django.contrib.auth.hashers import make_password
settings.configure()
print(make_password("mypassword"))
