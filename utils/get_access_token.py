import jwt

from datetime import datetime, timedelta
from django.conf import settings


def get_access_tokent(payload, expires):
    token = jwt.encode(
        {"exp": datetime.now() + timedelta(expires), **payload}, 
        settings.SECRET_KEY, 
        algorithm='HS256'
        )
