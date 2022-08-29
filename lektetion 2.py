"""
Fråga 1


inputen = input("Skriv in nåt så översätts det till pepega")
nyttord = ""
for i in inputen:
    if (i=='A' or i=='a' or i=='E' or i =='e' or i=='I' or i=='i' or i=='O' or i=='o' or i=='U' or i=='u'):
        nyttord += i
    else:
        nyttord += i + "o" + i
print(nyttord)
"""

"""
fråga 2


inputen = input("sig nått")
nytt = ""
for i in range(len(inputen)):
    back = len(inputen) - i
    nytt += inputen[back - 1]

print(nytt)

"""
"""
fråga 3
dic = {"Sverige": "Stockholm", "Norge": "Oslo", "Finland": "Helsingfors"}
dic.update({"danmark": "häsingör"})
dic.pop("Finland")
print(dic)
"""

"""
fråga 4
s1 = {"bannan", "päron", "äpple"}
s2 = {"kiwi", "annan", "päron"}
print(len(s1.union(s2)))

"""

