gate_open = True

print("--- System Online ---")

while gate_open:
    action = input("\n[System Idle] Type 'pass', 'intruder', or 'quit': ").lower()

    if action == "quit":
        print("Shutting down...")
        break
    
    elif action == "pass":
        print("Access granted.")

    elif action == "intruder":
        print("🚨 ALARM! Intruder detected!")
        
        
        choice = input("Do you want to 'neutralize' or 'shutdown'? ").lower()
        
        if choice == "neutralize":
            print("Threat eliminated. System returning to normal.")
            
        
        elif choice == "shutdown":
            print("Emergency Shutdown initiated!")
            gate_open = False
        
        else:
            print("Invalid command! Intruder escaped. System still active.")

print("--- System Offline ---")