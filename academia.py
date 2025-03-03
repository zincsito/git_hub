from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def enter(self, user, type):
        pass
    
class StrategyStudent(Strategy):
    def enter(self, user, type):
        return (f"Welcome {user}, [user type] -> {type}")
    
class StrategyTeacher(Strategy):
    def enter(self, user, type):
         return (f"Welcome {user}, [user type] -> {type}")
     
class StrategyAdmin(Strategy):
    def enter(self, user, type):
         return (f"Welcome {user}, [user type] -> {type}")

    
class Manager:
    def __init__(self, strategy):
        self.strategy = strategy
        
    def set_strategy(self, strategy):
        self.strategy = strategy
        
    def enter(self, user, type):
        return self.strategy.enter(user, type)
    
class Event:
    
    def __init__(self):
        self._observadores = []
        
    def adicionar_observador(self, observador):
        self._observadores.append(observador)
        
    def eliminar_observador(self, observador):
        self._observadores.remove(observador)
        
    def notificar(self, mensaje):
        for observador in self._observadores:
            observador.actualizar(mensaje)
            
class Observador(ABC):
    @abstractmethod
    def actualizar(self, mensaje):
        pass
    
class Register(Observador):
    def actualizar(self, mensaje):
        print(f"Status: {mensaje}")
    
class New_Course(Observador):
    def actualizar(self, mensaje):
       print(f"Status: {mensaje}")
       
class New_Grade(Observador):
    def actualizar(self, mensaje):
       print(f"Status: {mensaje}")
       
if __name__ == '__main__':
    grades = {}
    schedule = {
        'Monday' : 'Programming',
        'Tuesday' : 'Programming',
        'Wednesday' : 'Mats',
        'Thursday' : 'Spanish',
        'Friday' : 'Mats'
    }
    courses = ["Programming", "Mats", "Spanish"]
    students = ["Rodrigo", "Itzel", "Felipe", "Erick", "Fernando"]
    
    while True:
        print("---Welcome to IT academy system---")
        name = str(input("Enter user: "))
        type = str(input("Enter user type (Student - Teacher - Admin): "))
        
        while type != 'Student' and type != 'Teacher' and type != 'Admin':
            print("Error, user type not valid!, try again")
            type = str(input("Enter user type (Student - Teacher - Admin): "))
        
        if type == "Student":
            context = Manager(StrategyStudent())
            print(context.enter(name, type))
            op = 1
            while op != 0:
                print("[options]")
                print("0 - Change user type")
                print("1 - Check available courses")
                print("2 - Check schedule")
                print("3 - Check grades")
                op = int(input("Choose an option: "))
                if op == 0:
                    break
                elif op == 1:
                    print("*Available courses*")
                    for curso in courses:
                        print("-", curso)
                    
                    course = str(input("Choose a course: "))
                    event = Event()
                    register = Register()
                    event.adicionar_observador(register)
                    event.notificar("Successful registration!")
                        
                elif op == 2:
                    print("*Schedule*")
                    for day in schedule.items():
                        print(day)
                elif op == 3:
                    print("*Grades*")
                    for grade in grades.items():
                        print(grade)
        
        elif type == "Teacher":
            context = Manager(StrategyTeacher())
            print(context.enter(name, type))
            op = 1
            while op != 0:
                print("[options]")
                print("0 - Change user type")
                print("1 - Add course")
                print("2 - Enrolled students")
                print("3 - Register grade")
                op = int(input("Choose an option: "))
                if op == 0:
                    break
                elif op == 1:
                    print("*Add course*")
                    new_c = str(input("Add a name for the course: "))
                    courses.append(new_c)
                    
                    for curso in courses:
                        print("-", curso)
                    
                    event = Event()
                    add_c = New_Course()
                    event.adicionar_observador(add_c)
                    event.notificar("New course registration successful!")
                        
                elif op == 2:
                    print("*Enrolled students*")
                    for student in students:
                        print("-", student)
                elif op == 3:
                    print("*Register grade*")
                    print("--Current grades--")
                    for grade in grades.items():
                        print(grade)
                    
                    print("Add the new grade")
                    student_n = str(input("Student name: "))
                    student_g = int(input("Grade: "))
                    grades[student_n] = student_g

                    event = Event()
                    add_g = New_Grade()
                    event.adicionar_observador(add_g)
                    event.notificar("New grade registration successful!")
        
        elif type == "Admin":
            context = Manager(StrategyAdmin())
            print(context.enter(name, type))
        
        continue_option = input("Do you want to log in as a different user type? (y/n): ")
        if continue_option.lower() != 'y':
            break
