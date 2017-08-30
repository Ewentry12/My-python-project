import collections
class counter:
	def __init__(self,initial=0):
		self.value=initial
	def increment(self):
	    self.value+=1
	def get(self):
		return self.value
h=counter(11)
h.increment()
print(h.get())

class Memorizdict(dict):
	history=collections.deque(maxlen=3)
	def set(self,key,value):
			self.history.append(key)
			self[key]=value
	def get_history(self):
	    return self.history
	def get_value(self):
	    return self.value
d=Memorizdict({"foo":23})
d.set("alex",1200)
d.set("anna",1100)
d.set("saha",1000)
d.set("olya",1200)
print(d.get_history())
