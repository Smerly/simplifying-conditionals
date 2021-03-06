# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')


def make_accept_sound():
    print('made acceptance sound')


def has_sodium_nitrate():
    if 'sodium nitrate' in ingredients:
        return True
    else:
        return False


def has_sodium_benzoate():
    if 'sodium benzoate' in ingredients:
        return True
    else:
        return False


def has_sodium_oxide():
    if 'sodium oxide' in ingredients:
        return True
    else:
        return False


ingredients = ['sodium benzoate']
if has_sodium_nitrate() or has_sodium_benzoate() or has_sodium_oxide():
    print('!!!')
    print('there is a toxin in the food!')
    print('!!!')
    make_alert_sound()
else:
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()
