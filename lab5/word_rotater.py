CAP_FIRST_CHARACTER='A'
CAP_LAST_CHARACTER='Z'
LOWER_FIRST_CHARACTER='a'
LOWER_LAST_CHARACTER='z'

def rotater(sentence, num):

    for ch in sentence:
        ascii_code = ord(ch)

        if ascii_code > ord(CAP_FIRST_CHARACTER) and ascii_code < ord(CAP_LAST_CHARACTER):
            number_moved_by = ord(CAP_FIRST_CHARACTER)
        elif ascii_code > ord(LOWER_FIRST_CHARACTER) and ascii_code < ord(LOWER_LAST_CHARACTER):
            number_moved_by = ord(LOWER_FIRST_CHARACTER)
        else:
            print(ch, end="")
            continue

        new_code = ascii_code - number_moved_by
        after_rotation = (new_code + num)%26

        new_code_after_rotation = number_moved_by + after_rotation

        print(chr(new_code_after_rotation), end="")

rotater("Hello WoRld", -26)