# @Time     :2018/6/30 下午6:08
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

class School(object):
	def __init__(self, name, addr):
		self.name = name
		self.addr = addr
		self.students = []
		self.staffs = []

	def enroll(self, stu_obj):
		print("为新学员 %s 办理注册手续" % stu_obj.name)
		self.students.append(stu_obj)

	def hire(self, staff_obj):
		print("为新员工 %s 办理注册手续" % staff_obj.name)
		self.staffs.append(staff_obj)

class SchoolMember(object):
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex

	def tell(self):
		pass


class Teacher(SchoolMember):
	def __init__(self, name, age, sex, salary, course):
		super(Teacher, self).__init__(name, age, sex)
		self.salary = salary
		self.course = course

	def tell(self):
		print("""
		------ info of Teacher ------
		Name:%s
		Age:%s
		Sex:%s
		Salary:%s
		Course:%s
		""" % (self.name, self.age, self.sex, self.salary, self.course))

	def teach(self):
		print("%s is teaching is course [%s]" % (self.name, self.course))


class Student(SchoolMember):
	def __init__(self, name, age, sex, stu_id, grade):
		super(Student, self).__init__(name, age, sex)
		self.stu_id = stu_id
		self.grade = grade

	def tell(self):
		print("""
		------ info of Student ------
		Name:%s
		Age:%s
		Sex:%s
		Stu_id:%s
		Gread:%s
		""" % (self.name, self.age, self.sex, self.stu_id, self.grade))

	def pay_tuition(self, amount):
		print("%s has paid tution for  %s" % (self.name, amount))


school = School("Oldbay", "shahe")

t1 = Teacher("oldbay", 56, "M", 2000000, "Liunx")
t2 = Teacher("Alex", 36, "F", 20000, "Python")

s1 = Student("Jennings", 22, "M", 1001, "Python")

t1.tell()
s1.tell()

school.hire(t1)
school.enroll(s1)

print(school.students)
print(school.staffs)

school.staffs[0].teach()

for stu in school.students:
	stu.pay_tuition(5000)
