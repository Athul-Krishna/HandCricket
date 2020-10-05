
import random as r            # here importing random as r, so that whenever we needs this we can just type r

print("Welcome to Handcricket game! \n")
for i in range(0,3):
    print(i);
print("Get set go")
dec1=input("Odd or Even :  ").lower()       #asks user to input if he/she chooses odd or even
t1=int(input("User Input: "))
t2=r.randint(1,6)          # randomly picks numbers from 1 to 6
print(f"AI input: {t2}")
toss=t1+t2
if toss%2 == 0:
    dec="even"
else:
    dec="odd"
if dec1==dec:
    play=int(input("Batting(1) or Bowling(2)? "))
else:
    play=r.randint(1,2)
if play==1:
    print("You are batting!")
else:
    print("You are bowling!")
#-----------------------------------------------------

def innings1(c):             
        runs=0
        while True:
            r1=int(input("User input: "))
            r2=r.randint(1,6)
            print(f"AI input: {r2}")
            if r1==r2:
                print("OUT!!!")
                break
            else:
                if c==0:          #Shows user is batting
                    runs+=r1
                else:               #Shows AI is batting
                    runs+=r2
        return runs
    
def innings2(runs,c):
        chase = 0
        while runs>=chase:
            r1 = int(input("User input: "))
            r2 = r.randint(1, 6)
            print(f"AI input: {r2}")
            if r1 == r2:
                print("OUT!!!")
                break
            else:
                if c==0:          #Shows user is batting
                    chase+=r1
                else:               #Shows AI is batting
                    chase+=r2
        return chase

#-------------------------------------------------------

if play==1:
    runs1 = innings1(0)
    print(f"Your score: {runs1}")
    print("Bowl and beat AI")
    runs2 = innings2(runs1,1)
    if runs1>runs2:
        print("YOU WON!")
    else:
        print("YOU LOST")

#-------------------------------------------------------
        
if play==2:
    runs2 = innings1(1)
    print(f"AI score: {runs2} \n Bat and beat AI \n")
    runs1 = innings2(runs2,0)
    if runs1>runs2:
        print("YOU WON!")
    else:
        print("YOU LOST")
