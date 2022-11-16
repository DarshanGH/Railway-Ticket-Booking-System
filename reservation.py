import pandas as pd 
import mysql.connector as sql

conn = sql.connect(host = 'Localhost',
               user = 'root',
               password = '',
               database='reservation')

if conn.is_connected():
    print('successfully connected')


def menu():
    print()
    print('***********************************************************************')
    print(             '      Railway Ticket Booking System      '                 )

    
    print('1. add new passenger detail')
    print('2. add new in trainsdetail')
    print('3. show all from trainsdetail')
    print('4. show all from passenger')
    print('5. show PNR Status')
    print('6. reservation of ticket')
    print('7. cancel ticket')



menu()



def addpassengers():
    c1 = conn.cursor()
    L = []
    pname = input('Enter your name: ')
    L.append(pname)
    age = input('Enter your age: ')
    L.append(age)
    trainno = input('Enter Train No.: ')
    L.append(trainno)
    noofpass = input('Enter No. of passengers: ')
    L.append(noofpass)
    cls = input('Enter class: ')
    L.append(cls)
    destination = input('Enter Destination: ')
    L.append(destination)
    amount = input('Enter Fare: ')
    L.append(amount)
    status = input('Enter status: ')
    L.append(status)
    pnrno = input('Enter PNR NO.: ')
    L.append(pnrno)
    pas = (L)
    sql = 'insert into passengers(pname,age,trainno,noofpass,cls,destination,amt,status,pnrno)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    c1.execute(sql,pas)
    conn.commit()
    print('Record of passenger inserted')
    df = pd.read_sql('select * from passengers',conn)
    print(df)






def addtrainsdetail():
    c1 = conn.cursor()
    df = pd.read_sql('select * from trainsdetail',conn)
    print(df)
    L = []
    tname = input('Enter train name: ')
    L.append(tname)
    tnum = input('Enter train number: ')
    L.append(tnum)
    source = input('Enter source of train: ')
    L.append(source)
    destination = input('Enter destination of train: ')
    L.append(destination)
    fare = input('Enter fare: ')
    L.append(fare)
    Ac1 = input('Enter no of seats for Ac1: ')
    L.append(Ac1)
    Ac2 = input('Enter no of seats for Ac2: ')
    L.append(Ac2)
    Ac3 = input('Enter no of seats for Ac3: ')
    L.append(Ac3)
    sleeper = input('Enter no of seats for sleeper: ')
    L.append(sleeper)
    f = (L)
    sql = 'insert into trainsdetail(tname,tnum,source,destination,fare,Ac1,Ac2,Ac3,sleeper)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    c1.execute(sql,f)
    conn.commit()
    print('Record inserted in trains detail')


def showtrainsdetail():
    print('all trains detail')
    df=pd.read_sql('select * from trainsdetail',conn)
    print(df)


def showpassengers():
    print('all passengers detail')
    df = pd.read_sql('select * from passengers',conn)
    print(df)


def displaypnrstatus():
    print('PNR status window')
    a = (input('Enter Train No.: '))
    sql = 'select pname,status from passengers where trainno=%s;'%(a,)
    df = pd.read_sql(sql,conn)
    print(df)


def ticketreservation():
    print('We have the following seat types for you: ')
    print('tname is 1 for Sewagram Express from Mumbai: ')
    print()
    print('1. 1Ac Rs.2800 per person')
    print('2. 2Ac Rs.1710 per person')
    print('3. 3Ac Rs.1210 per person')
    print('4. sleeper Rs.460 per person')
    print()
    print('tname is 2 for Goa Express from Mumbai: ')
    print()
    print('1. 1Ac Rs.2640 per person')
    print('2. 2Ac Rs.1575 per person')
    print('3. 3Ac Rs.1100 per person')
    print('4. sleeper Rs.400 per person')
    print()
    print('tname is 3 for Amritsar Express from Mumbai: ')
    print()
    print('1. 1Ac Rs.4000 per person')
    print('2. 2Ac Rs.3000 per person')
    print('3. 3Ac Rs.2000 per person')
    print('4. sleeper Rs.770 per person')
    print()
    print('tname is 4 for Rajdhani Express from Mumbai: ')
    print()
    print('1. 1Ac Rs.5200 per person')
    print('2. 2Ac Rs.4200 per person')
    print('3. 3Ac Rs.3000 per person')
    print('4. sleeper Rs.1200 per person')
    
    tname = (input('Enter your choice of train name please: '))
    print(tname)
    x = int(input('Enter your choice of ticket please: '))
    n = int(input('How many tickets you need: '))

    
    if x == 1:
        print('you have chosen 1Ac ticket')
        s=2640*n
    elif x == 2:
        print('you have chosen 2Ac ticket')
        s=1575*n
    elif x == 3:
        print('you have chosen 3Ac ticket')
        s=1100*n
    elif x == 4:
        print('you have chosen sleeper ticket')
        s=400*n
    else:
        print('invalid option')

        print('please choose a train')
    print("Your total ticket price is = ",s,"\n")

    




def cancelticket():
    print('before any changes in the status')
    df = pd.read_sql('select * from passengers',conn)
    print(df)
    mc = conn.cursor()
    mc.execute("update passengers set status='cancelled' where pnrno='G1001'")
    conn.commit()
    df = pd.read_sql('select * from passengers',conn)
    print(df)


choice=""
choice = int(input('Enter your choice: '))
if choice == 1:
    addpassengers()
elif choice == 2:
    addtrainsdetail()
elif choice == 3:
    showtrainsdetail()
elif choice == 4:
    showpassengers()
elif choice == 5:
    displaypnrstatus()
elif choice == 6:
    ticketreservation()
elif choice == 7: 
    cancelticket()
else:
    print('invalid option')