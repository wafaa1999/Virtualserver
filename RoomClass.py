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
                    campous=rooms[i]['campous'],
                    name=rooms[i]['name']
                )
                response.append(row)
        return response

    def getCat(self, idDep):
        cat = []
        rooms = self._database.get_room()

        for i in range(len(rooms)):
            if rooms[i]['name'] != 'قاعة تدريس' and idDep == rooms[i]['idDepartment'] :
                row = dict(
                    name=rooms[i]['name'])
                cat.append(row)
        return cat

    def update_room(self,idDep,number,campous,type, name):
       result = self._database.update_data_for_room(idDep,number,campous,type, name)
       return result

    def add_room_to_dep(self, idDep, number, type, campous, name):
        result = self._database.add_room(idDep, number, type, campous, name)
        return result

    def delete_room(self, idDep, number):
        result = self._database.delete_room_from_dep(idDep, number)
        return result




