import pylab as py
import time

def prime_sieve(n):
    """returns a list of all primes under n"""
    p = [True] * n
    p[0] = p[1] = False
    for i in range(len(p)):
        if (p[i]):
            for j in range(i**2, len(p), i):
                p[j] = False
    ret = []
    for i in range(len(p)):
        if (p[i]):
            ret.append(i)
    return ret

def perfect_number(n):
    """returnerer det minste perfekte tallet over n"""
    #vi gjør om tallet vi får til nærmeste eksponent for en toerpotens fordi
    #vi ikke trenger så mange vanlige primtall
    exp = n.bit_length()
    #10 er en passende skalar for å sørge for at vi har nok primtall
    primes = prime_sieve(exp * 10)
    
    for i in range(len(primes)):
        #bruker Lucas Lehmer algoritmen for å teste for mersenneprimtall
        s = 4
        M = 2**primes[i] - 1
        for j in range(primes[i] - 2):
            s = ((s**2) - 2) % M
        #vi vil inkludere 6 som et perfekt tall, så vi må godkjenne 3 som mersenne
        if (s == 0 or primes[i] == 2):
            #perfect numbers on the form 2**(p - 1)(2**p - 1) if the latter 
            #factor is mersenne
            pn = 2**(primes[i] - 1) * M
            #dersom tallet er stort nok, godkjenner vi det
            if (pn > n):
                return pn
    #gi feilmelding dersom vi ikke hadde nok primtall for å finne vårt perfeke tall
    return -1

n = int(input("skriv inn eksponent til en toerpotens: "))
n = 2**n
print(f"finner neste perfekte tall etter {n} ({len(str(n))} sifre).")
t0 = time.time()
pn = perfect_number(n)
t = time.time()
print(f"Dette tallet er: {pn} ({len(str(pn))} sifre). Funnet på {t - t0:.4} sekunder")   
