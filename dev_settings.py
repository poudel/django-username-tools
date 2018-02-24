DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "j_#z&ong90bu#!j))e0=2*0ygv_7cd8wa8%ue10y_65pczq+-g"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "username_tools",
]

MIDDLEWARE = ()
