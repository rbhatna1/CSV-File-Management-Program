import csv
import os
def write():
    if os.path.isfile("Students.csv"):
        File=open("Students.csv","a",newline="")
        cw=csv.writer(File,delimitor=",")
    else:
        File=open("Students.csv","w",newline="")#Newline-To prevent an extra new line
        cw=csv.writer(File,delimator=",")
        Fields=["Rollno","Name"]
        cw.writerow(Fields)
    ans="y"
    while ans=="y":
        Rollno=int(input("Enter SNO:"))
        Name=input("Enter Name:")
        cw.writerow([RollNo,Name])#Not in double quotes as dynamic values being entered
        ans=input("Do you wish to add more")
    File.close() 
write()

def reading():
    File=open("Students.csv","r")#In reading newline not required
    b=csv.reader(File)
    for i in b: #Gives in the form of a list
        for a in b: #Gives the same thing without a list can be used to make further comparisons 
            print(a,end="")
             
def check():
    if os.isfile("student.csv","a"):
        print("Does exist")
    else:
        print("It does not exist")
#Numeric is a string in csv
        
Functions 2

def func():
    File=open("Students.csv","r")
    b=csv.reader(File)
    for i in b:
        if i[0].lower() in ["hr","manager"]:
            count+=1
    return count

def count:
    F=open("student.csv","r")
    cr=csv.reader(F)
    s=c=h=0
    for i in cr:
        if i[2].lower() in ["science"]:
            s+=1
        if i[2].lower() in ["commerce"]:
            c+=1
        if i[2].lower() in ["humanities"]:
            h+=1
    F.close()
    
def Marksbetween():
    with open('people.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if str(row[2]).isdigit():
                if int(row[2])<95 and int(row[2])>85:
                    print(row)
            else:
                pass       

def Student():  
    global Course
    file=open("StudCourse.csv", "w", newline="")
    cw=csv.writer(file, delimiter=",")
    fields=["Rno","SName","Course","Subjects"]
    cw.writerow(fields)
    choice="y"
    while choice=="y":
        Rno=int(input("Enter roll no: "))
        SName=input("Enter name ")
        Course=input("Enter course")
        Subject=SetSub()
        cw.writerow([Rno, SName, Course,Subject])
        choice=input("Add more? ")
    file.close()
    
def SetSub():            
    if Course.lower()=='science':
        return 'Phy-Che-Mat'
    elif Course.lower()=='commerce':
        return 'Acc-Bus-Eco'
    elif Course.lower()=='humanities':
        return 'His-Pol-Web'
    
def READ():      
    file=open("StudCourse.csv","r",newline="")
    b=csv.reader(file)
    for i in b:
        for j in i:
            print(j,end="")
        print()
        
def Humanities():
    with open('people.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if str(row[0]).isdigit():
                if row[2].lower() == 'humanities':
                    print(row)
            else:
                pass
            
def Altrecords(): 
    with open("StudCourse.csv", "r") as A:
        B = csv.reader(A)
        count=1
        for i in B:
            if count%2==0:
                print(i)
                count += 1
            else:
                count+=1
                pass

def Grade():
    with open('people.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if str(row[2]).isdigit():
                if int(row[2])>=96:
                    print('A1')
                elif int(row[2])>=91:
                    print('A2')
                elif int(row[2]) >= 85:
                    print('B1')
                elif int(row[2]) >= 82:
                    print('B2')
                elif int(row[2]) >= 73:
                    print('C1')
                elif int(row[2]) >= 65:
                    print('D1')
                elif int(row[2]) >= 50:
                    print('D2')
                elif int(row[2]) >= 33:
                    print('E1')
                elif int(row[2]) < 33:
                    print('Fail')
            else:
                pass
