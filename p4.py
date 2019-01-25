  #  def start_new_thread(function, args, kwargs={}):
     #def start_new_thread(function, args, kwargs={}):
    #"""Dummy implementation of _thread.start_new_thread().

    #Compatibility is maintained by making sure that ``args`` is a
    #tuple and ``kwargs`` is a dictionary.  If an exception is raised
    #and it is SystemExit (which can be done by _thread.exit()) it is
    #caught and nothing is done; all other exceptions are printed out
    #by using traceback.print_exc().

    #If the executed function calls interrupt_main the KeyboardInterrupt will be
    #raised when the function returns.

    #"""
    #if type(args) != type(tuple()):
    #    raise TypeError("2nd arg must be a tuple")
    #if type(kwargs) != type(dict()):
    #    raise TypeError("3rd arg must be a dict")
    #global _main
    #_main = False
    #try:
     #   function(*args, **kwargs)
    #except SystemExit:
     #   pass
    #except:
     #   import traceback
     #   traceback.print_exc()
  #  _main = True
   # global _interrupt
   # if _interrupt:
   #     _interrupt = False
   #     raise KeyboardInterrupt
   # def exit():
   # """Dummy implementation of _thread.exit()."""
   # raise SystemExit
def checkers() :
 from sys import stdin
 import requests
 import uuid
 import socket
 from urllib.request import urlopen, Request
 class color:
     PURPLE = '\033[95m'
     CYAN = '\033[96m'
     DARKCYAN = '\033[36m'
     BLUE = '\033[94m'
     GREEN = '\033[92m'
     YELLOW = '\033[93m'
     RED = '\033[91m'
     BOLD = '\033[1m'
     UNDERLINE = '\033[4m'
     END = '\033[0m'
 f = open("i.txt")
 line = f.readline()
 totalLines = len(f.readlines())
 f.close()
 f = open("i.txt")
 lines = f.readlines()
 url = "https://mailsac.com/inbox/" + lines[0].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
   print (color.RED + "SCRAPPING " + color.END)
 else:
   print (color.RED + "SCRAPPED" + color.GREEN + lines[0] + color.END)

 url = "https://mailsac.com/inbox/" + lines[1].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
     print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[1] + color.END)
  
 url = "https://mailsac.com/inbox/" + lines[2].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[2] + color.END)

 url = "https://mailsac.com/inbox/" + lines[3].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[3] + color.END)

 url = "https://mailsac.com/inbox/" + lines[4].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[4] + color.END)


 url = "https://mailsac.com/inbox/" + lines[5].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[5] + color.END)



 url = "https://mailsac.com/inbox/" + lines[6].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[6] + color.END)



 url = "https://mailsac.com/inbox/" + lines[7].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[7] + color.END)



 url = "https://mailsac.com/inbox/" + lines[8].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[8] + color.END)



 url = "https://mailsac.com/inbox/" + lines[9].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[9] + color.END)



 url = "https://mailsac.com/inbox/" + lines[10].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[10] + color.END)



 url = "https://mailsac.com/inbox/" + lines[11].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[11] + color.END)



 url = "https://mailsac.com/inbox/" + lines[12].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[12] + color.END)


 url = "https://mailsac.com/inbox/" + lines[13].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[13] + color.END)



 url = "https://mailsac.com/inbox/" + lines[14].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[14] + color.END)



 url = "https://mailsac.com/inbox/" + lines[15].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[15] + color.END)




 url = "https://mailsac.com/inbox/" + lines[16].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[16] + color.END)



 url = "https://mailsac.com/inbox/" + lines[17].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[17] + color.END)



 url = "https://mailsac.com/inbox/" + lines[18].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[18] + color.END)




 url = "https://mailsac.com/inbox/" + lines[19].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[19] + color.END)



 url = "https://mailsac.com/inbox/" + lines[20].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[20] + color.END)



 url = "https://mailsac.com/inbox/" + lines[21].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[21] + color.END)



 url = "https://mailsac.com/inbox/" + lines[22].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[22] + color.END)



 url = "https://mailsac.com/inbox/" + lines[23].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[23] + color.END)



 url = "https://mailsac.com/inbox/" + lines[24].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[24] + color.END)



 url = "https://mailsac.com/inbox/" + lines[25].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print ('done')

def checkersamz() :
 from sys import stdin
 import requests
 import uuid
 import socket
 from urllib.request import urlopen, Request
 class color:
     PURPLE = '\033[95m'
     CYAN = '\033[96m'
     DARKCYAN = '\033[36m'
     BLUE = '\033[94m'
     GREEN = '\033[92m'
     YELLOW = '\033[93m'
     RED = '\033[91m'
     BOLD = '\033[1m'
     UNDERLINE = '\033[4m'
     END = '\033[0m'
 f = open("i.txt")
 line = f.readline()
 totalLines = len(f.readlines())
 f.close()
 f = open("i.txt")
 lines = f.readlines()
 url = "https://mailsac.com/inbox/" + lines[0].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
   print (color.RED + "SCRAPPING " + color.END)
 else:
   print (color.RED + "SCRAPPED" + color.GREEN + lines[0] + color.END)

 url = "https://mailsac.com/inbox/" + lines[1].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
     print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[1] + color.END)
  
 url = "https://mailsac.com/inbox/" + lines[2].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[2] + color.END)

 url = "https://mailsac.com/inbox/" + lines[3].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[3] + color.END)

 url = "https://mailsac.com/inbox/" + lines[4].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[4] + color.END)


 url = "https://mailsac.com/inbox/" + lines[5].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[5] + color.END)



 url = "https://mailsac.com/inbox/" + lines[6].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[6] + color.END)



 url = "https://mailsac.com/inbox/" + lines[7].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[7] + color.END)



 url = "https://mailsac.com/inbox/" + lines[8].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[8] + color.END)



 url = "https://mailsac.com/inbox/" + lines[9].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[9] + color.END)



 url = "https://mailsac.com/inbox/" + lines[10].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[10] + color.END)



 url = "https://mailsac.com/inbox/" + lines[11].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[11] + color.END)



 url = "https://mailsac.com/inbox/" + lines[12].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[12] + color.END)


 url = "https://mailsac.com/inbox/" + lines[13].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[13] + color.END)



 url = "https://mailsac.com/inbox/" + lines[14].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[14] + color.END)



 url = "https://mailsac.com/inbox/" + lines[15].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[15] + color.END)




 url = "https://mailsac.com/inbox/" + lines[16].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[16] + color.END)



 url = "https://mailsac.com/inbox/" + lines[17].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[17] + color.END)



 url = "https://mailsac.com/inbox/" + lines[18].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[18] + color.END)




 url = "https://mailsac.com/inbox/" + lines[19].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[19] + color.END)



 url = "https://mailsac.com/inbox/" + lines[20].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[20] + color.END)



 url = "https://mailsac.com/inbox/" + lines[21].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[21] + color.END)



 url = "https://mailsac.com/inbox/" + lines[22].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[22] + color.END)



 url = "https://mailsac.com/inbox/" + lines[23].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[23] + color.END)



 url = "https://mailsac.com/inbox/" + lines[24].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[24] + color.END)



 url = "https://mailsac.com/inbox/" + lines[25].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print ('done')