#function

def func1():
    print "In func 1"
    func2()     #return value is None
def func2():
    print "In func 2"


print func1()



print "-------------------------"
def hello(name):
    print "Hello",name

result=hello("python")
print result
print "--------------------"
def hello(cost,rate=3.5):
    val =(cost*rate)   # cost,ratwe arwe initial variable
    return val
result=hello(5600)
print result
print "-----------------"
def greet(title,name):
    print "hello"+title+""+name
print "------------------"

