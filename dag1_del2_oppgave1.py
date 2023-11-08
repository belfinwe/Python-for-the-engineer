tekst = "Hello world!"

def rev(_t: str) -> str:
    res = ""
    for i in range(len(_t)-1, -1, -1):
        res += _t[i]
    return res


print(rev(tekst))