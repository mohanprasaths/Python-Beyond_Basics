# student_name = [
#     {"name" : "mohan","game":"cricket","last_name":"prasath"},
#     {"name" : "ironman","game" : "alien buster"},
#     {"name" :"prasath","game" : "basketball"}]
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
students = []


# for name in student_name:
#     if name["game"] == "basketball":
#           name["name"] = "Prasath"
#     try :
#         print("My name is {0} {2}` and I play {1}".format(name["name"],name["game"],name["last_name"]))
#     except KeyError as error:
#         print("My name is {0} ` and I play {1}".format(name["name"],name["game"]))
#         print(error)


def add_student(name, id, **kwargs):
    extra_keys = kwargs.keys()
    student_object = {"name": name, "id": id}
    for key in extra_keys:
        student_object[key] = kwargs[key]
    students.append(student_object)


def add_student_through_input():
    name = input("Enter name")
    id = input("Enter ID")
    add_student(name, id)


def print_all_students():
    to_return = "ddd"
    for student in students:
        to_return = to_return + "\n<br> \t" + "student name {0}".format(student["name"])
        if "specialSkill" in student.keys():
            to_return = to_return + "." + " Has special skill{0}".format(student["specialSkill"])
        if "performance" in student.keys():
            to_return = to_return + "." + " Has performance {0}".format(student["performance"])
    return (to_return)


def save_in_file():
    file_output = open("student.txt", "a")
    for student in students:
        file_output.writelines(student["name"] + "\n")
    file_output.close()


def read_from_file():
    file_read = open("student.txt", "r")
    returnString = ""
    for line in read_students_from_file(file_read):
        returnString = returnString + "\n" + line
        # print(line)
    file_read.close()
    return returnString


def read_students_from_file(f):
    for line in f:
        yield line


# try :
#     read_from_file()
# except Exception:
#     print("Exception occured while reading")
#
add_student(name="mohan",id="1",specialSkill="fighting",performance="Good")
add_student(name="Prasath",id="2",specialSkill="cricket",performance="Good")
add_student(name="Dummy",id="3",performance="OK")
#
# # while True :
# #     choice = input("type yes to continue")
# #     if choice == "yes":
# #         add_student_through_input()
# #     else:
# #         break
#
#
# print_all_students()
#
# try :
#     save_in_file()
# except:
#     print("Error while saving")

@app.route("/", methods=["GET", "POST"])
def myApp():
    if request.method == "GET":
        students = print_all_students()
    if request.method == "POST":
        add_student(name=request.form.get("student_name", ""), id=request.form.get("student_id", ""))
        students = print_all_students()
        try:
            save_in_file()
        except:
            print("Error while saving")
            return redirect(url_for("myApp"))
    print(students)
    return render_template("index.html", students=[{"name":students}])


if __name__ == "__main__":
    app.run(debug=True)
