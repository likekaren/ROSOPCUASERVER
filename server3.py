
from opcua import Server
from random import randint
import datetime
import time
import cx_Oracle

conn = cx_Oracle.connect('cjpt/123456@localhost/MES')#这里的顺序是用户名/密码@oracleserver的ip地址/数据库名字
cur = conn.cursor()
sql = "SELECT * FROM DUAL"
cur.execute(sql)
cur.close()
conn.commit()
conn.close()


server =Server()

url = "opc.tcp://192.168.1.16:4841"
server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace,"Parameters")

Temp = Param.add_variable(addspace,"Temperature",0)
Press = Param.add_variable(addspace,"Pressure",0)
Pow = Param.add_variable(addspace,"Powernum",0)
Flo = Param.add_variable(addspace,"Flowspeed",0)
Winds = Param.add_variable(addspace,"Windspeed",0)
Time = Param.add_variable(addspace,"Time",0)

Temp.set_writable()
Press.set_writable()
Pow.set_writable()
Flo.set_writable()
Winds.set_writable()
Time.set_writable()

server.start()
print("Server started at {}".format(url))

while True:
    
    Temperature = randint(10,50)
    Pressure = randint(200,999)
    Powernum = randint(2,9)
    Flowspeed = randint(10,70)
    Windspeed = randint(120,200)
    TIME = datetime.datetime.now()
    
    print(Temperature,Pressure,Powernum,Flowspeed,Windspeed,TIME)
    
    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Pow.set_value(Powernum)
    Flo.set_value(Flowspeed)
    Winds.set_value(Windspeed)
    Time.set_value(TIME)
    
    time.sleep(2)