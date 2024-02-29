Car_Start = False

print("Enter Your Command: ")
while True :
    i = input("> ").lower()
    if i == "help":
        print(" start = Starts Your Car.")
        print(" stop = Stops Your Car.")
        print(" quit = Exits The Program.")
    elif i == "start" :
        if Car_Start : print("Heyy The Car is Already Started.")
        else : 
            Car_Start = True
            print("Car Starts....Ready to Go!!")
    elif i == "stop" :
        if Car_Start :
            Car_Start = False
            print("The Car has Stopped!!")
        else : print("Heyy..The car is not moving!!")
    elif i == "quit" :
        print("Program Terminated")
        break
    else : 
        print(f'Invalid Command!! Enter "help" to view the available commands.')