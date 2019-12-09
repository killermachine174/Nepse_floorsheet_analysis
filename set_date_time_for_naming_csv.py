from datetime import datetime as dt


def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

def first_part():
    return (list(custom_strftime('%B {S}, %Y', dt.now()).split(' '))[1].split(',')[0])
def second_part():
    return dt.today().strftime('%B')
def third_part():
    return dt.today().year
the_name = '{}_{}_{}'.format(first_part(),second_part(),third_part())
