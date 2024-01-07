def JEEADVANCED(r):
    BTECH1=[['101','IIT BOMBAY, MAHARASHTRA   ','₹8.33 LAKHS','₹30 LPA','₹80 LPA','88%'],
            ['102','IIT DELHI, NEW DELHI      ','₹8.47 LAKHS','₹18 LPA','₹70 LPA','89%'],
            ['103','IIT MADRAS, TAMIL NADU    ','₹8.08 LAKHS','₹16 LPA','₹79 LPA','87.5%'],
            ['104','IIT KANPUR, UTTAR PRADESH ','₹8.38 LAKHS','₹15 LPA','₹62 LPA','85%'],
            ['105','IIT KHARAGPUR, WEST BENGAL','₹8.32 LAKHS','₹17 LPA','₹78 LPA','87%'],
            ['106','IIT ROORKEE, UTTRAKHAND   ','₹8.58 LAKHS','₹14 LPA','₹60 LPA','84%'],
            ['107','IIT GUWAHATI, ASSAM       ','₹8.56 LAKHS','₹16 LPA','₹75 LPA','86%'],
            ['108','IIT HYDERABAD, TELANGANA  ','₹8.93 LAKHS','₹16 LPA','₹58 LPA','86%']]
    cname='none'     #default value of college name
    if r==0:     #printing colleges available
        for i in BTECH1:
            print(i[1])
    if r>=1 and r<=500:     #printing colleges according to rank
        print('_________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME       \t    FEES\tAVG PACKAGE     MAX PACKAGE     PLACEMENT PERCENT")
        print('_________________________________________________________________________________________________')
        for i in BTECH1:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t  '+i[3]+'        '+i[4]+'\t     '+i[5]+'\n')
    elif r>=501 and r<=1000:
        print('_________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME       \t    FEES\tAVG PACKAGE     MAX PACKAGE     PLACEMENT PERCENT")
        print('_________________________________________________________________________________________________')
        for i in range(2,len(BTECH1)):
            print(BTECH1[i][0]+'  '+BTECH1[i][1]+'\t',BTECH1[i][2]+'\t  '+BTECH1[i][3]+'        '+BTECH1[i][4]+'\t     '+BTECH1[i][5]+'\n')
    elif r>=1001 and r<=5000:
        print('_________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME       \t    FEES\tAVG PACKAGE     MAX PACKAGE     PLACEMENT PERCENT")
        print('_________________________________________________________________________________________________')
        for i in range(4,len(BTECH1)):
            print(BTECH1[i][0]+'  '+BTECH1[i][1]+'\t',BTECH1[i][2]+'\t  '+BTECH1[i][3]+'        '+BTECH1[i][4]+'\t     '+BTECH1[i][5]+'\n')
    elif r>5001 and r<=10000:
        print('_________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME       \t    FEES\tAVG PACKAGE     MAX PACKAGE     PLACEMENT PERCENT")
        print('_________________________________________________________________________________________________')
        for i in range(5,len(BTECH1)):
            print(BTECH1[i][0]+'  '+BTECH1[i][1]+'\t',BTECH1[i][2]+'\t  '+BTECH1[i][3]+'        '+BTECH1[i][4]+'\t     '+BTECH1[i][5]+'\n')
    elif r>10000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')     #if no college is available for user the default college name is 'none'
    if r!=0 and r<10000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0     #accepting college id from user
        for i in BTECH1:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:     #if college name is not found then the value in college name will be 'none'
            return('none')
def JEEMAIN(r):
    BTECH2=[['109','NIT TRICHY, TAMIL NADU                                                  ','₹5.63 LAKHS','₹10 LPA','₹70 LPA','83%'],
            ['110','NIT SURATHKAL, KARNATAKA                                                ','₹5.53 LAKHS','₹9 LPA','₹40 LPA','82.5%'],
            ['111','AMRITA VISHWA VIDYAPEETHAM, COIMBATORE, TAMIL NADU (PRIVATE)            ','₹13.10 LAKHS','₹5 LPA','₹13 LPA','71%'],
            ['112','NIT ROURKELA, ODISHA                                                    ', '₹6.40 LAKHS','₹7 LPA','₹39 LPA','81%'],
            ['113','NIT WARANGAL, TELANGANA                                                 ','₹5 LAKHS','₹9 LPA','₹40 LPA','80%'],
            ['114','THAPAR INSTITUTE OF ENGINEERING AND TECHNOLOGY, PATIALA, PUNJAB(PRIVATE)','₹17.08 LAKHS','₹8 LPA','₹38 LPA','69%'],
            ['115','NIT CALICUT, KERALA                                                     ','₹5.48 LAKHS','₹9 LPA','₹50 LPA','79%'],
            ['116','NIT DURGAPUR, WEST BENGAL                                               ','₹5 LAKHS','₹8 LPA','₹33 LPA','77%'],
            ['117','VISVESVARAYA NIT, NAGPUR, MAHARASHTRA                                   ','₹5.50 LAKHS','₹8 LPA','₹22 LPA','75%']]
    cname='none'
    if r==0:
        for i in BTECH2:
            print(i[1])
    if r>=1 and r<=1000:
        print('___________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                  \t    FEES\tAVG PACKAGE\t  MAX PACKAGE     PLACEMENT PERCENT")
        print('___________________________________________________________________________________________________________________________________________________')
        for i in BTECH2:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t  '+i[3]+'\t     '+i[4]+'             '+i[5]+'\n')
    elif r>=1001 and r<=5000:
        print('___________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                  \t    FEES\tAVG PACKAGE\t  MAX PACKAGE     PLACEMENT PERCENT")
        print('___________________________________________________________________________________________________________________________________________________')
        for i in range(2,len(BTECH2)):
            print(BTECH2[i][0]+'  '+BTECH2[i][1]+'\t',BTECH2[i][2]+'\t  '+BTECH2[i][3]+'\t     '+BTECH2[i][4]+'             '+BTECH2[i][5]+'\n')
    elif r>=5001 and r<=12000:
        print('___________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                  \t    FEES\tAVG PACKAGE\t  MAX PACKAGE     PLACEMENT PERCENT")
        print('___________________________________________________________________________________________________________________________________________________')
        for i in range(3,len(BTECH2)):
            print(BTECH2[i][0]+'  '+BTECH2[i][1]+'\t',BTECH2[i][2]+'\t  '+BTECH2[i][3]+'\t     '+BTECH2[i][4]+'             '+BTECH2[i][5]+'\n')
    elif r>12001 and r<=25000:
        print('___________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                  \t    FEES\tAVG PACKAGE\t  MAX PACKAGE     PLACEMENT PERCENT")
        print('___________________________________________________________________________________________________________________________________________________')
        for i in range(5,len(BTECH2)):
            print(BTECH2[i][0]+'  '+BTECH2[i][1]+'\t',BTECH2[i][2]+'\t  '+BTECH2[i][3]+'\t     '+BTECH2[i][4]+'             '+BTECH2[i][5]+'\n')
    elif r>25000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')
    if r!=0 and r<25000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0
        for i in BTECH2:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:
            return('none')
def WBJEE(r):
    BTECH3=[['118','JADAVPUR UNIVERSITY, KOLKATA, WB                          ','₹10 LAKHS','₹10.50 LPA','₹58 LPA','88%'],
            ['119','HALDIA INSTITUTE OF TECHNOLOGY, KOLKATA, WB               ','₹4 LAKHS','₹5 LPA','₹18 LPA','65%'],
            ['120','HERITAGE INSTITUTE OF TECHNOLOGY, KOLKATA, WB             ','₹4 LAKHS','₹5.5 LPA','₹12 LPA','70%'],
            ['121','TECHNO INDIA UNIVERSITY, KOLKATA, WB                      ','₹5 LAKHS','₹3.5 LPA','₹16 LPA','61%'],
            ['122','KALYANI GOVERNMENT ENGINEERING COLLEGE, NADIA, WB         ','₹ 1 LAKH','₹3.5 LPA','₹19 LPA','69%'],
            ['123','(IEM) INSTITUE OF ENGINEERING AND MANAGEMENT, KOLKATA, WB ','₹5.83 LAKHS','₹4.5 LPA','₹10 LPA','68%']]
    cname='none'
    if r==0:
        for i in BTECH3:
            print(i[1])
    if r>=1 and r<=500:
        print('____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                    \t    FEES\tAVG PACKAGE\t  MAX PACKAGE     PLACEMENT PERCENT")
        print('____________________________________________________________________________________________________________________________________')
        for i in BTECH3:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t  '+i[3]+'\t     '+i[4]+'             '+i[5]+'\n')
    elif r>=501 and r<=3000:
        print('____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                    \t    FEES\tAVG PACKAGE\t  MAX PACKAGE     PLACEMENT PERCENT")
        print('____________________________________________________________________________________________________________________________________')
        for i in range(2,len(BTECH3)):
            print(BTECH3[i][0]+'  '+BTECH3[i][1]+'\t',BTECH3[i][2]+'\t  '+BTECH3[i][3]+'\t     '+BTECH3[i][4]+'             '+BTECH3[i][5]+'\n')
    elif r>=3001 and r<=5000:
        print('____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                    \t    FEES\tAVG PACKAGE\t  MAX PACKAGE     PLACEMENT PERCENT")
        print('____________________________________________________________________________________________________________________________________')
        for i in range(3,len(BTECH3)):
            print(BTECH3[i][0]+'  '+BTECH3[i][1]+'\t',BTECH3[i][2]+'\t  '+BTECH3[i][3]+'\t     '+BTECH3[i][4]+'             '+BTECH3[i][5]+'\n')
    elif r>5000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')
    if r!=0 and r<5000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0
        for i in BTECH3:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:
            return('none')
def BITSAT(r):
    BTECH4=[['124','BITS PILANI, RAJASTHAN                           ','₹19.19 LAKHS','₹15 LPA','₹36 LPA','87%'],
            ['125','BITS GOA                                         ','₹19.19LAKHS','₹20 LPA','₹43 LPA','85%'],
            ['126','BITS HYDERABAD, TELANGANA                        ','₹19.19 LAKHS','₹12 LPA','₹20 LPA','77%'],
            ['127','NIIT UNIVERSITY, RAJASTHAN                       ','₹14 LAKHS','₹6.16 LPA','₹24 LPA','67%'],
            ['128','SWAMI RAMA HIMALYAN UNIVERSITY (SRHU), UTTRAKHAND','₹8 LAKHS','₹7 LPA','₹10 LPA','66%']]
    cname='none'
    if r==0:
        for i in BTECH4:
            print(i[1])
    if r>=1 and r<=1000:
        print('____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                         \t    FEES\tAVG PACKAGE\t  MAX PACKAGE     PLACEMENT PERCENT")
        print('____________________________________________________________________________________________________________________________________')
        for i in BTECH4:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t  '+i[3]+'\t     '+i[4]+'             '+i[5]+'\n')
    elif r>=1001 and r<=5000:
        print('____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                  \t    FEES\tAVG PACKAGE\t  MAX PACKAGE     PLACEMENT PERCENT")
        print('____________________________________________________________________________________________________________________________________')
        for i in range(3,len(BTECH4)):
            print(BTECH4[i][0]+'  '+BTECH4[i][1]+'\t',BTECH4[i][2]+'\t  '+BTECH4[i][3]+'\t     '+BTECH4[i][4]+'             '+BTECH4[i][5]+'\n')
    elif r>5000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')
    if r!=0 and r<5000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0
        for i in BTECH4:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:
            return('none')
def VITEEE(r):
    BTECH5=[['129','VELLORE INSTITUTE OF TECHNOLOGY, VELLORE, TAMIL NADU (PRIVATE)','₹7.83 LAKHS','₹8 LPA','₹45 LPA','76%'],
            ['130','VIT CHENNAI, TAMIL NADU                                       ','₹7.83 LAKHS','₹7.25 LPA','₹41 LPA','72%'],
            ['131','VIT BHOPAL, MADHYA PRADESH                                    ','₹7.83₹LAKHS','₹7.25 LPA','₹41 LPA','72%'],
            ['132','VIT AMRAVATI, MAHARASHTRA                                     ','₹7.83LAKHS','₹7.25 LPA','₹41 LPA','72%'],
            ['133','WOXSEN UNIVERSITY, HYDERABAD, TELANGANA                       ','₹12 LAKHS','₹6.5 LPA','₹15 LPA','68%']]
    cname='none'
    if r==0:
        for i in BTECH5:
            print(i[1])
    if r>=1 and r<=1000:
        print('__________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                             \t    FEES\tAVG PACKAGE\t  MAX PACKAGE     PLACEMENT PERCENT")
        print('__________________________________________________________________________________________________________________________________________')
        for i in BTECH5:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t  '+i[3]+'\t     '+i[4]+'             '+i[5]+'\n')
    elif r>=1001 and r<=5000:
        print('__________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                             \t    FEES\tAVG PACKAGE\t  MAX PACKAGE     PLACEMENT PERCENT")
        print('__________________________________________________________________________________________________________________________________________')
        for i in range(2,len(BTECH5)):
            print(BTECH5[i][0]+'  '+BTECH5[i][1]+'\t',BTECH5[i][2]+'\t  '+BTECH5[i][3]+'\t     '+BTECH5[i][4]+'             '+BTECH5[i][5]+'\n')
    elif r>5000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')
    if r!=0 and r<5000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0
        for i in BTECH5:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:
            return('none')
          
