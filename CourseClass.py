from dataBaseClass import DataBase


class Course:
    def __init__(self):
        self._database = DataBase()

    def get_courses(self, idDep, year, sem):
        response = []
        resultForOne = []
        results = [[], [], [], [], [], [], [], [], [], [], []]
        # instrctor = self._database.get_instrctor(idIstructor)
        # idDep = str(instrctor[0]['idDepartment'])
        courses = self._database.get_courses_of_dep(idDep)
        flag = []
        years = []
        first = []
        for i in range(len(courses)):
            if courses[i]['year'] == year and courses[i]['semester'] == sem:
                row = dict(
                    name=courses[i]['name'],
                    number=courses[i]['number'],
                )
                response.append(row)
        # for k in range(11):
        #     flag.append(False)
        #     first.append(True)
        #     years.append("")
        #
        # for i in range(len(courses)):
        #     if idDep == courses[i]['toDepartments']:
        #         row = courses[i]['name']
        #
        #
        #         if (courses[i]['year']) == '-1':
        #             results[0].append(row)
        #             if first[0]:
        #               flag[0] = True
        #               years[0] = "المساقات الاختيارية"
        #               first[0] = False
        #
        #         elif (courses[i]['year']) == '1':
        #             if (courses[i]['semester']) == '1':
        #                 results[1].append(row)
        #                 if first[1]:
        #                   flag[1] = True
        #                   years[1] = "السنة الأولى"
        #                   first[1] = False
        #             else:
        #                 results[2].append(row)
        #                 if first[2]:
        #                   flag[2] = True
        #                   years[2] = "السنة الأولى"
        #                   first[2] = False
        #
        #         elif (courses[i]['year']) == '2':
        #             if (courses[i]['semester']) == '1':
        #                 results[3].append(row)
        #                 if first[3]:
        #                   flag[3] = True
        #                   years[3] = "السنة الثانية"
        #                   first[3] = False
        #
        #             else:
        #                 results[4].append(row)
        #                 if first[4]:
        #                   flag[4] = True
        #                   years[4] = "السنة الثانية"
        #                   first[4] = False
        #
        #         elif (courses[i]['year']) == '3':
        #             if (courses[i]['semester']) == '1':
        #                 results[5].append(row)
        #                 if first[5]:
        #                   flag[5] = True
        #                   years[5]="السنة الثالثة"
        #                   first[5] = False
        #
        #             else:
        #                 results[6].append(row)
        #                 if first[6]:
        #                   flag[6] = True
        #                   years[6]="السنة الثالثة"
        #                   first[6] = False
        #
        #         elif (courses[i]['year']) == '4':
        #             if (courses[i]['semester']) == '1':
        #                 results[7].append(row)
        #                 if first[7]:
        #                   flag[7] = True
        #                   years[7]="السنة الرابعة"
        #                   first[7] = False
        #
        #             else:
        #                 results[8].append(row)
        #                 if first[8]:
        #                   flag[8] = True
        #                   years[8]="السنة الرابعة"
        #                   first[8] = False
        #
        #         elif (courses[i]['year']) == '5':
        #             if (courses[i]['semester']) == '1':
        #                 results[9].append(row)
        #                 if first[9]:
        #                   flag[9] = True
        #                   years[9]="السنة الخامسة"
        #                   first[9] = False
        #
        #             else:
        #                 results[10].append(row)
        #                 if first[10]:
        #                   flag[10] = True
        #                   years[10]="السنة الخامسة"
        #                   first[10] = False
        # final = []
        # for j in range(1, 11):
        #     if flag[j]:
        #         resultForOne.append(years[j])
        #         if j % 2 == 1:
        #             resultForOne.append("الفصل الأول")
        #         else:
        #             resultForOne.append("الفصل الثاني")
        #         resultForOne.append(results[j])
        #     final = resultForOne.copy()
        #     resultForOne.clear()
        #     response.append(final)

        return response

    def add_course_to_dep(self, idDep, name, number, numberOfHour, type, year, sem,toDepartments , flag,specialty):
       response = []
       flag1 = True
       result = self._database.get_course_of_dep(idDep)
       for i in range(len(result)):
           if result[i]['number'] == number and idDep == result[i]['idDepartment']:
               flag1 = False
       if flag1:
           # idDep, name, number, numberOfHour, type, year, sem, flag,toDepartments,specialty
           response = self._database.add_course_to_dep(idDep, name, number, numberOfHour, type, year, sem, flag,toDepartments,specialty)
       else:
           response.append("0")

       return response

    def get_all_materials_of_department(self, idDep):
        response = []
        result = self._database.get_courses_of_dep(idDep)
        for i in range(len(result)):
            if idDep == str(result[i]['idDepartment']):
                row = dict(
                    name=result[i]['name'],
                    number=result[i]['number'],
                    year=result[i]['year'],
                    type=result[i]['type'],
                    courseHours=result[i]['courseHours'],
                    idDepartment=result[i]['idDepartment'],
                    semester=result[i]['semester'],
                    toDepartments=result[i]['toDepartments'],
                    flagFrom=result[i]['flagFrom'],
                    flagTo=result[i]['flagTo'],
                )
                response.append(row)


        return response

    def get_all_materials_of_sep_dep(self, idDep, id):
        response = []
        result = self._database.get_courses_of_dep(idDep)
        for i in range(len(result)):
            if idDep == str(result[i]['idDepartment']) and id == str(result[i]['toDepartments']):
                row = dict(
                    name=result[i]['name'],

                )
                response.append(row)

        return response

    def delete_Course_from_dep(self, idDep, number):
        result = self._database.delete_Course_from_department(idDep, number)
        return result

