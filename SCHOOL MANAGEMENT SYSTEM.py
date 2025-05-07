# SCHOOL MANAGEMENT SYSTEM 
# BY TEJWAR AND JASHAN

import mysql.connector
import datetime
from tabulate import tabulate

s = mysql.connector.connect( host = 'localhost' , user = 'root' , password = 'root' )
a = s.cursor()

# CREATING DATABASE>>>>>>>>>>>>>>>>>>>>>>>>

database = 'create database  if not exists school '
p = a.execute(database)
a.execute("use school")

# teacher table>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

a.execute('''create table if not exists teacher(
ref_id int primary key,
user_id int,
password int,
name varchar(20),
designation varchar(20),
age int,
basic_pay_statement int)''')

'''a.execute("insert into teacher  values(1,001,001,'SAKSHAM BHASKAR','PRINCIPLE',35,45000)")
a.execute("insert into teacher  values(2,002,002,'RAKESH KUMAR','SUBJECT TEACHER',37,30000)")
a.execute("insert into teacher  values(3,003,003,'JAYANT YADAV','SUBJECT TEACHER',25,30000)")
a.execute("insert into teacher  values(4,004,004,'GURMEET KAUR','SUBJECT TEACHER',30,30000)")
a.execute("insert into teacher  values(5,005,005,'MOHIT SHARMA','SUBJECT TEACHER',35,30000)")
a.execute("insert into teacher  values(6,006,006,'JASHANPREET SINGH','VICE PRINCIPLE',29,35000)")
a.execute("insert into teacher  values(7,007,007,'SHIVAM KUMAR','CO-ORDINATER',26,32000)")
a.execute("insert into teacher  values(8,008,008,'BABLU MISHRA','PT TEACHER',27,30000)")
a.execute("insert into teacher  values(9,009,009,'NISHAN SINGH','SUBJECT TEACHER',40,30000)")
a.execute("insert into teacher  values(10,010,010,'SURSANGAM KAUR','RECEPTION',33,20000)")'''

# student table kindergarden>>>>>>>>>>>>>>>>>>>>>>>>

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

# student table class_1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

# student table class_2>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

# student table class_3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

# student table class_4>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

# student table class_5>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

# LEAVE REQUEST TABLE TEACHER>>>>>>>>>>>>>>>>>>>>>>>>>>

a.execute('''create table if not exists leave_request_teacher(
name varchar(20),
ref_id int primary key,
from_date date,
to_date date,
reason varchar(50),
status varchar(20) default'pending'
)''')

# LEAVE REQUEST TABLE STUDENT>>>>>>>>>>>>>>>>>>>>>>>>>>

a.execute('''create table if not exists leave_request_student(
name varchar(20),
ref_id int primary key,
from_date date,
to_date date,
reason varchar(50),
status varchar(20) default'pending'
)''')

# PAY ROLL TABLE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

a.execute(''' create table if not exists payroll(
name varchar(20),
ref_id int primary key,
basic_salary int,
increm int,
tax int,
gross_amount int)''')

# CLASSES TABLE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

# GRANT TABLE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

a.execute(''' create table if not exists grants(
ref_id int primary key,
name varchar(20),
given_by varchar(20),
date date,
amount int,
purpose varchar(20)
)''')
        
# FEEDBACK TABLE>>>>>>>>>>>>>>>>>>>>>>>>>>>>

a.execute(''' create table if not exists feedback(
name varchar(20),
city varchar(20),
feedback varchar(50)
)''')

# event table>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

a.execute('''create table if not exists event(
s_no int,
name varchar(20),
date date
)''')

# CBSE NEWS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
a.execute('''create table if not exists cbse_news(
s_no int,
news varchar(50),
date date
)''')

# GOVERNMENT POLICIES>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
a.execute('''create table if not exists government_policies(
s_no int,
news varchar(50),
date date
)''')

# FAQ'S>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
a.execute('''create table if not exists faq(
s_no int,
question varchar(50),
date date,
status varchar(20)   
)''')

# ADMISSION FORMS   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
a.execute('''create table if not exists admission_forms(
name varchar(30),
class int,
father varchar(20),
mobile int,
status varchar(20)   
)''')

# BILLS
a.execute('''create table if not exists bills(
s_no int,
name varchar(30),
amount int,
remarks varchar(50)   
)''')

# MAIN>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

while True:
    
    print('********************PIONEER SCHOOL********************')
    print('                                    AMRITSAR                                         ')
    print("^^^^^^^^^^^^EXPECT THE BEST^^^^^^^^^^^^")

    value = input(''' 1. HEAD LOGIN
2. STAFF LOGIN
3. STUDENT LOGIN
4. ABOUT SCHOOL INFRASTRUCTURE
5. SHARE YOUR EXPERIENCE
6. CONTACT
7. SCHOOL CALENDER 
8. EVENTS
9. CBSE NEWS
10. GOVERNMENT POLICIES
11. FEE STRUCTURE
12. FAQ'S
13. PRINCIPLE'S DESK
14. DIRECTER'S DESK
15. CHALLENGE YOURSELF 
16. ADMISSION  
17. EXIT''')
    
# head login>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if value=='1':
        u = input("username").lower()        
        p = input("password").lower()
        if u=='sohan singh' and p == 'school123':
            print('WELCOME')
            h_value= input('''1. staff information
2. student information
3. generate payroll
4. leave application request
5. grant information
6. classes
7. FAQ'S
8. admission forms
9. school bills
            ''')

    # school bills
            if h_value=='9':
                i = input('''1. to see all bills
2. to add new bills
3. to delete previous bills''')
                
                if i =='1':
                    o = 'select * from bills'
                    a.execute(o)
                    data = a.fetchall()
                    for i in data:
                        print(i)
               
    # admission forms
            if h_value=='8':
                o = input('''1. see forms
2. approve or reject form''')
                if o=='1':
                    a.execute("select * from admission_forms")
                    data = a.fetchall()
                    for i in data:
                        print(i)
                
                if o=='2':
                    n = input('name')
                    p = input("accept of reject")
                    k = '''update table admission_forms
    set status='{}' where name ="{}" '''.format(n,p)
                    a.execute(k)
                    s.commit()
                    print("changes saved succesfully")

    # faq's
            if h_value== '7':
                o = input('''1. see faq's
2. update status of faq's''')

                if o =='1':
                        a.execute('seldct * from faq')
                        data = a.fetchall()
                        for i in data:
                            print(i)
                
                if o=='2':
                    l = input("enter s.no")
                    k = input("enter status to be added")
                    u = '''update table faq
                    set status = '{}' where s.no = {}'''.format(k,l)
                    a.execute(u)
                    s.commit()
                    print("changes saved")
                

    # staff information>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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
    # student information>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            if h_value =='2':
                v = input('''1. TO VIEW RECORDS ALL STUDENTS
2. TO VIEW LIST OF STUDENTS FROM A PARTICULAR CLASS
3. TO SEE A PARTICULAR STUDENT DETAIL
4. TO ENTER RECORDS OF  STUDENTS
5. TO CHANGE RECORD OF STUDENTS
    ''')

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
                
                if v=='5':
                    u= input('''1. change name
2. change mobile
3. change address''')

                    if u=='1':
                        n = input("enter ref_id")
                        c = input("enter class")
                        na = input("enter new name")
                        t =  '''update table class_{}
                        set name={} where ref_is = {}'''.format(c,na,n)
                        a.execute(t)
                        s.commit()
                        print("changes saved")
                    
                    if u=='2':
                        n = input("enter ref_id")
                        c = input("enter class")
                        na = input("enter new mobile")
                        t =  '''update table class_{}
                        set mobile={} where ref_is = {}'''.format(c,na,n)
                        a.execute(t)
                        s.commit()
                        print("changes saved")

                    if u=='3':
                        n = input("enter ref_id")
                        c = input("enter class")
                        na = input("enter new address")
                        t = '''update table class_{}
                        set address={} where ref_is = {}'''.format(c,na,n)
                        a.execute(t)
                        s.commit()
                        print("changes saved")

    # payroll>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

    # leave application of teachers>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

    # grants>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            if  h_value=='5':
                n = input('''1. all grants
2. filter by name
3. filter by amount''')
                
                if n=='1':
                    u = 'select * from grants'
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

    # classes>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

        else:
            print("invalid username or password")
            quit()

# campus
        if value == '4':
            o= input(''' 1. HIGH TECH COMPUTER LABS
2. LARGE CAMPUS
3. OVERALL CHILD GROWTH
4. MID DAY MEAL SCHEME
5. FREE EDUCATION, BOOKS,FOOD,UNIFORMS FOR ALL STUDENTS
6. REGULAR SPORTS EVENTS AND EXTRA CO CURRICULAR ACTIVITIES
7. HIGHLY QUALIFIED TEACHING FACULTY
8. SPECIAL PLAY ZONE FOR KINDERGARDEN
9. VIDYA-PARK
10. SMART CLASSES
    ''')
            if o=='1':
                print(''' # WELL DEVELOPED AC ROOMS
# LATEST TECHNOLOGY EQUIPMENTS
# TOP FACULTY
# INTERNET CONNECTIVITY''')
                
                if o=='2':
                    print('''# EXPANDED UPTO AREA OF 4 ACRES
# HUGE BUILDING
# ALL SAFTETY MEASURES FOLLOWED''')
                
                if o=='3':
                    print('''# WE FOCUS ON OVERALL GROWTH OF CHILD ALONG WITH ACADEMIC GROWTH
# REGULAR CO-CURRICULAR ACTIVITIES ARE CONDUCTED
# SKILL DEVELOPMENT SESSIONS ARE REGULARY CONDUCTED
# MORE EMPHASIS ARE LAID ON PRACTICAL LEARNING ''')
                
                if o=='4':
                    print('''# ALONG WITH AFFORDABLE EDUCATION OUR SCHOOL SERVES FREE MEAL TO KINDERGARDEN CHILDREN
# STUDENTS OF CLASS 1 AND 2 ALSO GET FREE MEAL
# ALL THE HYGIENE MEASURES ARE TAKEN INTO ACCOUNT WHILE PREPARING FOOD FOR CHILDREN
# THE MENU FOR MEAL IS DIFFERENT FOR EACH DAY OF WEEK (i.e 6 menus for 6 days)
# STUDENTS ARE ALSO TAUGHT ABOUT BENEFITS OF GREEN VEGETABLES AND HYGIENE FOOD WHILE EATING ''')
                
                if o=='5':
                    print('''# AS PER GIOVERNMENT GUIDLINES NO FEES IS CHARGED ON THE CHILDREN BELOW CLASS 5
# THEY ARE PROVIDED WITH FREE FOOD, EDUCATION,UNIFORM BOOKS ETC.
# MEDICATION IS ALSO FREE IN CASE OF HEALTH EMERGENCY IN SCHOOL HOURS''')
                
                if o=='6':
                    print('''# REGULAR ACTIVITIES ARE ARRANGED FOR CHILDREN TO BOOST THEIR TALENT AND MOTIVATION
# SPORTS ARE IMPORTANT PART OF STUDENT'S LIFE, THAT IS WHY OUR SCHOOL LAY EMPHASIS ON SPORTS AND OUR CHILDREN SHINE IN THE TOURNAMENTS
# WE HAVE VAST VARIETY OF SPORTS AND FULL EQUIPMENTS TOO
# STUDENTS CAN TAKE ANY SPORT AND LEARN IT UNDER SPECIALISED COACH''')
                
                if o=='7 ':
                    print('''# TOP TEACHING FACULTIES ARE THERE IN OUR SCHOOL
# WE HAVE A COMBINATION OF EXPERIENCED AND HIGHLY PASSIONATE YOUNG TEACHERS 
# WE BELIEVE THAT A GOOD TEACHER MAKES SUBJECT EASIER FOR THE CHILDREN, THAT IS WHY WE SEARCH FOR THOSE TEACHERS WHO CAN FULFILL THESE DEMANDS. ''')
                
                if o=='8':
                    print('''# SPECIAL PLAY AREA FOR KIDS
# BOTH INDOOR AND OUTDOOR FACILITIES ARE THERE
# CHILDREN OF KINDERGARDEN ARE GIVEN DEDICATED PERIODS FOR PLAY AND FUN ''')
                
                if o=='9':
                    print('''# WE ALSO HAVE A SPECIAL PLAY AREA FOR CHILDREN OF KINDERGARDEN CHILDREN
# A SPECIAL OUTDOOR AREA WHERE THE CHILDREN CAN LEARN VARIETY OF THINGS LIKE SHAPES, SPORTS AND MANY MORE
# WE CALL THE PARKS VIDYYA-PARK
# THIS IS GOVERNMENT'S INITIATIVE TO TEACH STUDENTS LESSONS WITH FUN''')
                
                if o=='10':
                    print('''# SMART BOARDS ARE INSTALLED IN EVERY CLASSROOM
# STUDENTS GET SPECIALISED VISUAL LEARNING
# THEY GET CRYSTAL CLEAR KNOWLEDGE OF EVERY TOPIC OF THE SUBJECT''')

    if value=='8':
        a.execute('select * from calender')
        print(tabulate(a,headers=['NAME','DATE'],tablefmt = 'jira'))
        data  = a.fetchall()
        for i in data:
            print(i)

    if value == '6':
        print('''email-pioneerschool@gmail.com
        mobile - 9856xxxx23
        twitter - xyz
        instagram = pioneerschool''')

    if value=='7':
        print('''
JAN******************************

1 Jan	Sunday	New Year's Day	Restricted Holiday
14 Jan	Saturday	Makar Sankranti	Restricted Holiday
14 Jan	Saturday	Lohri	Observance
15 Jan	Sunday	Pongal	Restricted Holiday
22 Jan	Sunday	Lunar New Year	Observance
26 Jan	Thursday	Republic Day	Gazetted Holiday
26 Jan	Thursday	Vasant Panchami	Restricted Holiday''')
        print('''
FEB******************************

5 Feb	Sunday	Guru Ravidas Jayanti	Restricted Holiday
5 Feb	Sunday	Hazarat Ali's Birthday	Restricted Holiday
14 Feb	Tuesday	Valentine's Day	Observance
15 Feb	Wednesday	Maharishi Dayanand Saraswati Jayanti	Restricted Holiday
18 Feb	Saturday	Maha Shivaratri/Shivaratri	Restricted Holiday
19 Feb	Sunday	Shivaji Jayanti	Restricted Holiday''')
        print('''
MARCH******************************

7 Mar	Tuesday	Dolyatra	Restricted Holiday
7 Mar	Tuesday	Holika Dahana	Restricted Holiday
8 Mar	Wednesday	Holi	Gazetted Holiday
21 Mar	Tuesday	March Equinox	Season
22 Mar	Wednesday	Chaitra Sukhladi	Restricted Holiday
22 Mar	Wednesday	Ugadi	Restricted Holiday
22 Mar	Wednesday	Gudi Padwa	Restricted Holiday
24 Mar	Friday	Ramadan Start	Observance
30 Mar	Thursday	Rama Navami	Gazetted Holiday''')    
        print('''
APRIL******************************

4 Apr	Tuesday	Mahavir Jayanti	Gazetted Holiday
6 Apr	Thursday	First day of Passover	Observance
6 Apr	Thursday	Maundy Thursday	Observance, Christian
7 Apr	Friday	Good Friday	Gazetted Holiday
9 Apr	Sunday	Easter Day	Restricted Holiday
14 Apr	Friday	Vaisakhi	Restricted Holiday
14 Apr	Friday	Ambedkar Jayanti	Central Government Holiday
14 Apr	Friday	Ambedkar Jayanti	Observance
15 Apr	Saturday	Mesadi / Vaisakhadi	Restricted Holiday
21 Apr	Friday	Jamat Ul-Vida (Tentative Date)	Restricted Holiday
22 Apr	Saturday	Ramzan Id/Eid-ul-Fitar	Gazetted Holiday
22 Apr	Saturday	Ramzan Id/Eid-ul-Fitar	Muslim, Common local holiday''')
        print('''
MAY******************************

1 May	Monday	International Worker's Day	Observance
5 May	Friday	Buddha Purnima/Vesak	Gazetted Holiday
9 May	Tuesday	Birthday of Rabindranath	Restricted Holiday
14 May	Sunday	Mother's Day	Observance''')
        print('''
JUNE******************************

18 Jun	Sunday	Father's Day	Observance
20 Jun	Tuesday	Rath Yatra	Restricted Holiday
21 Jun	Wednesday	June Solstice	Season
29 Jun	Thursday	Bakrid/Eid ul-Adha	Gazetted Holiday
2-30 JUN SUMMER VACATIONS''')
        print('''
JULY******************************

3 Jul	Monday	Guru Purnima	Observance
29 Jul	Saturday	Muharram/Ashura (Tentative Date)	Gazetted Holiday
1-19 Jul Summer vacations''')
        print('''
AUGUST******************************

6 Aug	Sunday	Friendship Day	Observance
15 Aug	Tuesday	Independence Day	Gazetted Holiday
16 Aug	Wednesday	Parsi New Year	Restricted Holiday
20 Aug	Sunday	Vinayaka Chathurthi	Restricted Holiday
29 Aug	Tuesday	Onam	Restricted Holiday
30 Aug	Wednesday	Raksha Bandhan (Rakhi)	Restricted Holiday''')
        print('''
SEPTEMBER******************************

6 Sep	Wednesday	Janmashtami (Smarta)	Restricted Holiday
7 Sep	Thursday	Janmashtami	Gazetted Holiday
19 Sep	Tuesday	Ganesh Chaturthi/Vinayaka Chaturthi	Restricted Holiday
23 Sep	Saturday	September Equinox	Season
28 Sep	Thursday	Milad un-Nabi/Id-e-Milad (Tentative Date)	Gazetted Holiday''')
        print('''
OCTOBER******************************

2 Oct	Monday	Mahatma Gandhi Jayanti	Gazetted Holiday
15 Oct	Sunday	First Day of Sharad Navratri	Observance, Hinduism
20 Oct	Friday	First Day of Durga Puja Festivities	Observance, Hinduism
21 Oct	Saturday	Maha Saptami	Restricted Holiday
22 Oct	Sunday	Maha Ashtami	Restricted Holiday
23 Oct	Monday	Maha Navami	Restricted Holiday
24 Oct	Tuesday	Dussehra	Gazetted Holiday
28 Oct	Saturday	Maharishi Valmiki Jayanti	Restricted Holiday
31 Oct	Tuesday	Halloween	Observance''')
        print('''
NOVEMBER******************************

1 Nov	Wednesday	Karaka Chaturthi (Karva Chauth)	Restricted Holiday
12 Nov	Sunday	Naraka Chaturdasi	Restricted Holiday
12 Nov	Sunday	Diwali/Deepavali	Gazetted Holiday
13 Nov	Monday	Govardhan Puja	Restricted Holiday
15 Nov	Wednesday	Bhai Duj	Restricted Holiday
19 Nov	Sunday	Chhat Puja (Pratihar Sashthi/Surya Sashthi)	Restricted Holiday
24 Nov	Friday	Guru Tegh Bahadur's Martyrdom Day	Restricted Holiday
27 Nov	Monday	Guru Nanak Jayanti	Gazetted Holiday''')
        print('''
DECEMBER ******************************

8 Dec	Friday	First Day of Hanukkah	Observance
15 Dec	Friday	Last day of Hanukkah	Observance
22 Dec	Friday	December Solstice	Season
24 Dec	Sunday	Christmas Eve	Restricted Holiday
25 Dec	Monday	Christmas	Gazetted Holiday
31 Dec	Sunday	New Year's Eve	Observance
25-31 Dec Winter Vacations
****************************************
''')
        
# STAFF LOGIN>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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
4. SALARY BILL DETAILS
5. STUDENT DETAILS''')

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
        
        if o=='5':
            if h_value =='2':
                v = input('''1. TO VIEW RECORDS ALL STUDENTS
2. TO VIEW LIST OF STUDENTS FROM A PARTICULAR CLASS
3. TO SEE A PARTICULAR STUDENT DETAIL
4. TO ENTER RECORDS OF  STUDENTS
5. TO CHANGE RECORD OF STUDENTS
    ''')

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
                
                if v=='5':
                    u= input('''1. change name
2. change mobile
3. change address''')

                    if u=='1':
                        n = input("enter ref_id")
                        c = input("enter class")
                        na = input("enter new name")
                        t =  '''update table class_{}
                        set name={} where ref_is = {}'''.format(c,na,n)
                        a.execute(t)
                        s.commit()
                        print("changes saved")
                    
                    if u=='2':
                        n = input("enter ref_id")
                        c = input("enter class")
                        na = input("enter new mobile")
                        t =  '''update table class_{}
                        set mobile={} where ref_is = {}'''.format(c,na,n)
                        a.execute(t)
                        s.commit()
                        print("changes saved")

                    if u=='3':
                        n = input("enter ref_id")
                        c = input("enter class")
                        na = input("enter new address")
                        t = '''update table class_{}
                        set address={} where ref_is = {}'''.format(c,na,n)
                        a.execute(t)
                        s.commit()
                        print("changes saved")
    
# Student login>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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
        
# feedback>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if value =='5':
        n = input('ENTER NAME')
        p = input("CITY")
        e = input("PLEASE SHARE YOUR EXPERIENCE OR FEEDBACK IN ABOUT 50 WORDS")
        u = 'insert into feedback values("{}","{}","{}")'.format(n,p,e)
        a.execute(u)
        s.commit()
        print("THANKS FOR YOUR VIEWS. YOUR RESPONSE HAS BEEN RECORDED")

# cbse news>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if value=='9':
        a.execute("select * from cbse_news")
        data = a.fetchall()
        for i in data:
            print(i)

# government policies>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if value=='10':
        a.execute("select * from government_policies")
        data = a.fetchall()
        for i in data:
            print(i)

# fee structure>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if value == '11':
        print('''class KINDERGARDEN - 500/month
class 1            - 890/month
class-2            - 900/month
class-3            - 900/month
class-4            - 1500/month
class-5            - 1500/month
class-6            - 1750/month
class-7            - 2150/month
class-8            - 2250/month
class-9            - 2300/month
class-10           - 2500/month
class-11           - 3200/month
class-12           - 3200/month''')

        print("EXTRA CHARGES LIKE SPORTS, VAN, UNIFORM ARE APPLICABLE")

# faq's>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if value=='12':
        a.execute("select * from faq")
        data = a.fetchall()
        for i in data:
            print(i)

# principle's desk>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    if  value == '13':
        print('''Principal’s Desk

A strong building requires a strong basement.Keeping this dictim in mind, 
school has planned for a road Map, where the school can give the best to 
the society. The students as future citizen are equipped with all the expertise
which is pumped in them by our dedicated staff through hard work and planning. 
An institution becomes a place of respect and worship through the efficiency, 
correctness and dedication of its inmates or staff. Regular, interaction and in 
touch with modern concept of knowledge help the staff to give the best to their 
students, so that the institution while earning the name and fame through its 
students out put, also serves the nation in its path toward development

R.K. Bhaskar
 ''')

# directer's desk>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    if  value == '14':
        print('''The modern world is a Competitive world and require the
products which are compatible with its diversity and excellence.
Keeping these in mind, the Pioneer School plans its pedagogy.
Besides the usual syllabi effective planning is done to chisel the 
students in their best potential not only in academic but also in other 
activities. Every effort is made by my dedicated staff to make the end
product a blend of educational physical and cultural expert, Keeping 
in mind the mid path of Modernity and tradition. I pray to the mighty 
to give the best to our institution, so that the student coming out of 
our institution are filled with Uniqueness.

Rashi Samra ''')

# quize>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    if  value == '15':
        print('''WELCOME TO THE QUIZE GAME''')
        value = int(input('''PRESS -
1. GK TEST
2. SCIENCE TEST
3. CURRENT AFFAIRS
4. COMMON SENSE
5. HISTORY
6. POLITY
7. GEOGRAPHY
8. ECONOMICS
9. ENGLISH
10. MATHS'''))

        # gk

        if value==1:
            score = 0
            print("THERE WILL BE 5 QUESTIONS AND EACH CORRECT ANSWER WILL GIVE YOU 5 POINTS AND WRONG ANSWER WILL DEDUCT 1 POINT")
            value = input("ARE YOU READY(PRESS ANY KEY TO CONTINUE)")
            answer = input("1. Capital of Bihar ?").lower()
            if answer=='patna':
                score +=5
            else:
                score -=1
            answer = input("2. Which team won maximum number of FIH HOCKEY WORLD CUPS ?").lower()
            if answer=='pakistan':
                score +=5
            else:
                score -=1
            answer = input("3. SHAPE OF EARTH ?").lower()
            if answer=='geoid':
                score +=5
            else:
                score -=1
            answer = input("4. NAME OF INDIA'S FIRST SATELLITE ?").lower()
            if answer=='aryabhatta':
                score +=5
            else:
                score -=1
            answer = input("5.SUPREME COMMANDER OF INDIAN MILITARY IS ____ ?").lower()
            if answer=='president':
                score +=5
            else:
                score -=1
            final = input("PRESS ANY KEY TO SEE FINAL SCORE")
            print("CONGRATS YOU HAVE SCORED " + str(score) + " out of 25 points")
        # science

        elif value ==2:
            score = 0
            print("THERE WILL BE 5 QUESTIONS AND EACH CORRECT ANSWER WILL GIVE YOU 5 POINTS AND WRONG ANSWER WILL DEDUCT 1 POINT")
            value = input("ARE YOU READY(PRESS ANY KEY TO CONTINUE)")
            answer = input("1. Color of copper sulphate solution ?").lower()
            if answer=='blue':
                score +=5
            else:
                score -=1
            answer = input("2. unsaturated carbon compounds releases flames of color ____ ?").lower()
            if answer=='yellow':
                score +=5
            else:
                score -=1
            answer = input("3.value of gravity increases/decreases with increase in height ?").lower()
            if answer=='decreases':
                score +=5
            else:
                score -=1
            answer = input("4. which is more elastic steel or rubber ?").lower()
            if answer=='steel':
                score +=5
            else:
                score -=1
            answer = input("5.nitrogen shows maximum covalency of___ ?").lower()
            if answer=='4':
                score +=5
            else:
                score -=1
            final = input("PRESS ANY KEY TO SEE FINAL SCORE")
            print("CONGRATS YOU HAVE SCORED " + str(score) + " out of 25 points")

        # current affairs
        elif value==3:
            o = input('''1. set 1
2. set 2 
3. set 3 ''')
            if o =='1':
                score = 0
                print("THERE WILL BE 5 QUESTIONS AND EACH CORRECT ANSWER WILL GIVE YOU 5 POINTS AND WRONG ANSWER WILL DEDUCT 1 POINT")
                value = input("ARE YOU READY(PRESS ANY KEY TO CONTINUE)")
                answer = input("1. India has topped the list of world's most populated countries(true/false) ?").lower()
                if answer=='true':
                    score +=5
                else:
                    score -=1
                answer = input("2. president of which country is chief guest of Republic day parade 2023 ?").lower()
                if answer=='egypt':
                    score +=5
                else:
                    score -=1
                answer = input("3.Which Indian movie has won golden globes award ?").lower()
                if answer=='rrr':
                    score +=5
                else:
                    score -=1
                answer = input("4. 2023 FIH HOCKEY WORLD CUP WAS HELD IN WHICH STATE OF INDIA ?").lower()
                if answer=='odisha':
                    score +=5
                else:
                    score -=1
                answer = input("5.WHICH CITY'S STADIUM WILL HOST THE FINAL MATCH OF 2023 ICC CRICKET WORLD CUP ?").lower()
                if answer=='ahmedabad':
                    score +=5
                else:
                    score -=1
                final = input("PRESS ANY KEY TO SEE FINAL SCORE")
                print("CONGRATS YOU HAVE SCORED " + str(score) + " out of 25 points")

            if o =='2':
                score = 0
                print("THERE WILL BE 5 QUESTIONS AND EACH CORRECT ANSWER WILL GIVE YOU 5 POINTS AND WRONG ANSWER WILL DEDUCT 1 POINT")
                value = input("ARE YOU READY(PRESS ANY KEY TO CONTINUE)")
                answer = input("1. which country won 2023 wtc final ?").lower()
                if answer=='australia':
                    score +=5
                else:
                    score -=1
                answer = input("2. name of lander of chandrayaan-3 mission ?").lower()
                if answer=='vikram':
                    score +=5
                else:
                    score -=1
                answer = input("3. lvmr space-rocket is developed by which country ?").lower()
                if answer=='india':
                    score +=5
                else:
                    score -=1
                answer = input("4. worlds largest inter-space research center is situated in which country?").lower()
                if answer=='usa':
                    score +=5
                else:
                    score -=1
                answer = input("5. world's largest hockey stadium is situated in which city?").lower()
                if answer=='rourkela':
                    score +=5
                else:
                    score -=1
                final = input("PRESS ANY KEY TO SEE FINAL SCORE")
                print("CONGRATS YOU HAVE SCORED " + str(score) + " out of 25 points")

            if o =='1':
                score = 0
                print("THERE WILL BE 5 QUESTIONS AND EACH CORRECT ANSWER WILL GIVE YOU 5 POINTS AND WRONG ANSWER WILL DEDUCT 1 POINT")
                value = input("ARE YOU READY(PRESS ANY KEY TO CONTINUE)")
                answer = input("1. rival of twitter is launched by which company?").lower()
                if answer=='meta':
                    score +=5
                else:
                    score -=1
                answer = input("2. byju's largest brand value among all ed-tech companies of india.true/false?").lower()
                if answer=='true':
                    score +=5
                else:
                    score -=1
                answer = input("3.world's largest hockey stadium is situated in which city ?").lower()
                if answer=='rourkela':
                    score +=5
                else:
                    score -=1
                answer = input("4. 2023 FIH HOCKEY WORLD CUP WAS HELD IN WHICH STATE OF INDIA ?").lower()
                if answer=='odisha':
                    score +=5
                else:
                    score -=1
                answer = input("5.suparco is launched before isro.true/false ?").lower()
                if answer=='true':
                    score +=5
                else:
                    score -=1
                final = input("PRESS ANY KEY TO SEE FINAL SCORE")
                print("CONGRATS YOU HAVE SCORED " + str(score) + " out of 25 points")    

            #common sense

        elif value ==4:
            score = 0
            print("THERE WILL BE 5 QUESTIONS AND EACH CORRECT ANSWER WILL GIVE YOU 5 POINTS AND WRONG ANSWER WILL DEDUCT 1 POINT")
            value = input("ARE YOU READY(PRESS ANY KEY TO CONTINUE)")
            answer = input("1. Imagine you are in a dark room and you have a candle and a lamp. you have only one matchstick.Which one will you light first ?").lower()
            if answer=='matchstick':
                score +=5
            else:
                score -=1
            answer = input("2. you buy to eat but never eats me.who am I ?").lower()
            if answer=='plate':
                score +=5
            else:
                score -=1
            answer = input("3.What goes up and never comes down ?").lower()
            if answer=='age':
                score +=5
            else:
                score -=1
            answer = input("4. Reema has four daughters. Ena,meena,teeka,chai.Name of their mother is  ?").lower()
            if answer=='reema':
                score +=5
            else:
                score -=1
            answer = input("5.You can never be able to pass through this gate.Which gate is this ?").lower()
            if answer=='colgate':
                score +=5
            else:
                score -=1
            final = input("PRESS ANY KEY TO SEE FINAL SCORE")
            print("CONGRATS YOU HAVE SCORED " + str(score) + " out of 25 points")


# history
        elif value ==5:
            score = 0
            print("THERE WILL BE 5 QUESTIONS AND EACH CORRECT ANSWER WILL GIVE YOU 5 POINTS AND WRONG ANSWER WILL DEDUCT 1 POINT")
            value = input("ARE YOU READY(PRESS ANY KEY TO CONTINUE)")
            answer = input('''1.  Name the only President to have been elected for two consecutive terms? 

(A) APJ Abdul Kalam

(B) Pratibha Patil

(C) Dr Zakir Hussain

(D) Rajendra Prasad  

choose from a,b,c,d''').lower()
            if answer=='d':
                score +=5
            else:
                score -=1
            answer = input("2. GANDHI-IRWIN PACT WAS SIGNED IN WHICH YEAR ?").lower()
            if answer=='1935':
                score +=5
            else:
                score -=1
            answer = input("3. First modern olympics was held in which city ?").lower()
            if answer=='athens':
                score +=5
            else:
                score -=1
            answer = input('''4. Which of the following movement began in 1942?

(A) Non-Cooperation movement

(B) Khilafat movement

(C) Quit India Movement

(D) Home Rule movement ''').lower()
            if answer=='c':
                score +=5
            else:
                score -=1
            answer = input('''5. 'AN EYE FOR AN EYE MAKES THE WORLD  BLIND' QUOTE WAS GIVEN BY-
(A) MAHATMA GANDHI
(B) SARDAR PATEL
(C) J.L NEHRU
(D) BHAGAT SINGH
''').lower()
            if answer=='a':
                score +=5
            else:
                score -=1
            final = input("PRESS ANY KEY TO SEE FINAL SCORE")
            print("CONGRATS YOU HAVE SCORED " + str(score) + " out of 25 points")

# polity
        elif value ==6:
            score = 0
            print("THERE WILL BE 5 QUESTIONS AND EACH CORRECT ANSWER WILL GIVE YOU 5 POINTS AND WRONG ANSWER WILL DEDUCT 1 POINT")
            value = input("ARE YOU READY(PRESS ANY KEY TO CONTINUE)")
            answer = input("1. total schedules in the constitution ____ ?").lower()
            if answer=='12':
                score +=5
            else:
                score -=1
            answer = input("2. Which article is related to constitutional amendment ?").lower()
            if answer=='368':
                score +=5
            else:
                score -=1
            answer = input("3.Recognised political parties can have their own flag (true/false) ?").lower()
            if answer=='true':
                score +=5
            else:
                score -=1
            answer = input("4. While making of the constitution, B.R Ambedakar was head of which commitee ?").lower()
            if answer=='drafting':
                score +=5
            else:
                score -=1
            answer = input("5.'objective resolution' is old form of ?").lower()
            if answer=='preamble':
                score +=5
            else:
                score -=1
            final = input("PRESS ANY KEY TO SEE FINAL SCORE")
            print("CONGRATS YOU HAVE SCORED " + str(score) + " out of 25 points")

# geography
        elif value ==7:
            o = input('''1. set 1
2. set 2
3. set 3''')
            if o=='1':
                score = 0
                print("THERE WILL BE 5 QUESTIONS AND EACH CORRECT ANSWER WILL GIVE YOU 5 POINTS AND WRONG ANSWER WILL DEDUCT 1 POINT")
                value = input("ARE YOU READY(PRESS ANY KEY TO CONTINUE)")
                answer = input("1. Mariana trench is located in which ___ ocean ?").lower()
                if answer=='pacific':
                    score +=5
                else:
                    score -=1
                answer = input("2. Does japan lies on ring of fire (true/false) ?").lower()
                if answer=='true':
                    score +=5
                else:
                    score -=1
                answer = input("3. Most efficient means of transport is ?").lower()
                if answer=='water' or ' water transport':
                    score +=5
                else:
                    score -=1
                answer = input("4.Which ocean touches the other three oceans ?").lower()
                if answer=='southern':
                    score +=5
                else:
                    score -=1
                answer = input("5.Which continent is termed as home of human-civilisation ?").lower()
                if answer=='asia':
                    score +=5
                else:
                    score -=1
                final = input("PRESS ANY KEY TO SEE FINAL SCORE")
                print("CONGRATS YOU HAVE SCORED " + str(score) + " out of 25 points")

            if o=='2':
                score = 0
                print("THERE WILL BE 5 QUESTIONS AND EACH CORRECT ANSWER WILL GIVE YOU 5 POINTS AND WRONG ANSWER WILL DEDUCT 1 POINT")
                value = input("ARE YOU READY(PRESS ANY KEY TO CONTINUE)")
                answer = input("1. which planet is called as twin of earth ?").lower()
                if answer=='venus':
                    score +=5
                else:
                    score -=1
                answer = input("2. equater,tropic of cancer,tropic of capricon collectively passes through which continent?").lower()
                if answer=='africa':
                    score +=5
                else:
                    score -=1
                answer = input("3. is mount everest fold mountain or block mountain?").lower()
                if answer=='fold mountain' or 'foldmountain':
                    score +=5
                else:
                    score -=1
                answer = input("4. beaches of western coast of india are rocky or sandy?").lower()
                if answer=='rocky':
                    score +=5
                else:
                    score -=1
                answer = input("5.great barrier reef is located in which country ?").lower()
                if answer=='australia':
                    score +=5
                else:
                    score -=1
                final = input("PRESS ANY KEY TO SEE FINAL SCORE")
                print("CONGRATS YOU HAVE SCORED " + str(score) + " out of 25 points")

            if o=='3':
                score = 0
                print("THERE WILL BE 5 QUESTIONS AND EACH CORRECT ANSWER WILL GIVE YOU 5 POINTS AND WRONG ANSWER WILL DEDUCT 1 POINT")
                value = input("ARE YOU READY(PRESS ANY KEY TO CONTINUE)")
                answer = input("1. longest river in the world?").lower()
                if answer=='nile':
                    score +=5
                else:
                    score -=1
                answer = input("2. deepest lake of the world is lake ______ ?").lower()
                if answer=='baikal':
                    score +=5
                else:
                    score -=1
                answer = input("3. most populous city of the world is ____ ?").lower()
                if answer=='tokyo':
                    score +=5
                else:
                    score -=1
                answer = input("4.world's second tallest mountain is located in which continent?").lower()
                if answer=='asia':
                    score +=5
                else:
                    score -=1
                answer = input("5.2020 olympics were held in which city?").lower()
                if answer=='tokyo':
                    score +=5
                else:
                    score -=1
                final = input("PRESS ANY KEY TO SEE FINAL SCORE")
                print("CONGRATS YOU HAVE SCORED " + str(score) + " out of 25 points")

# ECONOMICS
        elif value ==8:
            score = 0
            print("THERE WILL BE 5 QUESTIONS AND EACH CORRECT ANSWER WILL GIVE YOU 5 POINTS AND WRONG ANSWER WILL DEDUCT 1 POINT")
            value = input("ARE YOU READY(PRESS ANY KEY TO CONTINUE)")
            answer = input("1. GST IS A FORM OF DIRECT TAX ( true/false) ?").lower()
            if answer=='false':
                score +=5
            else:
                score -=1
            answer = input("2. ADAM SMITH IS THE _______ OF MODERN ECONOMICS ?").lower()
            if answer=='father':
                score +=5
            else:
                score -=1
            answer = input("3. total income of a country divided by total population is called per capita income (true/false)").lower()
            if answer=='true':
                score +=5
            else:
                score -=1
            answer = input("4. Main source of income of banks is ___ ?").lower()
            if answer=='loans' or ' giving loans':
                score +=5
            else:
                score -=1
            answer = input("5.barter system was very good method of exchange of commodities ( true/false)?").lower()
            if answer=='false':
                score +=5
            else:
                score -=1
            final = input("PRESS ANY KEY TO SEE FINAL SCORE")
            print("CONGRATS YOU HAVE SCORED " + str(score) + " out of 25 points")

# english
        elif value ==9:
            score = 0
            print("THERE WILL BE 5 QUESTIONS AND EACH CORRECT ANSWER WILL GIVE YOU 5 POINTS AND WRONG ANSWER WILL DEDUCT 1 POINT")
            value = input("ARE YOU READY(PRESS ANY KEY TO CONTINUE)")
            answer = input("1. They ___ playing football ( was/were/have) ?").lower()
            if answer=='were':
                score +=5
            else:
                score -=1
            answer = input("2. Jorden ______ me are going to watch movie ? ( as well as / tough)").lower()
            if answer=='as well as':
                score +=5
            else:
                score -=1
            answer = input("3. You ___ complete your work before goinfg to play ?(should,ought to)").lower()
            if answer=='should':
                score +=5
            else:
                score -=1
            answer = input("4. Ram ____ cooking food ?(is/are)").lower()
            if answer=='is':
                score +=5
            else:
                score -=1
            answer = input("5.______ is he ? (which/who/whose) ?").lower()
            if answer=='who':
                score +=5
            else:
                score -=1
            final = input("PRESS ANY KEY TO SEE FINAL SCORE")
            print("CONGRATS YOU HAVE SCORED " + str(score) + " out of 25 points")

# maths
        elif value ==10:
            score = 0
            print("THERE WILL BE 5 QUESTIONS AND EACH CORRECT ANSWER WILL GIVE YOU 5 POINTS AND WRONG ANSWER WILL DEDUCT 1 POINT")
            value = input("ARE YOU READY(PRESS ANY KEY TO CONTINUE)")
            answer = input("1. factorial of 5 is ?").lower()
            if answer=='120':
                score +=5
            else:
                score -=1
            answer = input("2. solve - 2 x 4 x 12121212 / 5555 x 0 +12 -7 = _____?").lower()
            if answer=='5':
                score +=5
            else:
                score -=1
            answer = input("3. SQUARE-ROOT OF 121 IS ____?").lower()
            if answer=='11':
                score +=5
            else:
                score -=1
            answer = input("4. 0 FACTORIAL IS = ______?").lower()
            if answer=='1':
                score +=5
            else:
                score -=1
            answer = input("5.smallest whole number is _____?").lower()
            if answer=='0':
                score +=5
            else:
                score -=1
            final = input("PRESS ANY KEY TO SEE FINAL SCORE")
            print("CONGRATS YOU HAVE SCORED " + str(score) + " out of 25 points")

# exit>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    if  value == '16':
        o = input('name')
        b = input("class to apply( from 1-10)")
        p = input("father name")
        q = input("mobile")
        h = 'insert into admission_forms values("{}",{},"{}",{},"pending")'.format(o,b,p,q)
        a.execute(h)
        s.commit()
        print("form applied succesfully")

# exit>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    if  value == '17':
        print("THANKS FOR VISITING")
        quit()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>          
