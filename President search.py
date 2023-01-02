import csv
import time

def searchbypresident():
    time.sleep(.5)
    Name=input('Enter Presidents Name\n')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    csv_file=csv.reader(open('names.csv', 'r'))

    for row in csv_file:
        if Name.title() in row[1]:
            print(row)
            time.sleep(1)
    user_input()
    
def searchbynumber():
    time.sleep(.5)
    number=str(input('Enter Age\n'))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    csv_file=csv.reader(open('names.csv', 'r'))

    for row in csv_file:
        if number in row [2]:
            print(row)
            time.sleep(1)
        else:
            print("Sorry no Presidents match that search")
            time.sleeep(1)
    user_input()

def searchbyplacement():
    time.sleep(.5)
    Placement=str(input('Enter Placement\n'))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    csv_file=csv.reader(open('names.csv', 'r'))

    for row in csv_file:
        if Placement in row [0]:
            print(row)
            time.sleep(1)
    user_input()

def user_input():
    print('enter 1 to search by Presidents Name')
    time.sleep(.5)
    print('enter 2 to search by Presidents Age')
    time.sleep(.5)
    print('enter 3 to search by Presidents Placement')
    time.sleep(.5)

    src=int(input('enter here:'))

    if src==1:
        searchbypresident()
    elif src==2:
        searchbynumber()

    elif src==3:
        searchbyplacement()
    
    else:
        print("\nsorry wrong input")
        time.sleep(1)
        print("try again")
        time.sleep(1)
        user_input()


user_input()