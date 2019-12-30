#!/usr/bin/env python
# coding: utf-8

# In[1]:


def introduction():
    print("Welcome to the Tic Tac Toe game!\n")
    global name_list
    while True:
        print("Please tell me your names!\n")
        name1=input()
        print("\nand?\n")
        name2=input()
        name_list=[name1,name2]
    
        if "" in name_list:
            print("Sorry ... this game needs two players...\n")
        else:
            break
        
    print(f"\nHi {name1} and {name2}! thank you for participating!\n")


# In[2]:


def rules():
    answer=input("Would you like me to explain the rules of this Tic Tac Toe game?\nyes/no?\n\n")
    if answer == "yes":
        print("\nJust put the symbol in 1-9 position on the map!\n")
        print("You win when you have 3 symbols in a row!\n")
    elif answer == "no":
        print("\nGreat! let's get started!\n")
    else:
        while True:
            answer=input("Please choose from yes/no?\n")
            if answer == "yes" or answer=="no":
                break


# In[ ]:


def win_check(gm):
    if gm[0]==gm[1]==gm[2] or gm[3]==gm[4]==gm[5]or gm[6]==gm[7]==gm[8] or gm[0]==gm[3]==gm[6]:
        return True
    elif gm[1]==gm[4]==gm[7]or gm[2]==gm[5]==gm[8]or gm[0]==gm[4]==gm[8]or gm[2]==gm[4]==gm[6]:
        return True
    return False


# In[11]:


def print_map(gm):
    print(f"\n|{gm[0]}|{gm[1]}|{gm[2]}|")
    print(f"|{gm[3]}|{gm[4]}|{gm[5]}|")
    print(f"|{gm[6]}|{gm[7]}|{gm[8]}|\n")


# In[12]:


def ladys_first(name_list):
    global p1
    global p2
    lady=input(f"Who would like to go first?\n{name_list[0]} or {name_list[1]}?\n\n")
    if lady==name_list[0]:
        p1=name_list[0]
        p2=name_list[1]
    else:
        p1=name_list[1]
        p2=name_list[0]


# In[13]:


def action_x(gm):
    put=0
    put=int(input("\nWhere would you like to place the X?\n"))
    while True:
        if not put in gm[::]:
            put=int(input("\nYou cannot put it there... pick another spot\n"))
        if put in gm[::]:
            break
    for i in range(9):
        if gm[i]==put:
            gm[i]="X"
        
def action_o(gm):
    put=0
    put=int(input("\nWhere would you like to place the O?\n"))  
    while True:
        if not put in gm[::]:
            put=int(input("\nYou cannot put it there... pick another spot\n"))
        if put in gm[::]:
            break
    for i in range(9):
        if gm[i]==put:
            gm[i]="O"


# In[14]:


def game(p1,p2):
    round_count=range(9)
    gm=list(range(1,10))
    print_map(gm)
    
    for i in round_count:
        if i%2==0:
            print(f"It's {p1}'s turn!")          
            action_x(gm)
            print_map(gm)
            if win_check(gm)==True:
                print(f"We have a WINNER -- {p1}!")
                break
            
        elif i%2!=0:
            print(f"It's {p2}'s turn!")
            action_o(gm)
            print_map(gm)
            if win_check(gm)==True:
                print(f"We have a WINNER -- {p2}!")
                break
                
    if win_check(gm)==False:
        print("Game Over! It's a DRAW!")


# In[15]:


name_list=[]
p1=""
p2=""
introduction()
rules()
ladys_first(name_list)
game(p1,p2)


# In[ ]:





# In[ ]:




