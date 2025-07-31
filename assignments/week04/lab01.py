Personal Information Manager


# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Teetan", 20, "Phatthalung", "Thailand")  # name, age, city, country
    hobbies = []

    while True:

    print("1 Display into, 2 Add hobby, 3 Remove hobby, 4 Edit age, 5 Exit")
    choice = input("What do you want to do?: ")
    if choice =="1":
         print("Name: ",person[0])
         print("Age: ",person[1])
         print("City: ",[2])
         print("Coutry: ",[3])
         print("Hobbies: ",[4])
    elif choice =="2":
         hobby =input("Insert new hobby: ")
         hobbies.append(Hobby)

    elif choice =="3":
         del bobbies[0]

    elif choice =="4":
         age = int(input("Inset new age"))
         person_list = list(person)
         person_list[1] = age
         person = turple(person_list)

    elif choice =="5":
         break



    hobby = input("Insert new hobby: ")
    hobbies.append(hobby)

    del hobbies[0]

    age = input("Insert new age: ")
    person_list = list(person)
    person_list[1] = age
    person = tuple(person_list)

if __name__ == "__main__":
    personal_info_manager()