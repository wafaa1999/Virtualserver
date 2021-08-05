from dataBaseClass import DataBase


class Instructor:
    def __init__(self):
        self._database = DataBase()

    def get_all_inst_of_department(self,idDep):
        response = []
        result = self._database.get_all_Isnt(idDep)
        for i in range(len(result)):
            if idDep == result[i]['idDepartment']:
                row = dict(
                    name=result[i]['name'],
                    idDepartment=result[i]['idDepartment'],
                )
                response.append(row)
        return response

    def add_Inst_to_dep(self, idDep, name):
        response = self._database.add_inst_to_deprtment( idDep, name)
        return response

    def delete_Inst_to_dep(self, idDep, name):
        response = self._database.delete_inst_to_deprtment(idDep, name)
        return response
