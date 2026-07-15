import bonuses.bonusfun as bonusfun

feet_inches=input("Enter feet and inches: ")
f,i=bonusfun.parse(feet_inches)
result=bonusfun.convert(f,i)
print(f"{f} feet and {i} inches is equal to {result} meters.")