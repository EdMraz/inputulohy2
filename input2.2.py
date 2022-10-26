def uloha2(string:str):
    counter = 0
    i = 0
    while i < len(string):
        for x in string[i]:
            if x.isnumeric() == True:
                counter+=1
                i+=1
            else:
                i+=1
    return counter

print(uloha2("Na farme mame od roku 2012 12 kráv a 230 oviec."))
print(uloha2("Skutok sa stal."))
print(uloha2("snehulienka a 7 trpazlikov."))
