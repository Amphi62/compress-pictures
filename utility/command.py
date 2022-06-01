import re


def check_is_option(value: str) -> bool:
    return value.startswith('-')


def check_next_is_ok(arguments, i):
    return len(arguments) > (i + 1)


def get_quality(value: str) -> int:
    if not re.findall(r'[0-9]+', value):
        raise Exception('La valeur doit être un chiffre pour la qualité.')

    result = int(value)

    if result > 100 or result <= 0:
        raise Exception('La valeur de la qualité doit être comprise entre 1 et 100')

    return result


def extension(value: str) -> str:
    if not value.startswith('.'):
        return '.' + value
    return value
