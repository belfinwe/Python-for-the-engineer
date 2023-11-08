# Oppgave 1
def summen(tallene):
    svar = 0
    for i in tallene:
        svar += i
    print(f"Summen av {tallene} er: {svar}")


def differansen(tallene):
    svar = tallene[0]
    for i in tallene[1:]:
        svar -= i
    print(f"Dersom differansen er å trekke fra alle talla er svaret: {svar}")

    for i in range(0, len(tallene)-2):
        no1 = tallene[i]
        no2 = tallene[i+1]
        print(f"Differansen mellom {no1} og {no2} er {no1-no2}")


def produkt(tallene):
    svar = 1
    for i in tallene:
        svar = svar * i
        print(f"{svar}")
    print(f"Produktet av {tallene} er: {svar}")



if __name__ == "__main__":
    _talliste = (27, 15, 6, 21, 52)
    summen(_talliste)
    differansen(_talliste)
    produkt(_talliste)