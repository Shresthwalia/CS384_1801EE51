import csv
import os
from os import stat
import shutil
import re
patternroll = re.compile(r'^[0-9]{4}[A-Za-z]{2}[0-9]{2}$')
patternsem_credit = re.compile(r'^[0-9]+$')
pattern = re.compile(r'^[A-Z]{2}[0-9]{3}$', re.I)
patterncredit = re.compile(r'AA|AB|BC|BB|CC|CD|DD|I|F', re.I)
if(os.path.isdir(r'./grades')):
    shutil.rmtree('./grades')
os.makedirs('./grades')

rolllist = []
header = ['roll', 'subject', 'credit', 'type', 'grade', 'semester']
file = open('./grades/misc.csv', 'a', newline='')
with file:
    mw = csv.writer(file)
    mw.writerow(header)
file = open('./acad_res_stud_grades.csv', 'r')
with file:
    reader = csv.reader(file)
    for row in reader:
        if(not row[0] == 'sl'):
            if(not (re.fullmatch(patternroll, row[1]) and re.fullmatch(patternsem_credit, row[2]) and re.fullmatch(patternsem_credit, row[5]) and re.fullmatch(pattern, row[4]) and re.fullmatch(patterncredit, row[6]))):
                file = open('./grades/misc.csv', 'a', newline='')
                with file:
                    mw = csv.writer(file)
                    lis1 = [row[1], row[4], row[5], row[8], row[6], row[2]]
                    mw.writerow(lis1)
                continue
            rollno1 = row[1]+'_individual.csv'
            if(not os.path.isfile('./grades/'+rollno1)):
                rolllist.append(row[1])
                mainl = open('./grades/'+rollno1, 'a', newline='')
                with mainl:
                    mw = csv.writer(mainl)
                    mw.writerow(['Roll: '+row[1]])
                    mw.writerow(['Semester Wise Details'])
                    mw.writerow(['Subject', 'Credits', 'Type', 'Grade', 'Sem'])
            lis1 = [row[4], row[5], row[8], row[6], row[2]]
            mainl = open('./grades/'+rollno1, 'a', newline='')
            with mainl:
                mw = csv.writer(mainl)
                mw.writerow(lis1)
#overall starts here
lis = []
for roll in rolllist:
    file = open('./grades/'+roll+'_individual.csv', 'r')
    with file:
        reader = csv.reader(file)
        for row in reader:
            if(re.fullmatch(pattern, row[0])):
                lis.append(row)
    slis = sorted(lis, key=lambda l: int(l[4]))
    lis.clear()
    prev = '0'
    status = True
    for li in slis:
        if(int(li[4])-int(prev) > 1):
            status = False
            break
        prev = li[4]
    if status == False:
        for ros in slis:
            lt = [roll,ros[0],ros[1],ros[2],ros[3],ros[4]]
            main1 = open('./grades/misc.csv', 'a', newline='')
            with main1:
                mw = csv.writer(main1)
                mw.writerow(lt)
        os.remove('./grades/'+roll+'_individual.csv')
        continue
    mainl = open('./grades/'+roll+'_overall.csv', 'a', newline='')
    with mainl:
        mw = csv.writer(mainl)
        mw.writerow(['Roll: '+roll])
        mw.writerow(['Semester', 'Semester Credits', 'Semester Credits Cleared',
                     'SPI', 'Total Credits', 'Total Credits Cleared', 'CPI'])
    grades = {'AA': 10, 'AB': 9, 'BB': 8, 'BC': 7,
              'CC': 6, 'CD': 5, 'DD': 4, 'F': 0, 'I': 0}
    currenttotal = 0
    currenttotalcleared = 0
    overalltotal = 0
    overalltotalcleared = 0
    cursem = 'W'
    spi1intocredits = 0
    cpiintocredits = 0
    for row in slis:
        if(cursem == 'W'):
            cursem = row[4]
        if(cursem == row[4]):
            currenttotal += int(row[1])
            if(grades[row[3]] > 0):
                currenttotalcleared += int(row[1])
                overalltotalcleared += int(row[1])
            spi1intocredits += (grades[row[3]]*int(row[1]))
            overalltotal += int(row[1])
        else:
            cpiintocredits += spi1intocredits
            lisc = [cursem, currenttotal, currenttotalcleared, spi1intocredits /
                    currenttotal, overalltotal, overalltotalcleared, cpiintocredits/overalltotal]
            mainl = open('./grades/'+roll+'_overall.csv', 'a', newline='')
            with mainl:
                mw = csv.writer(mainl)
                mw.writerow(lisc)
            cursem = row[4]
            currenttotal = int(row[1])
            if(grades[row[3]] > 0):
                currenttotalcleared = int(row[1])
                overalltotalcleared += int(row[1])
            spi1intocredits = (grades[row[3]]*int(row[1]))
            overalltotal += int(row[1])

    cpiintocredits += spi1intocredits
    lisc = [cursem, currenttotal, currenttotalcleared, spi1intocredits /
            currenttotal, overalltotal, overalltotalcleared, cpiintocredits/overalltotal]
    mainl = open('./grades/'+roll+'_overall.csv', 'a', newline='')
    with mainl:
        mw = csv.writer(mainl)
        mw.writerow(lisc)