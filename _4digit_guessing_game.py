import random

play = True
while play == True:
    anslist = [random.randint(0,9) , random.randint(0,9) , random.randint(0,9) , random.randint(0,9)]
    gsslist = [0,0,0,0]
    round_is_over = False
    tries = 15
    print("I thought of a 4 digit number.")# It is: " , anslist[0] , anslist[1] , anslist[2] , anslist[3])
   
    while round_is_over == False:
        gss = input("Make a guess. Enter 4 digits:")
       
        while gss.isdigit() == False or len(gss) != 4:
            gss = input("Wrong input! Make a guess. Enter 4 digits:")
       
       
       
        gsslist = [int(gss[0]) , int(gss[1]) , int(gss[2]) , int(gss[3])]

        bull = 0
        cows = 0
   
        for i in range(0,4):#tellies bulls and cows
            if anslist[i] == gsslist[i]:
                bull += 1
            elif gsslist[i] in anslist:
                cows += 1
       
        print(bull , " Bulls and " , cows , " cows")
        
        if bull == 4:
            print("You have guessed the correct number! congrats!")
            yesno = input("Game over. Would you like to try again (y/n)?")
           
            while yesno != 'n' or yesno != 'y':
                if yesno == 'n' or yesno == 'y':
                    break
               
                yesno = input("Wrong input! Would you like to try again (y/n)?")
               
            if yesno == 'n':
                play = False
               
            round_is_over = True

        elif tries == 5:
            print("here is a hint. Two of the correct numbers are" , anslist[random.randint(0,3)] , anslist[random.randint(0,3)])
            tries -=1

        else:
            tries -= 1
            if tries == 0:
                print("It is: " , anslist[0] , anslist[1] , anslist[2] , anslist[3])
                yesno = input("Game over. Would you like to try again (y/n)?")
           
                while yesno != 'n' or yesno != 'y':
                    if yesno == 'n' or yesno == 'y':
                        break
                   
                    yesno = input("Wrong input! Would you like to try again (y/n)?")
                   
                if yesno == 'n':
                    play = False
                   
                round_is_over = True
