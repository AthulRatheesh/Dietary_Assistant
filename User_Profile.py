import psycopg2 as pg
from config import config
def connect():
        conn=None
        params=config()
        try:
                print("Connecting.....")
                conn=pg.connect(**params)
                print("Connection Established!")

                
        except:
                print("Connection Failed")
connect()
class User_Profile():
        User={}         #User Data in dictionary format
        def Basic_Info(self):
                self.User['Name']=input("\nEnter name:")
                self.User['Age']=int(input("\nEnter age:"))
                self.User['Gender']=input("\nEnter gender:")
                self.User['Height']=int(input("\nEnter height:"))
                self.User['Weight']=int(input("\nEnter weight:"))
                
        def Activity_Details(self):
                print("[Extremely Inactive, Sedentary, Moderately Active, Vigorously Active, Extremely Active]")
                self.User['Activity_Level']=input("\nEnter Activity Level:")
                self.User['Health_Goal']=input("\nInput Weight Loss, Muscle Gain or Maintenance:")
        def Preferences(self):
                self.User['Diet_restriction']=input("\nEnter if any restriction (vegan, gluten-free):")
                self.User['Allergies']=input("\nInput if any allergies:").split(',')
        def Meal_Timings(self):
                self.User['Timing']=input("\nWhen do you typically eat??")
        def __init__(self) -> None:
                self.Basic_Info()
                print(self.User)
                self.Activity_Details()
                self.Preferences()
                self.Meal_Timings()
User_Profile()
                
              