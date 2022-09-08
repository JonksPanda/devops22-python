stop = False

while(stop == False):
    word = input("Pick any word")
    answer = input("Enter stop to quit").lower()

    if(answer == "stop"):
        stop = True
        print("stopping loop..")
    else:
        print(word)
        print(f"word lenght: {len(word)}")