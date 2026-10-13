applications =[{ "Company":"Google", "Role":"Software Engineer", "Status":"Applied" }, 
               {"Company":"Qualcomm","Role":"Associate Engineer","Status":"Assessment"}, 
               
               ]

allowed_status = ["applied","assessment","interview","rejected"]

def add_application(Company, Role, Status):
    application={
        "Company": Company,
        "Role": Role,
        "Status": Status
    }

    applications.append(application)



def display_applications():
    for application in applications:
        print("Company:", application["Company"])
        print("Role:", application["Role"])
        print("Status:", application["Status"])

def update_application_status():
    company = input("Enter company you want to update: ").strip()
    for application in applications:
        if application["Company"].lower() == company.lower():
            print("Application found!!") 
            new_status=input("Enter new application status:").strip().lower()
            
            if new_status not in allowed_status:
                print("Invalid status entered. enter valid status")
                return
            application["Status"]=new_status
            print("Application status updated successfully!!")
            break   
    else:
        print("Application not found")            
         
while True:
    print("=====Apply Track=====")
    print("1. Add Application")
    print("2. View Application")
    print("3. Update Application Status")
    print("4. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        print("Add Application selected")
##Adding an application
        company = input("Enter company name: ").strip()
        if company.strip() == "":
            print("Company name cannot be empty. please enter a name")
            continue
        role = input("Enter job role: ").strip()
        if role.strip() == "":
            print("Role cannot be empty")
            continue
        
        status = input("Enter application status: ").strip().lower()
        if status.strip() == "":
            print("status connot be empty ")
            continue
        if status not in allowed_status:
            print("Please enter valid status of your application")
            continue

        add_application(company, role, status)

    elif choice=="2":
        display_applications() 


    elif choice=="3":
        update_application_status() 


    elif choice=="4":
        print("Exiting ApplyTrack...")
        break
    else:
        print("Invalid choice. please enter 1, 2, 3 or 4.")    