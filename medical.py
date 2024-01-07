
def aiims(r):
    aiims=[['401','AIIMS DELHI, NEW DELHI          ', '8.5L', '26.6L', '69.0L', '74.81%'],
            ['402','AIIMS BHOPAL, MADHYA PRADESH    ', '6.9L', '28.0L', '64.5L', '73.15%'],
            ['403','AIIMS BHUBHNESHWAR, ODISHA      ', '6.9L', '27.7L', '64.7L', '79.51%'],
            ['404','AIIMS JODHPUR, RAJASTHAN        ', '5.8L', '27.6L', '69.8L', '73.59%'],
            ['405','AIIMS PATNA, BIHAR              ', '9.4L', '26.7L', '62.4L', '75.59%'],
            ['406','AIIMS RAIPUR, CHHATISGARH       ', '8.9L', '27.1L', '69.5L', '79.5%'],
            ['407','AIIMS RISHIKESH, UTTARAKHAND    ', '7.4L', '30.7L', '64.1L', '76.9%'],
            ['408','AIIMS RAEBARELI, UTTAR PRADESH  ', '6.3L', '29.1L', '64.5L', '70.33%'],
            ['409','AIIMS NAGPUR, MAHARASHTRA       ', '5.4L', '28.5L', '69.7L', '71.37%'],
            ['410','AIIMS MANGALGIRI, ANDHRA PRADESH', '5.3L', '26.4L', '62.9L', '77.35%']]
    if r==0:     #printing colleges available
        for i in aiims:
            print(i[1])
    if r>=1 and r<=500:     #printing colleges according to rank
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME        \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in aiims:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t      '+i[3]+'\t       '+i[4]+'        '+i[5]+'\n')
    elif r>=501 and r<=1000:
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME        \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in range(2,len(aiims)):
            print(aiims[i][0]+'  '+aiims[i][1]+'\t',aiims[i][2]+'\t      '+aiims[i][3]+'\t       '+aiims[i][4]+'        '+aiims[i][5]+'\n')
    elif r>=1001 and r<=5000:
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME        \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in range(4,len(aiims)):
            print(aiims[i][0]+'  '+aiims[i][1]+'\t',aiims[i][2]+'\t      '+aiims[i][3]+'\t       '+aiims[i][4]+'        '+aiims[i][5]+'\n')
    elif r>5001 and r<=10000:
        print('_____________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME        \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('_____________________________________________________________________________________________________________________________________')
        for i in range(5,len(aiims)):
            print(aiims[i][0]+'  '+aiims[i][1]+'\t',aiims[i][2]+'\t      '+aiims[i][3]+'\t       '+aiims[i][4]+'        '+aiims[i][5]+'\n')
    elif r>10000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')     #if no college is available for user the default college name is 'none'
    if r!=0 and r<10000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0     #accepting college id from user
        for i in aiims:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:     #if college name is not found then the value in college name will be 'none'
            return('none')

def neet(r):
    neet=[['411','St Johns Medical College, Bangalore, KARNATAKA                                    ', '6.0L', '29.4L', '44.9L', '54.79%'],
            ['412','CMC Vellore - Christian Medical College, TAMIL NADU                               ', '6.3L', '27.0L', '41.3L', '55.23%'],
            ['413','KMC Mangalore - Kasturba Medical College, KARNATAKA                               ', '8.9L', '21.5L', '45.0L', '54.97%'],
            ['414','AFMC Pune - Armed Forces Medical College, MAHARASHTRA                             ', '8.3L', '23.8L', '49.3L', '51.27%'],
            ['415','KPC Medical College and Hospital, Jadavpur, WEST BENGAL                           ', '7.0L', '20.3L', '48.5L', '50.46%'],
            ['416','Maulana Azad Medical College, New Delhi, DELHI                                    ', '7.8L', '25.1L', '49.7L', '51.86%'],
            ['417','HIMSR New Delhi - Hamdard Institute of Medical Sciences and Research, DELHI       ', '8.2L', '20.4L', '44.5L', '58.0%'],
            ['418','Grant Medical College, Mumbai, MAHARASHTRA                                        ', '8.3L', '27.9L', '49.5L', '50.7%'],
            ['419','IMS BHU- Institute of Medical Sciences Banaras Hindu University, UTTAR PRADESH    ', '5.3L', '26.8L', '49.2L', '56.07%'],
            ['420','IIMSR Lucknow - Integral Institute of Medical Sciences and Research, UTTAR PRADESH', '8.1L', '29.1L', '45.9L', '58.15%']]
    if r==0:
        for i in neet:
            print(i[1])
    if r>=1 and r<=1000:
        print('________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                          \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('________________________________________________________________________________________________________________________________________________')
        for i in neet:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t      '+i[3]+'\t       '+i[4]+'        '+i[5]+'\n')
    elif r>=1001 and r<=5000:
        print('________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                          \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('________________________________________________________________________________________________________________________________________________')
        for i in range(2,len(neet)):
            print(neet[i][0]+'  '+neet[i][1]+'\t',neet[i][2]+'\t      '+neet[i][3]+'\t       '+neet[i][4]+'        '+neet[i][5]+'\n')
    elif r>=5001 and r<=12000:
        print('________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                          \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('________________________________________________________________________________________________________________________________________________')
        for i in range(4,len(neet)):
            print(neet[i][0]+'  '+neet[i][1]+'\t',neet[i][2]+'\t      '+neet[i][3]+'\t       '+neet[i][4]+'        '+neet[i][5]+'\n')
    elif r>12001 and r<=25000:
        print('________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                          \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('________________________________________________________________________________________________________________________________________________')
        for i in range(5,len(neet)):
            print(neet[i][0]+'  '+neet[i][1]+'\t',neet[i][2]+'\t      '+neet[i][3]+'\t       '+neet[i][4]+'        '+neet[i][5]+'\n')
    elif r>25000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')
    if r!=0 and r<25000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0
        for i in neet:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:
            return('none')
def mcat(r):
    mcat=[['421','S. R. M. Institute of Science and Technology, TAMIL NADU          ', '8.3L', '16.4L', '40.0L', '51.34%'],
            ['422','Kalinga Institute of Industrial Technology, ODISHA                ', '9.3L', '15.5L', '35.3L', '58.94%'],
            ['423','Saveetha Institute of Medical and Technical Sciences, TAMIL NADU  ', '7.7L', '15.4L', '35.4L', '51.26%'],
            ['424','Annamalai University, TAMIL NADU                                  ', '6.7L', '21.9L', '40.9L', '55.18%'],
            ['425','K. S. Hegde Medical Academy, KARNATAKA                            ', '6.8L', '22.9L', '42.1L', '56.6%'],
            ['426','Krishna Institute of Medical Sciences, MAHARASHTRA                ', '7.5L', '17.0L', '41.8L', '58.86%'],
            ['427','Sri Venkateswara Institute of Medical Sciences, ANDHRA PRADESH    ', '5.1L', '19.2L', '36.9L', '55.17%'],
            ['428','REGIONAL INSTITUTE OF MEDICAL SCIENCES, MANIPUR                   ', '5.7L', '19.5L', '41.1L', '50.15%'],
            ['429','MAHATMA GANDHI MEDICAL COLLEGE AND RESEARCH INSTITUTE, PONDICHERRY', '5.8L', '23.1L', '37.2L', '58.01%'],
            ['430','CHRISTIAN MEDICAL COLLEGE, TAMIL NADU                             ', '7.7L', '23.4L', '37.7L', '54.98%']]
    if r==0:
        for i in mcat:
            print(i[1])
    if r>=1 and r<=500:
        print('________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                        \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('________________________________________________________________________________________________________________________________________________')
        for i in mcat:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t      '+i[3]+'\t       '+i[4]+'        '+i[5]+'\n')
    elif r>=501 and r<=3000:
        print('________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                        \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('________________________________________________________________________________________________________________________________________________')
        for i in range(1,len(mcat)):
            print(mcat[i][0]+'  '+mcat[i][1]+'\t',mcat[i][2]+'\t      '+mcat[i][3]+'\t       '+mcat[i][4]+'        '+mcat[i][5]+'\n')
    elif r>=3001 and r<=5000:
        print('________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                        \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('________________________________________________________________________________________________________________________________________________')
        for i in range(3,len(mcat)):
            print(mcat[i][0]+'  '+mcat[i][1]+'\t',mcat[i][2]+'\t      '+mcat[i][3]+'\t       '+mcat[i][4]+'        '+mcat[i][5]+'\n')
    else:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')
    if r!=0 and r<5000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0
        for i in mcat:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:
            return('none')

def pgimer(r):
    pgimer=[['431','Kasturba Medical College, Karnataka                     ', '5.1L', '24.8L', '42.4L', '56.14%'],
            ['432','Jamia Hamdard,New Delhi, Delhi                          ', '8.9L', '22.5L', '37.0L', '59.95%'],
            ['433','Siksha `O` Anusandhan, Odisha                           ', '9.6L', '17.2L', '35.2L', '54.04%'],
            ['434','Dr. D. Y. Patil Vidyapeeth, Maharashtra                 ', '7.9L', '24.7L', '38.6L', '59.26%'],
            ['435','Govt. Medical College & Hospital, Chandigarh            ', '9.0L', '21.9L', '40.2L', '57.74%'],
            ['436','Dayanand Medical College, Punjab                        ', '7.1L', '19.3L', '36.5L', '51.24%'],
            ['437','Sawai Man Singh Medical College, Rajasthan              ', '8.0L', '18.3L', '44.3L', '55.16%'],
            ['438','PSG Institute of Medical Sciences & Research, Tamil Nadu', '5.1L', '17.7L', '36.3L', '53.96%'],
            ['439','Datta Meghe Institute of Medical Sciences, Maharashtra  ', '8.0L', '21.5L', '38.8L', '56.75%'],
            ['440','M. S. Ramaiah Medical College, Karnataka                ', '7.1L', '19.6L', '43.6L', '59.86%']]
    if r==0:
        for i in pgimer:
            print(i[1])
    if r>=1 and r<=1000:
        print('________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                    \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('________________________________________________________________________________________________________________________________________________')
        for i in pgimer:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t      '+i[3]+'\t       '+i[4]+'        '+i[5]+'\n')
    elif r>=1001 and r<=5000:
        print('________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                    \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('________________________________________________________________________________________________________________________________________________')
        for i in range(3,len(pgimer)):
            print(pgimer[i][0]+'  '+pgimer[i][1]+'\t',pgimer[i][2]+'\t      '+pgimer[i][3]+'\t       '+pgimer[i][4]+'        '+pgimer[i][5]+'\n')
    elif r>5000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')
    if r!=0 and r<5000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0
        for i in pgimer:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:
            return('none')

def jipmer(r):
    jipmer=[['441','Jawaharlal Institute of Postgraduate Medical Education & Research, Pondicherry', '5.5L', '24.4L', '43.8L', '58.28%'],
            ['442','Christian Medical College, Vellore                                            ', '7.1L', '24.2L', '44.9L', '55.81%'],
            ['443','Kasturba Medical College, Manipal                                             ', '7.8L', '20.8L', '35.3L', '53.08%'],
            ['444','Sri Ramachandra Medical College and Research Institute, Chennai               ', '5.1L', '16.5L', '42.8L', '59.17%'],
            ['445','Hamdard Institute of Medical Sciences and Research, New Delhi                 ', '5.9L', '22.7L', '43.5L', '56.34%'],
            ['446','M S Ramaiah Medical College, Bangalore                                        ', '8.4L', '21.6L', '44.3L', '53.62%'],
            ['447','Dayanand Medical College and Hospital, Ludhiana, Punjab                       ', '6.9L', '21.7L', '37.6L', '59.0%'],
            ['448','Kasturba Medical College, Mangalore, KARNATAKA                                ', '5.6L', '22.1L', '42.2L', '59.09%'],
            ['449','Kalinga Institute of Medical Sciences, Bhubaneswar, ODISHA                    ', '6.2L', '20.4L', '43.2L', '50.17%'],
            ['450','SRM Medical College Hospital and Research Centre, Chennai, TAMIL NADU         ', '6.7L', '17.9L', '43.4L', '54.42%']]
    if r==0:
        for i in jipmer:
            print(i[1])
    if r>=1 and r<=1000:
        print('________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                        \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('________________________________________________________________________________________________________________________________________________')
        for i in jipmer:
            print(i[0]+'  '+i[1]+'\t',i[2]+'\t      '+i[3]+'\t       '+i[4]+'        '+i[5]+'\n')
    elif r>=1001 and r<=5000:
        print('________________________________________________________________________________________________________________________________________________')
        print("CNO         COLLEGE NAME                                                        \t FEES     AVG PACKAGE       MAX PACKAGE    PLACEMENT %")
        print('________________________________________________________________________________________________________________________________________________')
        for i in range(2,len(jipmer)):
            print(jipmer[i][0]+'  '+jipmer[i][1]+'\t',jipmer[i][2]+'\t      '+jipmer[i][3]+'\t       '+jipmer[i][4]+'        '+jipmer[i][5]+'\n')
    elif r>5000:
        print('NO COLLEGE AVAILABLE FOR YOU.');return('none')
    if r!=0 and r<5000:
        cn=input("Enter College Number (IF NO COLLEGE IS AVAILABLE FOR YOU THEN ENTER 'NONE'):");cname='';c=0
        for i in jipmer:
            if cn==i[0]:
                cname=i[1]
                return(cname);c+=1
        if c==0:
            return('none')
