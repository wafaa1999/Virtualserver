from dataBaseClass import DataBase


class Instructor:
    def __init__(self):
        self._database = DataBase()

    def get_all_inst_of_department(self,idDep):
        response = []
        result = self._database.get_all_Isnt(idDep)
        result2 = self._database.get_data_from_user()
        for i in range(len(result)):
            if idDep == result[i]['idDepartment']:
                for j in range(len(result2)):
                    if idDep == result2[j]['idDep']:
                         if result2[j]['name'] == result[i]['name']:
                             row = dict(
                                 name=result[i]['name'],
                                 idDepartment=result[i]['idDepartment'],
                                 email=result2[j]['email'],
                                 gender=result2[j]['gender'],

                             )
                             response.append(row)
        return response

    def add_Inst_to_dep(self, idDep, name):
        response = self._database.add_inst_to_deprtment( idDep, name)
        return response

    def delete_Inst_to_dep(self, idDep, name):
        response = self._database.delete_inst_to_deprtment(idDep, name)
        return response
