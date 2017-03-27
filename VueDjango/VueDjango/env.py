import os

DEFAULT_PROJECT_NAME = 'vue_boot'
DEFAULT_ENV = 'DEV'
IS_DEV = (os.getenv('ENV', DEFAULT_ENV).upper() == DEFAULT_ENV)
PROJECT_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def __get_env(name, default):
    prefix = os.getenv('PROJECT_ENV_VAR_PREFIX', DEFAULT_PROJECT_NAME)
    prefix_separator = os.getenv('PROJECT_ENV_SEPARATOR', '_')
    if prefix is None:
        return os.getenv(name, default)
    else:
        new_name = prefix + prefix_separator + name
        return os.getenv(new_name, default)


PROJECT_CONFIG = {
    'project_name': os.getenv('PROJECT_NAME', DEFAULT_PROJECT_NAME),
}

DB_CONFIG = {
    'mongodb': {
        'host': __get_env('ENV_MONGODB_HOST', 'mongodb://localhost/vue-django'),
        'db': __get_env('ENV_MONGODB_DB', 'vue-django')
    }
}

SITE_CONFIG = {
    'base_context': __get_env('BASE_CONTEXT', ''),
    'base_url': __get_env('BASE_CONTEXT', '') + '/',
    'static_url': __get_env('STATIC_URL', '/static/'),
    'session_time': int(__get_env('SESSION_COOKIE_AGE', str(24 * 60 * 60))),
    'session_name': os.getenv('PROJECT_NAME', DEFAULT_PROJECT_NAME) + '_' + 'session_id',
    'csrftoken_name': os.getenv('PROJECT_NAME', DEFAULT_PROJECT_NAME) + '_' + 'csrftoken',
    'log_level': ('DEBUG' if IS_DEV else 'INFO'),
    'log_path': __get_env('LOG_LOG_FOLDER', 'log'),
    'env': IS_DEV,
}
