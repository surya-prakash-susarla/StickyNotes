import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

class Mail:
	sender_mail_id = ''
	sender_password = ''
	receiver_mail_id = '' 
	message = ''
	smtp_session = None
	
	def __init__ ( self , sender , password,  receiver ):
		self.sender_mail_id = sender 
		self.sender_password = password
		self.receiver_mail_id = receiver
		self.smtp_session = smtplib.SMTP( SMTP_SERVER , SMTP_PORT )
		self.smtp_session.starttls()
		self.smtp_session.login(self.sender_mail_id , self.sender_password)
	
	def send_mail ( self, message ):
		self.message = message
		print("Sending messaage : ")
		#print(self.message)
		self.smtp_session.sendmail(self.sender_mail_id,self.receiver_mail_id,self.message)
		self.smtp_session.quit()
		return
	