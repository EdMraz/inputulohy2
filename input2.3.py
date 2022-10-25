def uloha3(string):
    for i in string:
        if i in 'aeiouy':
            continue
        else:
            return False
    return True


print(uloha3("aero"))
