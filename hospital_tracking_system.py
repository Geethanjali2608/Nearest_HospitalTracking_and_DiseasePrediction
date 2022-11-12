import mysql.connector

conn=mysql.connector.connect(host='localhost',password='geethu#2003',user='root',database='hospital_database')
if conn.is_connected():
  print("connection established...")
curs=conn.cursor()
while True:
 print("******************************************************************************")
 print("*    PROJECT TITLE:NEAREST HOSPITAL TRACKING AND DISEASE PREDICTION SYSTEM   *")
 print("******************************************************************************")
 print("*                                                                            *")
 print("*                        WELCOME NHTDP PORTAL                                *")
 print("*                                                                            *")
 print("******************************************************************************")
 print("*                                                                            *")
 print("*   We provide you the following services                                    *")
 print("*   1)Find nearest hospital from your location                               *")
 print("*   2)Predict diseases on the basis of symptoms                              *")
 print("*   3)Exit                                                                   *")
 print("******************************************************************************")
 op=int(input("Select your option:"))
 if(op==1):
    curs.execute("select distinct area from hospital_details")
    for i in curs:
      print(i)
    print("select area")
    area=input("enter area:")
    my_data=(area,)
    display="select * from hospital_details where area=%s"
    curs.execute(display,my_data)
    for i in curs:
      print(i)
    print()
    print()
    print()
    
    hosp=input("enter hospital preference:")
    my_data2=(hosp,)
    display="select * from hospital_details where hname=%s"
    curs.execute(display,my_data2)
    for i in curs:
        print(i)
    print()
    print()
    print("*******CHECK FOR AVAILABILITY OF SERVICE********")
    print("************************************************")
    
    display1="select dept from hospital_details where hname=%s"
    curs.execute(display1,my_data2)
    for i in curs:
        print(i)
    newdept=input("enter the dept:")
    dept=(newdept,)
    display=curs.execute('select * from hospital_details where dept like "/% %s /%"')
    curs.execute(display,dept)
    for i in curs:
      print(i)
    print("**************************************************")
    print("*         THANKS FOR USING OUR SERVICE           *")
    print("**************************************************")
    print("* DETAILS OF SELECTED HOSPITAL                   *")
    print("**************************************************")
    display="select * from hospital_details where hname=%s"
    curs.execute(display,my_data2)
    for i in curs:
        print(i)
 if(op==3):
    break

