class myfun():
    def __init__(self,eno,ename,eadd):
        self.eno=eno
        self.ename=ename
        self.eadd=eadd
    def display(self):
        print(self.eno,self.ename,self.eadd)
n=int(input("enter no:"))
n1=input("enter the name:")
n2=input("enter the address:")
n=myfun(n,n1,n2)
n.display()