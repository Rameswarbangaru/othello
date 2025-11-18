from game_logic import *
from board import *

# l=[[-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1]]
# l[4][4]=l[3][3]=0
# l[4][3]=l[3][4]=1
s = input("Do you want to continue previous game:")
if s == "NO":
    resetsave()
    person_choice1 = readsave()[0]
    person_choice2 = 1 - person_choice1
else:
    person_choice1=int(input("CHOICE1 :"))
    person_choice2=int(input("CHOICE2 :"))
l=readsave()[1:10]

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  MAIN  FUNCTION

while(count1+count0!=64):
    for i in range(7,-1,-1):
        for j in range(0,8):
            if (l[i][j]!=-1):
                print("",l[i][j],end=" ")
            else:
                print(l[i][j],end=" ")
        print()
    eligible_1=0
    eligible_2=0
    for i in range(0,8):
        for j in range(0,8):
            if l[i][j]==-1:
                index=fun1(j,i,person_choice1,l)
                if index>0:
                    eligible_1=1
                    print("green>>",f"({j},{i})")
    if eligible_1==1:
        while 1:
            x,y=map(int,input().split())
            indi=fun(x,y,person_choice1,l)
            if indi>0:
                break
            writesave(l,person_choice1)
    else:
        print(f"{person_choice1} cannot palce a coin ")
    for i in range(7,-1,-1):
        for j in range(0,8):
            if (l[i][j]!=-1):
                print("",l[i][j],end=" ")
            else:
                print(l[i][j],end=" ")
        print()
    for i in range(0,8):
        for j in range(0,8):
            if l[i][j]==-1:
                index=fun1(j,i,person_choice2,l)
                #print(j,i,person_choice2)
                if index>0:
                    eligible_2=1
                    print("green>>",f"({j},{i})")
    if eligible_2==1:
        while 1:
            x,y=map(int,input().split())
            indi=fun(x,y,person_choice2,l)
            if indi>0:
                break
            writesave(l,personchoice_2)
    else:
        print(f"{person_choice2} cannot palce a coin ")
    if eligible_1==0 and eligible_2==0:
        break
if count1>count0:
    print("1 is the WINNWER !!!!")
else:
    print("0 is the WINNER  !!!!!")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   END      OF    THE     CODE >>>