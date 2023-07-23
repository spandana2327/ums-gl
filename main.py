from insert import inserted
from update import updated
from delete import deleted
from read import reading

obj_department = inserted()
obj2_department = updated()
obj3_department = deleted()
obj4_department = reading()

obj_course = inserted()
obj2_course = updated()
obj3_course = deleted()
obj4_course = reading()

obj_faculty = inserted()
obj2_faculty = updated()
obj3_faculty = deleted()
obj4_faculty = reading()

obj_student = inserted()
obj2_student = updated()
obj3_student = deleted()
obj4_student = reading()

print("Welcome to the University Management System!")
print("Database Information:")
print("- Number of tables: 4")
print("- Table names: Student, Department, Faculty, Course")

# Displaying student table information
print("\nStudent Table Information:")
print("- Number of records: 4")
print("- Columns: sid, sname, courseid, dptid")

# Displaying department table information
print("\nDepartment Table Information:")
print("- Number of records: 2")
print("- Columns: departmentid, departmentname")

# Displaying faculty table information
print("\nFaculty Table Information:")
print("- Number of records: 5")
print("- Columns: facultyid, facultyname, departmentid, salary, courseid")

# Displaying course table information
print("\nCourse Table Information:")
print("- Number of records: 4")
print("- Columns: courseid, coursename, coursefees, duration")

print('------------------------------------------------------------')

print('*You can perform 4 operations on the database *')
print('For adding data, write "add"')
print('For updating data, write "update"')
print('For deleting data, write "delete"')
print('For reading data, write "read"')

opr = input('Please enter the operation: ')

if opr == 'add':
    print('For inserting data, please select the table:')
    print('1. Department')
    print('2. Course')
    print('3. Faculty')
    print('4. Student')

    tab = int(input('Enter the number to select the table: '))

    if tab == 1:
        dtid = int(input('Please enter department ID: '))
        dtname = input('Please enter department name: ')
        obj_department.dptinsert(dtid, dtname)
    elif tab == 2:
        crsid = int(input('Please enter course ID: '))
        crsname = input('Please enter course name: ')
        crsfees = float(input('Please enter course fees: '))
        duration = int(input('Please enter course duration: '))
        obj_course.crsinsert(crsid, crsname, crsfees, duration)
    elif tab == 3:
        facid = int(input('Please enter faculty ID: '))
        facname = input('Please enter faculty name: ')
        deptid = int(input('Please enter department ID: '))
        salary = float(input('Please enter salary: '))
        crsid = int(input('Please enter course ID: '))
        obj_faculty.facinsert(facid, facname, deptid, salary, crsid)
    elif tab == 4:
        sid = int(input('Please enter student ID: '))
        sname = input('Please enter student name: ')
        courseid = int(input('Please enter course ID: '))
        dptid = int(input('Please enter department ID: '))
        obj_student.studinsert(sid, sname, courseid, dptid)
    else:
        print('Invalid table selection!')

elif opr == 'update':
    print('For updating data, please select the table:')
    print('1. Department')
    print('2. Course')
    print('3. Faculty')
    print('4. Student')

    tab = int(input('Enter the number to select the table: '))

    if tab == 1:
        col = input('Please enter the column name: ')
        old = input('Please enter the old value: ')
        new = input('Please enter the new value: ')
        obj2_department.dptupdate(colname=col, oldval=old, newval=new)
    elif tab == 2:
        col = input('Please enter the column name: ')
        old = input('Please enter the old value: ')
        new = input('Please enter the new value: ')
        obj2_course.crsupdate(colname=col, oldval=old, newval=new)
    elif tab == 3:
        col = input('Please enter the column name: ')
        old = input('Please enter the old value: ')
        new = input('Please enter the new value: ')
        obj2_faculty.facupdate(colname=col, oldval=old, newval=new)
    elif tab == 4:
        col = input('Please enter the column name: ')
        old = input('Please enter the old value: ')
        new = input('Please enter the new value: ')
        obj2_student.studupdate(colname=col, oldval=old, newval=new)
    else:
        print('Invalid table selection!')

elif opr == 'delete':
    print('For deleting data, please select the table:')
    print('1. Department')
    print('2. Course')
    print('3. Faculty')
    print('4. Student')

    tab = int(input('Enter the number to select the table: '))

    if tab == 1:
        id = int(input('Please enter the department ID to delete data: '))
        obj3_department.dptdelete(id)
    elif tab == 2:
        id = int(input('Please enter the course ID to delete data: '))
        obj3_course.crsdelete(id)
    elif tab == 3:
        id = int(input('Please enter the faculty ID to delete data: '))
        obj3_faculty.facdelete(id)
    elif tab == 4:
        id = int(input('Please enter the student ID to delete data: '))
        obj3_student.studdelete(id)
    else:
        print('Invalid table selection!')

elif opr == 'read':
    print('For reading data, please select the table:')
    print('1. Department')
    print('2. Course')
    print('3. Faculty')
    print('4. Student')

    tab = int(input('Enter the number to select the table: '))

    if tab == 1:
        id = int(input('Please enter the department ID to read data: '))
        obj4_department.dptread(id)
    elif tab == 2:
        id = int(input('Please enter the course ID to read data: '))
        obj4_course.crsread(id)
    elif tab == 3:
        id = int(input('Please enter the faculty ID to read data: '))
        obj4_faculty.facread(id)
    elif tab == 4:
        id = int(input('Please enter the student ID to read data: '))
        obj4_student.studread(id)
    else:
        print('Invalid table selection!')

else:
    print('Invalid operation!')
