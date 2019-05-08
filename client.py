from opcua import Client
import time
import cx_Oracle
import threading


#conn = cx_Oracle.connect('cjpt/123456@localhost/MES')#这里的顺序是用户名/密码@oracleserver的ip地址/数据库名字


docx=open('xout.txt','w')
docy=open('yout.txt','w')
url = "opc.tcp://172.30.128.211:4859"

client = Client(url)

client.connect()
print("Client Connected")

def save_timer():
    docx.close()
    docy.close()
while True:
    Mos1 = client.get_node("ns=2;i=2")
    Motorspeed1 = Mos1.get_value()
    print(Motorspeed1)
    print(Motorspeed1,file=docx)


    Mos2 = client.get_node("ns=2;i=3")
    Motorspeed2 = Mos2.get_value()
    print(Motorspeed2)
    print(Motorspeed2, file=docy)


    #Mos3 = client.get_node("ns=2;i=4")
    #Motorspeed3 = Mos3.get_value()
    #print(Motorspeed3)

    #Mos4 = client.get_node("ns=2;i=5")
    #Motorspeed4 = Mos4.get_value()
    #print(Motorspeed4)
    
    #TIME = client.get_node("ns=2;i=6")
    #TIME_Value = TIME.get_value()
    #print(TIME_Value)

    #cur = conn.cursor()
    #sql = "UPDATE REBOTSTATUS SET EX1='"+str(Motorspeed1)+"',EX2='"+str(Motorspeed2)+"',EX3='"+str(Motorspeed3)+"',EX4='"+str(Motorspeed4)+"',RBTIME='"+str(TIME_Value)+"' WHERE ID='c01f1a4a9f1f43b9bde4323db4bf1a1f'"
    #sql = "UPDATE REBOTSTATUS SET EX1='"+str(Motorspeed1)+"' WHERE ID='2771e686d16747b88176ef3faf0a70f3'"
    #cur.execute(sql)

    #conn.commit()
    # conn.close()
    time.sleep(0.7)
    timer = threading.Timer(40, save_timer)
    timer.start()

