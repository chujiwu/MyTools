import unicodedata


def has_illegal_field_field(formula, illegal_field):
    is_illegal = True
    if illegal_field in formula:
        left_index = formula.index(illegal_field)
        right_index = formula.index(illegal_field) + len(illegal_field)
        left_char = formula[left_index - 1]
        right_char = formula[right_index]
        if is_not_field_name_char(left_char) and is_not_field_name_char(right_char):
            is_illegal = False

            # if near_char_no_related()
    return is_illegal


def is_japanese(char):
    for ch in char:
        name = unicodedata.name(ch)
        if "CJK UNIFIED" in name \
                or "HIRAGANA" in name \
                or "KATAKANA" in name:
            return True
    return False


def is_particular_symbol(char):
    res = False
    if char == '_':
        res = True
    if char == '-':
        res = True
    if char == '.':
        res = True
    return res


def is_not_field_name_char(char: str):
    res = True
    if char.isalpha():
        res = False
    if is_japanese(char):
        res = False
    if char.isalnum():
        res = False
    if is_particular_symbol(char):
        res = False
    return res


if __name__ == "__main__":
    if has_illegal_field_field("FORMAT(Field1漢字, \"zzzzz\")", "Field1"):
        print("NG")
    else:
        print("OK")
