import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
import calendar
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import re

class Train:
    def __init__(self,train_name,train_root,train_destination,train_depature,train_pickup,train_reaching_time):
        self.train_name=train_name
        self.train_root=train_root
        self.train_destination=train_destination
        self.train_reaching_time=train_reaching_time
        self.train_depatrue=train_depature
        self.train_pickup=train_pickup



    def trainInfo(self):
        
        if self.train_name in name:
            print("\nThe train is available :)") 
        else:
            print("The train is not available :(")
            quit()
        
    def trainPickup(self):
        Pickup=["Nagpur","Nashik","Mumbai","Pune","Amravti"]
        if self.train_pickup in Pickup:
            print("Pickup point available!!!")
            inp1=input("Enter Y to conform the pickup point:")
            if inp1=="Y".casefold():
                time.sleep(0.5)
                print("\nPickup Confirmed")
            else:
                print("Pickup Denied")
        else:
            print("\nThe pickup point is not available:")
            print("\nYou can choose the other pickup point given in the list",Pickup)
            inp2=input("Do you want to select a pickup point:")
            if inp2=="Y".casefold():
                c=input("Enter the pickup point:")
                if c in Pickup:
                    print("Pickup Confirmed")
                else:
                    quit()
        
    def trainDestination(self):
        Destination=["Delhi","Gurugram","Kolkata","Madhy Pradesh","Uttar Pradesh"]
        if self.train_destination in Destination:
            print("\nThe Destination is availabe :)")
            inp3=input("Enter Y to conform the Destination point:")
            if inp3=="Y".casefold():
                print("Destination Confirmed")
            else:
                print("Destination Denied")
                quit()
        else:
            print("The Destination point is not available:")
            print("You can choose the other Destionation point given in the list",Destination)
            inp2=input("Do you want to select a Destination point:")
            if inp2=="Y".casefold():
                d=input("Enter the Destination point:")
                if d in Destination:
                    print("Destination Confirmed")
                else:
                    quit()

    def booking_and_seats(self):
        print(f'Would you like to proceed with payment')
        proceed=input(f'\nEnter Y for Yes & N for NO:')
        no_of_person=int(input("Number of Passengers:"))
        ages=[]
        for i in range(no_of_person):
            ages_of_person=int(input("Enter the ages:"))
            ages.append(ages_of_person)
        ages

        no_of_seats=30
        print("Number of seats avaialbe are:",no_of_seats)
        if(no_of_seats<no_of_person):
              print(f"Sorry only {no_of_seats} are available")
              print("\nYour Ticket has been Booked in Waiting List\nYou Will be get to know seating status before 4 hrs of Departue!!!")
        else:
               
               print(f"Booking your seats....")
               time.sleep(2)
               print("Seats Booked!!!")
               no_of_seats=no_of_seats-no_of_person
        print("No of Seats availabe are:",no_of_seats)
        
        add_below_18=[]
        add_above_18=[]
        if proceed=="Y".casefold():
           print(f'Price above 18 --> 100/person\nPrice below 18 -->50')
           for k in range(len(ages)):
              if(ages[k]<18):
                add_below_18.append(50)
              else:
                add_above_18.append(100)
           total=sum(add_above_18)+sum(add_below_18)
           print(total)
   


    def booking_date_time(self):
        print("Please select the month and date :\n")
        year=int(input("Enter the year:"))
        month=int(input("Enter the month:"))
        print(calendar.month(year,month))
        date=int(input("Enter the date:"))
        if(date<32):
            time.sleep(2)
            print("Date Selected!!")
        else:
            print("Please Select other date as no train is available on this date")
            


    def recipt(self):

        print("Would you like to have receipt")
        rec=input("Press Y for yes and N for No")
        if rec=="y".casefold():
            f=open("recipt.txt","w")
            f.write("---- recipt ----\n")
            f.write("Personal Details\n")
            f.write(f'Name of the person is {u_name}\n')
            f.write(f'Age of the person is {u_age}\n')
            f.write(f'Gender of the person is {u_gender}\n')
            f.write(f'Contact No of the person is {u_contact_no}\n')
            f.write(f'Booking Status:')       
             #update to waiting and conformed
        
            f.close()


    def convert_txt_to_pdf(txt_file, pdf_file):
       c = canvas.Canvas(pdf_file, pagesize=letter)

       with open('recipt.txt', 'r') as file:
        content = file.read()

       c.setFont("Helvetica", 10)

       x, y = 50, 750

       for line in content.split('\n'):
        c.drawString(x, y, line)
        y -= 15  

       c.save()

       txt_file = "recipt.txt"
       pdf_file = "recipt.pdf"


     
    def send(self):
        u_gmail=input("Enter your gmail address:")
        g=[]
        g.append(u_gmail)
        smtp_port=587        
        smtp_server="smtp.gmail.com"

        email_sender="rajputar_1@rknec.edu"
        email_reciver=g
        print(email_reciver)
        email_password="ggqymwmazmmvjemv"


        subject="Passenger Recipt"

        def send_emails(email_reciver):

            for person in email_reciver:
                body='''
                Please Find the attachment below:
                '''
                em=MIMEMultipart()
                em['from']=email_sender
                em['To']=person
                em['Subject']=subject
   
                em.attach(MIMEText(body,"plain"))
    
        
                filename="recipt.pdf"
                attachment=open(filename,'rb')
        
        
                attachment_package=MIMEBase('application','octet-stream')
                attachment_package.set_payload((attachment).read())
                encoders.encode_base64(attachment_package)
                attachment_package.add_header('Content-Disposition','attachment;filename=' +filename)
                em.attach(attachment_package)
            
                text=em.as_string()
            
                print("connecting to server")
                TIE_server=smtplib.SMTP(smtp_server,smtp_port)
                TIE_server.starttls()
                TIE_server.login(email_sender,email_password)
                print("connected to sever")
                print()
        
        
                print(f"Sending mail to :{person}")
                TIE_server.sendmail(email_sender,person,text)
                print("email sent to",person)
                print()
            TIE_server.quit()
        
        
        send_emails(email_reciver)


    def finish(self):
        print("Thanks for visting the website")


print("----- WELCOME TO OUR WEBSITE -----")
            
print("\nHey will you please fill the details:\n")


def validate_name(u_name):
    pattern = r"^[a-zA-Z.]+(?: [a-zA-Z.]+)*$"  
    if re.match(pattern, u_name):
        return True
    else:
        return False
u_name = input("Enter your name: ")
if validate_name(u_name):
    time.sleep(1)
else:
    print("Please Enter the valid name!")
    exit()


def validate_age(u_age):
    pattern = r"^[1-9][0-9]?$" 
    if re.match(pattern, str(u_age)):
        return True
    else:
        return False
u_age = input("Enter your age: ")
if validate_age(u_age):
    time.sleep(1)
else:
    print("Please Enter the valid age!")
    exit()



def validate_input(u_gender):
    pattern = r"^[MFN]$"
    if re.match(pattern, u_gender):
        return True
    else:
        return False
u_gender = input("Enter your gender (M/F/N): ")
if validate_input(u_gender):
    time.sleep(1)
else:
    print("Please Enter the valid Gender!")
    exit()



def validate_contact_number(u_contact_no):
    pattern = r"^[0-9]{10}$"  # Pattern for a 10-digit contact number
    if re.match(pattern, u_contact_no):
        return True
    else:
        return False
u_contact_no = input("Enter your contact number: ")
if validate_contact_number(u_contact_no):
    time.sleep(1)
else:
    print("Invalid contact number!")
    exit()


print("\nThanks for filling the detail!!!\n")


print("\n Please Enter The Following Information\n")
name=["Duranto Express","Sevagram Express","Rajdhani Express","Garib Rath"]
print("This are the Trains Available:",name)

t_name=input("Enter the train name:")
t_pickup=input("Enter the train pickup point:")
t_destination=input("Enter the destination point:")



t=Train(t_name,"Nagpur-Delhi",t_destination,"7:30 PM",t_pickup,"12:00 AM")
t.trainInfo()
t.trainPickup()
t.trainDestination()
t.booking_date_time()
t.booking_and_seats()
t.recipt()
t.convert_txt_to_pdf(pdf_file='recipt.pdf')
t.send()
t.finish()