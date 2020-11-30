from math import floor
import csv
import pandas as pd
import os


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
                    if os.path.isfile(r'./'+code+'.csv'):
                        os.remove(r'./'+code+'.csv')
                    file = open(r'./'+code+'.csv', 'a+', newline="")
                    with file:
                        alltheentries = csv.writer(file)
                        alltheentries.writerow(temp)
                    map[code] = 0
                map[code] += 1
                file = open(r'./'+code+'.csv', 'a+', newline="")
                with file:
                    alltheentries = csv.writer(file)
                    alltheentries.writerow(r)
        file = open(r'.\branch_strength.csv', 'w', newline="")
        with file:
            alltheentries = csv.writer(file)
            alltheentries.writerow(["BRANCH_CODE", "STRENGTH"])
        temp2 = []
        for code in map.keys():
            temp2.append([code, map[code]])
        temp2 = sorted(temp2, key=lambda l: int(l[1]), reverse=True)
        for r in temp2:
            file = open(r'.\branch_strength.csv', 'a+', newline="")
            with file:
                alltheentries = csv.writer(file)
                alltheentries.writerow(r)
    branch_num = len(temp2)
    temp3 = [[0 for i in range(branch_num+2)]
             for j in range(groups_no+1)]
    temp3[0][0] = "group"
    temp3[0][1] = "total"
    for i in range(2, branch_num+2):
        temp3[0][i] = temp2[i-2][0]
    temp4 = len(str(groups_no))
    for i in range(1, groups_no+1):
        temp5 = temp4-len(str(i))
        temp3[i][0] = "Group_G"+'0'*temp5+str(i)+".csv"
    temp6 = []
    for i in range(len(temp2)):
        temp7 = floor(temp2[i][1]/groups_no)
        for j in range(1, groups_no+1):
            temp3[j][i+2] = temp7
        temp6.append(temp2[i][1]-groups_no*temp7)
    l = 1
    print(temp6)
    for i in range(len(temp6)):
        while temp6[i] > 0:
            temp3[l][i+2] += 1
            temp6[i] -= 1
            if l == groups_no:
                l = 1
            else:
                l += 1
    for i in range(1, groups_no+1):
        for j in range(2, branch_num+2):
            temp3[i][1] += temp3[i][j]
    if os.path.isfile(r'./stats_grouping.csv'):
        os.remove(r'./stats_grouping.csv')
    file = open(r'./stats_grouping.csv', 'w', newline="")
    with file:
        alltheentries = csv.writer(file)
        alltheentries.writerows(temp3)
    for i in range(1, groups_no+1):
        file = open(r'./'+temp3[i][0], 'w', newline="")
        with file:
            alltheentries = csv.writer(file)
            alltheentries.writerow(["Roll", "Name", "Email"])
    for i in range(2, branch_num+2):
        temp10 = pd.read_csv(r'./'+temp3[0][i]+'.csv')
        temp11 = 0
        for j in range(1, groups_no+1):
            f = temp10.iloc[temp11:temp11+temp3[j][i]]
            tyh = f.values.tolist()
            temp11 += temp3[j][i]
            file = open(r'./'+temp3[j][0], 'a+', newline="")
            with file:
                alltheentries = csv.writer(file)
                alltheentries.writerows(tyh)
    return


filename = "Btech_2020_master_data.csv"
groups_no = int(input("Enter No. of Groups : ", ))
group_allocation(filename, groups_no)
