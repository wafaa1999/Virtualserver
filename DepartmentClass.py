from dataBaseClass import DataBase


class Department:
    def __init__(self):
        self._database = DataBase()

    def get_all_dep(self):
        response = []
        result = self._database.get_data_from_dep()
        for i in range(len(result)):
            row = dict(
                name=str(result[i]['_id']),
                idDepartment=result[i]['name'],
            )
            response.append(row)

        return response

