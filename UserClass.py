from dataBaseClass import DataBase


class User:
    def __init__(self):
        self._database = DataBase()

    def check_user(self, idUser, password):
        response = []
        flag = True
        userData = self._database.get_data_from_user()
        for i in range(len(userData)):
            if idUser == userData[i]['userName'] and password == userData[i]['password']:
                flag = False
                row = dict(
                    idIstructor=userData[i]['idInstructor'],
                    type=userData[i]['type'])
                response.append(row)
        if flag:
            row1 = dict(
                idIstructor='None',
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
