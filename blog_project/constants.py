SECRET_KEY = 'l0on+3p@53(-hpeffu$s_su0qa4)fpz$57jx6f6zpfv2mdd@2u'


LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

AUTH_USER_MODEL = 'users.CustomUser'

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587
EMAIL_USE_TLS = True