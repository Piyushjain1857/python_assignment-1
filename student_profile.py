# Name: Piyush Jain
# Roll No: 2501060053
# Cours: BCA
# Semster: 1st
# Subjet: Problem Solving with Python
# Assignment: Unit-1 Mini Project
# Title: Student Profile 
# Date: 13 Nov 2025

print("WELCOM TO STUDNT PROFILE APP")
print("this ap takes your detail and makes profile!!")
print("you will see sum python operators and string stufs\n")

studname = input("Enter your full name: ")
rollnumbr = input("Type roll number: ")
progrm = input("Wht program (ex. BCA): ")
univ = input("Give university name: ")

city = input("Which city you live in? ")
aeg = int(input("Your age? "))
hobi = input("Your hobby: ")

numa = int(input("put first number: "))
numb = int(input("put secnd number: "))

# Operators area
print("Aritmetic Opertars:")
print(str(numa) + " + " + str(numb) + " = " + str(numa + numb))
print(str(numa) + " - " + str(numb) + " = " + str(numa - numb))
print(str(numa) + " * " + str(numb) + " = " + str(numa * numb))
print(str(numa) + " / " + str(numb) + " = " + str(numa / numb))
print(str(numa) + " % " + str(numb) + " = " + str(numa % numb))
print(str(numa) + " ** " + str(numb) + " = " + str(numa ** numb))

# Assignments
temp = numa
print("Assigment Oprtrs:")
temp += 10
print("temp += 10", temp)
temp -= 2
print("temp -= 2", temp)
temp *= 3
print("temp *= 3", temp)

# Comparison
print("Comparsion Oprtrs:")
print(str(numa) + " == " + str(numb), numa == numb)
print(str(numa) + " > " + str(numb), numa > numb)

# Logical
print("Logical Ops:")
print((numa > 5) and (numb > 5))
print((numa < 0) or (numb < 0))

# Identity
print("Ident Ops:")
print("numa is numb:", numa is numb)
print("numa is not numb:", numa is not numb)

# Membership
sampl_str = "Python Program"
print("Membrshp Ops:")
print("'P' in", sampl_str, 'P' in sampl_str)
print("'x' not in", sampl_str, 'x' not in sampl_str)

print("------ PYTHON STRING METHOD DEMO -------")
print("Big letters name:", studname.upper())           
print("Small city:", city.lower())                     
print("Nice Hobby:", hobi.title())                     
print("City with a->@:", city.replace("a", "@"))       

# Escape sequence demo
print("Newline si here\nSecond line seen!")         
print("Quote in string: \"python is nice\"")        

print("-------------STUDNT PROFILE SYSTEM---------------")
print("Name: " + studname)
print("Roll No: " + rollnumbr)
print("Cours: " + progrm)
print("Univ: " + univ)
print("Cty: " + city)
print("Age: " + str(aeg))
print("Hobby: " + hobi)
print("------------------------------------------")
print("welcom to Python Programin!")
print("------------------------------------------")

saveit = input("save profile? (y/n): ")
if saveit.lower() == "y":
    fle = open("studnt_profile.txt", "w")
    fle.write("----- STUDNT PROFILE -----\n")
    fle.write("Name: " + studname + "\n")
    fle.write("Roll No: " + rollnumbr + "\n")
    fle.write("Cours: " + progrm + "\n")
    fle.write("Univ: " + univ + "\n")
    fle.write("City: " + city + "\n")
    fle.write("Age: " + str(aeg) + "\n")
    fle.write("Hobby: " + hobi + "\n")
    fle.write("--------------------------\n")
    fle.close()
    print("Profile saved in studnt_profile.txt")
else:
    print("Profile not saved")
