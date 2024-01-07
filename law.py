def ailet(r):
    law1=[['201',"NLU DELHI- NATIONAL LAW UNIVERSITY (GOVT.)       ","₹5.75 LAKHS","₹8 LPA","₹15 LPA","85%"],
          ['202','NORTHCAP UNIVERSITY, GURGAON, HARYANA (PRIVATE)  ','₹8.46 LAKHS','₹4.5 LPA','₹14 LPA','73%'],
          ['203','SAGE UNIVERSITY, INDORE, MADHYA PRADESH (PRIVATE)','₹1.35 LAKHS','₹4.6 LPA','₹11 LPA','70%'],
          ['204','XAVIER LAW SCHOOL, BHUBANESWAR,ODISHA (PRIVATE)  ','₹7.6 LAKHS','₹3.5 LPA','₹10 LPA','60%'],
          ['205','SUSHANT UNIVERSITY, GURGAON, HARYANA(PRIVATE)    ','₹10.33 LAKHS','₹3 LPA','₹10 LPA','75%']]
    if r==0:     #printing colleges available
        for i in law1:
            print(i[1])
    if r>=1 and r<=1000:     #printing colleges according to rank
        print('__________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                           \t    FEES\tAVG PACKAGE\t  MAX PACKAGE     PLACEMENT PERCENT")
        print('__________________________________________________________________________________________________________________________________________')
        for i in law1:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t  '+i[3]+'\t     '+i[4]+'             '+i[5]+'\n')
    elif r>=1001 and r<=5000:
        print('__________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                           \t    FEES\tAVG PACKAGE\t  MAX PACKAGE     PLACEMENT PERCENT")
        print('__________________________________________________________________________________________________________________________________________')
        for i in range(2,len(law1)):
            for i in range(2,len(law1)):
                print(law1[i][0]+'  '+law1[i][1]+'\t',law1[i][2]+'\t  '+law1[i][3]+'\t     '+law1[i][4]+'             '+law1[i][5]+'\n')
    elif r>5000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')     #if no college is available for user the default college name is 'none'
    if r!=0 and r<5000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0     #accepting college id from user
        for i in law1:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:     #if college name is not found then the value in college name will be 'none'
            return('none')

def lsat(r):
    law2=[['206','School of Law UPES Dehradun, Dehradun, Uttarakhand                                   ','₹ 1,648,500','₹ 4,79,000','₹1500000','74%'],
          ['207','Bennett University, Greater Noida, Uttar Pradesh                                     ','₹1,775,000','₹6.57 LPA','₹7.5 LPA','75%'],
          ['208','Indore Institute of Law, Indore, Madhya Pradesh                                      ','₹8,48,000','₹3.5 LPA','₹8.1 LPA','60%'],
          ['209','LPU Jalandhar - Lovely Professional University, Phagwara, Punjab                     ','₹8,40,000','₹6.4 LPA','₹15.8 LPA','46%'],
          ['210','SRM University, Delhi-NCR, Sonepat, Haryana                                          ', '₹8,67,160','₹4.5 LPA','₹10 LPA','67%'],
          ['211','Narsee Monjee Institute of Management Studies, Hyderabad, Telangana                  ','₹5,07,500','₹6.7 LPA','₹10 LPA','58%'],
          ['212','The NorthCap University, Gurgaon, Haryana                                            ','₹8,46,000','₹4.5 LPA','₹14 LPA','73%'],
          ['213','Sushant University, Gurgaon, Haryana                                                 ','₹10,33,600','₹3 LPA','₹10 LPA','75%'],
          ['214','Jagannath University, Jaipur, Rajasthan                                              ','₹3,80,000','₹2.5 LPA','₹07 LPA','49%'],
          ['215','NMIMS Bangalore - Narsee Monjee Institute of Management Studies, Bangalore, Karnataka','₹5,07,500','₹5.7 LPA','₹09 LPA','52%']]
    if r==0:
        for i in law2:
            print(i[1])
    if r>=1 and r<=500:
        print('__________________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                                     \t    FEES         AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('__________________________________________________________________________________________________________________________________________________________')
        for i in law2:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t  '+i[3]+'\t     '+i[4]+'  '+i[5])
    elif r>=501 and r<=1000:
        print('__________________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                                     \t    FEES         AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('__________________________________________________________________________________________________________________________________________________________')
        for i in range(2,len(law2)):
            print(law2[i][0]+'  '+law2[i][1]+'\t',law2[i][2]+'\t  '+law2[i][3]+'\t     '+law2[i][4]+'        '+law2[i][5]+'\n')
    elif r>=1001 and r<=5000:
        print('__________________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                                     \t    FEES         AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('__________________________________________________________________________________________________________________________________________________________')
        for i in range(4,len(law2)):
            print(law2[i][0]+'  '+law2[i][1]+'\t',law2[i][2]+'\t  '+law2[i][3]+'\t     '+law2[i][4]+'        '+law2[i][5]+'\n')
    elif r>5001 and r<=10000:
        print('__________________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                                     \t    FEES         AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('__________________________________________________________________________________________________________________________________________________________')
        for i in range(5,len(law2)):
            print(law2[i][0]+'  '+law2[i][1]+'\t',law2[i][2]+'\t  '+law2[i][3]+'\t     '+law2[i][4]+'      '+law2[i][5]+'\n')
    elif r>10000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')
    if r!=0 and r<10000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0
        for i in law2:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:
            return('none')
def duet(r):
    law3=[['216','SRM University, Delhi-NCR, Sonepat, Haryana           ','₹8,67,160','₹4.5 LPA','₹10 LPA','67%'],
          ['217','Jindal Global Law School, Sonipat, Haryana            ','₹18,00,000','₹7 LPA','₹15 LPA','22%'],
          ['218','Faculty of Law DU - Faculty of Law University of Delhi','₹13,934','₹2 LPA','₹05 LPA','46%'],
          ['219','Bennett University, Greater Noida, Uttar Pradesh      ','₹1,775,000','₹6.57 LPA','₹07 LPA','75%']]
    if r==0:
        for i in law3:
            print(i[1])
    if r>=1 and r<=1000:
        print('___________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                     \t    FEES         AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('___________________________________________________________________________________________________________________________')
        for i in law3:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t  '+i[3]+'\t     '+i[4]+'        '+i[5]+'\n')
    elif r>=1001 and r<=5000:
        print('___________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                     \t    FEES         AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('___________________________________________________________________________________________________________________________')
        for i in range(2,len(law3)):
            print(law3[i][0]+'  '+law3[i][1]+'\t',law3[i][2]+'\t  '+law3[i][3]+'\t     '+law3[i][4]+'        '+law3[i][5]+'\n')
    elif r>5000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')
    if r!=0 and r<5000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0
        for i in law3:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:
            return('none')
def clat(r):
    law4=[['220','School of Law UPES Dehradun, Uttarakhand                                          ','₹ 1,648,500','₹ 4,79,000','₹1500000 ','74%'],
          ['221','Bennett University, Greater Noida, Uttar Pradhesh                                 ','₹1,775,000','₹6.57 LPA','₹7.5 LPA  ','75%'],
          ['222','CMR University School of Legal Studies, Bangalore, Karnataka                      ','₹ 675,000','₹5 LPA','₹10 LPA  ','60%'],
          ['223','NLU Hyderabad - NALSAR University of Law, Telangana,(Public/Government)           ','₹ 810,000','₹7.6 LPA','₹12 LPA  ','72%'],
            ['224','MNLU Mumbai - Maharashtra National Law University, Maharashtra                    ','₹ 841,750','₹7 LPA','₹12 LPA  ','65%'],
            ['225','Indore Institute of Law, Indore, Madhya Pradesh                                   ','₹8,48,000','₹3.5 LPA','₹8.1 LPA ','60%'],
            ['226','Institute of Law, Nirma University, Ahmedabad, Gujarat (Private)                  ','₹ 1,244,700','₹8.3 LPA','₹16 LPA  ','50%'],
            ['227','NLIU Bhopal - National Law Institute University, Madhya Pradesh(Public/Government)','₹ 917,500','₹10 LPA','₹16 LPA  ','54%'],
            ['228','LPU Jalandhar - Lovely Professional University, Phagwara, Punjab                  ','₹8,40,000','₹6.4 LPA','₹15.8 LPA','46%'],
            ['229','CNLU Patna - Chanakya National Law University, Bihar(Public/Government)           ','₹ 703,500','₹3.5 LPA','₹9 LPA   ','30%']]
    if r==0:
        for i in law4:
            print(i[1])
    if r>=1 and r<=500:
        print('__________________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                          \t    FEES         AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('__________________________________________________________________________________________________________________________________________________________')
        for i in law4:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t  '+i[3]+'\t     '+i[4]+'        '+i[5]+'\n')
    elif r>=501 and r<=1000:
        print('__________________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                          \t    FEES         AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('__________________________________________________________________________________________________________________________________________________________')
        for i in range(2,len(law4)):
            print(law4[i][0]+'  '+law4[i][1]+'\t',law4[i][2]+'\t  '+law4[i][3]+'\t     '+law4[i][4]+'        '+law4[i][5]+'\n')
    elif r>=1001 and r<=5000:
        print('__________________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                          \t    FEES         AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('__________________________________________________________________________________________________________________________________________________________')
        for i in range(4,len(law4)):
            print(law4[i][0]+'  '+law4[i][1]+'\t',law4[i][2]+'\t  '+law4[i][3]+'\t     '+law4[i][4]+'        '+law4[i][5]+'\n')
    elif r>5001 and r<=10000:
        print('__________________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                          \t    FEES         AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('__________________________________________________________________________________________________________________________________________________________')
        for i in range(5,len(law4)):
            print(law4[i][0]+'  '+law4[i][1]+'\t',law4[i][2]+'\t  '+law4[i][3]+'\t     '+law4[i][4]+'        '+law4[i][5]+'\n')
    elif r>10000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')
    if r!=0 and r<10000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0
        for i in law4:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:
            return('none')
