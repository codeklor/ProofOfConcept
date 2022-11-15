'''
Created on Nov 14, 2022

@author: Kristopher Carter

READ ME
Lists are constructed in the following structure:
[[title, duration], [title, duration],...]

TO DOS:
 - Need to test error handling if lists have 1 or less title and user has less time than duration
 - Need to save lists to permanent storage (.txt file)
 - Be able to read those .txt files in, edit them as needed, then save them again.
 - Develop UI
'''

# Bring in necessary packages
import random

# Define print menu function
def menu():
    print("*    What would you like to do?    *")
    print("*    1 - Add a show                *")
    print("*    2 - Add a movie               *")
    print("*    3 - Get a recommendation      *")
    print("*    4 - View shows list           *")
    print("*    5 - View movies list          *")
    print("*    6 - Remove show from list     *")
    print("*    7 - Remove movie from list    *")
    print("*    0 - Exit                      *")


# Define function to add a show and its episode duration to the movies list
def addShow(tempLst):
    showLst.append(tempLst)


# Define function to add a movie and its duration to the movies list
def addMovie(tempLst):
    movieLst.append(tempLst)
    

# Define function to remove show from list by comparing unicode values
def removeShow(title):
    for i in range(len(showLst)):
        # Try block to handle index out of range error when comparing two unequal strings
        try:
            # Compare Unicode of the two titles
            if showLst[i][0] == title:
                showLst.pop(i)
                print(title, "removed from shows!")
        except:
            continue
    

# Define function to remove movie from list by comparing Unicode values   
def removeMovie(title):
    for i in range(len(movieLst)):
        # Try block to handle index out of range error when comparing two unequal strings
        try:
            # Compare Unicode of the two titles
            if title == movieLst[i][0]:
                movieLst.pop(i)
                print(title, "removed from movies!")
        except:
            continue


# Define function to view list of shows   
def viewShows():
    print("\n")
    print("*************** SHOWS ****************")
    print(f"{'Title' : <30}{'Duration' : >8}")
    print("-" * 38)
    for i in range(len(showLst)):
        print(f"{showLst[i][0] : <30}{showLst[i][1] : >8}")
    print("**************************************")
    print("\n")
        
               
# Define function to view list of movies   
def viewMovies():
    print("\n")
    print("*************** MOVIES ***************")
    print(f"{'Title' : <30}{'Duration' : >8}")
    print("-" * 38)
    for i in range(len(movieLst)):
        print(f"{movieLst[i][0] : <30}{movieLst[i][1] : >8}")
    print("**************************************")
    print("\n")


# Define get recommendation function
def getRecommendation(format, time):
    
    # Shows
    if format == 1:
        
        if len(showLst) < 1:
            print("You have no shows in your list.")
            break
            
        elif len(showLst) == 1:
            print("**** Watcher Show Recommendation *****")
            print(f"{'Title' : <30}{'Duration' : >8}")
            print("-" * 38)
            print(f"{showLst[0][0] : <30}{showLst[0][1] : >8}")
            print("\n")
            break
        
        else:
            while True:
                # Generating random index of show
                index = random.randrange(0, len(showLst))       
            
                if showLst[index][1] <= time:
                    print("**** Watcher Show Recommendation *****")
                    print(f"{'Title' : <30}{'Duration' : >8}")
                    print("-" * 38)
                    print(f"{showLst[index][0] : <30}{showLst[index][1] : >8}")
                    print("\n")
                    break
    
    # Movies   
    if format == 2:
        
        if len(movieLst) < 1:
            print("You have no movies in your list.")
            break
            
        elif len(showLst) == 1:
            print("**** Watcher Movie Recommendation *****")
            print(f"{'Title' : <30}{'Duration' : >8}")
            print("-" * 38)
            print(f"{movieLst[0][0] : <30}{movieLst[0][1] : >8}")
            print("\n")
            break
        
        else:
            while True:
                # Generating random index of show
                index = random.randrange(0, len(showLst))       
            
                if showLst[index][1] <= time:
                    print("**** Watcher Movie Recommendation *****")
                    print(f"{'Title' : <30}{'Duration' : >8}")
                    print("-" * 38)
                    print(f"{movieLst[index][0] : <30}{movieLst[index][1] : >8}")
                    print("\n")
                    break
    
    else:
        print("Error. Please enter valid option.")
    
    

# Define main function
def main():
    print("******** WELCOME TO WATCHER ********")
    menu()
    userInput = int(input("Enter choice: "))
    if userInput == 0:
        print("Going so soon?... O.K.")
    
    while True:
        
        if userInput == 1:
            title = input("Enter title of show: ")
            duration = int(input("Enter duration of individual show episodes in minutes: "))
            tempLst = [title, duration]
            addShow(tempLst)
            
        elif userInput == 2:
            title = input("Enter title of movie: ")
            duration = int(input("Enter duration of movie in minutes: "))
            tempLst = [title, duration]
            addMovie(tempLst)
            
        elif userInput == 3:
            print("\n")
            print("Do you want to watch a movie or a show?")
            print("1 - Show")
            print("2 - Movie")
            format = int(input("1 or 2: "))
            time = int(input("Enter how much time you have in minutes: "))
            print("\n")
            getRecommendation(format, time)
        
        elif userInput == 4:
            viewShows()
        
        elif userInput == 5:
            viewMovies()
        
        elif userInput == 6:
            title = input("Enter title of show to remove (case sensitive): ")
            removeShow(title)
            
        elif userInput == 7:
            title = input("Enter title of movie to remove (case sensitive): ")
            removeMovie(title)
            
        elif userInput == 0:
            print("Exiting. Have a nice day!")
            break
        
        else:
            print("Error. You entered:", userInput, " Which is invalid.")
            print("Please try again...")
        menu()
        userInput = int(input("Enter choice: "))


# initialize empty lists in a global scope
movieLst = []
showLst = []

# call main
main()