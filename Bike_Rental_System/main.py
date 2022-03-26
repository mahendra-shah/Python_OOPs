from BikeRental import openBikes

'''
This programm will assume 1 second as an hour/day/week. 
'''

def mainFunction():
    Bikers = openBikes(100)

    while(True):
        print("""
            ----------------------------------------\n
                1 -- for Rent Bike on Hourly basis - 5$.
                2 -- for Rent Bike on Daily basis- 20$.
                3 -- for Rent Bike on Weekly basis- 100$.
                4 -- for Return Bike. 
                5 -- for show customers record. 
                9 -- to quit the programm\n
            ----------------------------------------
        """)
        try:
            print(f"Available Bikes in inventory {Bikers.stock}\n")
            userChoice = int(input("Enter your Choice: "))            
        
            if userChoice == 1:
                user_name = input("Enter your Name: ")
                user_demand = int(input("How much bikes you want: "))
                Bikers.rent_bike_on_hourly(user_name, user_demand)

            elif userChoice == 2:
                user_name = input("Enter your Name: ")
                user_demand = int(input("How much bikes you want: "))
                Bikers.rent_bike_on_daily(user_name, user_demand)

            elif userChoice == 3:
                user_name = input("Enter your Name: ")
                user_demand = int(input("How much bikes you want: "))
                Bikers.rent_bike_on_weekly(user_name, user_demand)

            elif userChoice == 4:
                user_name = input("Enter your Name: ")
                Bikers.billing(user_name)

            elif userChoice == 5:
                Bikers.showRecords()

            elif userChoice == 9:
                print(f"Thanks for visiting")
                break
            
            else:
                print("Not a valid option :( try again!")
                continue

        except:
            print('Unhhhh.... no no no!!!\ntry again...')

if __name__ == '__main__':
    mainFunction()
