def vypocitej_bmi(vaha: float, vyska: float) -> float:
    return vaha / (vyska ** 2)


def ziskani_kategorie(BMI: float) -> str:
    if BMI < 18.5:
        return "dle BMI trpíte podváhou."
    elif 25 <= BMI <= 29.9:
        return "dle BMI trpíte nadváhou."
    elif BMI > 29:
        return "dle BMI trpíte obezitou."
    else:
        return "dle BMI máte normální váhu."


def main():
    while True:  # Nekonečný cyklus, dokud nejsou vstupy správné
        try:
            vaha = float(input("Vložte svoji váhu v kg: "))
            vyska = float(input("Vložte svoji výšku v m: "))

            BMI = vypocitej_bmi(vaha, vyska)
            Kategorie = ziskani_kategorie(BMI)

            print(f"Vaše BMI je: {BMI:.2f}, {Kategorie}")
            break  # Správné zadání → ukončit cyklus

        except ValueError:
            print("Chyba: Zadejte prosím platná čísla.")


if __name__ == "__main__":
    main()