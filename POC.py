print("Press 1 to enter a show")
print("Press 2 to enter a movie")
print("Press 3 to go to your recommended")
print("Press 4 to exit")

emptyDict = {}
userInput = int(input("Enter an option: "))

while userInput is not 4:
    
    if userInput is 1:
        k = input("Enter show title: ")
        v = int(input("Enter show time in minutes: "))
        emptyDict.update({k:v})
    elif userInput is 2:
        k = input("Enter movie title: ")
        v = int(input("Enter movie time in minutes: "))
        emptyDict.update({k:v})
    elif userInput is 3:
        v = int(input("Enter available time in minutes: "))
        items = emptyDict.items()
        print("Here is your recommended shows and movies: ")
        for item in items:
            if item[1] <= v:
                print(item[0])
    elif userInput is not 1 or userInput is not 2 or userInput is not 3:
        print("Input does not match options, please try again...")
        print("Press 1 to enter a show")
        print("Press 2 to enter a movie")
        print("Press 3 to go to your recommended")
        print("Press 4 to exit")
    print("Press 1 to enter a show")
    print("Press 2 to enter a movie")
    print("Press 3 to go to your recommended")
    print("Press 4 to exit")
    userInput = int(input("Enter an option: "))
