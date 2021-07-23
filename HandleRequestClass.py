import string
from flask import Flask, jsonify, request

from CourseClass import Course
from InstructorClass import Instructor
from RoomClass import Room
from UserClass import User
from flask_mail import Mail, Message
import random

app = Flask(__name__)

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "company.employee.99@gmail.com"
app.config['MAIL_PASSWORD'] = "aass2233@"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/test', methods=['Get'])
def gg():
    response = row = dict(
            state='Failed', )

    return jsonify({'response': response})

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
        characters = string.ascii_letters + string.digits + string.punctuation
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


@app.route("/getMaterialsOfDepartment", methods=['GET'])
def getMaterialsOfDepartment():
    course = Course()
    idIstructor = request.args.get('idIstructor')
    year = request.args.get('year')
    sem = request.args.get('sem')
    response = course.get_courses(idIstructor, year, sem)
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
    course = Course()
    response = course.add_course_to_dep(idDep, name, number, numberOfHour,
                                          type, year, sem)
    return jsonify({'response': response})


@app.route("/editRoom", methods=['GET'])
def redirect_editRoom():
    response =[]
    idDep = request.args.get('idDep')
    number = request.args.get('number')
    campous = request.args.get('campous')
    type = request.args.get('type')
    room1 = Room()
    result = room1.update_room(idDep,number,campous,type)
    row = dict(
        state=result, )
    response.append(row)
    return jsonify({'response': response})









if __name__ == "__main__":
    app.run(debug=True)
