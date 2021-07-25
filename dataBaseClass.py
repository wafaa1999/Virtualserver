from pymongo import MongoClient


class DataBase:
    def __init__(self):
        Client = MongoClient('mongodb+srv://WD-project:wafaa12345@cluster0.v5htd.mongodb.net/test')
        self._db = Client['Schedule']

    def get_data_from_user(self):
        collection = self._db.User
        result = []
        for i in collection.find():
            result.append(i)
        return result

    def update_password_for_Inst(self, instID, passwordCode):
        oldValue = []
        newValue = []
        collection = self._db["User"]
        for i in collection.find():
            if instID == i['idInstructor']:
                doc = collection.find_one_and_update(
                    {"idInstructor": instID},
                    {"$set":
                         {"password": passwordCode}
                     }, upsert=True
                )

    def get_courses_of_dep(self, toDepartments):
        collection = self._db.Course
        result = []
        for i in collection.find().sort("year"):
            result.append(i)
        return result

    def get_instrctor(self, idInstructor):
        collection = self._db.Instructor
        result = []
        for i in collection.find():
            if idInstructor == str(i['_id']):
                result.append(i)
        return result

    def get_room(self):
        collection = self._db.Room
        result = []
        for i in collection.find():
            result.append(i)
        return result

    def get_course_of_dep(self, idDep):
        course = self._db.Course
        result = []
        for i in course.find():
            result.append(i)
        return result

    def add_course_to_dep(self, idDep, name, number, numberOfHour, type, year, sem):
        collection = self._db.Course
        row = {
            "name": name,
            "type": type,
            "number": number,
            "courseHours": numberOfHour,
            "year": year,
            "idDepartment": idDep,
            "semester": sem,
            "toDepartments": idDep,
        }

        result = collection.insert_one(row)
        flag: str = '1'
        return flag

    def update_data_for_room(self,idDep,number,campous,type):
        flag = False
        collection = self._db["Room"]
        for i in collection.find():
            if number == i['number'] and idDep == i['idDepartment']:
                flag = True
                doc = collection.find_one_and_update(
                    {"number": number},
                    {"$set":
                         {"campous": campous,
                          "type":type}
                     }, upsert=True
                )
        if flag:
            return '1'
        else: return  '0'

    def add_room(self,idDep, number, type, campous):
        flag = self.check_room(number)
        if flag == 'False':
            collection = self._db.Room
            row = {
                "type": type,
                "number": number,
                "idDepartment": idDep,
                "campous": campous
            }
            result = collection.insert_one(row)
            return flag
        return flag

    def check_room(self, number):
        collection = self._db.Room
        result = []
        for i in collection.find():
            if i['number'] == number:
                return 'True'
        return 'False'

    def delete_room_from_dep(self, idDep, numberr):
        flag = False
        collection = self._db["Room"]
        for i in collection.find():
            if numberr == i['number'] and idDep == i['idDepartment']:
                reselt = collection.delete_one({"number": numberr})
                return 'True'





