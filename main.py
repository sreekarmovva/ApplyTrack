applications =[{ "Company":"Google", "Role":"Software Engineer", "Status":"Applied" }, 
               {"Company":"Qualcomm","Role":"Associate Engineer","Status":"Assessment"}, 
               
               ]

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
      
add_application("Deloitte", "Analyst", "Interview" ) 
display_applications()     
