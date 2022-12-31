#   project name      : student report card maker
#   made by             : Bikram Pal
#   session               : 2021-22
#   roll  no               : 12677315

import mysql.connector
from prettytable import PrettyTable


# global variable for report
school_name = 'Hariyana Vidya Mandir'
school_address = 'BA-193,Sector-1,Saltlake,Kolkata-700064'
school_email = 'hvm123@gmail.com'
school_phone = '033 2334 2404'

def clear():
  for _ in range(65):
     print()

def check_for_class(x):
      try:
            x_int=int(x)
            if x_int>13:
              print("The number you entered exceed the limits ")
              print("Enter your value correctly!!!")
              x=input("Enter value: ")
              check_for_class(x)
            else:
              pass
      except ValueError:
            print("You have entered the value wrong")
            print("It should not contain any alphabet")
            print("Enter correctly !!")
            x=input("Enter value: ")
            check_for_class(x)
      return x


def check_for_admno(x):
      try:
            x_int=int(x)
      except ValueError:
            print("You have entered the value wrong")
            print("It should not contain any alphabet")
            print("Enter correctly !!")
            x=input("Enter value: ")
            check_for_admno(x)
      return x


def check_for_session(x):
  l1=['2020-21','2021-22','2019-20']
  if x in l1:
    pass
  else:
    print("Enter the value correctly!!!!")
    print("The value should be of form (2018-19)")
    x=input("Enter value: ")
    check_for_session(x)
  return x

def check_for_term(x):
  if x=="UT-1" or x=="UT-2":
    pass
  else:
    print("Enter the value correctly!!!")
    print("it should be of format (UT-2)")
    x=input("Enter value:")
    check_for_term(x)
  return x


def check_for_string(x):
      if x.isalpha()==True:
            pass
      else:
            print("You have entered the value wrong")
            print("It should not contain any numbers")
            print("Enter correctly !!")
            x=input("Enter value: ")
            check_for_string(x)
      return x

def check_for_integer(x):
      try:
            x_int=int(x)
            if x_int>100 or x_int==100:
              print("The number you entered is more than '100' ")
              print("Enter your value correctly!!!")
              x=input("Enter value: ")
              check_for_integer(x)
            else:
              pass
      except ValueError:
            print("You have entered the value wrong")
            print("It should not contain any alphabet")
            print("Enter correctly !!")
            x=input("Enter value: ")
            check_for_integer(x)
      return x

def check_for_section(x):
      l1=["B5","B6","B7","B8","A","B","C","a","b","c"]
      if x in l1:
            pass
      else:
            print("The section must be from the list given below")
            print(l1)
            print("enter correctly !!")
            x=input("Enter value: ")
            check_for_section(x)
      return x


def add_student():
    conn = mysql.connector.connect(
      host='localhost', database='report_card', user='root', password='Bikram@2004')
    cursor = conn.cursor()
    clear()
    print('\t\t\tAdd New Student Screen')
    print('-'*120)
    print("")
    print("Enter Student`s name:    (ex-Amit Kumar)")
    name = input('Enter value: ')
    name = check_for_string(name)
    print("Enter Student`s Father name     (ex-Ajit Kumar)")
    fname = input('Enter value: ')
    fname = check_for_string(fname)
    print("Enter Student`s class     (ex-12)")
    clas = input('Enter value: ')
    clas = check_for_integer(clas)
    print("Enter Student`s Section    (ex-B5)")
    section = input('Enter value: ')
    section = check_for_section(section)
    sql ='insert into student(name,fname,class,section,status) values ("'+name+'","'+fname+'","'+clas+'","'+section+'","active");'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\n\n New Student added successfully.....')
    wait=input('\n\n\nPress any key to continue...')
    main_menu()


def add_marks():
    conn = mysql.connector.connect(
        host='localhost', database='report_card', user='root', password='Bikram@2004')
    cursor = conn.cursor()
    clear()
    print('Add New marks Screen')
    print('-'*120)
    print("Enter Students Admision Number     (ex-110)")
    admno = input('Enter value : ')
    admno = check_for_admno(admno)
    print("Enterr the Term Name     (ex-UT-1)")
    term = input('Enter value : ')
    term = check_for_term(term)
    print("Enter session in the given format      (2020-21)")
    session = input('Enter value : ')
    session = check_for_session(session)
    print("Enter Marks in Physics     (ex-88)")
    phy = input('Enter value : ')
    phy = check_for_integer(phy)
    print("Enter the Marks in Chemistry      (ex-88)")
    chem = input('Enter value : ')
    chem = check_for_integer(chem)
    print("Enter Marks in Maths      (ex-88)")
    math = input('Enter value : ')
    math = check_for_integer(math)
    print("Enter Marks in English      (ex-88)")
    eng = input('Enter value : ')
    eng = check_for_integer(eng)
    print("Enter Marks in Compter      (ex-88)")
    comp = input('Enter value : ')
    comp = check_for_integer(comp)
    sql = 'insert into marks(admno,term,session,phy,chem,math,eng,comp) values (' + \
        admno+',"'+term+'","'+session+'",'+phy+','+chem+','+math+','+eng+','+comp+');'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\n\n New Marks added successfully.....')
    wait = input('\n\n\nPress any key to continue...')
    main_menu()

def modify_student():
    conn = mysql.connector.connect(
        host='localhost', database='report_card', user='root', password='Bikram@2004')
    cursor = conn.cursor()
    clear()
    print('Modify Student Information - Screen')
    print('-'*120)
    print("Enter Students Admision Number     (ex-110)")
    admno = input('Enter value : ')
    admno = check_for_admno(admno)
    print('\n1.   Name  ')
    print('\n2.   Father Name  ')
    print('\n3.   Class  ')
    print('\n4.   Section  ')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field=''
    if choice ==1:
       field ='name' 
    if choice == 2:
       field = 'fname'
    if choice == 3:
       field = 'class'
    if choice == 4:
       field = 'section'
    value =input('Enter new value :')   
    sql ='update student set '+field+' ="'+value +'" where admno ='+admno+';'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\n\n Student Record Updated.....')
    wait = input('\n\n\nPress any key to continue......')
    main_menu()

def modify_marks():
    conn = mysql.connector.connect(
        host='localhost', database='report_card', user='root', password='Bikram@2004')
    cursor = conn.cursor()
    clear()
    print('Modify Marks - Screen')
    print('-'*120)
    print("Enter Students Admision Number     (ex-110)")
    admno = input('Enter value : ')
    admno = check_for_admno(admno)
    print("Enter the Term name       (ex-UT-1)")
    term = input('Enter value : ')
    term = check_for_term(term)
    print("Enter the Session in the given format       (ex-2019-20)")
    session = input('Enter value : ')
    session = check_for_session(session)
    print('\n1.   Physics  ')
    print('\n2.   Chemistry  ')
    print('\n3.   Mathematics  ')
    print('\n4.   English  ')
    print('\n5.   Computer  ')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
       field = 'phy'
    if choice == 2:
       field = 'chem'
    if choice == 3:
       field = 'math'
    if choice == 4:
       field = 'eng'
    if choice == 5:
       field = 'comp'

    value = input('Enter new value :')
    sql = 'update marks set '+field+' ='+value + ' where admno ='+admno+' AND term="'+term+'" AND session="'+session+'";'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print("\n\n\nMarks updated.......\n\n\n")
    wait=input("Press any key to continue.... ")
    main_menu()

    
def search_student(field):
  conn = mysql.connector.connect(
      host='localhost', database='report_card', user='root', password='Bikram@2004')
  cursor = conn.cursor()
  sql ='select * from student where '
  msg ='Enter '+field +' :'
  value = input(msg)
  if field=='admno':
     sql = sql + field +'=' +value+';'
  else:
     sql = sql + field +' like "%'+value+'%" or fname like "%'+value +'%";'
  cursor.execute(sql)
  records = cursor.fetchall()
  clear()
  print('Search Result for '+field+' : '+value)
  print('-'*120)
  print("Admno\t","Name\t\t","Fname\t\t","Class\t","Sectiom\t","Status")
  for record in records:
    print(record[0],"\t",record[1],"\t\t",record[2],"\t\t",record[3],"\t",record[4],"\t",record[5])
  conn.close()
  wait = input('\n\n\n Press any key to continue.....')
  main_menu()


def search_marks():
    conn = mysql.connector.connect(
      host='localhost', database='report_card', user='root', password='Bikram@2004')
    cursor = conn.cursor()
    print("Enter the students Admission Number      (ex-113)")
    admno = input('Enter value : ')
    admno = check_for_admno(admno)
    print("Enter the Session in the given format     (ex-2019-20)")
    session = input('Enter value : ')
    session = check_for_session(session)
    sql ='select * from marks where admno = '+admno + ' and session ="'+session+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Search Result for Admission No :'+admno +' Session : '+session)
    print('-'*120)
    print("Admno","\t","Term","\t","Session","\t","Physics","\t","Chemistry","\t","Maths","\t","English","\t","Computer")
    for record in records:
      print(record[0],"\t",record[1],"\t",record[2],"\t",record[3],"\t",record[4],"\t\t",record[5],"\t",record[6],"\t",record[7])
    conn.close()
    wait = input('\n\n\n Press any key to continue.....')
    main_menu()

def search_menu():
      clear()
      print(' S E A R C H    M E N U')
      print('-'*120)
      print('\n1.  Admission No')
      print('\n2.  Name / Father Name')
      print('\n3.  Student Term Marks')
      print('\n4.  back to main')
      print('\n\n')
      field=''
      def search_choice():
        choice = input('Enter your choice ...: ')
        if choice == '1':
          field='admno'
          search_student(field)
        elif choice == '2':
          field='name'
          search_student(field)
        elif choice == '3':
          search_marks()
        elif choice == '4':
          main_menu()
        else:
          print("Enter your your choice correctly!!!")
          print("your choice should be within the numbers listed above")
          search_choice()
      search_choice()

def report_single_term(): 
    conn = mysql.connector.connect(
        host='localhost', database='report_card', user='root', password='Bikram@2004')
    cursor = conn.cursor()
    clear()
    print("Enter the students Admission Number      (ex-109)")
    admno = input('Enter value : ')
    admno = check_for_admno(admno)
    print("Enter the Session in the given format        (ex-2020-21)")
    session = input('Enter value : ')
    session = check_for_session(session)
    print("Enter the Term name       (ex-UT-1)")
    term = input('Enter value : ')
    term = check_for_term(term)
    sql ='select s.admno,name,fname,phy,math,chem,eng,comp from  \
          student s,marks m  where s.admno = m.admno and s.admno = '+admno +' and m.session = "'+session+'" and m.term ="'+term+'";'
    cursor.execute(sql)
    record = cursor.fetchone()
    clear()
    print(school_name)
    print(school_address)
    print('Phone :',school_phone ,' Email :', school_email)
    print('-'*120)
    print('Admno :',record[0],' Name :',record[1], '   Father Name :',record[2])
    print('Session :', session, ' Term :', term)
    print('-'*120)
    print('Subject','\t\tMax_marks','\tmin-marks','\tmarks obtained')
    print('Physics','\t\t100','\t\t33\t\t',record[3])
    print('Chemistry','\t100','\t\t33\t\t',record[4])
    print('Mathematics','\t100','\t\t33\t\t',record[5])
    print('English','\t\t100','\t\t33\t\t',record[6])
    print('Computer','\t100','\t\t33\t\t',record[7])
    print('-'*120)
    total = record[3]+record[4]+record[5]+record[6]+record[7]
    percentage = total*100/500
    print('Total Marks : ',total,' \t% Marks :',percentage)
    conn.close()
    wait = input('\n\n\n Press any key to continue.....')
    main_menu()

def report_whole_class(): 
    conn = mysql.connector.connect(
        host='localhost', database='report_card', user='root', password='Bikram@2004')
    cursor = conn.cursor()
    print("Enter the students class        (ex-11)")
    clas = input('Enter value : ')
    clas = check_for_class(clas)
    print("Enter the students Section       (ex-A) ")
    section = input('Enter value : ')
    section = check_for_section(section)
    print("Enter the students Session        (ex-2020-21)")
    session = input('Enter value :')
    session = check_for_session(session)
    print("Enter the Term name         (ex-UT_2)")
    term = input('Enter value : ')
    term = check_for_term(term)
    sql ='select s.admno,name,fname,phy,math,chem,eng,comp from  \
          student s, marks m  where s.admno = m.admno  AND s.class="'+clas+'" AND s.section ="'+section +'" and m.session = "'+session+'" and m.term ="'+term+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print(school_name)
    print(school_address)
    print('Phone :',school_phone ,' Email :', school_email)
    print('-'*120)
    print('Class Wise Report Card:',clas,'-',section, 'Session : ',session, ' Term :',term)
    print('-'*120)
    t = PrettyTable(['admno', 'Name', 'Father Name', 'Phy', 'Chem', 'Math','Eng','Comp','Total'])
    for idr, name, fname, phy,chem,math,eng,comp in records:
      total = phy+chem+math+eng+comp
      t.add_row([idr, name, fname, phy, chem, math, eng, comp,total])
    print(t)
    conn.close()
    wait = input('\n\n\n Press any key to continue.....')
    main_menu()


def report_whole_session():
    conn = mysql.connector.connect(
        host='localhost', database='report_card', user='root', password='Bikram@2004')
    cursor = conn.cursor()
    print("Enter the Session in the given format       (ex-2020-21)")
    session = input('Enter value : ')
    session = check_for_session(session)
    sql = 'select s.admno,name,fname,class, section,term,phy,math,chem,eng,comp from  \
          student s, marks m  where s.admno = m.admno  and m.session = "'+session+'" ORDER BY class,section,term;'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print(school_name)
    print(school_address)
    print('Phone :', school_phone, ' Email :', school_email,'\n\n')

    print('Whole Session Report Card:', '           Session : ', session)
    print('-'*120)
    t = PrettyTable(['admno', 'Name', 'Father Name','Class','section','Term', 'Phy',
                     'Chem', 'Math', 'Eng', 'Comp', 'Total'])
    for idr, name, fname,clas1,section, term, phy, chem, math, eng, comp in records:
      total = phy+chem+math+eng+comp
      t.add_row([
        idr, name, fname,clas1, section, term, phy, chem, math, eng, comp, total])
    print(t)
    conn.close()
    wait = input('\n\n\n Press any key to continue.....')
    main_menu()


def report_topper_list():
    conn = mysql.connector.connect(
        host='localhost', database='report_card', user='root', password='Bikram@2004')
    cursor = conn.cursor()
    print("Enter the Session in the given format        (ex-2020-21)")
    session = input('Enter value : ')
    session = check_for_session(session)
    print("Enter the Term name        (ex-UT-1)")
    term = input('Enter value : ')
    term = check_for_term(term)
    print("Enter the students class        (ex-12)")
    clas = input('Enter value : ')
    clas = check_for_class(clas)
    print("Enter the students section         (ex-C)")
    section = input('Enter value : ')
    section = check_for_section(section)
    sql = 'select s.admno, name, fname,phy,chem,math,eng,comp, phy+chem+math+eng+comp "Total" from student s, marks m \
           where s.admno = m.admno and class = "'+clas+'" and section = "'+section+'" and session ="'+session+'" and term="'+term+'" order by total Desc;'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print(school_name)
    print(school_address)
    print('Phone :', school_phone, ' Email :', school_email, '\n\n')

    print('T O P P E R S    L I S T \n\n Class :',clas,'           Session : ', session, ' Term :',term)
    print('-'*120)
    t = PrettyTable(['admno', 'Name', 'Father Name', 'Physics', 'Chemistry', 'Mathematics','English','Computer', 'Total'])
    for idr, name, fname, phy, chem, math, eng, comp, total in records:
        t.add_row([idr, name, fname, phy, chem, math, eng, comp,total])
    print(t)
    conn.close()
    wait = input('\n\n\n Press any key to continue.....')
    main_menu()


def report_menu():
      clear()
      print(' R E P O R T   M E N U ')
      print("\n1.  Single Term report card")
      print('\n2.  Whole class report card')
      print('\n3.  Whole Session report Card ')
      print('\n4.  Class Wise- Toppers')
      print('\n5.  Back to main menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        report_single_term()
      if choice == 2:
        report_whole_class()
      if choice == 3:
        report_whole_session()
      if choice == 4:
        report_topper_list()
      if choice == 5:
        main_menu()



def main_menu():
  clear()
  print(' R E P O R T   C A R D   M E N U  ')
  print("\n1.  Add Student")
  print('\n2.  Modify Student Record')
  print('\n3.  Add marks')
  print('\n4.  Modify Marks')
  print('\n5.  Search Menu')
  print('\n6.  Report Menu')
  print('\n7.  Close application')
  print('\n\n')
  print("Enter form the above options carefully")
  def main_menu_choice():
    choice = input('Enter your choice ...: ')
    choice = check_for_integer(choice)
    if choice == '1':
      add_student()
    elif choice == '2':
      modify_student()
    elif choice == '3':
      add_marks()
    elif choice == '4':
      modify_marks()
    elif choice == '5':
      search_menu()
    elif choice == '6':
      report_menu()
    elif choice == '7':
      exit_screen()
    else:
      print("Enter your choice correctly ")
      main_menu_choice()
  main_menu_choice()
  
def passcode():
  print("Confirm your Identity:    ")
  print("\n")
  user_name=input("Enter a user name: ")
  password=input("Enter the password: ")

  if  user_name=="bikram" and password=="Bikram@14":
    main_menu()
  elif user_name=="ayan" and password=="Ayan@12":
    main_menu()
  elif user_name=="ayushi" and password=="Ayushi@13":
    main_menu()
  else:
    print("You have entered the wrong user name and password")
    print("Want to ReEnter the password ? ")
    print("Enter 'y' for YES or 'n' for NO")
    choice=input("Enter value :")
    if choice=='y':
      passcode()
    elif choice=='n':
      exit_screen()
    else:
      print("Your choice was incorrect")
      print("Exiting the program")

def exit_screen():
  print("Thank You for using")
  print("Come back later :)")
passcode()
