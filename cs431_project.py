# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 14:24:40 2019

@author: DHANUSH
"""

import sys

class DFA:
    
    
    def __init__ (self):
        #defining gamma phi and sigma
        self.gamma="abcdefghijklmnopqrstuvwxyz"
        self.gamma_no_c="abdefghijklmnopqrstuvwxyz"
        self.gamma_no_o="abcdefghijklmnpqrstuvwxyz"
        self.gamma_no_m="abcdefghijklnopqrstuvwxyz"
        self.phi="@"
        self.notgamma=""
        self.delta="."
        self.dfa_state_dic={1:{self.gamma:2,self.notgamma:9},
                            2:{self.phi:3,self.gamma:2,self.delta:1},
                            3:{self.notgamma:9,self.gamma:4},
                            4:{self.gamma:4,self.delta:5},
                            5:{self.notgamma:9,self.gamma_no_c:4,"c":6},
                            6:{self.gamma_no_o:4,self.delta:5,"o":7},
                            7:{self.gamma_no_m:4,self.delta:5,"m":8},
                            8:{self.gamma:4,self.delta:5,"":9}}
        
        
    
def main():
    print("Project 1 for CS 341")
    print("Semester: Spring 2019")
    print("Written By: Dhanush Sureshbabu, ds676")
    print("Instructor: Marvin Nakyama, marvin@njit.edu")
    
    print()
    user_input=input("Do you want to enter a string y/n")
    
    if(user_input=="y"):
        string=input("PLEASE ENTER STRING")
    else:
        print("OKAY BYE")
        sys.exit(0)
    

    dfa=DFA()
    dfadic=dfa.dfa_state_dic
    state=1
    
    

    for i in string:
        
        next_state=False
        for key in dfadic[state]:
            if(i in key):
              
              print("character is: ",i)
              state=(dfadic[state][key])
              print("next state is: ",state)
              next_state=True
              break
        if(next_state==False):
            print("String not in lang")
            break
    if(next_state!=False):
        
        if(state==8):
            print("STRING IN LANG")
        else:
            print("not in lang")
    
                

if __name__ == "__main__":
    main()                
        
        