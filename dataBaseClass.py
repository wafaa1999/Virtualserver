from pymongo import MongoClient


class DataBase:
    def __init__(self):
        Client = MongoClient('mongodb+srv://WD-project:wafaa12345@cluster0.v5htd.mongodb.net/test')
        self._db = Client['Schedule']

    def add_inst_to_deprtment(self, idDep, name,email,gender):
        collection = self._db.Instructor
        flag = True
        res = self.get_data_from_Inst()
        for i in range(len(res)):
            if res[i]['name'] == name and res[i]['idDepartment'] == idDep:
                flag = False

        if flag:
            row = {
                "idDepartment": idDep,
                "name": name,
                "type": 'normal',
                "email": email,
                "gender":gender
            }
            result = collection.insert_one(row)

        return flag

    def get_data_from_user(self):
        collection = self._db.User
        result = []
        for i in collection.find():
            result.append(i)
        return result

    def get_data_from_user1(self):
        collection = self._db.User
        result = []
        for i in collection.find():
            row = dict(
                idDep=i['idDep'],
                gender=i['gender'],
                type=i['type'],
                name=i['name'],
                id=i['userName'],
                email=i['email'],
                picked=i['picked'],
                code=i['code']
            )
            result.append(row)
        return result


    def get_user(self, idDep):
        response = []
        result = self.get_data_from_user()
        for i in range(len(result)):
            if result[i]['idDep'] == idDep or result[i]['type'] == 'head' or result[i]['type'] == 'head of department':
                row = dict(
                    idDep=idDep,
                    gender=result[i]['gender'],
                    type=result[i]['type'],
                    name=result[i]['name'],
                    id=result[i]['userName'],
                    picked=result[i]['picked'],
                    email=result[i]['email'],
                    code=result[i]['code']

                    )
                response.append(row)

        return  response

    def add_to_user(self, idDep, name, email, gender, userName, passwordCode):
        # idDep, name, email, gender, userName, passwordCode
        collection1 = self.get_data_from_Inst()
        for i in range(len(collection1)):
            if collection1[i]['name'] == name and collection1[i]['idDepartment'] == idDep:
                result = str(collection1[i]['_id'])
                break

        collection = self._db.User
        row = {
            "userName":userName ,
            "password": passwordCode,
            "email": email,
            "type": 'normal',
            "gender": gender,
            "name": name,
            "idDep": idDep,
            "idIstructor": result,
            "picked":'false',
            "code":'00000000'

        }

        result = collection.insert_one(row)




    def get_data_from_dep(self):
        collection = self._db.Department
        result = []
        for i in collection.find():
            result.append(i)
        return result

    def get_data_from_Inst(self):
        collection = self._db.Instructor
        result = []
        for i in collection.find():
            result.append(i)
        return result

    def set_code(self, instID, passwordCode):
        collection = self._db.User
        doc = collection.find_one_and_update(
            {"idIstructor": instID},

            {"$set":
                 {"code": passwordCode}
             }, upsert=True
        )

    def update_password_for_Inst(self, instID, passwordCode):
        oldValue = []
        newValue = []
        collection = self._db.User
        doc = collection.find_one_and_update(
                    {"idIstructor": instID},

                    {"$set":
                         {"password": passwordCode}
                     }, upsert=True
                )

    def update_pass(self, userName, old, new):
        collection = self._db.User
        flag = False
        for i in collection.find():
            if i['userName'] == userName and i['password'] == old:
                flag = True
        if flag:
            doc = collection.find_one_and_update(
                {"userName": userName,
                 "password": old},

                {"$set":
                     {"password": new}
                 }, upsert=True
            )
            return flag
        return  flag



    def edit_picker(self, userName):
        collection = self._db.User
        doc = collection.find_one_and_update(
            {"userName": userName},

            {"$set":
                 {"picked": 'true'}
             }, upsert=True
        )
        return 'true'


    def get_courses_of_dep(self, idDep):
        collection = self._db.Course
        result = []
        for i in collection.find().sort("year"):
            result.append(i)
        return result

    def get_all_Isnt(self, idDep):
        collection = self._db.Instructor
        result = []
        for i in collection.find():
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

    def add_course_to_dep(self, idDep, name, number, numberOfHour, type, year, sem, flag,toDepartments,specialty):
        if flag == '0':
            flagFrom = 'false'
            flagTo = 'false'
        elif flag == '1':
            flagFrom = 'true'
            flagTo = 'false'
        else:
            flagFrom = 'false'
            flagTo = 'true'

        collection = self._db.Course
        row = {
            "name": name,
            "type": type,
            "number": number,
            "courseHours": numberOfHour,
            "year": year,
            "idDepartment": idDep,
            "semester": sem,
            "toDepartments": toDepartments,
            "flagFrom": flagFrom,
            "flagTo": flagTo,
            "specialty":specialty
        }

        result = collection.insert_one(row)
        flag: str = '1'
        return flag

    def update_data_for_room(self,idDep,number,campous,type, name):
        flag = False
        collection = self._db["Room"]
        for i in collection.find():
            if number == i['number'] and idDep == i['idDepartment']:
                flag = True
                doc = collection.find_one_and_update(
                    {"number": number},
                    {"$set":
                         {"campous": campous,
                          "type":type,
                          "name":name}
                     }, upsert=True
                )
        if flag:
            return '1'
        else: return  '0'

    def add_room(self,idDep, number, type, campous, name):
        flag = self.check_room(number)
        if flag == 'False':
            collection = self._db.Room
            row = {
                "type": type,
                "number": number,
                "idDepartment": idDep,
                "campous": campous,
                "name": name
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
        return 'False'

    def delete_inst_to_deprtment(self, idDep, name):
        response = []
        collection = self._db.Instructor

        result = collection.delete_one({"idDepartment": idDep,
                               "name": name
                               })
        row = {
            "flag": 'true', }

        collection1 = self._db.User

        result1 = collection1.delete_one({"idDep": idDep,
                                        "name": name
                                        })
        row = {
            "flag": 'true', }


        response.append(row)
        return response

    def delete_Course_from_department(self, idDep, number):
        response = []
        collection = self._db.Course

        result = collection.delete_one({"idDepartment": idDep,
                                        "number": number})
        row = {
            "flag": 'true', }
        response.append(row)
        return response

#     def updatcourse(self):
#
#         collection = self._db["Instructor"]
#         collection.update_many({}, {"$set": {"gender": '??????'}}, upsert=False, array_filters=None)
#
#
# d = DataBase().updatcourse()