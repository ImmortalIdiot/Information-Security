import traceback
INCORRECT_INPUT_PHRASE = "Incorrect input"


def require_not_null(x):
    try:
        if not x:
            raise ValueError
    except ValueError:
        print(traceback.print_exc())
        exit(1)


def require_symbols_in_string(s, alphabet):
    try:
        for c in s:
            if c not in alphabet:
                raise ValueError
    except ValueError:
        print(traceback.print_exc())
        exit(1)


def incorrect_user_input():
    try:
        raise ValueError
    except ValueError:
        print(INCORRECT_INPUT_PHRASE)
        exit(1)
