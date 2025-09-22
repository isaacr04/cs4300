favorite_books = [("Mother of Learning", "Domagoj Kurmaić"),
                  ("The Light of All That Falls", "James Islington"),
                  ("Golden Son", "Pierce Brown"),
                  ("Demon in White", "Christopher Ruocchio"),
                  ("Malcolm X", "Manning Marable")]

def slice_list(list):
    first_three = list[:3]
    print(first_three)

def make_students():
    students = ["John C.", "Emily T.", "Laura K.", "Megan S."]

    student_dict = {}
    for student in students:
        student_dict[students.index(student)] = student

    return student_dict