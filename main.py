import sys
import os
import json



#The LoadPasswordFile tries to load the txt file with the passwords inside
def LoadPasswordFile():
    try:
        with open("ExtremeSecurePasswordSafe.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []



#The SavePasswordFile tries to save the changes the user did to the txt file
def SavePasswordFile(passwordList):
    try:
        with open("ExtremeSecurePasswordSafe.txt", "w") as file:
            json.dump(passwordList, file)
    except Exception as e:
        with open("ExtremeSecurePasswordSafe.txt", "x") as file:
            json.dump(passwordList, file)



userExitWish = False

print("\n------------------------------------------------------------------------------------\n")

print("Welcome to the sketchy 'Password Manager' you dont want to trust!")


while not userExitWish:
    passwordList = LoadPasswordFile()

    print("\n--------------------------------\n")

    print("\nThe actions you can do are:")
    print("(1) View all passwords")
    print("(2) Add a password")
    print("(3) Delete a password")
    print("(4) Self destruction")
    print("(5) Exit my masterpiece")

    userActionInput = input("\nPlease only type the number without the clamp: ")


    if userActionInput == "1":
        print("Here is your entire list of passwords:\n")

        for passwordId, password in enumerate(passwordList, 1):
            print(f"{passwordId}. {password}")


    elif userActionInput == "2":
        newInput = {}

        newInput["Website or service"] = input("Which website or service does the user data belong to?: ")
        newInput["Username or Email"] = input("What is the username or email: ")
        newInput["Password"] = input("And last but not least, what is the password: ")

        passwordList.append(newInput)

        print(f"The information for this input are added to your password list!")

        SavePasswordFile(passwordList)


    elif userActionInput == "3":
        for passwordId, password in enumerate(passwordList, 1):
            print(f"{passwordId}. {password}")

        if passwordList:
            try:
                print("Which password do you want to remove?")
                removePasswordId = int(input("Enter the ID of the password: "))

                if 1 <= removePasswordId <= len(passwordList):
                    removedPassword = passwordList.pop(removePasswordId - 1)
                    print(f"{removedPassword} was removed from the list!")

                    SavePasswordFile(passwordList)


                else:
                    print("Invalid number!")
                    print("Please choose a valid task!")

            except ValueError:
                print("Please enter a valid number!")

        else:
            print("There is no password to remove")



    elif userActionInput == "4":
        if os.path.exists("ExtremeSecurePasswordSafe.txt"):
            print("Oh mann you really pressed (5), whether by accident or on purpose, there’s no going back now, your passwords are gone")
            print("\nheheheha")
            os.remove("ExtremeSecurePasswordSafe.txt")
        else:
            print("You were lucky this time!")


    elif userActionInput == "5":
        print("Thank for using my masterpiece")
        print("But why do you use a Password Manager that you cant trust?")
        SavePasswordFile(passwordList)

        sys.exit()


    else:
        print("What are you doing :(")