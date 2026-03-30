students = {}
id = 1

def register_students ():
        global id
        name = input("add a name: ")
        print(f"{name} has been registered correctly")
        age = None
        while age is None:
            try:
                age = int(input("Enter an age: "))
                if age < 0:
                    print("Error, age should not be negative")
                    age = None
                    continue
                elif age > 140:
                    print("mistake, age must be realistic")
                    age = None
                    continue
                else:
                    print("age has been successfully registered.")                  
            except ValueError:
                print("=" *80)
                print("No letters are allowed, nor is space soft")
                print("=" *80)
                continue

            course = input("Enter a course: ")
            state = None
            while state is None: 
                try:
                    print(f"El student {name} está:")
                    state = int(input(f"1: Activo\n2: Inactivo\n"))
                    if state == 1:
                        state = "Active"
                    elif state == 2:
                        state = "Inactive"
                    else:
                        print("option is not valid")
                        state = None
                except ValueError:
                    print("You can't write letters")
                    state = None
            registrar = {"id":id,"name":name,"age":age,"course":course,"state":state}
            students[id]=registrar
            id += 1
            print("=" * 70)
            print(f"student {name} registered correctly.")



def consultar_lista():
        if len(students) == 0:
            print("=" * 50)
            print("No hay students registrados")

        for student in students.values():
            print("=" * 70)
            print(f"ID: {student["id"]} | name: {student["name"]} | age: {student["age"]} | course: {student["course"]} | state: {student["state"]}")


        
def buscar_student():
        salir = False
        while salir == False:
            print("=" * 70)
            print("1: Search for ID")
            print("2: Search for name")
            print("3: Search for age")
            print("4: Search for state")
            print("5: Search for course")
            print("6: return to Menu")
            Option = None
            while Option is None:
                try:
                    Option = int(input("Enter Option (1-6): ").strip())
                except ValueError:
                    print("=" * 70)
                    print("You cannot leave it empty or write letters")
            if Option == 1:
                try:
                    buscar = int(input("Enter un ID de student: ").strip())
                    if not buscar in students:
                        print("=" * 70)
                        print("this ID de student no existe")
                    else:
                        for student in students.values():
                            if buscar == student["id"]:
                                print(f"ID: {student["id"]} | name: {student["name"]} | age: {student["age"]} | course: {student["course"]} | state: {student["state"]}")
                except ValueError:
                    print("=" * 70)
                    print("You cannot leave it empty or write letters")
            elif Option == 2:
                buscar = input("Enter a name de student: ")
                if not buscar in students:
                    print("=" * 70)
                    print("This Student Name does not exist")
                else:
                    for student in students.values():
                        if buscar == student["name"]:
                            print(f"ID: {student["id"]} | name: {student["name"]} | age: {student["age"]} | course: {student["course"]} | state: {student["state"]}")

            elif Option == 3:
                buscar = int(input("Enter a student age: ").strip())
                if not buscar in students:
                    print("=" * 70)
                    print("this student age does not exist")
                else:
                    for student in students.values():
                        if buscar == student["age"]:
                            print(f"ID: {student["id"]} | name: {student["name"]} | age: {student["age"]} | course: {student["course"]} | state: {student["state"]}")
            elif Option == 4:
                buscar = None
                while buscar is None:
                    try:
                        buscar = int(input("1: Active | 2: Inactive: ").strip())
                        if buscar == 1:
                            buscar = "Active"
                        elif buscar == 2:
                            buscar = "Inactive"
                        else:
                            print("=" * 70)
                            print("option is not valid")
                            print("=" * 70)

                            buscar = None
                    except ValueError:
                        print("=" * 70)
                        print("You cannot leave it empty or write letters")
                        print("=" * 70)
                    for student in students.values():
                        if buscar == student["state"]:
                            print(f"ID: {student["id"]} | name: {student["name"]} | age: {student["age"]} | course: {student["course"]} | state: {student["state"]}")
            elif Option == 5:
                buscar = input("Enter a Student Course:")
                for student in students.values():
                    if buscar == student["course"]:
                        print(f"ID: {student["id"]} | name: {student["name"]} | age: {student["age"]} | course: {student["course"]} | state: {student["state"]}")
            elif Option == 6:
                salir = True
            else: 
                print("=" * 70)
                print("option is not valid")

def actualizar_informacion():
    try:
        actualizar = int(input("enter an id to update: "))
        if actualizar not in students:
            print("student no encontrado.")
            return
        student = students[actualizar]
        print(f"Actualizando: {student['name']} | Leave blank so as not to change.")

        name = input(f"name ({student['name']}): ")
        if name.strip() != "":
            student["name"] = name

        try:
            age = input(f"age ({student['age']}): ")
            if age.strip() != "":
                student["age"] = int(age)
        except ValueError:
            print("age does not validate, the previous one is maintained.")

        course = input(f"course ({student['course']}): ")
        if course.strip() != "":
            student["course"] = course

        state = input(f"state ({student['state']}) - 1: Active / 2: Inactive: ")
        if state.strip() == "1":
            student["state"] = "Active"
        elif state.strip() == "2":
            student["state"] = "Inactive"
        print(f"student {student['name']} updated correctly.")
    except ValueError:
        print("id is not valid.")

def delete_student():
    try:
        id = int(input("Enter ID a delete: "))
        if id in students:
            name = students[id]["name"]
            del students[id]
            print(f"student {name} deleted corretlyc.")
        else:
            print("=" * 70)
            print("student not found")
    except ValueError:
        print("ID no valido.")


def menu():
    print("=" * 80)
    print("students registration")
    print("=" * 80)
    print("1: register a student.")
    print("2: consult students list")
    print("3: Search a student")
    print("4: Delete a student")
    print("5: update a student")
    print("6: Exit")

salir = False
while salir == False:

    menu()

    Option = None
    while Option is None:
        try:
            Option = int(input("Digita una Option (1-6): ").strip())
        except ValueError:
            print("No se puede digitar letras")
            Option = None
    
    if Option == 1:
        register_students()
    elif Option == 2:
        consultar_lista()
    elif Option == 3:
        buscar_student()
    elif Option == 4:
        delete_student()
    elif Option == 5:
        actualizar_informacion()
    elif Option == 6:
        salir = True
    else:
        print("\n", "=" * 20, "option is not valid", "=" * 20, "\n")