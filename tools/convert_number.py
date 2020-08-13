from num2words import num2words


def convert_number(numb: int):
    return num2words(numb, lang='fr')
