

#############SQL COMMANDS
#create database mvd;
#use mvd;
#create table official(username char(30),password char(15));
#insert into official values("sanmay@123","123456");
#insert into official values("raman@123","12345");
#create table public(regno char(10),password char(25));

#############[Official-[Username:sanmay@123,Password:123456],[Username:raman@123,Password:12345]]

#[Public-[Password is name@123-Eg: lolith@123]]

#############Copy and paste the URL of 'HTML FILE.html' after opening it on the 460th line:



import os 
import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="",database="mvd")
if con.is_connected():
    print("Connectivity Successfull")
else:
    print("Connectivity Fail")


print("Vehicle Department")
print("Login To View Information")
print()
print()

mg=True
while mg==True:
    
    print("Enter 'O' to login as Department Official")
    print("Enter 'P' to login as Public User")
    print()
    a=input("Enter O or P :")

    s=1
    f=2

    if a=="O" or a=="o":
        x=True
        while x==True:
            cur=con.cursor()
            cur.execute("select * from official")
            row=cur.fetchall()
            
            u=input("Enter Username :")
            p=input("Enter Password :")
            for i in row:
                b=i[0]
                c=i[1]
                if b==u and c==p:
                    print()
                    print("Login Successful")
                    m=s
                    x=False
                    cur.close()
                    break
            else:
                print()
                print("Login Failed")
                print("Please Try Again")
                print()
                m=f
                cur.close()
                x=False
                break
                

                

        if m==1:
            y=True

            while y==True:
                print("What do you want to do. Select your needed option")
                print()
                print("Enter 1 to Create New Registration Details")
                print("Enter 2 to View Vehicle Details")
                print("Enter 3 to Edit Details [Except Registration Number]")
                print("Enter 4 to Edit Registration Number")
                print("Enter 5 to Delete All Details")
                print("Enter 6 to logout from your account")
                print()

                enter=int(input("Enter The Number Based On Your Choice :"))
                print()

                if enter==1:
                    cur=con.cursor()
                    
                    name=input("Enter The Name:")
                    dob=input("YYYY-MM-DD:")
                    idp=input("Enter ID Proof:")
                    idno=input("Enter ID Proof No:")
                    veh=input("Enter New Vehicle Registration Number:")
                    mod=input("Enter Vehicle Company And Model Name:")
                    lic=input("Enter License Number:")
                    p1="@123"
                    pf=name+p1

                    
                    cur.execute("select * from public")
                    row=cur.fetchall()
                    for i in row:
                        b1=i[0]
                        if b1==veh:
                            print("Registration Number Already Exist")
                            print()
                            k=f
                            break

                    else:

                        print()
                        cur.execute("insert into public values('{}','{}')".format(veh,pf))
                        con.commit()
                        cur.close()
                        y=False
                        k=s



                    if k==1:
                        txt=".txt"
                        txtf=veh+txt

                        f=open(txtf,"w")
                        f.write("Name : ")
                        f.write(name)
                        f.write("\n")
                        f.write("Date Of Birth : ")
                        f.write(dob)
                        f.write("\n")
                        f.write("ID Proof : ")
                        f.write(idp)
                        f.write("\n")
                        f.write("ID Prood Number : ")
                        f.write(idno)
                        f.write("\n")
                        f.write("Registration Number : ")
                        f.write(veh)
                        f.write("\n")
                        f.write("Vehicle Company and Model Name : ")
                        f.write(mod)
                        f.write("\n")
                        f.write("License Number : ")
                        f.write(lic)
                        f.write("\n")
                        f.close()
                        
                        f=open(txtf,"r")
                        for line in f:
                            print(line)
                        f.close()

                    ab=input("Enter e to continue on your program or press any other key to logout :")
                    if ab=="e":
                        y=True
                    else:
                        y=False
                    
                elif enter==2:
                    check=input("Enter Vehicle Registration Number :")
                    cur=con.cursor()
                    cur.execute("select * from public")
                    row=cur.fetchall()
                    for i in row:
                        b1=i[0]
                        if b1==check:
                            print("Details Found")
                            print()

                            txt=".txt"
                            txtf=check+txt

                            f=open(txtf,"r")
                            for line in f:
                                print(line)
                            f.close()
                            ab=input("Enter e to continue on your program or press any other key to logout:")
                            print()
                            if ab=="e":
                                y=True
                            else:
                                y=False
                            break

                    else:
                        print("Details does not exist")
                        print()
                        ab=input("Enter e to continue on your program or press any other key to logout:")
                        if ab=="e":
                            y=True
                        else:
                            y=False
                            print("Logged Out Successfully")
                

                elif enter==3:


                    check=input("Enter Present Vehicle Registration Number ")
                    cur=con.cursor()
                    cur.execute("select * from public")
                    row=cur.fetchall()
                    con.commit()
                    cur.close()
                    for i in row:
                        b1=i[0]
                        if b1==check:
                            print("Details Found")

                            xy=True
                            while xy==True:
                                print()
                                txt=".txt"
                                txtf=check+txt
                                f=open(txtf,"r")
                                data=f.readlines()
                                f.close()

                                print("Enter 1 to edit name")
                                print("Enter 2 to edit Date Of Birth")
                                print("Enter 3 to edit ID Proof")
                                print("Enter 4 to edit ID Proof Number")
                                print("Enter 5 to edit Vehicle Model")
                                print("Enter 6 to edit License Number")
                                print("Enter 7 to Go Back")

                                raja=int(input("Enter the number based on your chioce of editing :"))
                        
                                if raja==1:
                                    edit=input("Enter Name :")
                                    ed="Name : "
                                    enter="\n"
                                    j=ed+edit+enter
                                    data[0]=j

                                    mass="@123"
                                    lock=edit+mass

                                    f=open(txtf,"w")
                                    f.writelines(data)
                                    f.close()

                                    cur=con.cursor()
                                    cur.execute("update public set password='{}' where regno='{}'".format(lock,check))
                                    con.commit()
                                    cur.close()
                                    print("Done")
                                    
                                    
                                elif raja==2:
                                    edit=input("Enter DOB :")
                                    ed="Date Of Birth : "
                                    enter="\n"
                                    j=ed+edit+enter
                                    
                                    data[1]=j

                                    f=open(txtf,"w")
                                    f.writelines(data)
                                    f.close()
                                    

                                elif raja==3:
                                    edit=input("Enter ID Proof :")
                                    ed="ID Proof : "
                                    enter="\n"
                                    j=ed+edit+enter
                                    
                                    data[2]=j

                                    f=open(txtf,"w")
                                    f.writelines(data)
                                    f.close()
                                    
                                elif raja==4:
                                    edit=input("Enter ID Proof Number :")
                                    ed="ID Proof Number : "
                                    enter="\n"
                                    j=ed+edit+enter
                                    
                                    data[3]=j

                                    f=open(txtf,"w")
                                    f.writelines(data)
                                    f.close()

                                
                                    
                                
                                elif raja==5:
                                    edit=input("Enter Vehicle Companay Model Name:")
                                    ed="Vehicle Company and Model Name : "
                                    enter="\n"
                                    j=ed+edit+enter
                                    
                                    data[5]=j

                                    f=open(txtf,"w")
                                    f.writelines(data)
                                    f.close()
                                    

                                elif raja==6:
                                    edit=input("Enter License Number :")
                                    ed="Name : "
                                    enter="\n"
                                    j=ed+edit+enter
                                    
                                    data[6]=j

                                    f=open(txtf,"w")
                                    f.writelines(data)
                                    f.close()
                                    
                                    
                                elif raja==7:
                                    
                                    xy=False
                                    y=True
                                    break

                                else:
                                    print("Try Again")
                    

                    else:
                        if raja==7:
                            print("Went Back")
                            print()
                        else:
                            print("Details Not Found")
                            print()
                            y=True
                        

                elif enter==4:
                    check=input("Enter Present Vehicle Registration Number :")
                    cur=con.cursor()
                    cur.execute("select * from public")
                    row=cur.fetchall()
                    for i in row:
                        b1=i[0]
                        if b1==check:
                            print("Details Found")

                            print()
                            txt=".txt"
                            txtf=check+txt
                            f=open(txtf,"r")
                            data=f.readlines()
                            f.close()
                                
                            edit=input("Enter New Reistration Number :")
                            ed="Registration Number : "
                            enter="\n"
                            j=ed+edit+enter
                                    
                            data[4]=j

                            os.remove(txtf)

                            jan=".txt"
                            janit=edit+txt

                            f=open(janit,"w")
                            f.writelines(data)
                            f.close()
                            cur.execute("update public set regno='{}' where regno='{}'".format(edit,check))
                            con.commit()
                            cur.close()
                            break
                    else:
                        print("Details not found")

                elif enter==5:
                    check=input("Enter your Registration Number")
                    cur=con.cursor()
                    cur.execute("select * from public")
                    row=cur.fetchall()
                    for i in row:
                        b1=i[0]
                        if b1==check:
                            print("Details Found")
                            print()

                            txt=".txt"
                            txtf=check+txt
                            os.remove(txtf)
                            cur.execute("delete from public where regno='{}'".format(check))
                            con.commit()
                            cur.close()
                            print("Your file has been deleted successfully")
                            break
                    else:
                        print("Details not found")
                            

                            
                    
                        
                
                elif enter==6:
                    print("Logged Out Successfully")
                    y=False
                else:
                    print("Incorrect Option, Try Again")


    

    if a=="P" or a=="p":
        x=True
        while x==True:
            cur=con.cursor()
            cur.execute("select * from public")
            row=cur.fetchall()
            
            u=input("Enter Registration Number :")
            p=input("Enter Password :")
            for i in row:
                b=i[0]
                c=i[1]
                if b==u and c==p:
                    print()
                    print("Login Successful")
                    m=s
                    x=False
                    cur.close()
                    break
            else:
                print()
                print("Login Failed")
                print("Please Try Again")
                print()
                m=f
                cur.close()
                x=False
                break
                        
                   
        if m==1:
            y=True

            while y==True:
                print("What do you want to do. Select your needed option")
                print()
                
                print("Enter 1 to View Your Registration Details")
                print("Enter 2 to View Information To Edit Your Registration Details")
                print("Enter 3 to Log Out From Your Account")
                enter=int(input("Enter The Number Based On Your Choice :"))
                print()

                if enter==1:
                    cur=con.cursor()
                    cur.execute("select * from public")
                    row=cur.fetchall()
                    for i in row:
                        b1=i[0]
                        if b1==u:
                            

                            txt=".txt"
                            txtf=u+txt

                            f=open(txtf,"r")
                            for line in f:
                                print(line)
                            f.close()
                            ab=input("Enter e to continue on your program or press any other key to logout :")
                            if ab=="e":
                                y=True
                            else:
                                y=False
                            break

                elif enter==2:
                    print()
                    print("Fill The Form and sent a scanned copy to 'rtomlxxxxx@gmail.com' ")
                    import webbrowser
 
                    webbrowser.open("file:///C:/Users/TOSHIBA/Desktop/Python/HTML%20FILE.html")

                    
                        
                elif enter==3:
                    print("Logged Out Successfully")
                    y=False
                        

                

                    
                
                
                    

                          
                            

                            

                    
                    
                    
                    





            
                    
            
            







        


