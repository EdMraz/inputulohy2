def uloha1(n,ret):
    d = len(ret)
    if d > n:
        return ret[n:n+1:]
    else:
        return "Daný znak neexistuje v zadanom čísle.(Zlý index)"

print(uloha1(3,"kuk"))
print(uloha1(6,"kamikadze"))
