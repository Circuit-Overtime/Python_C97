
n = 4
while n > 0:
    a = int(input("Guess a Number between 0 to 10:  "))
    if(a > 10):
        print("Enter a valid Input! (A number between 0 to 10)")
        n = n + 0
        n = 4
        print("No. of tries has been reset. DO NOT MAKE SAME MISTAKE AGAIN!!!!!\n\n")
        

        a = int(input("Guess a Number between 0 to 10:  "))

        
    if a > 2:
        print("Oh! Close Try but the actual answer is lesser that what you have guessed")
        print("Remaining tries = ", n-1)
        n = n-1
    if a < 2:
        print("Oh! Close Try but the actual answer is greater than what you have guessed")
        print("Remaining tries = ", n-1)
        n = n-1

    if a == 2:
        print("CONGRATULATIONS!!! YOU HAVE GUESSED THE CORRECT NUMBER...")
        print("You Have Taken", 4-n, "Tries")
        n = n + 0
        print("The Answer was 2")
        break

    if(n == 0):
        print("You have exhausted the try limit. Remember TRY LIMIT DOES NOT GROW ON TREES (its limitted haha)")
        print("The Answer was 2")

    
         
    



