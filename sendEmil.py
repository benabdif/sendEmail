import smtplib
import time
from email.message import EmailMessage

import schedule


class Email:
    email = 'fadilf00100@gmail.com'
    password = 'nfdjgnohphdxjqib'
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def sendEmail(self):
        #contacts = ['YourAddress@gmail.com', 'test@example.com']

        msg = EmailMessage()
        msg['Subject'] = 'Check out Bronx (tests_Fadhel)!'
        msg['From'] = self.email
        #msg['To'] = 'humidi@dolftech.com','r.ghareeb@dolftech.com','yuvaraj@dolftech.com','fadilf00100@gmail.com','fadhel@dolftech.com'
        msg['To'] = 'fadilf00100@gmail.com','fadhel@dolftech.com','yuvaraj@dolftech.com'
        
        msg.set_content('This is a plain text email')

        msg.add_alternative("""\
        <!DOCTYPE html>
        <html>
            <body>
                <h1 style="color:SlateGray;">This is an Test eamil sending by Fadhel, using python language!</h1>
                <p>No need to replace</p>
            </body>
        </html>
        """, subtype='html')


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.email, self.password)
            smtp.send_message(msg)
            
            
    def timesend(self):
        # This method to send every spicifice time
        #schedule.every().day.at('11:30').do(self.sendEmail) # This code to send every day
        schedule.every(120).seconds.do(self.sendEmail)
        while True:
            schedule.run_pending()
            time.sleep(1)
            
final_result = Email('fadilf00100@gmail.com', 'nfdjgnohphdxjqib')       
     
final_result.timesend()

    
    
  
  

        
        

# def email():
#     print('Hello, Fadhel')
    
# def email2():
#     print('Hello, Form anther email.')
    
# # Time....

# schedule.every(3).seconds.do(email)

# #schedule.every().day.at('11:30').do(email2)

# while True:
#     schedule.run_pending() 
#     time.sleep(1)
    

