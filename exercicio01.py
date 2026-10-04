c2 = int(input("Qual a concentração de CO₂ (ppm): "))

if c2 <= 800:
    print("Ar adequado")
elif c2 <= 1200:
    print("Atenção")
else:
    print("Ventilar a sala")
    
