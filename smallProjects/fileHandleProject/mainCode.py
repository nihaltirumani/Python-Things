# This project can read the last message which the user wrote!

command = input("Write or tell : ")

if command.lower() == "write":
    message = input("What do you want to write : ")
    file = open("smallProjects/fileHandleProject/Lastmessage.txt", "w")
    file.write(message)
    print("You have wriiten the message!")
    print("Rerun again to see is it working.")

elif command.lower() == "tell":
    file = open("smallProjects/fileHandleProject/Lastmessage.txt", "r")
    print(f"The last message which was told by you is {file.read()}")