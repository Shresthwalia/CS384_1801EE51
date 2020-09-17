# Function to add two numbers 
def add(num1, num2): 
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
	#Multiplication Logic 
	multiplication =num1*num2
	return multiplication

# Function to divide two numbers 
def divide(num1, num2): 
	#DivisionLogic
	if(num2==0):
		return 0
	division=num1/num2 
	return division

# Function to add power function
#You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2): #num1 ^ num2
	#DivisionLogic
	# Base Cases
	if(num1==0 and num2 < 0 ):
		return 0
	if(num2<0):
		return round(1/power(num1,-num2),3)
	if (num1 == 0): 
		return 0
	if (num2 == 0): 
		return 1
	#If num2 is Even 
	powerexp = 0
	if(num2%2==0) :
		powerexp=power(num1,num2/2)
		powerexp= powerexp * powerexp
    #If num2 is odd
	else:
		powerexp = num1
		powerexp= powerexp * power(num1,num2-1) 
	return powerexp
	
# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printGP(a, r, n):
	if(not isinstance(n,int)):
		return [0]
	gp=[]
	for i in range(0,n):
		gp.append(a*power(r,i)) 
	return gp 

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n):
	if(not isinstance(n,int)):
		return [0] 
	ap=[]
	for i in range(0,n):
		ap.append(a+(i*d))
	return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n): 
	hp=[]
	if(not isinstance(n,int)):
		return hp
	ap=printAP(a,d,n)
	for i in range(0,n):
		if(ap[i]==0):
			hp.append(round(0,3))
		else:
			hp.append(round(1/ap[i],3))
	return hp
