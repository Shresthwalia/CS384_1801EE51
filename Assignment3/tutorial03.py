import csv
import os
import shutil
import re
import datetime
os.system('cls')

def del_create_analytics_folder():
    # del the analytics folder including subfolder
    # mkdir the analytics folder (only mkdir)
    if(os.path.isdir(r'./analytics')):
        shutil.rmtree('./analytics')
    os.makedirs('./analytics')
    pass

def course():
    # Read csv and process
    pass


def country():
    # Read csv and process
    if(not os.path.isdir(r'./analytics')):
        os.makedirs('./analytics')
    if(os.path.isdir(r'./analytics/country')):
        shutil.rmtree('./analytics/country')
    os.makedirs('./analytics/country')
    path='./analytics/country'
    mainlist = open('./studentinfo_cs384.csv', 'r')
    with mainlist:
        reader=csv.reader(mainlist)
        for row in reader:
            if(row[0]=='id'):
               temp=row 
            countryname=row[2]+'.csv'
            pa=os.path.join(path,countryname)
            if(not row[0]=='id'):
                if(not os.path.isfile(pa)):
                    mainl = open(pa, 'w',newline='')
                    with mainl:
                        mw=csv.writer(mainl)
                        mw.writerow(temp)
            if(not row[0]=='id'):
                mainl = open(pa, 'a',newline='')
                with mainl:
                    mw=csv.writer(mainl)
                    mw.writerow(row)

    pass

def email_domain_extract():
    # Read csv and process
    if(not os.path.isdir(r'./analytics')):
        os.makedirs('./analytics')
    if(os.path.isdir(r'./analytics/email_domain')):
        shutil.rmtree('./analytics/email_domain')
    os.makedirs('./analytics/email_domain')
    path='./analytics/email_domain'
    mainlist = open('./studentinfo_cs384.csv', 'r')
    pattern = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,18}$')
    with mainlist:
        reader=csv.reader(mainlist)
        for row in reader:
            if(row[0]=='id'):
               temp=row 
            if(not row[0]=='id'):
                if(re.match(pattern,row[3])):
                    res = row[3][row[3].index('@')+1:] 
                    ret=res[:res.index('.')]
                    pi=os.path.join(path,ret+'.csv')
                    if(not os.path.isfile(pi)):
                        mainl = open(pi, 'w',newline='')
                        with mainl:
                            mw=csv.writer(mainl)
                            mw.writerow(temp)
                    mainl = open(pi, 'a',newline='')
                    with mainl:
                        mw=csv.writer(mainl)
                        mw.writerow(row)
                else:
                    pi=os.path.join(path,'misc.csv')
                    if(not os.path.isfile(pi)):
                        mainl = open(pi, 'w',newline='')
                        with mainl:
                            mw=csv.writer(mainl)
                            mw.writerow(temp)
                    mainl = open(pi, 'a',newline='')
                    with mainl:
                        mw=csv.writer(mainl)
                        mw.writerow(row)
    pass

def gender():
    # Read csv and process
    if(not os.path.isdir(r'./analytics')):
        os.makedirs('./analytics')
    if(os.path.isdir(r'./analytics/gender')):
        shutil.rmtree('./analytics/gender')
    os.makedirs('./analytics/gender')
    mainlist = open('./studentinfo_cs384.csv', 'r')
    with mainlist:
        reader=csv.reader(mainlist)
        for row in reader:
            if(row[4]=='Male'):
                male = open('./analytics/gender/male.csv','a',newline='')
                with male:
                    mw=csv.writer(male)
                    mw.writerow(row)
            elif(row[4]=='Female'):
                female =open('./analytics/gender/female.csv','a',newline='')
                with female:
                    fw=csv.writer(female)
                    fw.writerow(row)
            else:
                male = open('./analytics/gender/male.csv','a',newline='')
                with male:
                    mw=csv.writer(male)
                    mw.writerow(row) 
                female =open('./analytics/gender/female.csv','a',newline='')
                with female:
                    fw=csv.writer(female)
                    fw.writerow(row)
                          
    pass

def date_validation(day, month, year): 
      
    isValidDate = True
    try : 
        datetime.datetime(int(year),  
                          int(month), int(day)) 
          
    except ValueError : 
        isValidDate = False
    if((int(year))<1995 or (int(year))>2020):
        isValidDate = False
    return isValidDate
def dob():
    # Read csv and process
    if(not os.path.isdir(r'./analytics')):
        os.makedirs('./analytics')
    if(os.path.isdir(r'./analytics/dob')):
        shutil.rmtree('./analytics/dob')
    os.makedirs('./analytics/dob')
    path='./analytics/dob'
    category1='./analytics/dob/bday_1995_1999.csv'
    category2='./analytics/dob/bday_2000_2004.csv'
    category3='./analytics/dob/bday_2005_2009.csv'
    category4='./analytics/dob/bday_2010_2014.csv'
    category5='./analytics/dob/bday_2015_2020.csv'
    category6='./analytics/dob/misc.csv'
    mainlist = open('./studentinfo_cs384.csv', 'r')
    with mainlist:
        reader=csv.reader(mainlist)
        for row in reader:
            if(row[0]=='id'):
                m1=open(category1,'w',newline='')
                with m1:
                        mw=csv.writer(m1)
                        mw.writerow(row)
                m2=open(category2,'w',newline='')
                with m2:
                        mw=csv.writer(m2)
                        mw.writerow(row)
                m3=open(category3,'w',newline='')
                with m3:
                        mw=csv.writer(m3)
                        mw.writerow(row)
                m4=open(category4,'w',newline='')
                with m4:
                        mw=csv.writer(m4)
                        mw.writerow(row)
                m5=open(category5,'w',newline='')
                with m5:
                        mw=csv.writer(m5)
                        mw.writerow(row)
                m6=open(category6,'w',newline='')
                with m6:
                        mw=csv.writer(m6)
                        mw.writerow(row)
            else:
                res = row[5].split('-')
                if(not date_validation(res[0],res[1],res[2])):
                    m6=open(category6,'a',newline='')
                    with m6:
                        mw=csv.writer(m6)
                        mw.writerow(row)
                elif((int(res[2]))>=1995 and (int(res[2]))<=1999):
                    m1=open(category1,'a',newline='')
                    with m1:
                        mw=csv.writer(m1)
                        mw.writerow(row)
                elif((int(res[2]))>=2000 and (int(res[2]))<=2004):
                    m2=open(category2,'a',newline='')
                    with m2:
                        mw=csv.writer(m2)
                        mw.writerow(row)
                elif((int(res[2]))>=2005 and (int(res[2]))<=2009):
                    m3=open(category3,'a',newline='')
                    with m3:
                        mw=csv.writer(m3)
                        mw.writerow(row)
                elif((int(res[2]))>=2010 and (int(res[2]))<=2014):
                    m4=open(category4,'a',newline='')
                    with m4:
                        mw=csv.writer(m4)
                        mw.writerow(row)
                elif((int(res[2]))>=2015 and (int(res[2]))<=2020):
                    m5=open(category5,'a',newline='')
                    with m5:
                        mw=csv.writer(m5)
                        mw.writerow(row)
    pass

def state():
    # Read csv and process
    if(not os.path.isdir(r'./analytics')):
        os.makedirs('./analytics')
    if(os.path.isdir(r'./analytics/state')):
        shutil.rmtree('./analytics/state')
    os.makedirs('./analytics/state')
    path='./analytics/state'
    mainlist = open('./studentinfo_cs384.csv', 'r')
    with mainlist:
        reader=csv.reader(mainlist)
        for row in reader:
            if(row[0]=='id'):
               temp=row 
            statename=row[7]+'.csv'
            pa=os.path.join(path,statename)
            if(not row[0]=='id'):
                if(not os.path.isfile(pa)):
                    mainl = open(pa, 'w',newline='')
                    with mainl:
                        mw=csv.writer(mainl)
                        mw.writerow(temp)
            if(not row[0]=='id'):
                mainl = open(pa, 'a',newline='')
                with mainl:
                    mw=csv.writer(mainl)
                    mw.writerow(row)
    pass

def blood_group():
    # Read csv and process
    if(not os.path.isdir(r'./analytics')):
        os.makedirs('./analytics')
    if(os.path.isdir(r'./analytics/blood_group')):
        shutil.rmtree('./analytics/blood_group')
    os.makedirs('./analytics/blood_group')
    path='./analytics/blood_group'
    mainlist = open('./studentinfo_cs384.csv', 'r')
    with mainlist:
        reader=csv.reader(mainlist)
        for row in reader:
            if(row[0]=='id'):
               temp=row 
            bloodname=row[6]+'.csv'
            pa=os.path.join(path,bloodname)
            if(not row[0]=='id'):
                if(not os.path.isfile(pa)):
                    mainl = open(pa, 'w',newline='')
                    with mainl:
                        mw=csv.writer(mainl)
                        mw.writerow(temp)
            if(not row[0]=='id'):
                mainl = open(pa, 'a',newline='')
                with mainl:
                    mw=csv.writer(mainl)
                    mw.writerow(row)
    pass

# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    if(not os.path.isdir(r'./analytics')):
        os.makedirs('./analytics')
    temp=['id','first name','last name','country','email','gender','dob','blood group','state']
    new_fil=open('./analytics/studentinfo_cs384_names_split.csv','a',newline='')
    with new_fil:
        mw=csv.writer(new_fil)
        mw.writerow(temp)
    mainlist = open('./studentinfo_cs384.csv', 'r')
    with mainlist:
        reader=csv.reader(mainlist)
        for row in reader:
            if(row[0] != 'id'):
                name_split = row[1].split(' ')
                first_name = name_split[0]
                last_name = name_split[1:]
                last=''
                for i in last_name:
                    last=last+i+' '
                temp = [row[0], first_name, last, row[2],
                        row[3], row[4], row[5], row[6], row[7]]
                newf=open('./analytics/studentinfo_cs384_names_split.csv', 'a',newline='')
                with newf:
                    mw=csv.writer(newf)
                    mw.writerow(temp) 
    pass
