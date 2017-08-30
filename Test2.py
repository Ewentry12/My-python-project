
import this
import utestfunc
print(utestfunc.var)
this.test()
#def maker(N):
#	def action(X):
#		return X**N
#	return action
#h=maker(2)
#print(h(1000))
#def maker(N):
#	return lambda X:X**N
#h=maker(2)
#print(h(1000))
class food:
	def _init_(self,start):
		self.state=start
	def nested(self,label):
		print(label,self.state)
	F=food(0)
	F.nested('spam')