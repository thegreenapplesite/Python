import datetime
import imaplib
import email

global mail

class XX:
    def __init__(self):
        self.dict={}
        self.keytodelete=0
    
    def returndict(self):
        return self.dict
    
    def returnkeytodelete(self):
        return self.dict[self.keytodelete]
    
    def setkeytodelete(self,a):
        self.keytodelete=a
    
    def msg(self):
        print("Process Terminated")
    
    def delmsg(self):
        a=input("Indicate which one you want to delete:")
        return a

    def givemeinput(self):
        myvalue= int(input("Please enter how many mails you want to check:"))
        return myvalue
    
    def createdictionary(self,a,b):
        self.dict[a]=b
        
    def printdictionary(self):
        print(self.dict)
        
    def connecttomymailbox(self,a):
        myvalue=a
        date = (datetime.date.today() - datetime.timedelta(3)).strftime("%d-%b-%Y")
        mail = imaplib.IMAP4_SSL('imap.mail.yahoo.com',993)
        mail.login('YourUser', 'YourPassword')
        mail.list()
        mail.select("inbox")
        result,data = mail.uid('search', None, "ALL")
        latest_email_uid = data[0].split()[-1]
        for i in range(0,myvalue):    
            latest_email_uid=int(latest_email_uid)-i
            latest_email_uid=str(latest_email_uid)
            result,data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            try:
                
                raw_email = data[0][1]
                self.createdictionary(i, latest_email_uid)
                email_message = email.message_from_string(raw_email)
                x=str(email.utils.parseaddr(email_message['From']))
                print(str(i) + ": " + x + " Subject: " +  str(email_message['Subject']) )
                
                 
            except TypeError:
                print("Error")
        
        mail.close()
        mail.logout()
    
    def deleteall(self):
        b=[]
        for key in self.dict:
            b.append(key)
        self.deletemymail(b)
    
    
    
    def deletemymail(self,a=[]):
        mail = imaplib.IMAP4_SSL('imap.mail.yahoo.com',993)
        mail.login('YourUser', 'YourPassword')
        mail.list()
        mail.select("inbox")
        i=0
        for i in range(len(a)):
            self.setkeytodelete(int(a[i]))
            mail.uid('STORE',self.returnkeytodelete(),'+FLAGS', '(\\Deleted)')
            mail.expunge();
            print("Email " + str(a[i]) + " Deleted")
        

    
obj=XX()            
inp=obj.givemeinput()
obj.connecttomymailbox(inp)
myans=''
myans=raw_input("Do you want to delete any email Y/N:")
if myans in ['Y','y']:
    a=[]
    workfile=raw_input("Please enter your numbers(or all to delete them all):")
    a=workfile.split(" ")
    if (a[0].lower()=="all"):
        obj.deleteall()
    else:
        obj.deletemymail(a)
else:
    print("Program Terminated")
