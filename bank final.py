import mysql.connector as sq
mydb=sq.connect(host="localhost",user="root",passwd="root",database="Bank1")

def openacc():
    n=input("Enter Name : ")
    print("\n")
    ac =input("Enter Account No :")
    print("\n")
    db=input("Enter D.O.B (yyyy-mm-dd) :")
    print("\n")
    ad=input("Enter Address : ")
    print("\n")
    p=input("Enter Phone number: ")
    print("\n")
    em=input("Enter EmailID:")
    print("\n")
    aad=input("Enter Aadhar No: ")
    print("\n")
    ob=int(input("Enter Opening Balance : "))
    print("\n")       
    c1=mydb.cursor()
    Q1="Insert into account values('{}','{}','{}','{}','{}','{}','{}',{})".format(n,ac,db,ad,p,em,aad,ob)
    Q2="Insert into ammount values('{}','{}',{})".format(n,ac,ob)
    c1.execute(Q1)
    c1.execute(Q2) 
    mydb.commit()
    print("-"*50)
    print(2*"\t"+"Data Entered successfully")
    print("-"*50,"\n")
    print("\n")
    cont()
    if x1=="y" or x1=="Y":
         admin_menu()
    elif x1=="n" or x1=="N":
        print("*"*50)
        print(9*"\t"+"THANK YOU FOR USING BANKING SYSTEM")
        print("*"*50,"\n")
        input()
        print("\n")
    else:
        print("invalid choice")
    
def depo():
    ac=input("Enter Account No :")
    am = int(input("Enter Amount: "))
    a="select balance from ammount where acno='{}'"
    c1=mydb.cursor()
    c1.execute(a.format(ac))
    myresult = c1.fetchone()
    tam=myresult[0]+am
    sql="update ammount set balance={} where acno='{}'"
    c1.execute(sql.format(tam,ac))
    mydb.commit()
    print("-"*70)
    print(2*"\t"+"Amount deposited successfully to your account")
    print("-"*70,"\n")
    print("\n")
    cont()
    if x1=="y" or x1=="Y":
        cust_menu()
    elif x1=="n" or x1=="N":
        print("*"*50)
        print(2*"\t"+"THANK YOU FOR USING BANKING SYSTEM")
        print("*"*50,"\n")
        input()
        print("\n")
    else:
        print("invalid choice")
    

def withdr():
    ac=input("Enter Account No :")
    am = int(input("Enter Amount: "))
    a="select balance from ammount where acno='{}'"
    c1=mydb.cursor()
    c1.execute(a.format(ac))
    myresult = c1.fetchone()
    tam=myresult[0]-am
    sql="update ammount set balance={} where acno='{}'"
    c1.execute(sql.format(tam,ac))
    mydb.commit()
    print("-"*70)
    print(2*"\t"+"Amount withdrawn successfully from your account")
    print("-"*70,"\n")
    print("\n")
    cont()
    if x1=="y" or x1=="Y":
        cust_menu()
    elif x1=="n" or x1=="N":
        print("*"*50)
        print(2*"\t"+"THANK YOU FOR USING BANKING SYSTEM")
        print("*"*50,"\n")
        input()
        print("\n")
    else:
        print("invalid choice")
    
    
def balance():
    ac=input("Enter Account No :")
    a="select balance from ammount where acno='{}'"
    c1=mydb.cursor()
    c1.execute(a.format(ac))
    myresult=c1.fetchone()
    print("\n")
    print("Account Balance:INR",myresult[0])
    print("\n")
    cont()
    if x1=="y" or x1=="Y":
         cust_menu()
    elif x1=="n" or x1=="N":
        print("*"*70)
        print(2*"\t"+"THANK YOU FOR USING BANKING SYSTEM")
        print("*"*70,"\n")
        input()
        print("\n")
    else:
        print("invalid choice")
    

def accdetails():
    ac=input("Enter Account No:")
    a="select * from account where acno='{}'"
    c1=mydb.cursor()
    c1.execute(a.format(ac))
    myresult=c1.fetchone()
    print("-"*50)
    print(2*"\t"+"Account details")
    print("-"*50,"\n")
    print("\n")
    print("Name:",myresult[0])
    print("Account numbet:",myresult[1])
    print("Date of Birth:",myresult[2])
    print("Address:",myresult[3])
    print("phone number:",myresult[4])
    print("Email ID:",myresult[5])
    print("Aadhar No:",myresult[6])
    print("\n")
    cont()
    if x1=="y" or x1=="Y":
         cust_menu()
    elif x1=="n" or x1=="N":
        print("*"*70)
        print(2*"\t"+"THANK YOU FOR USING BANKING SYSTEM")
        print("*"*70,"\n")
        input()
        print("\n")
    else:
        print("invalid choice")
        

def modify_acc():
    a1=input("Enter Customer/'s Account No:")
    
    print("----------------------------Modify screen-----------------------------")
    print('\n 1. Customer Name')
    print('\n 2. Account number')
    print('\n 3. DOB')
    print('\n 4. Customer Address')
    print('\n 5. Customer Phone No')
    print('\n 6. Customer Email ID')
    choice=int(input("What do you want to change?"))
    new_data=input('Enter New value :')
    c1=mydb.cursor()
    if choice == 1:
        field_name='name'
    if choice == 2:
        field_name='acno'
    if choice == 3:
        field_name="dob"
    if choice == 4:
        field_name='address'
    if choice == 5:
        field_name='phn'
    if choice == 6:
        field_name='email'
       
    Q="update account set {}='{}' where acno='{}'".format(field_name,new_data,a1)
    v1="update ammount set {}='{}' where acno='{}'".format(field_name,new_data,a1)
    c1.execute(Q)
    if field_name=='name' or field_name=='acno':
        c1.execute(v1)
        
    print("-"*50)
    print(2*"\t"+"Customer Information modified..")
    print("-"*50,"\n")
    print("\n")
    cont()
    if x1=="y" or x1=="Y":
         admin_menu()
    elif x1=="n" or x1=="N":
        print("*"*50)
        print(2*"\t"+"THANK YOU FOR USING BANKING SYSTEM")
        print("*"*50,"\n")
        input()
        print("\n")
    else:
        print("invalid choice")
    
        
def display_all():
    c1=mydb.cursor()
    c1.execute("select * from account")
    data=c1.fetchall()
    print("-"*50)
    print(2*"\t"+"Dettails of all accounnts")
    print("-"*50,"\n")
    for r in data:
        print(r,"\n")
    cont()
    if x1=="y" or x1=="Y":
         admin_menu()
    elif x1=="n" or x1=="N":
        print("*"*50)
        print(2*"\t"+"THANK YOU FOR USING BANKING SYSTEM")
        print("*"*50,"\n")
        input()
        print("\n")
    else:
        print("invalid choice")
    
    
def closeacc():
    ac=input("Enter Account no:")
    Q1="delete from account where acno='{}'"
    Q2="delete from ammount where acno='{}'"
    c1=mydb.cursor()
    c1.execute(Q1.format(ac))
    c1.execute(Q2.format(ac))
    mydb.commit()
    print("-"*50)
    print(2*"\t"+"Your Account Is Closed..")
    print("-"*50,"\n")
    print("\n")
    cont()
    if x1=="y" or x1=="Y":
         cust_menu()
    elif x1=="n" or x1=="N":
        print("*"*50)
        print(2*"\t"+"THANK YOU FOR USING BANKING SYSTEM")
        print("*"*50,"\n")
        input()
        print("\n")
    else:
        print("invalid choice")
    
    

def trnsfer():
    a1=(input("Enter your Account No :"))
    a2=(input("Enter the AccountNo you want to transfer to :"))
    am=int(input("Enter Ammount to be transfered : "))
    a="select balance from ammount where acno='{}'"
    c1=mydb.cursor()
    c1.execute(a.format(a1))
    myresult = c1.fetchone()
    tam1=myresult[0]-am
    sql="update ammount set balance = '{}' where acno = '{}'"
    c1.execute(sql.format(tam1,a1))
    c1.execute(a.format(a2))
    myresult=c1.fetchone()
    tam2=myresult[0]+am
    c1.execute(sql.format(tam2,a2)) 
    mydb.commit()
    print("-"*70)
    print(2*"\t"+"Amount Transferred successfully")
    print("-"*70,"\n")
    print("\n")
    cont()
    if x1=="y" or x1=="Y":
         cust_menu()
    elif x1=="n" or x1=="N":
        print("*"*50)
        print(2*"\t"+"THANK YOU FOR USING BANKING SYSTEM")
        print("*"*50,"\n")
        input()
        print("\n")
    else:
        print("invalid choice")

def main_menu():
    print("*"*50)
    print(2*"\t"+"Banking System")
    print("*"*50,"\n")
    print("1.Admin Login\n2.Customer Login")
    choice=int(input("Select your choice:"))
    if choice==1:
        print("\n")
        admin_id=input("Enter Admin Username-")
        password=input("Enter password-")
        if admin_id=="ansh" and password=="1234":
            print("\n")
            admin_menu()
        else:
            print("\n")
            print("Id/Password is incorrect")
            print("\n")
            main_menu()
    elif choice==2:
        print("\n")
        cust_id=input("Enter Customer Username-")
        password=input("Enter password-")
        if cust_id=="ansh" and password=="1970":
            print("\n")
            cust_menu()
        else:
            print("Id/Psssword is incorrect")
            main_menu()
                   
        
def admin_menu():
    print("~~~~~~~~~~~~~~~~~~~~admin Menu~~~~~~~~~~~~~~~~~~~~\n")
    print("1.Add new account\n")
    print("2.Modify account details\n")
    print("3.Display all accounts\n")
    print("4.Exit")
    c=int(input("Enter your choice:"))
    if c==1:
        openacc()
    elif c==2:
        modify_acc()
    elif c==3:
        display_all()
    elif c==4:
        main_menu()
    else:
        print("Invalid Choice")
        
def cust_menu():
    print("~~~~~~~~~~~~~~~~~~~~customer Menu~~~~~~~~~~~~~~~~~~~~\n")
    print("1.Deposit Ammount\n")
    print("2.Withdraw Ammount\n")
    print("3.Transfer Money\n")
    print("4.Balance Enquiry\n")
    print("5.Account Details\n")
    print("6.Close an account\n")
    print("7.Exit\n")
    ch=int(input("Enter your Choice:"))
    if ch==1:
        depo()
    elif ch==2:
        withdr()
    elif ch==3:
        trnsfer()
    elif ch==4:
        balance()
    elif ch==5:
        accdetails()
    elif ch==6:
        closeacc()
    elif ch==7:
        main_menu()
    else:
        print("Invalid Choice")
        
        
def cont():
    print("Do you want to continue? (y/n)")
    global x1
    x1=input("Enter your choice:")
       

main_menu()


