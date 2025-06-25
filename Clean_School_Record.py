import pandas as pd 
from Projects_Data import exam_record
class School_Exam_Record:

    def __init__(self):
        self.mypd=None


    def welcome(self):
        print("""
=========================================================================== 
📊           WELCOME TO PYTHON PANDAS 
📁     Mini Project 1: Clean School Exam Records
=========================================================================== 
👨‍💻 Name       : Junaid Mustafa Jamali
📅 Date       : 24 June 2025

🧹 IN THIS PROJECT I PRACTICE:
   🔍 Duplicate Detection
   🧽 Duplicate Removal
   🏷️  Column Renaming using rename() and df.columns
______________________________________________________________________________
""")
        
        
    def create_df(self,data):
        try:
            self.mypd=pd.DataFrame(data)
        except Exception as e :
            print("ERROR : ",e)


    def save_df(self):
        try:
            self.mypd.to_csv("School_Exam_Record.csv",index=False)
        except Exception as e :
            print("ERROR : ",e)

    @staticmethod
    def static_message():
        print("""
===========================================================================
📰 U.S. Role and Trump’s Strategy
===========================================================================

🇺🇸 Trump’s administration says U.S. strikes set back Iran’s 
    nuclear program by months, though some intelligence 
    suggests the damage was not total.

🏛️ The White House is now exploring a “quick U.S. exit” strategy, 
    aiming to de-escalate U.S. involvement while maintaining 
    regional influence.
===========================================================================
""")
        
    def project_task(self):
        print("""
                      PROJECT TASKS
===========================================================================
1️⃣ Check for duplicate rows (full row).
2️⃣ Find duplicates based on StudentID or Name.
3️⃣ Remove duplicate entries.
4️⃣ Rename "Math" to "Math_Score" and "Science" to "Science_Score" using rename().
5️⃣ Rename all columns to new readable names using df.columns = [...].              
===========================================================================              
""") 


    def showing_duplicate(self):
        try:
            print(f"""
__________________________________________________________________________
                  VIEW OF CURRENT DATA FRAME IS : 
___________________________________________________________________________ 
{self.mypd}      
____________________________________________________________________________                             
""")
            dup = self.mypd[self.mypd.duplicated()]
            print(f"""
                  SHOWING ALL DUPLICATES IN THE DATA FRAME 
____________________________________________________________________________                             
{dup}
____________________________________________________________________________                             
""")
        except Exception as e:
            print(f"❌ ERROR : {e}")
     
        
    def finding_duplicate(self):
        try:
            dup=self.mypd[self.mypd.duplicated(subset=["StudentID","Name"],keep=False)]
            print(f"""
______________________________________________________________________
                  DUPLICATES ROWS BASED ON THE StudentID or Name.
______________________________________________________________________
{dup}
______________________________________________________________________
""")
        except Exception as e:
            print(f"❌ ERROR : {e}")
        
    def removing_dup(self):
        try:
            print(f"""
______________________________________________________________________
                  BEFORE REMOVING DATA FRAME VIEW
______________________________________________________________________
{self.mypd}
______________________________________________________________________
""")
            self.mypd.drop_duplicates(inplace=True)
            print(f"""
                  AFTER REMOVING DUPLICATES 
______________________________________________________________________
{self.mypd}                  
______________________________________________________________________
""")
        except Exception as e:
            print(f"❌ ERROR : {e}")
        
    def using_rename(self):
        try:
            re1=self.mypd.rename(columns={"Math":"Math_Score","Science" : "Science_Score"})
            print(f"""
______________________________________________________________________
                  BEFORE RENAME 
______________________________________________________________________
{self.mypd}
""")
            print(f"""
                    AFTER RENAME 
______________________________________________________________________
{re1}  
______________________________________________________________________
""")
        except Exception as e:
            print(f"❌ ERROR : {e}")

            
    def rename_all(self):
        try:
            print(f"""
______________________________________________________________________
                  VIEW OF DATA FRAME BEFORE RENAMING
______________________________________________________________________
{self.mypd}                 
______________________________________________________________________
""")
            self.mypd.columns=["STUDENT_ROLL_NO","STUDENT_NAME","SUB1_Math","SUB2_Science","SUB3_Eng"]
            print(f"""
                   AFTER RENAMING ALL COLUMNS NAME 
______________________________________________________________________
{self.mypd}
______________________________________________________________________
""")
        except Exception as e:
            print(f"❌ ERROR : {e}")



clean = School_Exam_Record()
clean.welcome()
clean.create_df(exam_record)
clean.save_df()
clean.static_message()
while True:
    clean.project_task()
    try:
        choice = int(input("SELECT AN OPTION ( 1️⃣ TO 5️⃣ ) : "))
        match choice:
            case 1:
                clean.showing_duplicate()
            case 2:
                clean.finding_duplicate()
            case 3:
                clean.removing_dup()
            case 4:
                clean.using_rename()
            case 5:
                clean.rename_all()
            case _:
                print("-------------------------------------------------")
                print(f"❌ INVALID CHOICE PLEASE (1 TO 5) FOR NEXT TIME ")
                print("--------------------------------------------------")
                break
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

