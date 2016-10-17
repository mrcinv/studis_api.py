from requests import get
from datetime import datetime

# Module variables to connect to STUDIS api
KEY = "SECRET API KEY"
URL = "https://studis.site.com"
ENDPOINT="/api/"

def call(apiname, **kwargs):
    """Calls STUDIS API function with apiname and keyword arguments.

    Example:
    >>> import studis_api
    >>> studis_api.call('osebeapi/oseba',courses=)
    """
    studis_headers = {"Content-Type": "application/json",
                     "AUTHENTICATION_TOKEN": KEY}
    response = get(URL+ENDPOINT+apiname, headers=studis_headers)
    return response.json()

class CourseList():
    """Class for list of all courses in Moodle and order them by id and idnumber."""
    def __init__(self,year=None):
        if not year:
            year = datetime.now().strftime("%Y")
        self.courses = call('studijapi/%s/izvajanjepredmeta' % str(year))
        data = call('studijapi/%s/predmet' % str(year))
        self.by_id = {}
        self.by_idnumber = {}
        for course in self.courses:
            self.by_id[course['idpredmet']] = course
            self.by_idnumber[course['sifra_predmeta']] = course
        for course in data:
            keys = self.by_id.keys()
            if course['id'] in keys:
                self.by_id[course['id']].update(course)


class StudentList():
    """Class representing student list
    """
    def __init__(self,date=None):
        if date==None:
            date_str = datetime.now().strftime("%Y-%m-%d")
        self.students = call('/studentiapi/student?date='+date_str)
        self.by_idnumber = {}
        for student in self.students:
            self.by_idnumber[student['vpisna_stevilka']] = student

class StaffList():
    """Class representing list of personel."""
    def __init__(self):
        self.staff = call('/osebeapi/oseba/')
        self.by_id = {}
        for person in self.staff:
            self.by_id[person['id']] = person

class StudyTree():
    "Class representing stusy tree of programs and years"
    def __init__(self,date=None):
        if date==None:
            date_str = datetime.now().strftime("%Y")
        self.programs = call('//studijapi/studijskodrevo/'+date_str)
        self.tree = {}
        self.by_id = {}
        for program in self.programs:
            self.by_id[program['id']] = program
            if not program['parent']:
                self.tree[program['id']] = program
        for program in self.programs:
            if program['parent']:
                parent = self.by_id[program['parent']]
                parent['children'] = parent.get('children',[])+[program]
