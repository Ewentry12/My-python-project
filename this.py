import sys
import utestfunc
def glob3():
#utestfunc.var=0
	utestfunc.var+=1
#glob=sys.modules['utestfunc']

def test():
	#print(utestfunc.var)
	utestfunc.local();
	utestfunc.glob1();
	utestfunc.glob2();
	glob3();
	print(utestfunc.var)
	