import studis_api as studis
import moodle_api.moodle_api as mdl

ROLES = {'nosilci': 3,'asistenti':4, 'ostali':4}

def lang_format(self, data):
        "Transform given field to multilang string with <span class=\"multilang\""
        template =  "<span class=\"multilang\" lang=\"{}\">{}</span>"
        new_value = ""
        if len(value) == 1:
            for lang in value:
                new_value += value[lang]
        else:
            for lang in value:
                if value[lang]:
                    new_value += template.format(lang, value[lang])
        return new_value    
                
def user(s_user, auth="ldap", moodle_courses=None):
    if s_user.get('predmetnik'):
        course_idnumbers = [c['sifra_predmeta'] for c in s_user.get('predmetnik')]
    else:
        course_idnumbers = []
    user = mdl.User( username = s_user['upn'].strip(),
            firstname = s_user['ime'],
            lastname = s_user['priimek'],
            email = s_user['email'],
            auth = auth,
            idnumber = s_user.get('vpisna_stevilka'),
            password = 'Geslo je t4ko doloceno z ldap',
            course_idnumbers = course_idnumbers)
    if moodle_courses:
        user.enrolments(moodle_courses)
    return user

def course(s_course):
    return mdl.Course(fullname = lang_format(s_course['naslov']),
            summary = lang_format(s_course['opis']),
            idnumber = s_course['sifra_predmeta'],
            semester = s_course['semester'])

def cathegory(s_tree):
    return mdl.Cathegory(name = mdl.lang_format(s_tree['title']),
            parent_idnumber = s_tree['parent'],
            idnumber = s_tree['id'])


    

def teacher_enrolments(course, m_courses, s_courses, s_teachers):
    pass