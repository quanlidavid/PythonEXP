import sys

script, input_encoding, error = sys.argv


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(next_lang, " : ", raw_bytes, "<===>", cooked_string)


def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)


print(0b1011010)
# Return the Unicode code point for a one-character string.
print(ord('Z'))
print(chr(90))



# python Ex23_StringsBytesandCharacterEncodings.py utf-8 strict
# python Ex23_StringsBytesandCharacterEncodings.py big5 replace
