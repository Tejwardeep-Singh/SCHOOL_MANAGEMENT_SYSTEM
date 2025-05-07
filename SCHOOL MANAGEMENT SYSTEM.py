# SCHOOL MANAGEMENT SYSTEM 
# BY TEJWAR AND JASHAN

import mysql.connector
import datetime
from tabulate import tabulate

s = mysql.connector.connect( host = 'localhost' , user = 'root' , password = 'Tejwar' )
a = s.cursor()

# CREATING DATABASE

database = 'create database  if not exists school '
p = a.execute(database)
a.execute("use school")

# teacher table

a.execute('''create table if not exists teacher(
ref_id int primary key,
user_id int,
password int,
name varchar(20),
designation varchar(20),
age int,
basic_pay_statement int)''')

'''a.execute("insert into teacher  values(1,001,001,'BABLU MISHRA','PRINCIPLE',45,45000)")
a.execute("insert into teacher  values(2,002,002,'RAKESH KUMAR','SUBJECT TEACHER',37,30000)")
a.execute("insert into teacher  values(3,003,003,'JAYANT YADAV','SUBJECT TEACHER',25,30000)")
a.execute("insert into teacher  values(4,004,004,'GURMEET KAUR','SUBJECT TEACHER',30,30000)")
a.execute("insert into teacher  values(5,005,005,'MOHIT SHARMA','SUBJECT TEACHER',35,30000)")
a.execute("insert into teacher  values(6,006,006,'JASHANPREET SINGH','VICE PRINCIPLE',29,35000)")
a.execute("insert into teacher  values(7,007,007,'SHIVAM KUMAR','CO-ORDINATER',26,32000)")
a.execute("insert into teacher  values(8,008,008,'SAKSHAM DHILLON','PT TEACHER',27,30000)")
a.execute("insert into teacher  values(9,009,009,'NISHAN SINGH','SUBJECT TEACHER',40,30000)")
a.execute("insert into teacher  values(10,010,010,'SURSANGAM KAUR','RECEPTION',33,20000)")'''

# student table kindergarden

a.execute('''create table if not exists kindergarden(
ref_id int primary key,
admission_number int,
password int,
name varchar(20),
father_name varchar(20),
class varchar(20),
address varchar(20),
mobile int)''')

'''a.execute("insert into kindergarden values(001,101,001,'sukhchain singh','wariam singh','kindergarden','amritsar',9856)")
a.execute("insert into kindergarden values(002,102,002,'himmat singh','hardy sandhu','kindergarden','amritsar',9854)")
a.execute("insert into kindergarden values(003,103,003,'raju ghosla','ramesh ghosla','kindergarden','amritsar',9888)")
a.execute("insert into kindergarden values(004,104,004,'tanveer bhatia','rajesh bhatia','kindergarden','amritsar',9870)")
a.execute("insert into kindergarden values(005,105,005,'priya kumari','ram kumar','kindergarden','amritsar',9832)")'''

# student table class_1

a.execute('''create table if not exists class_1(
ref_id int primary key,
admission_number int,
password int,
name varchar(20),
father_name varchar(20),
class varchar(20),
address varchar(20),
mobile int)''')

'''a.execute("insert into class_1 values(006,106,006,'priya pandey','garry pandey','class_1','amritsar',9856)")
a.execute("insert into class_1 values(007,107,007,'preetam singh','ramandeep sandhu','class_1','amritsar',9854)")
a.execute("insert into class_1 values(008,108,008,'arjun ghosla','karan ghosla','class_1','amritsar',9888)")
a.execute("insert into class_1 values(009,109,009,'harmanpreet','varun singh','class_1','amritsar',9870)")
a.execute("insert into class_1 values(010,110,010,'tom boon','harry boon','class_1','amritsar',9832)")'''

# student table class_2

a.execute('''create table if not exists class_2(
ref_id int primary key,
admission_number int,
password int,
name varchar(20),
father_name varchar(20),
class varchar(20),
address varchar(20),
mobile int)''')

'''a.execute("insert into class_2 values(011,111,011,'mandeep singh','harwinder singh','class_2','amritsar',9856)")
a.execute("insert into class_2 values(012,112,012,'gurjant singh','garry pandey','class_2','amritsar',9856)")
a.execute("insert into class_2 values(013,113,013,'sonakshi','kuljinder singh','class_2','amritsar',9856)")
a.execute("insert into class_2 values(014,114,014,'arun sharma','varun sharma','class_2','amritsar',9856)")
a.execute("insert into class_2 values(015,115,015,'jami malhotra','vijay malhotra','class_2','amritsar',9856)")'''

# student table class_3

a.execute('''create table if not exists class_3(
ref_id int primary key,
admission_number int,
password int,
name varchar(20),
father_name varchar(20),
class varchar(20),
address varchar(20),
mobile int)''')

'''a.execute("insert into class_3 values(016,116,016,'priya pandey','garry pandey','class_3','amritsar',9856)")
a.execute("insert into class_3 values(017,117,017,'preetam singh','ramandeep sandhu','class_3','amritsar',9854)")
a.execute("insert into class_3 values(018,118,018,'arjun ghosla','karan ghosla','class_3','amritsar',9888)")
a.execute("insert into class_3 values(019,119,019,'harmanpreet','varun singh','class_3','amritsar',9870)")
a.execute("insert into class_3 values(020,120,020,'tom boon','harry boon','class_3','amritsar',9832)")'''

# student table class_4

a.execute('''create table if not exists class_4(
ref_id int primary key,
admission_number int,
password int,
name varchar(20),
father_name varchar(20),
class varchar(20),
address varchar(20),
mobile int)''')

'''a.execute("insert into class_4 values(021,121,021,'priya pandey','garry pandey','class_4','amritsar',9856)")
a.execute("insert into class_4 values(022,122,022,'preetam singh','ramandeep sandhu','class_4','amritsar',9854)")
a.execute("insert into class_4 values(023,123,023,'arjun ghosla','karan ghosla','class_4','amritsar',9888)")
a.execute("insert into class_4 values(024,124,024,'harmanpreet','varun singh','class_4','amritsar',9870)")
a.execute("insert into class_4 values(025,125,025,'tom boon','harry boon','class_4','amritsar',9832)")'''

# student table class_5

a.execute('''create table if not exists class_5(
ref_id int primary key,
admission_number int,
password int,
name varchar(20),
father_name varchar(20),
class varchar(20),
address varchar(20),
mobile int)''')

'''a.execute("insert into class_5 values(026,126,026,'mandeep singh','harwinder singh','class_5','amritsar',9856)")
a.execute("insert into class_5 values(027,127,027,'gurjant singh','garry pandey','class_5','amritsar',9856)")
a.execute("insert into class_5 values(028,128,028,'sonakshi','kuljinder singh','class_5','amritsar',9856)")
a.execute("insert into class_5 values(029,129,029,'arun sharma','varun sharma','class_5','amritsar',9856)")
a.execute("insert into class_5 values(030,130,030,'jami malhotra','vijay malhotra','class_5','amritsar',9856)")'''

# LEAVE REQUEST TABLE TEACHER

a.execute('''create table if not exists leave_request_teacher(
name varchar(20),
ref_id int primary key,
from_date date,
to_date date,
reason varchar(50),
status varchar(20) default'pending'
)''')

# LEAVE REQUEST TABLE STUDENT

a.execute('''create table if not exists leave_request_student(
name varchar(20),
ref_id int primary key,
from_date date,
to_date date,
reason varchar(50),
status varchar(20) default'pending'
)''')

# PAY ROLL TABLE

a.execute(''' create table if not exists payroll(
name varchar(20),
ref_id int primary key,
basic_salary int,
increm int,
tax int,
gross_amount int)''')

# CLASSES TABLE

a.execute(''' create table if not exists classes(
room_no int,
type varchar(20),
year_constructed date,
current_status varchar(20))''')

'''a.execute("insert into classes  values(1,'kindergarden','2001-06-15','occupied')")
a.execute("insert into classes  values(2,'class_1','2001-06-15','occupied')")
a.execute("insert into classes  values(3,'class_2','2001-06-15','occupied')")
a.execute("insert into classes  values(4,'class_3','2001-06-15','occupied')")
a.execute("insert into classes  values(5,'class_4','2001-06-15','occupied')")
a.execute("insert into classes  values(6,'class_5','2001-06-15','occupied')")
a.execute("insert into classes  values(7,'staff room','2001-06-15','occupied')")
a.execute("insert into classes  values(8,'principle office','2009-09-15','occupied')")
a.execute("insert into classes  values(9,'computer lab','2011-08-15','occupied')")
a.execute("insert into classes  values(10,'science lab','2015-03-12','occupied')")
a.execute("insert into classes  values(11,'sports room','2007-04-03','occupied')")
a.execute("insert into classes  values(12,'library','2008-06-18','occupied')")
a.execute("insert into classes  values(13,'kitchen','2002--08-27','occupied')")'''

# GRANT TABLE

a.execute(''' create table if not exists grants(
ref_id int primary key,
name varchar(20),
given_by varchar(20),
date date,
amount int,
purpose varchar(20)
)''')
        
# FFEEDBACK TABLE

a.execute(''' create table if not exists feedback(
name varchar(20),
city varchar(20),
feedback varchar(50)
)''')

# MAIN

while True:
    
    print('********************PIONEER SCHOOL********************')
    print('                                    AMRITSAR                                         ')
    print("^^^^^^^^^^^^EXPECT THE BEST^^^^^^^^^^^^")

    value = input(''' 1. HEAD LOGIN
2. STAFF LOGIN
3. STUDENT LOGIN
4. ABOUT SCHOOL
5. SHARE YOUR EXPERIENCE
6. EXIT''')


    # about school
    
    if value == '4':
        print(''' # HIGH TECH COMPUTER LABS
# LARGE CAMPUS
# OVERALL CHILD GROWTH
# MID DAY MEAL SCHEME
# FREE EDUCATION, BOOKS,FOOD,UNIFORMS FOR ALL STUDENTS
# REGULAR SPORTS EVENTS AND EXTRA CO CURRICULAR ACTIVITIES
# HIGHLY QUALIFIED TEACHING FACULTY
# SPECIAL PLAY ZONE FOR KINDERGARDEN
# VIDYA-PARK
# SMART CLASSES
    ''')

    # head login

    if value == "1":
        username = input("username")
        password = input("password")
        if username == 'sohan singh' and password == 'brownmunde':
            print("logged in successfully")
        else:
            print("wrong username or password")

        h_value = input('''1. staff information
2. student information
3. generate payroll
4. leave application request
5. grant information
6. classes
    ''')

    # staff information

        if h_value =='1':
            n = input('''1. see details all staff members
2. see details of particular staff member
3. add new staff member
4. delete record of a staff member
5. add new column in staff list
6. delete a column from staff list''')
            if n =='1':
                a.execute("select * from teacher")
                print(tabulate(a,headers=['REF_ID' ,'NAME','DESIGNATION','AGE','BASIC SALARY'],tablefmt = 'jira')) 
                data  = a.fetchall()
                for i in data:
                    print(i)
            if n =='2':
                n_ = int(input("enter ref_id of staff member"))
                execute="select * from teacher where ref_id ={}".format(n_)
                a.execute(execute)
                print(tabulate(a,headers=['REF_ID' ,'NAME','DESIGNATION','AGE','BASIC SALARY'],tablefmt = 'jira'))
                s.commit()
                data = a.fetchall()
                for i in data:
                    print(i)

            if n =='3':
                ref_id = input("ENTER REF_ID")
                name = input("ENTER THE NAME OF STAFF MEMBER")
                designation  = input("ENTER DESIGNATION")
                age = input("ENTER AGE")
                basic_salary = input("BASIC SALARY STATEMENT")
                execute="insert into teacher values({},'{}','{}',{},{})".format(ref_id,name,designation,age,basic_salary)
                a.execute(execute)
                s.commit()

                if n=='4':
                    d = input("enter field that is to be deleted")
                    ref_id = input("enter ref_id")
                    execute="delete {} from teacher where ref_id ={}".format(d,ref_id)
                    a.execute(execute)
                    s.commit()

                if n=='5':
                    c = input("ENTER NAME OF COLUMN TO BE ADDED")
                    t = input("ENTER TYPE OF COLUMN ( text,int )")
                    b = ''' alter table teacher
    add column {} {}'''
                    a.execute(b).format(c,t)
                    s.commit()


                if n=='6':
                    c = input("ENTER NAME OF COLUMN TO BE DELETED")
                    b = ''' alter table teacher
    drop column {}'''
                    a.execute(b).format(c)
                    s.commit()
    # student information

        if h_value =='2':
            v = input('''1. TO VIEW RECORDS ALL STUDENTS
2. TO VIEW LIST OF STUDENTS FROM A PARTICULAR CLASS
3. TO SEE A PARTICULAR STUDENT DETAIL
4. TO ENTER RECORDS OF  STUDENTS''')

            if v =='1':
                a.execute('select * from kindergarden')
                data = a.fetchall()
                for i in data:
                    print(i)
                a.execute('select * from class_1')
                data_1 = a.fetchall()
                for i in data_1:
                    print(i)
                a.execute('select * from class_2')
                data_2 = a.fetchall()
                for i in data_2:
                    print(i)
                a.execute('select * from class_3')
                data_3 = a.fetchall()
                for i in data_3:
                    print(i)
                a.execute('select * from class_4')
                data_4 = a.fetchall()
                for i in data_4:
                    print(i)
                a.execute('select * from class_5')
                data_5 = a.fetchall()
                for i in data_5:
                    print(i)

            if v=='2':
                t = input('ENTER CLASS')
                p="select * from {}".format(t) 
                a.execute(p)
                data = a.fetchall()
                for i in data:
                    print(i)

            if v=='3':
                t = input("ENTER CLASS")
                r = input("ENTER REF_ID")
                p ='select * from {} where ref_id={}'.format(t,r) 
                a.execute(p)
                data = a.fetchall()
                for i in data:
                    print(i)

            if v=='4':
                c = input("ENTER CLASS")
                r = input("ENTER REF_ID")
                m = input("ENTER ADMISSION NUMBER")
                n = input('ENTER NAME')
                f = input("ENTER FATHER NAME")
                l = input("ENTER CLASS (IN ROMAN LETTERS)")
                d = input("ENTER ADDRESS")
                b = input("ENTER MOBILE")

                I ="insert into {} values({},{},'{}','{}','{}','{}',{})".format(c,r,m,n,f,l,d,b)
                a.execute(I)
                s.commit()
                print("record saved successfully")

    # payroll

        if h_value=='3':
            k = input("name")
            l = input("ref_id")
            m = int(input("basic salary"))
            n = int(input("increment amount"))
            i = int(input("tax amount"))
            gross = m+n-i
            j = " insert into payroll values('{}',{},{},{},{},{})".format(k,l,m,n,i,gross)
            a.execute(j)
            s.commit()
            print("RECORD SAVED SUCCESSFULLY")

    # leave application of teachers

        if h_value=='4':
            n = input('''1. see leave requests
2. approve or reject request
    ''')
            if n=='1':
                p = 'select * from leave_request_teacher'
                a.execute(p)
                print(tabulate(a,headers=['NAME','REF_ID','FROM DATE','TO DATE','REASON','STATUS'],tablefmt='jira'))
                i = input("enter ref_id")
                j = input("approve or reject application")
                k='''update leave_request_teacher
    set status={} where ref_id={}'''.format(j,i)
                a.execute(k)
                s.commit()
                print("TASK COMPLETE")

            if n=='2':
                i = input("enter ref_id")
                j = input("approve or reject application")
                k='''update leave_request_teacher
    set status="{}" where ref_id={}'''.format(j,i)
                a.execute(k)
                s.commit()
                print("TASK COMPLETE")

    # grants

        if  h_value=='5':
            n = input('''1. all grants
2. filter by name
3. filter by amount''')
            
            if n=='1':
                u = 'select * from grant'
                a.execute(u)
                data = a.fetchall()
                for i in data:
                    print(i)

            if n=='2':
                k = input("ENTER NAME")
                u = 'select * from grants where name={}'.format(k)
                a.execute(u)
                data = a.fetchall()
                for i in data:
                    print(i)

            if n=='3':
                k = input("ENTER AMOUNT")
                u = 'select * from grants where amount={}'.format(k)
                a.execute(u)
                data = a.fetchall()
                for i in data:
                    print(i)

    # classes

        if h_value=='6':
            n = input('''1. see data
2. add new room
3. alter room details''')
            if n =='1':
                a.execute("select * from classes")
                data = a.fetchall()
                for i in data:
                    print(i)
            
            if n=='2':
                q = input("room number")
                r = input("type")
                s = input("year constructed")
                t = input("current status")
                u='insert into classes values({},"{}","{}","{}")'.format(q,r,s,t)
                a.execute(u)
                s.commit()
                print("NEW ROOM ADDED SUCCESSFULLY")
            
            if n=='3':
                p = input('''1. change status
2. change type
3. change year constructed''')
                if p=='1':
                    k = input("new status")
                    n = input("room number")
                    u = "update table classes set status={} where room_no = {}".format(n,k)
                    a.execute(u)
                    s.commit()
                    print("changes saved successfully")

                if p=='2':
                    k = input("new type")
                    n = input("room number")
                    u = "update table classes set type={} where room_no = {}".format(n,k)
                    a.execute(u)
                    s.commit()
                    print("changes saved successfully")

                if p=='3':
                    k = input("new type")
                    n = input("room number")
                    u = "update table classes set year_constructed={} where room_no = {}".format(n,k)
                    a.execute(u)
                    s.commit()
                    print("changes saved successfully")

    # STAFF LOGIN

    if value=='2':
        n = input("user name")
        p = input("password")
        print("WELCOME")
        l ="select * from teacher where user_id={}".format(n)
        a.execute(l)
        data=a.fetchall()
        for i in data:
            print(i)
        o = input('''1. VIEW PROFILE
2. LEAVE APPLICATION REQUEST TO HEAD
3. APPROVE LEAVE APPLICATION OF STUDENT
4. SALARY BILL DETAILS''')

        if o=='1':
            l ='select * from teacher where user_id={}'.format(n)
            a.execute(l)
            print(tabulate(a,headers=['REF_ID','USER_ID','PASSWORD','NAME','DESIGNATION','AGE','SALARY'],tablefmt='jira'))

        if o=='2':
            name = input('name')
            ref_id = input("ref_id")
            date1 = input("from date(yyyy:mm:dd)")
            date2 = input("to date(yyyy:mm:dd)")
            reason=input("enter reason")
            status = 'pending'
            v = 'insert into leave_request_teacher values("{}",{},"{}","{}","{}","{}")'.format(name,ref_id,date1,date2,reason,status)
            a.execute(v)
            s.commit()
            print("request sent successfully")


        if o=='3':
            n = input('''1. see leave requests
    2. approve or reject request
    ''')
            if n=='1':
                p = 'select * from leave_request_student'
                a.execute(p)
                print(tabulate(a,headers=['NAME','REF_ID','FROM DATE','TO DATE','REASON','STATUS'],tablefmt='jira'))
                i = input("enter ref_id")
                j = input("approve or reject application")
                k='''update leave_request_teacher
    set status={} where ref_id={}'''.format(j,i)
                a.execute(k)
                s.commit()
                print("TASK COMPLETE")

            if n=='2':
                i = input("enter ref_id")
                j = input("approve or reject application")
                k='''update leave_request_teacher
    set status="{}" where ref_id={}'''.format(j,i)
                a.execute(k)
                s.commit()
                print("TASK COMPLETE")

        if o=='4':
            n = input("ENTER USERNAME")
            u = 'select * from payroll where ref_id = {}'.format(n)
            a.execute(u)
            data = a.fetchall()
            for i in data:
                print(i)
    
    # Student login

    if value=='3':
        n = input("ENTER REF_ID")
        p = input("ENTER CLASS")

        q = input('''1. VIEW PROFILE
2. APPLY FOR LEAVE''')

        if q=='1':
            n = input("ENTER REF_ID")
            p = input("ENTER CLASS")
            u = 'select * from {} where ref_id = {}'.format(p,n)
            a.execute(u)
            data = a.fetchall()
            for i in data:
                print(i)

        if q=='2':
            name = input('name')
            ref_id = input("ref_id")
            date1 = input("from date(yyyy:mm:dd)")
            date2 = input("to date(yyyy:mm:dd)")
            reason=input("enter reason")
            status = 'pending'
            v = 'insert into leave_request_student values("{}",{},"{}","{}","{}","{}")'.format(name,ref_id,date1,date2,reason,status)
            a.execute(v)
            s.commit()
            print("request sent successfully")
        
    # feedback

    if value =='5':
        n = input('ENTER NAME')
        p = input("CITY")
        e = input("PLEASE SHARE YOUR EXPERIENCE OR FEEDBACK IN ABOUT 50 WORDS")
        u = 'insert into feedback values("{}","{}","{}")'.format(n,p,e)
        a.execute(u)
        s.commit()
        print("THANKS FOR YOUR VIEWS. YOUR RESPONSE HAS BEEN RECORDED")

    # exit
    
    if value == '6':
        print("THANKS FOR VISITING")
        quit()
            
            
            

