def viewNotes():
    with open("letterGrade.txt","r",encoding=("utf-8")) as file:
        print(file.read())


def note_enter():
    name = input("name: ")
    surname = input("surname: ")
    note1 = input("midterm: ")
    note2 = input("final: ")
    with open("examInformation.txt","a",encoding = ("utf-8")) as file:
        file.write(name + " " + surname +": "+ note1 + "," + note2 + "\n")
    

def saveNotes():
    with open("examInformation.txt","r",encoding = ("utf-8")) as file:
        for result in file.readlines():
            liste = result.split(":")
            note = liste[1].split(",")
            not1 = (int(note[0])* 0.4) + (int(note[1])* 0.6)

    if not1 >= 90:
        letterGrade = "AA"
    elif not1 >= 85:
        letterGrade = "BA"
    elif not1 >= 80:
        letterGrade = "BB"
    elif not1 >= 75:
        letterGrade = "CB"
    elif not1 >= 65:
        letterGrade = "CC"
    elif not1 >= 58:
        letterGrade = "DC"
    elif not1 >= 50:
        letterGrade = "DD"
    else:
        letterGrade = "FF"

    with open("letterGrade.txt","a",encoding=("utf-8")) as file:
        file.write(liste[0] + ":  " +letterGrade+ "\n")
    

while True:
    process = input("1- view notes\n2- note enter\n3- save notes\n4- exit\n")
    
    if process == '1':
        viewNotes()
    elif process == '2':
        note_enter()
    elif process == '3':
        saveNotes()
    else:
        break