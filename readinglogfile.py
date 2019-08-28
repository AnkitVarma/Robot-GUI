f = open('test.txt','r')
name = f.read().splitlines()

for i in name:
        print(i)
        if "forward" in i and "objectnotdetected" in i:
                print("Moving forward")
        elif "right" in i and "objectnotdetected" in i:
                print("Moving right")
        elif "left" in i and "objectnotdetected" in i:
                print("Moving left")
        elif "backward" in i and "objectnotdetected" in i:
                print("Moving backward")
