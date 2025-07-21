PluralNoun= input("enter a Plural Noun: ")
while not PluralNoun.isalpha() :
    print("Please Enter a Valid Word!")
    PluralNoun = input("enter a Plural Noun: ")


Place= input("enter a Place: ")
while not Place.isalpha() :
    print("Please Enter a Valid Word!")
    PluralNoun = input("enter a Place: ")


Noun= input("enter a Noun: ")
while not Noun.isalpha() :
    print("Please Enter a Valid Word!")
    Noun = input("enter a Noun: ")

INGNoun= input("enter a Noun with Ing: ")
while not Noun.isalpha() :
    print("Please Enter a Valid Word!")
    Noun = input("enter a Noun with Ing: ")

Number = input("enter a Number: ")
while Number.isalpha() :
    print("Please Enter a Valid Number!")
    Number = input("enter a Number: ")

RoInFamily = input("Enter Someone Role in Family, ex: father,son... : ")
while not RoInFamily.isalpha() :
    print("Please Enter a Valid Word!")
    RoInFamily = input("enter a Role in Family, ex: father: ")

Adjective = input("Enter an Adjective: ")
while not Adjective.isalpha() :
    print("Please Enter a Valid Adjective!")
    Adjective = input("enter an Adjective: ")

BodyPart = input("Enter Name of a Body Part: ")
while not BodyPart.isalpha():
    print("Please Enter a Valid Body Part!")
    BodyPart = input("enter a Body Part: ")

print("Here's Your Story:")
print(f"One day, a man wanted to eat some {PluralNoun} ."
      f"\nand for that he goes to {Place} in order to buy them. Accidently,"
      f"\nhe found one {Noun} that weigh {Number} Kgs, he started {INGNoun},"
      f"\nand then recognized that it was his {RoInFamily}."
      f"\nhe was {Adjective} by finding his lost {RoInFamily}."
      f"\nand then carry it with his {BodyPart} to his house."
      "\nand they lived a long happy life.")
