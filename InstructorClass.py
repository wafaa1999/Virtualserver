from dataBaseClass import DataBase


class Instructor:
    def __init__(self):
        self._database = DataBase()

    def get_all_inst_of_department(self,idDep):
        response = []
        result = self._database.get_all_Isnt(idDep)
        for i in range(len(result)):
            row = dict(
                name=result[i]['name'],
                idDepartment=result[i]['idDepartment'],
            )
            response.append(row)

        return response