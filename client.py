import rpyc
from threading import Thread
import time

reach=0
net=None
input_var=None
user_name=None

def myprint(message):
	print message

def checkAndPrint(delay,dont):
        global reach
        global net
        global user_name
        global input_var
        while(1==1):
                length=conn.root.replyLength(1)
                if (input_var=="exit"):      
                        break
                while(reach<length):
                        net=conn.root.replyWith(reach)
                        reach=reach+1
                        print net
        
                        
conn = rpyc.connect("localhost",18888)
conn.root.setCallback(myprint)

user_name = raw_input("Please enter your name: ")
print "Type exit to leave the conversation"
conn.root.serverPrint(user_name)
reach = conn.root.replyLength(1)

try:
       t= Thread(target=checkAndPrint,args=(0,0))
       t.start()
       
       while(1==1):
               
                input_var = raw_input()
                if(input_var=="exit"):
                        time.sleep(1)
                        input_var = user_name + " has left the conversation" 
                        conn.root.setCallback(myprint)
                        conn.root.serverPrintMessage(input_var)
                        conn.root.serverExit(user_name)
                        break
                reach=reach+1
                input_var = user_name + ":" + input_var 
                conn.root.setCallback(myprint)
                conn.root.serverPrintMessage(input_var)
        	
except  Exception, errtxt:
        print "You have left the room"



        
