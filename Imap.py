import datetime
import imaplib
import re

def msg():
    print("Process Terminated")

def givemeinput():
    myvalue= int(input("Please enter how many mails you want to check:"))
    return myvalue

def connecttomymailbox(a):
    myvalue=a
    date = (datetime.date.today() - datetime.timedelta(3)).strftime("%d-%b-%Y")
    mail = imaplib.IMAP4_SSL('imap.mail.yahoo.com',993)
    mail.login('Your_Account', 'Your_Password')
    mail.list()
    mail.select("inbox")
    result,data = mail.uid('search', None, "ALL")
    latest_email_uid = data[0].split()[-1]
    for i in range(0,myvalue):    
        latest_email_uid=int(latest_email_uid)-i
        latest_email_uid=str(latest_email_uid)
        result,data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        msubject=re.search(r'(Subject): (.*?) .*',raw_email,0)
        mfrom = re.search(r'(From): (.*?) .*',raw_email,0)
        try:
            print( mfrom.group() + "\t"  + msubject.group() )
        except AttributeError:
            msubject=re.search(r'(Subject:.*?) .*',raw_email,0)
            mfrom = re.search(r'(From:.*?) .*',raw_email,0)
            print( mfrom.group() + "\t"  + msubject.group() )
        
    
inp=givemeinput()
connecttomymailbox(inp)
msg()