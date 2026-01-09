import time
import sys

def typewriter(text):
    for char in text:
        
        print(char, end="", flush=True)
        time.sleep(0.05)  
    print() 


typewriter("Accessing HIT Mainframe...")
typewriter("Loading student profile: Jonathan...")


for i in range(118):

    print(".", end="", flush=True) 
    time.sleep(0.05) 

typewriter("SUCCESS! 9th Grade Python track confirmed.")