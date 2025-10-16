import pandas as h
a={
    'patient name':['sandeep','rishi','dhanush','bhanu','lokesh','jaya surya'],
    'morning_Scenario':[72,82,68,102,22,211],
    'afternoon_Scenario':[85,62,91,50,68,198],
    'evening_Scenario':[63,64,57,128,66,2],
    'patient status':['moderately normal😒','normal😊','moderately critical😢','dead💀','mission impossible☠️','RIP🪦']
}
b=h.DataFrame(a,index=[1,2,3,4,5,6])
print(b,'\n----------------------------------------------------------------------------------------------')
print(b.loc[[1,2,4]],'\n----------------------------------------------------------------------------------------------')
print(b.loc[[4,5,6]],'\n----------------------------------------------------------------------------------------------')
print("...........THANK YOU FOR VISITING OUR NBKRIST CLINIC 🙏...........")