from math import floor
import csv
import pandas as pd
import shutil
import os
def deletepreviouswork():
    if os.path.exists(r'./groups'):
        shutil.rmtree(r'./groups')
    os.mkdir(r'./groups')
    if os.path.exists(r'./branches'):
        shutil.rmtree(r'./branches')
    os.mkdir(r'./branches')
    return 
def group_allocation(filename, groups_no):
    # Entire Logic
    # You can add more functions, but in the test case, we will only call the group_allocation() method,
    file = open(r'./'+filename, 'r')
    with file:
        alltheentries = csv.reader(file)
        temp = []
        map = {}
        for r in alltheentries:
            if temp == []:
                temp = r
            else:
                code = r[0][4:6]
                code = code.upper()
                if map.get(code) == None:
                    if os.path.isfile(r'./branches/'+code+'.csv'):
                        os.remove(r'./branches/'+code+'.csv')
                    file = open(r'./branches/'+code+'.csv', 'a+', newline="")
                    with file:
                        alltheentries = csv.writer(file)
                        alltheentries.writerow(temp)
                    map[code] = 0
                map[code] += 1
                file = open(r'./branches/'+code+'.csv', 'a+', newline="")
                with file:
                    alltheentries = csv.writer(file)
                    alltheentries.writerow(r)
        file = open(r'.\branch_strength.csv', 'w', newline="")
        with file:
            alltheentries = csv.writer(file)
            alltheentries.writerow(["BRANCH_CODE", "STRENGTH"])
        branchstrengthtable = []
        for code in map.keys():
            branchstrengthtable.append([code, map[code]])
        branchstrengthtable = sorted(branchstrengthtable, key=lambda l: int(l[1]), reverse=True)
        for r in branchstrengthtable:
            file = open(r'.\branch_strength.csv', 'a+', newline="")
            with file:
                alltheentries = csv.writer(file)
                alltheentries.writerow(r)
    branch_num = len(branchstrengthtable)
    groupdatatable = [[0 for i in range(branch_num+2)]
             for j in range(groups_no+1)]
    groupdatatable[0][0] = "group"
    groupdatatable[0][1] = "total"
    for i in range(2, branch_num+2):
        groupdatatable[0][i] = branchstrengthtable[i-2][0]
    padding = len(str(groups_no))
    for i in range(1, groups_no+1):
        paddingcount = padding-len(str(i))
        groupdatatable[i][0] = "Group_G"+'0'*paddingcount+str(i)+".csv"
    leftover = []
    for i in range(len(branchstrengthtable)):
        floorstrength = floor(branchstrengthtable[i][1]/groups_no)
        for j in range(1, groups_no+1):
            groupdatatable[j][i+2] = floorstrength
        leftover.append(branchstrengthtable[i][1]-groups_no*floorstrength)
    inde = 1
    for i in range(len(leftover)):
        while leftover[i] > 0:
            groupdatatable[inde][i+2] += 1
            leftover[i] -= 1
            if inde == groups_no:
                inde = 1
            else:
                inde += 1
    for i in range(1, groups_no+1):
        for j in range(2, branch_num+2):
            groupdatatable[i][1] += groupdatatable[i][j]
    if os.path.isfile(r'./stats_grouping.csv'):
        os.remove(r'./stats_grouping.csv')
    file = open(r'./stats_grouping.csv', 'w', newline="")
    with file:
        alltheentries = csv.writer(file)
        alltheentries.writerows(groupdatatable)
    for i in range(1, groups_no+1):
        file = open(r'./groups/'+groupdatatable[i][0], 'w', newline="")
        with file:
            alltheentries = csv.writer(file)
            alltheentries.writerow(["Roll", "Name", "Email"])
    #here we are using pandas library to make database
    for i in range(2, branch_num+2):
        databasestructure = pd.read_csv(r'./branches/'+groupdatatable[0][i]+'.csv')
        countindex = 0
        for j in range(1, groups_no+1):
            f = databasestructure.iloc[countindex:countindex+groupdatatable[j][i]]
            tyh = f.values.tolist()
            countindex += groupdatatable[j][i]
            file = open(r'./groups/'+groupdatatable[j][0], 'a+', newline="")
            with file:
                alltheentries = csv.writer(file)
                alltheentries.writerows(tyh)
    return
deletepreviouswork()
filename = "Btech_2020_master_data.csv"
groups_no = int(input("Enter No. of Groups : ", ))
group_allocation(filename, groups_no)
