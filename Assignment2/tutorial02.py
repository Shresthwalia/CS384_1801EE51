# All decimal 3 places
import math
# Function to compute mean
def mean(first_list):
    # mean Logic
    mean_value=summation(first_list)/len(first_list) 
    return round(mean_value,6)


# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    lis=sorting(first_list.copy())
    median_value=0
    n=len(lis)
    if(len(lis)%2==0):
        median_value=(lis[int((n/2)-1)]+lis[int(n/2)])/2
    else:
        median_value=lis[(int((n+1)/2)-1)]
        return round(median_value,6)


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    standard_deviation_value=math.sqrt(variance(first_list))
    return round(standard_deviation_value,6)


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    avg=mean(first_list)
    lis=[]
    for i in first_list:
        lis.append((i-avg)*(i-avg))
    variance_value=mean(lis)
    return round(variance_value,6)


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    for i in first_list:
        if(not isinstance(i,(int,float))):
            return 0
    for i in second_list:
        if(not isinstance(i,(int,float))):
            return 0
    rmse_value=math.sqrt(mse(first_list,second_list))
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    lis=[]
    for (i,j) in zip(first_list,second_list):
        lis.append(((i-j)*(i-j)))
    mse_value=mean(lis)
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    if(len(first_list)!=len(second_list)):
        return 0
    lis=[]
    for i,j in zip(first_list,second_list):
        lis.append(abs(i-j))
    mae_value=mean(lis)
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    avg=mean(first_list)
    numerator=mse(first_list,second_list)
    denominator=variance(first_list)
    nse_value=1-(numerator/denominator)
    return round(nse_value,6)


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    lis=[]
    avgf=mean(first_list)
    avgs=mean(second_list)
    for i,j in zip(first_list,second_list):
        lis.append((i-avgf)*(j-avgs))
    avg=mean(lis)
    pcc_value=(avg/(standard_deviation(first_list)*standard_deviation(second_list)))
    return round(pcc_value,6)


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    var=standard_deviation(first_list)
    avg=mean(first_list)
    lis=[]
    for i in first_list:
        lis.append(((i-avg)/var)*((i-avg)/var)*((i-avg)/var))
    skewness_value=mean(lis)
    return round(skewness_value,6)
    
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

#quickSort Algorithm
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 


def sorting(first_list):
    # Sorting Logic
    quickSort(first_list,0,len(first_list)-1)
    return first_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    var=standard_deviation(first_list)
    avg=mean(first_list)
    lis=[]
    for i in first_list:
        lis.append(((i-avg)/var)*((i-avg)/var)*((i-avg)/var)*((i-avg)/var))
    kurtosis_value=mean(lis)
    return round(kurtosis_value,6)


# Function to compute sum. You cant use Python functions
def summation(first_list):
    summation_value=0
    for i in first_list:
        if(not isinstance(i,(int,float))):
            return 0
    for i in first_list :
        summation_value+=i
    return round(summation_value,6)
