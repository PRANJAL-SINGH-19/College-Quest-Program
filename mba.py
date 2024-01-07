def cat(r):
    cat=[['301','IIM Ahmedabad, Gujarat                                        ', '23.0 L ', '25.0 L', '45.0 LPA', '95%'],
            ['302','IIM Bangalore, Karnataka                                      ', '19.0 L ', '28.6 LPA', '54.0 LPA', '89%'],
            ['303','IIM Calcutta, West Bengal                                     ', '23.0 L ', '27.0 LPA', '75.0 LPA', '83%'],
            ['304','IIM Lucknow, UP                                               ', '19.25 L', '23.5 LPA', '41.0 LPA', '70%'],
            ['305','IIM Indore, MP                                                ', '16.1 L ', '22.0 LPA', '34.0 LPA', '79%'],
            ['306','IIT Kharagpur, West Bengal                                    ', '10.56 L', '22.0 LPA', '56.0 LPA', '86%'],
            ['307','IIM Kozhikode, Kerela                                         ', '20.5 L ', '20.47 LPA', '66.0 LPA', '91%'],
            ['308','Department Of Management, IITDelhi, National Capital Territory', '9.89 L ', '20.01 LPA', '43.0 LPA', '76%'],
            ['309','SJM School Of Management, IITBombay, Maharashtra              ', '8.27 L ', '21.0 LPA', '39.0 LPA', '84%'],
            ['310','IIM Tiruchirappalli, Tamil Nadu                               ', '16.8 L ', '14.5 LPA', '29.0 LPA', '88.9%']]
    if r==0:     #printing colleges available
        for i in cat:
            print(i[1])
    if r>=1 and r<=500:     #printing colleges according to rank
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                           \t FEES           AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in cat:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t  '+i[3]+'\t     '+i[4]+'        '+i[5]+'\n')
    elif r>=501 and r<=1000:
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                           \t FEES           AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in range(2,len(cat)):
            print(cat[i][0]+'  '+cat[i][1]+'\t',cat[i][2]+'\t  '+cat[i][3]+'\t     '+cat[i][4]+'        '+cat[i][5]+'\n')
    elif r>=1001 and r<=5000:
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                           \t FEES           AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in range(4,len(cat)):
            print(cat[i][0]+'  '+cat[i][1]+'\t',cat[i][2]+'\t  '+cat[i][3]+'\t     '+cat[i][4]+'        '+cat[i][5]+'\n')
    elif r>5001 and r<=10000:
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                           \t FEES           AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in range(5,len(cat)):
            print(cat[i][0]+'  '+cat[i][1]+'\t',cat[i][2]+'\t  '+cat[i][3]+'\t     '+cat[i][4]+'        '+cat[i][5]+'\n')
    elif r>10000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')     #if no college is available for user the default college name is 'none'
    if r!=0 and r<10000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0     #accepting college id from user
        for i in cat:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:     #if college name is not found then the value in college name will be 'none'
            return('none')
def cmat(r):
    cmat=[['311','Great Lake Institute, Tamil Nadu     ', '12.25 L', '10.4 LPA', '23 LPA  ', '78%'],
          ['312','KIITSM Bhubaneshwar, Odisha            ', '14.5 L ', '7 LPA   ', '15 LPA  ', '72%'],
          ['313','Alliance School Of Business, Karnataka ', '13.50 L', '13 LPA  ', '21 LPA  ', '71%'],
          ['314','Amity Noida, UP                        ', '04.62 L', '10.5 LPA', '18 LPA  ', '86%'],
          ['315','BIM Noida, UP                          ', '12 L   ', '8.03 LPA', '16 LPA  ', '79%'],
          ['316','Goa Institute Of Management, Goa       ', '18.04 L', '11 LPA  ', '15 LPA  ', '69%'],
          ['317','LPU Jalandhar, Punjab                  ', '5.43 L ', '6.3 LPA ', '11 LPA  ', '75%'],
          ['318','Dept Of Management Pune, Maharashtra   ', '1.29 L ', '5 LPA   ', '7.6 LPA ', '56%'],
          ['319','Xavier Mumbai, Maharashtra             ', '5.2 L  ', '15 LPA  ', '18 LPA  ', '95%'],
          ['320','Global Institute Of Business, Karnataka', '7.25 L ', '6.85 LPA', '12.4 LPA', '87%']]
    if r==0:
        for i in cmat:
            print(i[1])
    if r>=1 and r<=500:
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                 \t FEES           AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in cmat:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t  '+i[3]+'\t     '+i[4]+'        '+i[5]+'\n')
    elif r>=501 and r<=1000:
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                 \t FEES           AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in range(2,len(cmat)):
            print(cmat[i][0]+'  '+cmat[i][1]+'\t',cmat[i][2]+'\t  '+cmat[i][3]+'\t     '+cmat[i][4]+'        '+cmat[i][5]+'\n')
    elif r>=1001 and r<=5000:
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                 \t FEES           AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in range(4,len(cmat)):
            print(cmat[i][0]+'  '+cmat[i][1]+'\t',cmat[i][2]+'\t  '+cmat[i][3]+'\t     '+cmat[i][4]+'        '+cmat[i][5]+'\n')
    elif r>5001 and r<=10000:
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                 \t FEES           AVG PACKAGE       MAX PACKAGE  PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in range(5,len(cmat)):
            print(cmat[i][0]+'  '+cmat[i][1]+'\t',cmat[i][2]+'\t  '+cmat[i][3]+'\t     '+cmat[i][4]+'        '+cmat[i][5]+'\n')
    elif r>10000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')
    if r!=0 and r<10000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0
        for i in cmat:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:
            return('none')
def xat(r):
    xat=[['321','XLRI Jamshedpur, Jharkhand                            ', '25.8 L ', '23 LPA  ', '67 LPA   ', '98%'],
            ['322','Great Lakes Institute Of Management, Tamil Nadu       ', '13.25 L', '10.4 L  ', '18 LPA   ', '87%'],
            ['323','Xavier Bhubhaneshwar, Odisha                          ', '20.3 L ', '15 LPA  ', '27 LPA   ', '79%'],
            ['324','IMT Ghaziabad, UP                                     ', '19.4 L ', '12 LPA  ', '18.97 LPA', '86%'],
            ['325','Loyola Institue Of Business Administration, Tamil Nadu', '17.2 L ', '9 LPA   ', '17.9 LPA ', '81%'],
            ['326','SIMSREE Mumbai, Maharashtra                           ', '1.34 L ', '10.2 LPA', '15.6 LPA ', '86.9%']]
    if r==0:
        for i in xat:
            print(i[1])
    if r>=1 and r<=1000:
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                 \t FEES           AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in xat:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t  '+i[3]+'\t     '+i[4]+'        '+i[5])
    elif r>=1001 and r<=5000:
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                 \t FEES           AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in range(2,len(xat)):
            print(xat[i][0]+'  '+xat[i][1]+'\t',xat[i][2]+'\t  '+xat[i][3]+'\t     '+xat[i][4]+'        '+xat[i][5]+'\n')
    elif r>5000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')
    if r!=0 and r<5000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0
        for i in xat:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:
            return('none')
def snap(r):
    snap=[['327','Symbiosis Institute Pune, Maharashtra               ', '15.2 L ', '18 LPA ', '24 LPA  ', '89%'],
            ['328','Symbiosis Insitute Hyderabad, Telangana             ', '16.1 L ', '19 LPA ', '27.7 LPA', '96%'],
            ['329','Symbiosis Centre Of Managament & HRD, Maharashtra   ', '15.76 L', '15 LPA ', '20 LPA  ', '87%'],
            ['330','LM Thapar School Of Management, Punjab              ', '8 L    ', '5.6 LPA', '7.9 LPA ', '76%'],
            ['331','Symbiosis Institue Of Management Nagpur, Maharashtra', '16 L   ', '12 LPA ', '17.2 LPA', '80%']]
    if r==0:
        for i in snap:
            print(i[1])
    if r>=1 and r<=1000:
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                 \t FEES           AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in snap:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t  '+i[3]+'\t     '+i[4]+'        '+i[5]+'\n')
    elif r>=1001 and r<=5000:
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                 \t FEES           AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in range(2,len(snap)):
            print(snap[i][0]+'  '+snap[i][1]+'\t',snap[i][2]+'\t  '+snap[i][3]+'\t     '+snap[i][4]+'        '+snap[i][5]+'\n')
    elif r>5000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')
    if r!=0 and r<5000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0
        for i in snap:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:
            return('none')
def mat(r):
    mat=[['332','School Of Management BML, Haryana              ', '11 L  ', '8 LPA  ', '9 LPA   ', '94%'],
         ['333','PSG College Coimbatore, Tamil Nadu                ', '8 L   ', '5.8 LPA', '9 LPA   ', '74%'],
         ['334','Department Of Management And Sciences, Maharashtra', '1.35 L', '8 LPA  ', '15.3 LPA', '78%'],
         ['335','Christ University, Tamil Nadu                     ', '4.6 L ', '7 LPA  ', '12 LPA  ', '79.4%']]
    if r==0:
        for i in mat:
            print(i[1])
    if r>=1 and r<=1000:
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                        \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in mat:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t  '+i[3]+'\t     '+i[4]+'        '+i[5]+'\n')
    elif r>=1001 and r<=5000:
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                        \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in range(2,len(mat)):
            print(mat[i][0]+'  '+mat[i][1]+'\t',mat[i][2]+'\t  '+mat[i][3]+'\t     '+mat[i][4]+'        '+mat[i][5]+'\n')
    elif r>5000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')
    if r!=0 and r<5000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0
        for i in mat:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:
            return('none')
