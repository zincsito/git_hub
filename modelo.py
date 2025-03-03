from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AcademicHistory(Base):
    __tablename__ = 'academic_history'

    id = Column(Integer, primary_key=True, server_default=text("nextval('academic_history_id_seq'::regclass)"))
    student_id = Column(Integer, nullable=False)
    course_id = Column(Integer, nullable=False)
    grade = Column(Float, nullable=False)
    date = Column(Date, nullable=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, server_default=text("nextval('users_id_seq'::regclass)"))
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(Integer, nullable=False)
    type = Column(String(40), nullable=False)
    active = Column(Boolean, nullable=False)


class StudentsDatum(Base):
    __tablename__ = 'students_data'

    id = Column(Integer, primary_key=True, server_default=text("nextval('students_data_id_seq'::regclass)"))
    academic_id = Column(ForeignKey('academic_history.id'), nullable=False)
    register = Column(Integer, nullable=False)
    program = Column(String(50), nullable=False)
    status = Column(String(30), nullable=False)
    user_id = Column(ForeignKey('users.id'), nullable=False)

    academic = relationship('AcademicHistory')
    user = relationship('User')


class TeachersDatum(Base):
    __tablename__ = 'teachers_data'

    id = Column(Integer, primary_key=True, server_default=text("nextval('teachers_data_id_seq'::regclass)"))
    department = Column(String(100), nullable=False)
    specialties = Column(String(100), nullable=False)
    academic_load = Column(String(50), nullable=False)
    schedule = Column(String(30), nullable=False)
    user_id = Column(ForeignKey('users.id'), nullable=False)

    user = relationship('User')


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, server_default=text("nextval('courses_id_seq'::regclass)"))
    content = Column(String, nullable=False)
    credits = Column(Float, nullable=False)
    prerequisites = Column(String, nullable=False)
    quotas = Column(Float, nullable=False)
    schedule = Column(String, nullable=False)
    teacher_id = Column(ForeignKey('teachers_data.id'), nullable=False)

    teacher = relationship('TeachersDatum')


class Qualification(Base):
    __tablename__ = 'qualifications'

    id = Column(Integer, primary_key=True, server_default=text("nextval('qualifications_id_seq'::regclass)"))
    teacher_id = Column(ForeignKey('teachers_data.id'), nullable=False)
    student_id = Column(ForeignKey('students_data.id'), nullable=False)
    course_id = Column(ForeignKey('courses.id'), nullable=False)
    qualification = Column(Float, nullable=False)

    course = relationship('Course')
    student = relationship('StudentsDatum')
    teacher = relationship('TeachersDatum')


class Registration(Base):
    __tablename__ = 'registrations'

    id = Column(Integer, primary_key=True, server_default=text("nextval('registrations_id_seq'::regclass)"))
    course_id = Column(ForeignKey('courses.id'), nullable=False)
    student_id = Column(ForeignKey('students_data.id'), nullable=False)

    course = relationship('Course')
    student = relationship('StudentsDatum')
