# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:11:55 2019

@author: DHANUSH
"""




import sys

class PDA:
    
    def __init__(self):
        #defining the language 
        self.C="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
        self.N="0123456789"
        self.start="$"
        self.lparen="("
        self.rparen=")"
        self.op="+-*/%"
        self.stack=[]
        
        
        self.pda_state_dic={1:{self.start:2},
                            2:{self.lparen:2,self.C:4,self.N:3},
                            3:{self.op:2,self.N:3,self.rparen:5,self.start:6},
                            4:{self.C:4,self.op:2,self.start:6,self.N:4,self.rparen:5},
                            5:{self.rparen:5,self.start:6,self.op:2}
                       
                            }
        
        

def main():

    print("Project 2 for CS 341")
    print("Semester: Spring 2019")
    print("Written By: Dhanush Sureshbabu, ds676")
    print("Instructor: Marvin Nakyama, marvin@njit.edu")
    
    print()
    while True:
  
        user_input=input("Do you want to enter a string y/n")
    
        if(user_input=="y"):
            string=input("Please Enter A String")
    
        else:
            #print("OKAY BYE")
            sys.exit(0)
    
        
        pda=PDA()
        pda_dic=pda.pda_state_dic
        state=1
        stack=pda.stack
        
        for i in string:
            not_accept=False
            next_state=False
            #prints current state
            print("current state is ",state)
            
            
            
    
            
            for key in pda_dic[state]:
                if(i in key):
                 #going to next_states   
                    state=pda_dic[state][key]
                    
                    next_state=True
                    break
            
            if(next_state==False):
                print("Not Accepted")
                not_accept=True
                break
            print("character is ",i) 
            
            #Push/Pop from the stack
            if(i==pda.start and state==2):
                stack.append("$")
                print("Symbol: '$' was pushed to stack")
            elif(i==pda.lparen):
                stack.append(pda.lparen)
                print("Symbol: '",pda.lparen,"' was pushed to stack")
            elif(i==pda.rparen):
                
                if(stack.pop()!=pda.lparen):
                    print("Not accepted")
                    not_accept=True
                    break
                print("Symbol: '",pda.lparen,"' was popped from stack")
            elif(i==pda.start):
                
                if(stack.pop()!=pda.start):
                    
                 
                    print("Not accepted")
                    not_accept=True
                    break
                print("Symbol: '$' was popped from stack")
        
        #check if final state and stack is empty
        if(state==6 and len(stack)==0):
            print("state is: 6, this is final state and an accepting state")
            print("Accepted")
        elif(not_accept==False):
            print("Not accepted")
                        

if __name__ == "__main__":
    main()                
    
    
    
    
    
    
    