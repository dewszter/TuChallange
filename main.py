def DelbaraMed7():
   m = int(input("Skriv nedre gräns: "))
   n = int(input("Skriv övre gräns: "))
   print("\n Här är alla talen som är delbara med 7:")
   
   for num in range(m, (n + 1)):
        if num % 7 == 0:
            print(num)

def DivisionMedRest():
    m = int(input("Skriv nedre gräns: "))
    n = int(input("Skriv övre gräns: "))
    a = int(input("Skriv delaren: "))
    b = int(input("Skriv den önskade resten: "))

    print("\n Här är talen som när man delar de med " + str(a) + " så får man resten " + str(b) + ":")
    for num in range(m, (n + 1)):
        if num % a == b:
            print(num)

def Kongurent():
    m = int(input("Skriv nedre gräns: "))
    n = int(input("Skriv övre gräns: "))
    b = int(input("Skriv modulo: "))
    r = int(input("Skriv den önskade resten: "))

    print("\n Här är talen som blir kongurenta när man delar de med " + str(b) + " och får resten " + str(r) + ":")
    for num in range(m, (n + 1)):
        if num % b == r:
            print(num)
            
def PerfektaTal():
    m = int(input("Skriv nedre gräns: "))
    n = int(input("Skriv övre gräns: "))

    print("\n Här är de perfekta talen:")
    for num in range(m, (n + 1)):
        sum = 0
        for p in range(1, num):
            if  num % p == 0:
                    sum += p
                    
        if num == sum:
            print(num)
                        