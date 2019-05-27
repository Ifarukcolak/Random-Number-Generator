#Generate random number using Linear Congruential Method

a = 0
c = 0
m = 0
x0 = 0 

def setup_lcg_parameters(a1,c1,m1,x1):  
	global a,c,m,x0	
	a,c,m,x0 = a1,c1,m1,x1
	
def generate_random_number(count):
	global a,c,m,x0
	for i in range(count):
		x0 = (a*x0 + c) % m
		print( x0 )
	
	
setup_lcg_parameters(21,49,100,0)

generate_random_number(10)
