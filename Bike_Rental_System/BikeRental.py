import datetime

class openBikes:
    def __init__(self, stock):
        self.stock = stock      ## total bikes
        self.users = {}       ## customer data
        self.money = 0     ## money by choosed plan
        self.time = ''      ## time record
        self.selectedPlan = ''       ## selected plan 
        self.cuntr = 0      ## bike alloted to customer 

    def showRecords(self):
        print(self.users)        ## customer details

    # rent bike on hourly basis
    def rent_bike_on_hourly(self, name, user_demand):   
        print(f"Available Bikes in inventory {self.stock}")
        if user_demand > self.stock:
            print(f"Bike shortage! You can have max {self.stock} bikes.")

        else:
            self.selectedPlan = 'Hourly'
            self.users.update({name:{self.selectedPlan:user_demand}})
            print("Bike rented successfully!")
            self.stock -= user_demand
            xt = datetime.datetime.now()
            self.time = xt.strftime("%s")
            print(f"\nBikes now available in enventory - {self.stock}")
            input("press any key to continue except power button...")

    # rent bike on Daily basis
    def rent_bike_on_daily(self, name, user_demand):     
        print(f"Available Bikes in inventory {self.stock}")
        if user_demand > self.stock:
            print(f"Bike shortage! You can have max {self.stock} bikes.")

        else:
            self.selectedPlan = 'Daily'
            self.users.update({name:{self.selectedPlan:user_demand}})
            print("Bike rented successfully!")
            self.stock -= user_demand
            xt = datetime.datetime.now()
            self.time = xt.strftime("%s")
            print(f"\nBikes now available in enventory - {self.stock}")
            input("press any key to continue except power button...")

    # rent bike on Weekly basis
    def rent_bike_on_weekly(self, name, user_demand):        
        print(f"Available Bikes in inventory {self.stock}")
        if user_demand > self.stock:
            print(f"Bike shortage! You can have max {self.stock} bikes.")

        else:
            self.selectedPlan = 'Weekly'
            self.users.update({name:{self.selectedPlan:user_demand}})
            print("Bike rented successfully!")
            self.stock -= user_demand
            xt = datetime.datetime.now()
            self.time = xt.strftime("%s")
            print(f"\nBikes now available in enventory - {self.stock}")
            input("press any key to continue except power button...")

    # generate bill
    def billing(self, user_name):        
        if user_name in self.users.keys():
            self.selectedPlan = list(self.users[user_name].keys())[0]
            self.cuntr = self.users[user_name][self.selectedPlan]
            xt = datetime.datetime.now()
            xtime = xt.strftime("%s")
            final_time = int(xtime)-int(self.time)
            if self.selectedPlan == 'Hourly':
                self.money = final_time*5

            elif self.selectedPlan == 'Daily':
                self.money = final_time*20

            elif self.selectedPlan == 'Weekly':
                self.money = final_time*100
  
            if self.cuntr >= 3:
                x = self.money/10*3
                self.money = x
                print("You are eligible for our 30% family discount")
                print(f"Thanks for using our Service {user_name.upper()} \nHere is your bill ({self.money} $)")
                self.stock+=self.cuntr
            else:
                print(f"Thanks for using our Service {user_name.upper()} \nHere is your bill ({self.money} $)")
                self.stock+=self.cuntr
            self.users.pop(user_name)
            

        else:
            print(f"\nsorry {user_name} not in record")
            input("press any key to continue except power button...")

if __name__ == '__main__':
    pass
