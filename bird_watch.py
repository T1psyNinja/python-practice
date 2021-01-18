bird_watch = True

while bird_watch == True:
    try:
        day_one = int(input("Day One:How many birds did you see today?"))
    except ValueError:
        print("Numbers only")
    try:
        day_two = int(input("Day Two:How many birds did you see today?"))
    except ValueError:
        print("Numbers only")
    try:
        day_three = int(input("Day Three:How many birds did you see today?"))
    except ValueError:
        print("Numbers only")
    try:
        day_four = int(input("Day Four:How many birds did you see today?"))
    except ValueError:
        print("Numbers only")
    else:
        total_birds = day_two + day_two + day_three + day_four
        watch_average = total_birds / 4
        print("First day:",day_one)   
        print("Second day:",day_two)
        print("Third day:",day_three)
        print("Fourth day:",day_four)
        print("Total Birds seen:",total_birds)
        print("Average birds seen per day:", watch_average) 