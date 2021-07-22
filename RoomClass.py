from dataBaseClass import DataBase


class Room:
    def __init__(self):
        self._database = DataBase()

    def get_rooms_of_dep(self, idDep):
        response = []
        rooms = self._database.get_room()
        for i in range(len(rooms)):
            if idDep == rooms[i]['idDepartment']:
                row = dict(
                    number=rooms[i]['number'],
                    type=rooms[i]['type'],
                    campous=rooms[i]['campous']
                )
                response.append(row)
        return response

    def update_room(self,idDep,number,campous,type):
       result = self._database.update_data_for_room(idDep,number,campous,type)
       return result


