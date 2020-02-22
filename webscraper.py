#! python3

import bs4, requests, smtplib
from personal import *

# ------------------------------------------------------------------

# used code from: https://www.codementor.io/@gergelykovcs/how-and-why-i-built-a-simple-web-scrapig-script-to-notify-us-about-our-favourite-food-fcrhuhn45

# Download page

# get data from webpage
getPage = requests.get('https://ara.kaist.ac.kr/board/BuySell/')
# validate if everything downloaded without issues,
# display error message & stops script if anything goes wrong
getPage.raise_for_status()

# Parse text for items
itemlist = bs4.BeautifulSoup(getPage.text, 'html.parser')
items = itemlist.select('.title')

the_one = '버즈'
flength = len(the_one)
available = False
for item in items:
    for i in range(len(item.text)):
        chunk = item.text[i:i+flength].lower()
        if chunk == the_one:
            available = True

if available:
    # send e-mail alert (use smtplib module & gmail accound)
    # print to console e-mail addresses where the alert was sent
    conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
    conn.ehlo() # call this to start the connection
    conn.starttls() # starts tls encryption. When we send our password it will be encrypted
    conn.login(myGmail, gmailAppPW)
    conn.sendmail(myGmail, toAddress, 'Subject: Galaxy Buds')
    conn.quit()
    print('Sent notification e-mails for the following recipients')
    for i in range(len(toAddress)):
        print(toAddress[i])
    print('')

else:
    # print to console that the food is not available
    print('Galaxy Buds are not available today')
