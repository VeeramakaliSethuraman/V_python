class student:
    def __init__(self,student_id,student_name):
        self.student_id=student_id
        self.student_name=student_name
    def display_attributes(self):
        print("Student ID:",self.student_id)
        print("Student Name:",self.student_name)
    def add_class(self,student_class):
        self.student_class=student_class
    def remove_name(self):
        del self.student_name
s=student("24","Veera")
s.display_attributes()
s.add_class("Python")
print("all attributes:",vars(s))
s.remove_name()
print("Student Name is Removed:",vars(s))
