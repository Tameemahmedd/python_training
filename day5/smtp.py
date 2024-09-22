'''
To send mail 
    enable in gmail the 2 step verification 
Then 
    use below link to create app password
    with app password and your mail id try to run the below code

    #https://support.google.com/accounts/answer/185833?hl=en
'''

import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'tameemahmed344@gmail.com'
email_passwd = 'rlik xghd dvej mwgq'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='mtd.nithin@gmail.com', msg=" Hello Sir,  NAME: Tameem Ahmed Mulla, TEAMMATE NAME: Prateek Kannojia, TEAM NUMBER:TEAM 4(T4), CASE STUDY: No.2 (MCQ Based Online Exam Application),  GITHUB REPO LINK:https://github.com/Tameemahmedd/python_training,")
connection.close()
print('Mail sent successfully')