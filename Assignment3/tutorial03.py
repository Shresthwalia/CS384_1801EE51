import csv
import os
import shutil
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
    pass


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
def dob():
    # Read csv and process
    pass


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
