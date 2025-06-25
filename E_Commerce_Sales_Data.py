import pandas as pd 
from Projects_Data import ecom_data



class E_Comerce_Sales_Data:

    def __init__(self):
        self.mypd=None


    def project_welcome(self):
        print("""
==============================================================================================
              🛒 Mini Project 2: Clean E-Commerce Sales Data
                🛒 Mini Project 2: Clean E-Commerce Sales Data
            🎯 Goal:
            Clean up and format customer sales data for dashboard.      
===============================================================================================             
""")  

    def creating_df(self,data):
        try:
            self.mypd=pd.DataFrame(data)
        except Exception as e:
            print(f"❌ ERROR : {e}")

    def saving_df_into_csv(self):
        try:
            self.mypd.to_csv("E_Commerce_Sales_Data.csv",index=False)
        except Exception as e:
            print(f"❌ ERROR : {e}")


    def project_task(self):
        print("""
__________________________________________________________________________________________
                         PROJECT TASKS
__________________________________________________________________________________________
1.Find customers who placed duplicate orders using CustomerID or Email.
2.Remove full duplicate entries.
3.Use drop_duplicates(subset=["CustomerID"]) to keep the first order.
4.Rename columns: "TotalAmount" to "Order_Value", "City" to "Customer_City".
5.Rename all columns for a report-friendly format.   
__________________________________________________________________________________________
                                     
""")    
    def find_duplicate(self):
        try:
            duplicates=self.mypd.duplicated(subset=["CustomerID","Email"])  
            print(f"""
__________________________________________________________________________________________
                  FINDING CUSTOMERS BASED ON CustomerID or Email.
__________________________________________________________________________________________
{duplicates}
__________________________________________________________________________________________
""")  
        except Exception as e:
               print(f"❌ ERROR : {e}")


    def removing_duplicates(self):
        try:
            print(f"""
__________________________________________________________________________________________
                  BEFORE REMOVING DUPLICATES THE VIEW OF DATA FRAME IS : 
__________________________________________________________________________________________
{self.mypd}                  
__________________________________________________________________________________________                  
""") 
            self.mypd.drop_duplicates(inplace=True)
            print(f"""
                  AFTER REMOVING DUPLICATES
__________________________________________________________________________________________ 
{self.mypd}
__________________________________________________________________________________________                  
""")
        except Exception as e:
             print(f"❌ ERROR : {e}")

    def droping_on_condition(self):
        try:
            print(f"""
__________________________________________________________________________________________                  
                  DATA FRAME BEFORE REMOVING 
__________________________________________________________________________________________     
{self.mypd}                               
__________________________________________________________________________________________                  

""")
            self.mypd.drop_duplicates(subset=["CustomerID"],keep="first",inplace=True)
            print(f"""
                  AFTER DROPING 
__________________________________________________________________________________________                  
{self.mypd}
__________________________________________________________________________________________                  
""")
        except Exception as e:
               print(f"❌ ERROR : {e}")



    def remaing_column(self):
        try:
            print(f"""
__________________________________________________________________________________________ 
                  BEFORE RENAMING VIEW OF DATA FRAME IS :                 
__________________________________________________________________________________________ 
                  {self.mypd}                 
__________________________________________________________________________________________                  
""")    
            re_naming=self.mypd.rename(columns={ "TotalAmount" : "Order_Value", "City":"Customer_City"})
            print(f"""
                  AFTER RENAMING THE VIEW OF DATA FRAME IS : 
__________________________________________________________________________________________                  
{re_naming}
__________________________________________________________________________________________                  
""") 
        except Exception as e:
               print(f"❌ ERROR : {e}")

    def re_naming_all(self):
        try:
            print(f"""
__________________________________________________________________________________________  
                  BEFORE RENAIMG THE NAMES OF COLUMN IS :                
__________________________________________________________________________________________
                  {self.mypd}                  
__________________________________________________________________________________________                  

""")
            self.mypd.columns=["CustomerID_NO","Cus_Name","Cus_Email","Cus_City","cus_Total_Bill","Date_Of_Order"]
            print(f"""
__________________________________________________________________________________________  
                  AFTER RENAMING  THE NAMES OF COLUMN IS :                
__________________________________________________________________________________________
                  {self.mypd}                  
__________________________________________________________________________________________                  

""")
        except Exception as e:
               print(f"❌ ERROR : {e}")

            



sales=E_Comerce_Sales_Data()
sales.project_welcome()
sales.creating_df(ecom_data)
sales.saving_df_into_csv()   
while True:
    sales.project_task()
    try:
        option = int(input("SELECT OPTION FROM (1 TO 5) : "))
        if option ==1:
            sales.find_duplicate()
        elif option==2:
            sales.removing_duplicates()
        elif option ==3:
            sales.droping_on_condition()
        elif option ==4:
            sales.remaing_column()
        elif option ==5:
            sales.re_naming_all()
        else:
            pass
    except Exception as e:
        print(f"❌ ERROR : {e}") 
    again = (input("DO YOU WANT TO CONTINUE (YES/NO) : ")).strip().lower()
    if again =="yes":
        continue
    elif again =="no":
            print("\n" + "="*90)
            print("🎉 Project Completed Successfully! 🎉")
            print("-" * 90)
            break
    else:
        print("________________________________________________")
        print("❌ WRONG INPUT NEXT CORRECT INPUT FOR NEXT TIME")
        print("__________________________________________________")
        break        

                  
            


            
                           
        
    