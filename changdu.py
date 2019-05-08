import math
point_a = input('please input point A coordinates: For Example:1,1\r\n')
point_b = input('please input point B coordinates: For Example:2,2\r\n')
#point_c = input('please input point C coordinates: For Example:1,3\r\n')
x1=float(point_a.split(',')[0])
y1=float(point_a.split(',')[1])
x2=float(point_b.split(',')[0])
y2=float(point_b.split(',')[1])
#x3=float(point_c.split(',')[0])
#y3=float(point_c.split(',')[1])
#根据a,b两点构造直线方程 AX+BY+C=0
A=y2-y1
B=x1-x2
C=x2*y1-x1*y2
#计算c点到直线距离
#distance=abs(A*x3+B*y3+C)/math.sqrt(A*A+B*B)-0.2
#print('The distance of Point C to the line AB is:%f'%distance)

while True:
    point_c = input('please input point C coordinates: For Example:1,3\r\n')
    x3 = float(point_c.split(',')[0])
    y3 = float(point_c.split(',')[1])
    distance = abs(A * x3 + B * y3 + C) / math.sqrt(A * A + B * B) - 0.2
    print('The distance of Point C to the line AB is:%f' % distance)

