import os


def env_var(var_name):
    return os.environ.get(var_name, f'Environment variable "{var_name}" is not set.')
