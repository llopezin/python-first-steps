students = [
    {"name": "Ana", "age": 22, "grade": 8.5},
    {"name": "Luis", "age": 21, "grade": 6.7},
    {"name": "Carlos", "age": 23, "grade": 9.1},
    {"name": "Elena", "age": 20, "grade": 4.3},
    {"name": "Lucía", "age": 22, "grade": 7.2},
    {"name": "Marcos", "age": 21, "grade": 5.9},
    {"name": "Sofía", "age": 23, "grade": 9.8}
]

def main():
   print('Main running')

   myGroup = StudentsGroup(students, passingGrade=5)
   print('List')
   print(myGroup.getStudentsNamesByDescendingGrade())
   print('List above 7')
   print(myGroup.getStudentsOverGrade(7))





class StudentsGroup:
   def __init__(self, students, passingGrade):
      self.students = students
      self.passingGrade = passingGrade

   def getStudentsSortedByGrade(self):
      return list(sorted(self.students, key=lambda std: std['grade'], reverse=True))
   
   def getPassedStudents(self):
      return list(filter(lambda std: std['grade'] >= self.passingGrade, self.students))
   
   def getPassedStudentsNames(self):
      return list(map(lambda x: x['name'], self.getPassedStudents(self.passingGrade)))
   
   def getStudentsNamesByDescendingGrade(self):
      return list(map(lambda x: x['name'], self.getStudentsSortedByGrade()))
   
   def getStudentsOverGrade(self, grade):
      return list(map(lambda std: std['name'] , filter(lambda x: x['grade'] > grade, self.students)))
   
main()