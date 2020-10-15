import csv
import os
import shutil
import re
import datetime
os.system('cls')

def course():
    # Read csv and process
    pass


def country():
    # Read csv and process
    if(not os.path.isdir(r'C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics')):
        os.makedirs('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics')
    if(os.path.isdir(r'C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/country')):
        shutil.rmtree('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/country')
    os.makedirs('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/country')
    path='C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/country'
    mainlist = open('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/studentinfo_cs384.csv', 'r')
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
country()

def email_domain_extract():
    # Read csv and process
    if(not os.path.isdir(r'C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics')):
        os.makedirs('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics')
    if(os.path.isdir(r'C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/email_domain')):
        shutil.rmtree('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/email_domain')
    os.makedirs('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/email_domain')
    path='C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/email_domain'
    mainlist = open('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/studentinfo_cs384.csv', 'r')
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
email_domain_extract()

def gender():
    # Read csv and process
    if(not os.path.isdir(r'C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics')):
        os.makedirs('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics')
    if(os.path.isdir(r'C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/gender')):
        shutil.rmtree('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/gender')
    os.makedirs('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/gender')
    mainlist = open('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/studentinfo_cs384.csv', 'r')
    with mainlist:
        reader=csv.reader(mainlist)
        for row in reader:
            if(row[4]=='Male'):
                male = open('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/gender/male.csv','a',newline='')
                with male:
                    mw=csv.writer(male)
                    mw.writerow(row)
            elif(row[4]=='Female'):
                female =open('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/gender/female.csv','a',newline='')
                with female:
                    fw=csv.writer(female)
                    fw.writerow(row)
            else:
                male = open('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/gender/male.csv','a',newline='')
                with male:
                    mw=csv.writer(male)
                    mw.writerow(row) 
                female =open('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/gender/female.csv','a',newline='')
                with female:
                    fw=csv.writer(female)
                    fw.writerow(row)
                          
    pass

gender()
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
    if(not os.path.isdir(r'C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics')):
        os.makedirs('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics')
    if(os.path.isdir(r'C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/dob')):
        shutil.rmtree('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/dob')
    os.makedirs('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/dob')
    path='C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/dob'
    category1='C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/dob/bday_1995_1999.csv'
    category2='C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/dob/bday_2000_2004.csv'
    category3='C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/dob/bday_2005_2009.csv'
    category4='C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/dob/bday_2010_2014.csv'
    category5='C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/dob/bday_2015_2020.csv'
    category6='C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/dob/misc.csv'
    mainlist = open('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/studentinfo_cs384.csv', 'r')
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

dob()
def state():
    # Read csv and process
    if(not os.path.isdir(r'C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics')):
        os.makedirs('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics')
    if(os.path.isdir(r'C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/state')):
        shutil.rmtree('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/state')
    os.makedirs('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/state')
    path='C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/state'
    mainlist = open('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/studentinfo_cs384.csv', 'r')
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
state()

def blood_group():
    # Read csv and process
    if(not os.path.isdir(r'C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics')):
        os.makedirs('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics')
    if(os.path.isdir(r'C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/blood_group')):
        shutil.rmtree('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/blood_group')
    os.makedirs('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/blood_group')
    path='C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/analytics/blood_group'
    mainlist = open('C:/Users/Shrestha Walia/CS384_1801EE51/Assignment3/studentinfo_cs384.csv', 'r')
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

blood_group()
# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass
