import string
from flask import Flask, jsonify, request

from CourseClass import Course
from DepartmentClass import Department
from InstructorClass import Instructor
from RoomClass import Room
from UserClass import User
from flask_mail import Mail, Message
import random
from flask_cors import CORS

from dataBaseClass import DataBase

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "company.employee.99@gmail.com"
app.config['MAIL_PASSWORD'] = "aass2233@"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/loginAuthorization', methods=['Get'])
def loginAuthorization():
    idUser = request.args.get('idUser')
    password = request.args.get('password')
    user = User()
    response = user.check_user(idUser, password)
    return jsonify({'response': response})


@app.route('/checkAndSendEmail', methods=['Get'])
def checkAndSendEmail():
    email = request.args.get('email')
    print(email)
    user1 = User()
    response = user1.check_email(email)
    if response[0]['email'] == "None":
        row = dict(
            state='Failed', )
        response.clear()
        response.append(row)
        return jsonify({'response': response})
    else:
        characters = string.ascii_letters + string.digits
        passwordCode = ''.join(random.choice(characters) for i in range(8))
        msg = "Use this code to reset your password :" + passwordCode
        subject = "Reset Password"
        email = response[0]['email']
        message = Message(subject, sender="company.employee.99@gmail.com", recipients=email.split())
        message.body = msg
        mail.send(message)

        row = dict(
            state='Done',
            idIstructor=response[0]['idIstructor'])
        response.clear()
        response.append(row)
        user1.update_password(response[0]['idIstructor'], passwordCode)
        return jsonify({'response': response})


@app.route("/SendNotification", methods=['GET'])
def SendNotification():
    idDep = request.args.get('idDep')
    note = request.args.get('note')
    flag = request.args.get('flag')
    result = DataBase().get_data_from_user1()

    try:
        if flag == '1':
            # من رئيس قسم لدكاترته
            for i in range(len(result)):
                if result[i]['idDep'] == idDep and result[i]['type'] == 'normal':
                    if result[i]['email'] == 'wafaa199.wd@gmail.com':
                        msg = note
                        subject = "Notification"
                        email = result[i]['email']
                        message = Message(subject, sender="company.employee.99@gmail.com", recipients=email.split())
                        message.body = msg
                        mail.send(message)


        elif flag == '2':
            # من العميد لرؤساء الاقسام
            for m in range(len(result)):
                if result[m]['type'] == 'head of department':
                    if result[m]['email'] == 'wafaa199.wd@gmail.com':
                        msg = note
                        subject = "Notification"
                        email = result[m]['email']
                        message = Message(subject, sender="company.employee.99@gmail.com", recipients=email.split())
                        message.body = msg
                        mail.send(message)


        elif flag == '3':
            # من العميد لدكاترة
            for k in range(len(result)):
                if result[k]['type'] == 'normal':
                    if result[k]['email'] == 'wafaa199.wd@gmail.com':
                        msg = note
                        subject = "Notification"
                        email = result[k]['email']
                        message = Message(subject, sender="company.employee.99@gmail.com", recipients=email.split())
                        message.body = msg
                        mail.send(message)

        elif flag == '4':
            for m in range(len(result)):
                if result[m]['type'] == 'head of department' and result[m]['idDepartment'] == idDep:
                    if result[m]['email'] == 'wafaa199.wd@gmail.com':
                        msg = note
                        subject = "Notification"
                        email = result[m]['email']
                        message = Message(subject, sender="company.employee.99@gmail.com", recipients=email.split())
                        message.body = msg
                        mail.send(message)
        response = "true"
    except:
        response = 'false'
    return jsonify({'response': response})


@app.route("/getMaterialsOfDepartment", methods=['GET'])
def getMaterialsOfDepartment():
    course = Course()
    idDep = request.args.get('idDep')
    year = request.args.get('year')
    sem = request.args.get('sem')
    response = course.get_courses(idDep, year, sem)
    return jsonify({'response': response})


@app.route("/getRoomsofDep", methods=['GET'])
def getRoomsofDep():
    room = Room()
    idDep = request.args.get('idDep')
    response = room.get_rooms_of_dep(idDep)
    return jsonify({'response': response})


@app.route("/addCourseToDepartment", methods=['GET'])
def addCourseToDepartment():
    idDep = request.args.get('idDep')
    name = request.args.get('name')
    number = request.args.get('number')
    numberOfHour = request.args.get('numberOfHour')
    type = request.args.get('type')
    year = request.args.get('year')
    sem = request.args.get('sem')
    flag = request.args.get('flag')
    specialty = request.args.get('specialty')
    toDepartments = request.args.get('toDepartments')
    course = Course()
    # idDep, name, number, numberOfHour, type, year, sem,toDepartments , flag,specialty
    response = course.add_course_to_dep(idDep, name, number, numberOfHour,
                                        type, year, sem, toDepartments, flag, specialty)
    return jsonify({'response': response})


@app.route("/editRoom", methods=['GET'])
def editRoom():
    response = []
    idDep = request.args.get('idDep')
    number = request.args.get('number')
    campous = request.args.get('campous')
    type = request.args.get('type')
    name = request.args.get('name')

    room1 = Room()
    result = room1.update_room(idDep, number, campous, type, name)
    row = dict(
        state=result, )
    response.append(row)
    return jsonify({'response': response})


@app.route("/getAllMaterialsOfDepartment", methods=['GET'])
def getAllMaterialsOfDepartment():
    response = []
    idDep = request.args.get('idDep')
    course2 = Course()
    response = course2.get_all_materials_of_department(idDep)
    return jsonify({'response': response})


@app.route("/addRoomToDepartment", methods=['GET'])
def addRoomToDepartment():
    response = []
    idDep = request.args.get('idDep')
    number = request.args.get('number')
    type = request.args.get('type')
    campous = request.args.get('campous')
    name = request.args.get('name')
    room1 = Room()
    result = room1.add_room_to_dep(idDep, number, type, campous, name)
    if result == 'False':
        row = dict(
            stat='Done'
        )
        response.append(row)
    else:
        row1 = dict(
            stat='Failed'
        )
        response.append(row1)
    return jsonify({'response': response})


@app.route("/deleteRoomFromDep", methods=['GET'])
def deleteRoomFromDep():
    response = []
    idDep = request.args.get('idDep')
    number = request.args.get('number')
    room2 = Room()
    result = room2.delete_room(idDep, number)
    row = dict(
        stat=result
    )
    response.append(
        row
    )
    return jsonify({'response': response})


@app.route("/getDep", methods=['GET'])
def getDep():
    user = request.args.get('username')
    passs = request.args.get('passs')
    data5 = User()
    response = data5.get_dep(user, passs)
    return jsonify({'response': response})


@app.route("/getAllIsn", methods=['GET'])
def getAllIsn():
    response = []
    idDep = request.args.get('idDep')
    inst2 = Instructor()
    response = inst2.get_all_inst_of_department(idDep)
    return jsonify({'response': response})


@app.route("/getAllDep", methods=['GET'])
def getAllDep():
    dep = Department()
    response = dep.get_all_dep()
    return jsonify({'response': response})


@app.route("/getMatOfSpeDep", methods=['GET'])
def getMatOfSpeDep():
    idDep = request.args.get('idDep')
    id = request.args.get('id')
    response = Course().get_all_materials_of_sep_dep(idDep, id)
    return jsonify({'response': response})


@app.route("/getRoomCat", methods=['GET'])
def getRoomCat():
    idDep = request.args.get('idDep')
    room1 = Room()
    response = room1.getCat(idDep)
    return jsonify({'response': response})


@app.route("/addInstToDepartment", methods=['GET'])
def addInstToDepartment():
    response = []
    idDep = request.args.get('idDep')
    name = request.args.get('name')
    email = request.args.get('email')
    gender = request.args.get('gender')
    response = Instructor().add_Inst_to_dep(idDep, name)
    if (response != 'false'):
        characters = string.ascii_letters + string.digits
        characters1 = string.digits
        userName = ''.join(random.choice(characters1) for i in range(8))
        passwordCode = ''.join(random.choice(characters) for i in range(8))
        # msg = "Use this userName" + userName + " and password to login to the system " + passwordCode
        # subject = "Welcome to the system!"
        # email = email
        # message = Message(subject, sender="company.employee.99@gmail.com", recipients=email.split())
        # message.body = msg
        # mail.send(message)
        DataBase().add_to_user(idDep, name, email, gender, userName, passwordCode)

    return jsonify({'response': response})


@app.route("/deleteInsFromDep", methods=['GET'])
def deleteInstFromDep():
    idDep = request.args.get('idDep')
    name = request.args.get('name')
    response = Instructor().delete_Inst_to_dep(idDep, name)
    return jsonify({'response': response})


@app.route("/deleteCourseFromDep", methods=['GET'])
def deleteCourseFromDep():
    idDep = request.args.get('idDep')
    number = request.args.get('number')
    response = Course().delete_Course_from_dep(idDep, number)
    return jsonify({'response': response})


@app.route("/getUsers", methods=['GET'])
def redirect_getUsers():
    idDep = request.args.get('idDep')
    response = DataBase().get_user(idDep)
    return jsonify({'response': response})


@app.route("/getAllUsers", methods=['GET'])
def redirect_getAllUser():
    response = DataBase().get_data_from_user1()
    return jsonify({'response': response})


@app.route("/editPicked", methods=['GET'])
def editPiked():
    response = []
    userName = request.args.get('userName')
    response = DataBase().edit_picker(userName)
    return jsonify({'response': response})




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3500)
