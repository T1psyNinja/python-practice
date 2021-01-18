keeping_track = True
while keeping_track == True:
    calories_eaten = []
    

    caloric_goal = int(input("What is your daily caloric goal?  ",  ))
    calories_eaten.append(int(input("How many calories did you eat?  ",  )))
    print(calories_eaten)
    
    another_snack = input("Did you have anything esle? y/n  ", ) 
    if another_snack == "y":
        while another_snack == "y":
            if another_snack == "y":
                print(calories_eaten.append(int(input("How many calories was that?  ",  ))))
                print(sum(calories_eaten))               
                another_snack = input("Did you have anything esle? y/n  ",  )
            if another_snack == "n":
                continue
        another_snack == "n"
        if another_snack == "n":
            total = 0
            
            total_calories = sum(calories_eaten) + total
                
            surplus = total_calories - caloric_goal
            deficit = caloric_goal - total_calories
            if total_calories > caloric_goal:
                print(total_calories)
                print("You are ",surplus ,"calories over your goal")
            if total_calories < caloric_goal:
                print(total_calories)
                print("You are", deficit, "calories under your goal")    
            if total_calories == caloric_goal:
                print(total_calories)
                print("You have met your goal")
            exit

