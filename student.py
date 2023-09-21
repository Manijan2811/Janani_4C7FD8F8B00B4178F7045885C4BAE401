#implement a function called sort_students that takes a list of student objects as inpput and sorts the list based on their CGPA(Cumulative Grade Point Average) in descending order.Each student object has the following attributes:name(string),roll_number(string),and cgpa(float).Test the function with different input lists of students.

class student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
def sort_students(student_list):
    sorted_students=sorted(student_list,key=lambda 
                     student:student.cgpa,reverse=True)
    return sorted_students
students=[
  student("Janani","CB21S261670",9.1),
  student("Harini","Cb21S261671",9),
  student("Mani","CB21S261672",8.9)
]
sorted_students=sort_students(students)
for student in sorted_students:
  print("Name: {},Roll_Number: {},CGPA: {}".format(student.name,student.roll_number,student.cgpa))
    
    