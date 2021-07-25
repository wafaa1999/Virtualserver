from dataBaseClass import DataBase


class User:
    def __init__(self):
        self._database = DataBase()

    def check_user(self, idUser, password):
        response = []
        flag = True
        userData = self._database.get_data_from_user()
        depData = self._database.get_data_from_dep()

        for i in range(len(userData)):
            if idUser == userData[i]['userName'] and password == userData[i]['password']:
                inst = self._database.get_instrctor(userData[i]['idInstructor'])
                for j in range(len(depData)):
                    if  inst[0]['idDepartment'] == str(depData[j]['_id']):
                        flag = False
                        row = dict(
                            idDep=inst[0]['idDepartment'],
                            type=userData[i]['type'],
                            name=inst[0]['name'],
                             depName=depData[j]['name'])
                        response.append(row)

        if flag:
            row1 = dict(
                idDep='None',
                type='None')
            response.append(row1)

        return response

    def check_email(self, email):
        response = []
        flag = True
        print(email)
        userData = self._database.get_data_from_user()
        for i in range(len(userData)):
            val = userData[i]['email']
            if email == val:
                flag = False
                row = dict(
                    idIstructor=userData[i]['idInstructor'],
                    email=userData[i]['email'],
                )
                response.append(row)
        if flag:
            row1 = dict(
                idIstructor='None',
                email='None')
            response.append(row1)

        return response

    def update_password(self, instID, passwordCode):
        self._database.update_password_for_Inst(instID, passwordCode)
