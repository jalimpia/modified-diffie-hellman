import math
import random, sys, os, rabinMiller, cryptomath

def generateKey(p,q,keySize):
   # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
   #print('Generating p prime...')
   p = rabinMiller.generateLargePrime(keySize)
   #print('Generating q prime...')
   q = rabinMiller.generateLargePrime(keySize)
   n = p * q

   # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
   #print('Generating e that is relatively prime to (p-1)*(q-1)...')
   while True:
      e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
      if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
         break

   # Step 3: Calculate d, the mod inverse of e.
   #print('Calculating d that is mod inverse of e...')
   d = cryptomath.findModInverse(e, (p - 1) * (q - 1))
   return (e, d, n)

# e, d, n = generateKey(1062668879033,909887539849,keySize)
# print("e=",e)
# print("d=",d)
# print("n=",n)
#
# ct = pow(1299709,e,n)
# pt = pow(ct,d,n)
# print(ct)
# print(pt)
