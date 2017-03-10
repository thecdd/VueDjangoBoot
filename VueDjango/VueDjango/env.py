import os

default_env = 'DEV'
IS_DEV = (os.getenv('ENV', default_env).upper() == default_env)

DB_CONFIG = {
    'mongodb': {
        'host': os.getenv('ENV_MONGODB_HOST', 'mongodb://localhost/vue-django'),
        'db': os.getenv('ENV_MONGODB_DB', 'vue-django')
    }
}

SITE_CONFIG = {
    'static_url': os.getenv('STATIC_URL', '/static/'),
    'base_url': os.getenv('BASE_URL', '/'),
}
