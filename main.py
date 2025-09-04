import datetime

print("-"*110)
print("\t\t\t\t\t TechnoPropertyNepal🏠")
print("-"*110)
print("-"*110)
print("\t\t\t\t\tLocation: Kamalpokhari, Kathmandu")
print("-"*110)
print("\n")
print("Welcome to TechnoPropertyNepal🙏")
print("\n")

with open("data.txt",'r') as file:
    myDictionary={}
    kitta=101
    for line in file:
        line=line.replace('\n','')
        myDictionary[kitta]=(line.split(','))
        kitta=kitta+1
    print(myDictionary)

print("\n")
print("Below are the option available with us⬇️")
print("-"*80)
print("Kitta \t District    Direction\tAnna\tPrice\tAvailability")
print("-"*80)
        

with open("data.txt",'r')as file:
    kitta=101
    for line in file:
        print(kitta,"\t",line.replace(',','\t'))
        kitta+=1
        print("-"*80)

print("\n")
print("-->Below are the option that you can choose:\n")
print("1. Press 1 to rent the land")
print("2. Press 2 to return the land")
print("3. Press 3 to exit")
print("\n")

loop=True
while loop:
    print("\n")
    userinput=(input("Please enter the appropirate option that you want to processed:"))
    if userinput== "1":
        print("Thank you for renting")
        print("\n")
        print("Please enter the detail:")
        name=input("Enter your name:")
        phone=input("Enter the phone number:")
        
        
        continue_loop = True
        user_land=[]
        print_bill=False

        while continue_loop:
            print("\n")
            
            try:
                kitta_num=int(input("Enter the kitta number:"))
                while(kitta_num==102):
                    print("You cant buy this kitta number land")
                    kitta_num=int(input("Enter the kitta number:"))

                while(kitta_num<=100 or kitta_num>=104):
                    print("Please enter the correct kitta number")
                    kitta_num=int(input("Enter the kitta number:"))
            except ValueError as e:
                print("Invalid input! Please enter integer for kitta number")
                continue
            
            is_available = myDictionary[kitta_num][4]
            if is_available == "Availabel":
                print("Sorry, This land is already rented")
                continue

            
            print("\n")
            anna_land=int(myDictionary[kitta_num][2])
            print(kitta_num,"Kitta number has",anna_land,"anna of land")
            available=myDictionary[kitta_num][4]
            print("Kitta number",kitta_num,"is",available)
            month=int(input("Enter the month you want to rent for:"))
            per_month_price=int(myDictionary[kitta_num][3])

            bill_kitta_num=kitta_num
            anna=anna_land
            month_=month
            total_price=month_*per_month_price


            user_land.append([bill_kitta_num,anna,month_,per_month_price,total_price])
            print(user_land)

            myDictionary[kitta_num][4] = "Availabel"

            more=input("Do you want more?(yes/no)")
            if more.lower() =="yes":
                continue_loop = True
            else:
                print_bill=True
                if print_bill:
                    grand_total=0
                    for i in user_land:
                        grand_total+=int(i[4])


                    print("\n")
                    print("\t \t \t \t \t  Technoproperty Nepal")
                    print("\n")
                    print("\t \t \t \tAddress: Kamalpokhari Kathmandu Metroplitan")
                    print("\n")
                    print("\t\t\tContact: 9801099876 || Email: techonrental@gmail.com")
                    print("\n")
                    print("Name of the customer: ",name,"\n")
                    print("Phone of the customer:",phone,"\n")

                    print("."*100)
                    print("\t\t Kitta No.\t Aana \t Month \t Price per month\tTotal Price ")
                    print("."*100)

                    for i in user_land:
                        print("\t\t",i[0],"\t\t",i[1],"\t",i[2],"\t",i[3],"\t\t\t",i[4])
                        print("."*100)
                    print("Grand total is",grand_total)
                    print("Thank you for using Technorental services")

                    today_date_and_time= datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                    with open(name + str(phone) + today_date_and_time +".txt",'w')as file:
                        file.write("\n")
                        file.write("\t \t \t \t \t \t  Technoproperty Nepal")
                        file.write("\n")
                        file.write("\t \t \t \t Address: Kamalpokhari Kathmandu Metroplitan")
                        file.write("\n")
                        file.write("\t\t\tContact: 9801099876 || Email: techonrental@gmail.com")
                        file.write("\n\n")
                        file.write("Name of the customer: "+ name +"\n")
                        file.write("Phone of the customer:"+ phone +"\n")
                        file.write("."*100)
                        file.write("\n")
                        file.write("\t\t Kitta No.\t Aana \t Month \t Price per month\tTotal Price \n")
                        file.write("."*100)
                        file.write("\n")

                        for i in user_land:
                            file.write("\t\t"+ str(i[0])+ "\t\t\t" + str(i[1])+"\t\t"+str(i[2])+"\t\t"+str(i[3])+"\t\t\t\t"+str(i[4]))
                            file.write("\n")
                            file.write("."*100)
                            file.write("\n")
                            continue_loop = False
                        file.write("Thank you for using Techno property services \n")
                        file.write("The grand total is:"+str(grand_total))
                            

    elif userinput=="2":
        print("Thank you for returning")
        names=input("Enter your name:")
        phones=input("Enter your phone number:")
        user_lands=[]
        print_bill=False
        loops=True
        while loops:
            try:
                kitta_num=int(input("Enter the kitta number:"))
                while(kitta_num==102):                     
                    print("You cannot return this land because it is not in our system")
                    kitta_num=int(input("Enter the kitta number:"))

                while(kitta_num<=100 or kitta_num>=104):
                    print("The kitta number you have provided is not in our system")
                    kitta_num=int(input("Enter the kitta number:"))
                rent_month=int(input("Enter the month you have rented for:"))
                return_month=int(input("Enter the returning month:"))
            except ValueError as e:
                print("Invalid input, Enter integer!")
                continue
            loops=False
            
            if rent_month==return_month:
                        
                    anna_land=int(myDictionary[kitta_num][2])
                    per_month_price=int(myDictionary[kitta_num][3])

                    bill_kitta_num=kitta_num
                    anna=anna_land
                    total_price=rent_month*per_month_price
                    amount_with_fine= 0

                
                    user_lands.append([bill_kitta_num,anna,per_month_price,rent_month,return_month,total_price,amount_with_fine])
                    
                    myDictionary[kitta_num][4]= "Available" 
                    print("The kitta number",kitta_num,"land has been sucessfully return and the land is available")
                    mores=input("Want to return more land?")
                    if mores.lower()=="yes":
                        loops=True
                    else:
                        print_bill=True
                        if print_bill:
                            grand_total=0
                            for i in user_lands:
                                grand_total+=int(i[5])

                            print("\n")
                            print("\t \t \t \t \t  Technoproperty Nepal")
                            print("\n")
                            print("\t \t \t \tAddress: Kamalpokhari Kathmandu Metroplitan")
                            print("\n")
                            print("\t\t\tContact: 9801099876 || Email: techonrental@gmail.com")
                            print("\n")
                            print("Name of the customer: ",names,"\n")
                            print("Phone number of the customer:",phones,"\n")

                            print("."*120)
                            print("\t Kitta No.\t Aana \t Price per month \t Rented month \t Return month \tTotal Price \t Amount with fine ")
                            print("."*120)

                            for i in user_lands:
                                print("\t",i[0],"\t\t",i[1],"\t",i[2],"\t\t\t\t",i[3],"\t\t",i[4],"\t",i[5],"\t",i[6])
                                print("."*120)

                                print("Thank you for returning")
                                print("The grand total is:",grand_total)

                                today_date_and_time= datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                                with open(names + str(phones) + today_date_and_time +".txt",'w')as file:
                                    file.write("\n")
                                    file.write("\t \t \t \t \t \t \t   Technoproperty Nepal")
                                    file.write("\n")
                                    file.write("\t \t \t \t \t Address: Kamalpokhari Kathmandu Metroplitan")
                                    file.write("\n")
                                    file.write("\t\t\t \t Contact: 9801099876 || Email: techonrental@gmail.com")
                                    file.write("\n")
                                    file.write("\n")
                                    file.write("Name of the customer: "+names+"\n")
                                    file.write("Phone number of the customer:"+phones+"\n")

                                    file.write("."*110)
                                    file.write("\n")
                                    file.write("\t Kitta No.\t Aana \t Price per month \t Rented month \t Return month \tTotal Price \t Amount with fine \n")
                                    file.write("."*110)
                                    file.write("\n")

                                    for i in user_lands:
                                        file.write("\t"+str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t\t\t"+str(i[3])+"\t\t\t\t"+str(i[4])+"\t\t\t"+str(i[5])+"\t\t\t"+str(i[6]))
                                        file.write("\n")
                                        file.write("."*110)
                                        file.write("\n")
                                    file.write("Thank you for using Techno property service \n")
                                    file.write("The grand total is:"+str(grand_total))
                        

            elif rent_month<return_month:

                anna_land=int(myDictionary[kitta_num][2])
                per_month_price=int(myDictionary[kitta_num][3])

                bill_kitta_num=kitta_num
                anna=anna_land

                delayed_month=return_month-rent_month
                
                total_price=rent_month*per_month_price

                fine_price= round(10/100*delayed_month*per_month_price)
                
                amount_with_fine=total_price+fine_price
                

                
                user_lands.append([bill_kitta_num,anna,per_month_price,rent_month,return_month,total_price,amount_with_fine])

                myDictionary[kitta_num][4]= "Available"
                print("The kitta number",kitta_num,"land has been sucessfully return and the land is available")
                mores=input("Want to return more land?")
                if mores.lower()=="yes":
                    loops=True
                else:
                    print_bill=True
                    if print_bill:
                        grand_total=0
                        for i in user_lands:
                            grand_total+=int(i[5])

                        print("\n")
                        print("\t \t \t \t \t  Technoproperty Nepal")
                        print("\n")
                        print("\t \t \t \tAddress: Kamalpokhari Kathmandu Metroplitan")
                        print("\n")
                        print("\t\t\tContact: 9801099876 || Email: techonrental@gmail.com")
                        print("\n")
                        print("Name of the customer: ",names,"\n")
                        print("Phone number of the customer:",phones,"\n")

                        print("."*120)
                        print("\t Kitta No.\t Aana \t Price per month \t Rented month \t Return month \tTotal Price \t Price with fine ")
                        print("."*120)

                        for i in user_lands:
                            print("\t",i[0],"\t\t",i[1],"\t",i[2],"\t\t\t\t",i[3],"\t\t",i[4],"\t",i[5],"\t",i[6])
                            print("."*120)

                        print("Thank you for returning")
                        print("The grand total is:",grand_total)
                
            
                        today_date_and_time= datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                
                        with open(names + str(phones) + today_date_and_time +".txt",'w')as file:
                            file.write("\n")
                            file.write("\t \t \t \t \t \t \t   Technoproperty Nepal")
                            file.write("\n")
                            file.write("\t \t \t \t \t Address: Kamalpokhari Kathmandu Metroplitan")
                            file.write("\n")
                            file.write("\t\t\t \t Contact: 9801099876 || Email: techonrental@gmail.com")
                            file.write("\n")
                            file.write("\n")
                            file.write("Name of the customer: "+names+"\n")
                            file.write("Phone number of the customer:"+phones+"\n")

                            file.write("."*110)
                            file.write("\n")
                            file.write("\t Kitta No.\t Aana \t Price per month \t Rented month \t Return month \tTotal Price \t Price with fine \n")
                            file.write("."*110)
                            file.write("\n")

                            for i in user_lands:
                                file.write("\t"+str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t\t\t"+str(i[3])+"\t\t\t\t"+str(i[4])+"\t\t\t"+str(i[5])+"\t\t\t"+str(i[6]))
                                file.write("\n")
                                file.write("."*110)
                                file.write("\n")
                            file.write("Thank you for using Techno property service \n")
                            file.write("The grand total is:"+str(grand_total))
            
            elif rent_month>return_month:

                anna_land=int(myDictionary[kitta_num][2])
                per_month_price=int(myDictionary[kitta_num][3])

                bill_kitta_num=kitta_num
                anna=anna_land
                total_price=rent_month*per_month_price
                amount_with_fine= 0

                
                user_lands.append([bill_kitta_num,anna,per_month_price,rent_month,return_month,total_price,amount_with_fine])
                    
                myDictionary[kitta_num][4]= "Available" 
                print("The kitta number",kitta_num,"land has been sucessfully return and the land is available")
                mores=input("Want to return more land?")
                if mores.lower()=="yes":
                    loops=True
                else:
                    print_bill=True
                    if print_bill:
                        grand_total=0
                        for i in user_lands:
                            grand_total+=int(i[5])

                            print("\n")
                            print("\t \t \t \t \t  Technoproperty Nepal")
                            print("\n")
                            print("\t \t \t \tAddress: Kamalpokhari Kathmandu Metroplitan")
                            print("\n")
                            print("\t\t\tContact: 9801099876 || Email: techonrental@gmail.com")
                            print("\n")
                            print("Name of the customer: ",names,"\n")
                            print("Phone number of the customer:",phones,"\n")

                            print("."*120)
                            print("\t Kitta No.\t Aana \t Price per month \t Rented month \t Return month \tTotal Price \t Amount with fine ")
                            print("."*120)

                            for i in user_lands:
                                print("\t",i[0],"\t\t",i[1],"\t",i[2],"\t\t\t\t",i[3],"\t\t",i[4],"\t",i[5],"\t",i[6])
                                print("."*120)

                            print("Thank you for returning")
                            print("The grand total is:",grand_total)

                            today_date_and_time= datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                            with open(names + str(phones) + today_date_and_time +".txt",'w')as file:
                                file.write("\n")
                                file.write("\t \t \t \t \t \t \t   Technoproperty Nepal")
                                file.write("\n")
                                file.write("\t \t \t \t \t Address: Kamalpokhari Kathmandu Metroplitan")
                                file.write("\n")
                                file.write("\t\t\t \t Contact: 9801099876 || Email: techonrental@gmail.com")
                                file.write("\n")
                                file.write("\n")
                                file.write("Name of the customer: "+names+"\n")
                                file.write("Phone number of the customer:"+phones+"\n")

                                file.write("."*110)
                                file.write("\n")
                                file.write("\t Kitta No.\t Aana \t Price per month \t Rented month \t Return month \tTotal Price \t Amount with fine \n")
                                file.write("."*110)
                                file.write("\n")

                                for i in user_lands:
                                    file.write("\t"+str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t\t\t"+str(i[3])+"\t\t\t\t"+str(i[4])+"\t\t\t"+str(i[5])+"\t\t\t"+str(i[6]))
                                    file.write("\n")
                                    file.write("."*110)
                                    file.write("\n")
                                file.write("Thank you for using Techno property service \n")
                                file.write("The grand total is:"+str(grand_total))
                                file.write("\n")
                                file.write("Note:The price of rented month will be applicable")
    else:
        if userinput=="3":
            print("\n")
            print("Thank you for using our system")
            loop=False