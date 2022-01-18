# Define a class in Python to store the details of students (rollNumber, Mark1, Mark2), with the following methods.
# readData() - to assign values to class attributes
# computeTotal() - find the total marks
# print_details() - to display the attribute values and the total marks
# Create an object of the class and invoke the methods
class students:
  def readdata(self,rnum,m1,m2):
    self.rollnumber=rnum
    self.mark1=m1
    self.mark2=m2
  def print_details(self):
    print("rollnumber ",self.rollnumber)
    print("Mark1 ",self.mark1)
    print("Mark2 ",self.mark2)
  def computeTotal(self):
    print("total :",(self.mark1+self.mark2))

s1=students()
s1.readdata(1,10,5)
s1.print_details()
s1.computeTotal()