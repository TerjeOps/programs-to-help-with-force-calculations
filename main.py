
# numerator betyr talet over brøkstreken, og determinator er talet under brøkstreken
import math
# while True gjer at den går i loop
while True:
    numerator = input("what is the numerator")
    numerator = int(numerator)

    determinator = input("what is the determinator?")
    determinator = int(determinator)

    length = input("what is the total lenght of the vector?")
    length = float(length)

    fzfraction = float(math.sqrt(determinator**2/(numerator**2+determinator**2)))
    fz = float(fzfraction*length)
    fx = float(numerator/determinator*fz)

    print("fz=", fz, "kN")
    print("fx=", fx, "kN")
    again = input("type new to do a new vector")
    again = str(again)
    if again != 'new':
        break #break gjer at den går ut av loopen, dersom "new" ikkje blir skrive.
