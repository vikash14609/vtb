import urllib
import uuid
import socket
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
print("\033[1;31;40m Warning : THIS TOOL IS JUST FOR EDUCATIONAL PURPOSE AND TO CHECK WEBSITE SECURITY \033[0m")
print (color.BOLD + '' + color.END)
print("\033[1;31;40m             ₳ⱠɆӾ ₴₦ł₣₣ł₦₲ ₮ØØⱠ ₳₦Đ ฿ⱤɄ₮Ɇ₣ØⱤ₵ɆⱤ         \033[0m")

print("\033[1;31;40m             **************************      \033[0m")

password = int(input("Please enter your unique digit: "))
if password == 319720286:
    print(color.GREEN + "WELCOME NOOB TO CRACKING WORLD" + color.END)
else:
    print(color.GREEN + "YOY. I AM WATCHING YOU ASSHOLE" + color.END)
    exit()
host = socket.gethostname()
ip = socket.gethostbyname(host)
print("Your Computer IP Address is:" + ip)
print ("MAC address: " , end="") 

print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 

for ele in range(0,8*6,8)][::-1]))
print(color.GREEN + "MAC address did not match" + color.END)
print(color.GREEN + "Pay 8$ Bitcoins to Activate your MAC Address or Use on your Asus Max " + color.END)
print(color.GREEN + " 17tkaF1G1Ee4G8tVsmi39HKXbeWDgaKA26" + color.END)

 


