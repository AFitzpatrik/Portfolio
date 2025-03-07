
'''
tkinter je knihovna pro vytváření grafických rozhraní v Pythonu.
messagebox slouží k zobrazení chybových hlášek nebo dialogů.
Importuješ potřebné nástroje pro tvorbu okna a zobrazení zpráv.
'''

'''
Podváha: BMI nižší než 18,5
Normální váha: BMI mezi 18,5 a 24,9
Nadváha: BMI mezi 25 a 29,9
Obezita: BMI 30 a více
'''

vaha = float(input("Vlož svojí váhu v KG "))
vyska = float(input("Vlož svojí výšku v M ")) # BMI = hmotnost (kg) / (výška v metrech)².


#BMI = vaha / (vyska)**2

vyskaBMI = vyska**2
BMI = vaha/vyskaBMI

if BMI < 18.5:
    print(f"Vaše BMI je {BMI:.3f}, dle BMI trpíte podváhou.")

elif  BMI > 29:
    print(f"Vaše BMI je {BMI:.3f}, dle BMI trpíte obezitou.")

elif 25 <= BMI <= 29.9:
    print(f"Vaše BMI je {BMI:.3f}, dle BMI trpíte nadváhou.")

else:
    print(f"Vaše BMI je {BMI:.3f}, dle BMI máte normální váhu.")



#elif 18.5 <= BMI <= 24.9: