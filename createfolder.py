print(">> D&D File Creator\n")
f = open("dnd.txt", "w")
f.write("D&D File Creator\n")

#basic_info
name = input(">> Name: ")
clss = input(">> Class: ")
lvl = int(input(">> Level: "))

#stats
stats = list()
st = stats.append(int(input("\n>> Strenght: ")))
dx = stats.append(int(input("\n>> Dexterity: ")))
cn = stats.append(int(input("\n>> Constitution: ")))
it = stats.append(int(input("\n>> Inteligence: ")))
wd = stats.append(int(input("\n>> Wisdom: ")))
ch = stats.append(int(input("\n>> Charism: ")))

f.write(f"{name};{clss};{lvl};{stats}\n")
f.close()

print(">> End\n")

print("2")
