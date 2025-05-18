import smtplib

email = "" 
password = ""

Connection = smtplib.SMTP("smtp.gmail.com")
Connection.starttls()
Connection.login(user=email,password=password)
Connection.sendmail(from_addr=email,to_addrs="",msg="Hello World")
Connection.close()



