import inspect
import inspect
def func1():
 func2()
 
def func2():
 s = inspect.stack()
 print(s)
 print ("what is my function name:", s[0][3])
 print ("what is function name where I get called:", s[1][3])
 
func1()
 