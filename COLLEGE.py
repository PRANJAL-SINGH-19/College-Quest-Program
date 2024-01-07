from courses import engineering,law,mba,medical     #importing user-defined modules
import datetime as dt     #importing pre-defined modules
def course():     #function to print courses
    print("[ 1 ] : ENGINEERING")
    print("[ 2 ] : MEDICAL SCIENCE")
    print("[ 3 ] : BUSINESS STUDIES")
    print("[ 4 ] : LAW")
a1='NONE'     #default value of variable which will store college name
def choice(choice):     #function to handle exams
    global w
    if choice=='1':
        w=0
        print("YOUR COURSE: ENGINEERING")
        qqq='a'
        while qqq not in 'yY':
            print('_'*155,'\n')
            print("[ 1 ] : JEE ADVANCED\n[ 2 ] : JEE MAIN\n[ 3 ] : WBJEE\n[ 4 ] : BITSAT\n[ 5 ] : VITEEE")
            q=input("Choose Exam: ")
            qqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
            print('_'*155,'\n')
            if qqq in 'yY':
                global a1
                if q=='1':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")     #displaying colleges according to the selected exam
                        engineering.JEEADVANCED(0)     
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")     #displaying colleges according to rank
                            a1=engineering.JEEADVANCED(r)     #returning college name
                elif q=='2':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        engineering.JEEMAIN(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=engineering.JEEMAIN(r)
                elif q=='3':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        engineering.WBJEE(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=engineering.WBJEE(r)
                elif q=='4':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        engineering.BITSAT(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=engineering.BITSAT(r)
                elif q=='5':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        engineering.VITEEE(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=engineering.VITEEE(r)
                else:
                    print('INVALID INPUT')
    elif choice=='2':
        w=0
        print("YOUR COURSE: MEDICAL SCIENCE")
        qqq='a'
        while qqq not in 'yY':
            print('_'*155,'\n')
            print("[ 1 ] : AIIMS\n[ 2 ] : NEET\n[ 3 ] : MCAT\n[ 4 ] : PGIMER\n[ 5 ] : JIPMER")
            q=input("Choose Exam: ")
            qqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
            print('_'*155,'\n')
            if qqq in 'yY':
                if q=='1':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        medical.aiims(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=medical.aiims(r)
                elif q=='2':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        medical.neet(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=medical.neet(r)
                elif q=='3':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        medical.mcat(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=medical.mcat(r)
                elif q=='4':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        medical.pgimer(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=medical.pgimer(r)
                elif q=='5':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        medical.jipmer(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=medical.jipmer(r)   
                else:
                    print('INVALID INPUT')
    elif choice=='3':
        w=0
        print("YOUR COURSE: BUSINESS STUDIES")
        qqq='a'
        while qqq not in 'yY':
            print('_'*155,'\n')
            print("[ 1 ] : CAT\n[ 2 ] : CMAT\n[ 3 ] : XAT\n[ 4 ] : SNAP\n[ 5 ] : MAT")
            q=input("Choose Exam: ")
            qqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
            print('_'*155,'\n')
            if qqq in 'yY':
                if q=='1':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        mba.cat(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=mba.cat(r)
                elif q=='2':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        mba.cmat(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=mba.cmat(r)
                elif q=='3':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        mba.xat(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=mba.xat(r)
                elif q=='4':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        mba.snap(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=mba.snap(r)
                elif q=='5':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        mba.mat(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=mba.mat(r)
                else:
                    print('INVALID INPUT')
    elif choice=='4':
        w=0
        print("YOUR COURSE: LAW")
        qqq='a'
        while qqq not in 'yY':
            print('_'*155,'\n')
            print("[ 1 ] : AILET\n[ 2 ] : LSAT\n[ 3 ] : DUET\n[ 4 ] : CLAT")
            q=input("Choose Exam: ")
            qqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
            print('_'*155,'\n')
            if qqq in 'yY':
                if q=='1':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        law.ailet(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=law.ailet(r)
                elif q=='2':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        law.lsat(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=law.lsat(r)
                elif q=='3':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        law.duet(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=law.duet(r)
                elif q=='4':
                    qqqq='a'
                    while qqqq not in 'yY':
                        print("COLLEGES YOU CAN GET IN THROUGH THIS EXAM:\n")
                        law.clat(0)
                        print('_'*155,'\n')
                        r=int(input('Enter your RANK:'))
                        qqqq=input("ENTER y TO CONFIRM OR ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
                        if qqqq in 'yY':
                            print("COLLEGES AVAILABLE FOR YOU:")
                            a1=law.clat(r)
                else:
                    print('INVALID INPUT')
    else:
        print("************WRONG CHOICE*************")
        print("**********PLEASE ENTER A VALID INPUT!!***********")
        course()
w=1       
print("********************************************************************WELCOME*************************************************************************")
print("___________________________________________________________SELECT YOUR CAREER COURSE________________________________________________________________\n")
course()
qq='a'
while qq not in 'yY':
    while w!=0:
        b=input("SELECT YOUR STREAM: ")
        qq=input("ENTER y TO CONFIRM AND ANY OTHER KEY TO CHANGE YOUR CHOICE : ")
        if qq in 'Yy':
            choice(b)
#****************************************************************************************************************************************************
    
def stuin():     #accepting students information
    c1=1
    while c1:
        a=input("Enter First Name:")
        if a.isalpha()==True:     #handling invalid inputs
            print("Accepted");c1=0
        else:
            print("Please Enter Only Alphabets")
            c1=1
    c2=1
    while c2:
        b=input("Enter Last Name:")
        if b.isalpha()==True:
            print("Accepted");c2=0
        else:
            print("Please Enter Only Alphabets")
            c2=1
    c3=1
    while c3:
        c=input("Enter Phone Number:")
        if c.isdigit()==True and len(c)==10:
            print("Accepted");c3=0
        else:
            print("Please Enter Numbers Of Valid Length:")
            c3=1
    c4=1
    while c4:
        d1=["@gmail.com","@outlook.in","@yahoo.com","@rediffmail.com"]
        d=input("Enter E-Mail ID:");d2=0;d3=""
        for i in d1:
            if i in d:
                d2+=1
        if d2==1:
            print("Accepted");c4=0
        else:
            print("Enter E-Mail ID In Valid Format")
            c4=1
    c5=1
    while c5:
        e=input("Enter State:")
        e1=e.split();e2=0
        for i in e1:
            if i.isalpha()==True:
                e2+=1
            elif i.isspace()==True:
                e2+=1
        if e2==len(e1):
            print("Accepted");c5=0
        else:
            print("Use Only Alphabets And Space(s)")
            c5=1
    c6=1
    while c6:
        f=input("Enter City:")
        if f.isalpha()==True:
            print("Accepted");c6=0
        else:
            print("Use Only Alphabets");c6=1
    c7=1
    while c7:
        g=""
        print("[ 1 ] : CBSE\n[ 2 ] : CISCE\n[ 3 ] : NIOS\n[ 4 ] : OTHER")
        g1=input("Select Educational Board:")
        if g1=="1":
            g+="CBSE";c7=0
        elif g1=="2":
                g+="CISCE";c7=0
        elif g1=="3":
                g+="NIOS";c7=0
        elif g1=="4":
                g2=input("Enter Board Name:")
                g+=g2;c7=0
        else:
            print("Please Use A Valid Input:")
            c7=1
    h=input("Enter Name Of School:")
    i=input("Enter Your Residential Address:")
    print("-"*155)
    print("                                                                   Your ID Has Been Created!")
    print("-"*155)
    print(" First Name:",a,"\n\n","Last Name:",b,"\n\n","Phone Number:",c,"\n\n","E-Mail ID:",d,"\n\n","State:",e,"\n\n","City:",f,"\n\n","Board:",g,"\n\n","School Name:",h,"\n\n","Residential Address:",i,"\n\n","College Name:",a1)
    print("-"*155)
    print("Save Data Or Make Changes?")
    j=input("Save Data[1]\nMake Changes[2]\n:")
    if j=="1":
        print("Saved Successfully")
    elif j=="2":
        print("What would you like to change:?")
        ch='y'
        while ch=='y':     #condition to modify any details
            print("First Name[1]\nLast Name[2]\nPhone Number[3]\nE-Mail ID[4]\nState[5]\nCity[6]\Board[7]\nSchool Name[8]\nResidential Address[9]")
            new=input(":")
            if new=="1":
                anew=input("Enter First Name:")
                a=anew
            elif new=="2":
                bnew=input("Enter Last Name:")
                b=bnew
            elif new=="3":
                cnew=input("Enter Phone Number:")
                c=cnew
            elif new=="4":
                dnew=input("Enter E-Mail ID:")
                d=dnew
            elif new=="5":
                enew=input("Enter State:")
                e=enew
            elif new=="6":
                fnew=input("Enter City:")
                f=fnew
            elif new=="7":
                gnew=input("Enter Board:")
                g=gnew
            elif new=="8":
                hnew=input("Enter Name Of School:")
                h=hnew
            elif new=="9":
                inew=input("Enter Residential Address:")
                i=inew
            ch=input('Enter y to make any other change or any other character to continue.')
        print("-"*155)
        print("                                                                   Record Updated Successfully!")
        print("-"*155)
        print(" First Name:",a,"\n\n","Last Name:",b,"\n\n","Phone Number:",c,"\n\n","E-Mail ID:",d,"\n\n","State:",e,"\n\n","City:",f,"\n\n","Board:",g,"\n\n","School Name:",h,"\n\n","Residential Address:",i,"\n\n","College Name:",a1)
    tm=dt.datetime.now()
    d=dt.date.today();time=str(tm.hour)+':'+str(tm.minute)     #date and time of output
    if a1 not in ['none','NONE']:
        print("\n************************************************************************************************************************************************************")
        print("*                                                                      NAILED IT!                                                                          *")
        print("************************************************************************************************************************************************************")
        print("                                                                          ()_")
        print("                                                                          || `-._.-.")
        print("                                                                          ||_    .'")
        print("                                                                          || `-.'")
        print("                                                     +                    ||                    +")
        print("                                                     |                    ||                    |")
        print("                                                    / \               _,,.||.__                / \ ")
        print("                                                   /___\           ,-'         `-.            /___\ ")
        print("                                             ______|===|_________,'               `.__________|===|______")
        print("                                            /      |===|        /      COLLEGE      \         |===|      \ ")
        print("                                           /___________________/                     \____________________\ ")
        print("                                           |  +-----+ +-----+  |`-._              _.-'|  +-----+ +-----+  |")
        print("                                           |  ||_|_|| ||_|_||  | |. `'----------'' .| |  ||_|_|| ||_|_||  |")
        print("                                           |  ||_|_|| ||_|_||  | |:  | ||    :| |  :| |  ||_|_|| ||_|_||  |")
        print("                                        ---| %%---%%+ +%%%--+  | |:__| ||____:| |__:| |  +-%%%-+ %%---%%% |---")
        print("                                           |%%%%_%%%%_%%%%%____| |/  | || -  :| |  \| |___%%%%%_%%%%_%%%%%|")
        print("                                             `|   %|   `|'   |`.`-._ | |'    `| |__.-'.'|  %|'   `|   %|MJP")
        print("                                                             |`.`-._``---....---''_.-'.'|")
        print("                                                             `. `-._``---....---''_.-' .'")
        print("                                                               `.   ``---....---''   .'")
        print("                                                                 `.                .'")
        print("                                                                   `.            .'")
        print("                                                                     `.        .'")
        print("                                                                      ().    .()")
        print("                                        /\_/\_/\_/\_/\_/\_/\_/\_/\_/\_||:    :||_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\ ")
        print("                                        ||=||=||=||=||=||=||=||=||=||=||:    :||=||=||=||=||=||=||=||=||=||=||")
        print('                                        """"""""""""""""""""""""""""""""      """""""""""""""""""""""""""""""" ')
        print("                                        ----------------------------------------------------------------------")
        print("Dear",a,end=',\n')
        print('Congratulations!!\n')
        print(a1+'''\nis delighted to invite you at the Admission Counseling session 2022-2023 from 9 AM onwards.
Please note, if you are offered the admission you are required to submit the 1st installment of fee to confirm admission.
At the time of Counseling, you are advised to bring some documents. The information will be sent at your given mobile number/email.

Applying to college can be both exciting and stressful. We understand this year may present additional challenges and that you may have many more questions.
The Admission staff is eager to work with you to make this process as smooth and stress-free as possible. Please let me know if you have questions, or if you
need further information about the College. Best wishes for continued success this academic year.\n
Thank You!\n\nTIME:''',time+'\nDATE:',d)
        print("\n************************************************************************************************************************************************************\n")
    a=0
    while a==0:
        id=input("Do you want to receive notifications afterwards? (Y [Id will be saved]/ N [Id will be deleted])")
        if id in'Yy':
            print('Id saved');a=1
        elif id in 'Nn':
            print('Id deleted');a=1
        else:
            print('Invalid Input');a=0
stuin()    
