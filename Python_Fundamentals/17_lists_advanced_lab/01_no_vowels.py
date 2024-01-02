def check_if_vowel(char):
    volwel_char_codes=[65,97,69,101,73,105,79,111,85,117]
    if ord(char) in volwel_char_codes:
        return True
    else:
        return False
def filter_non_vowels(string):
    non_vowels=[char for char in string if not check_if_vowel(char)]
    return ''.join(non_vowels)

print(filter_non_vowels(input()))