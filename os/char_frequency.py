def character_frequency(filename):
    try:
        f = open(filename)
    except OSError:
        return None

    chars = {}
    for line in f:
        for char in line:
            chars[char] = chars.get(char, 0)+1
    f.close()
    return chars
