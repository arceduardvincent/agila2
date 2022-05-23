import os
DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = "cod3geas@gmail.com"
# EMAIL_HOST_PASSWORD = "iamlegend1990"

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = env.str("EMAIL_HOST", "smtp.sendgrid.net")
# EMAIL_HOST_USER = 'apikey'
# EMAIL_HOST_PASSWORD = "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"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
#
# DEFAULT_FROM_EMAIL = 'roseann.mojsic@crowdbotics.com'
