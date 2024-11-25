import os

# Overlaying production
from cvat.settings.production import *

# Add the $CVAT_HOST to the CSRF_TRUSTED_ORIGINS
CSRF_TRUSTED_ORIGINS = [f"https://{os.getenv('CVAT_HOST')}"]


# Email verification
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = os.getenv('ACCOUNT_EMAIL_REQUIRED') == 'True'
ACCOUNT_EMAIL_VERIFICATION = os.getenv('ACCOUNT_EMAIL_VERIFICATION')

# Email backend settings for Django
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASS')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') == 'True'

# Site ID which is used for the templates (i.e. email invites)
sid = int(os.getenv('SITE_ID'))
if sid > 0:
    SITE_ID = int(sid)
else:
    raise ValueError('SITE_ID must be greater than 0')
