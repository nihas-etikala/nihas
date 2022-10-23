command = ""
started = False

while True:
    command = input('>').lower()
    if command == 'start':
        if started:
            print("car is already started!")
        else:
            started = True
            print('the car started ')
    elif command == 'stop':
        if started:
             print("the car  stopped")
        else:
            print('the car is already stopped')
            started = False
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to exit''')
    elif command == "quit":
        print('thanks for playing')
        break
    else:
        print("i don't understand that")

