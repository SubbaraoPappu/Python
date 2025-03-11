def common_subjects(grade1,grade2, grade3):
    if not grade1 or not grade2 or not grade3:
            return set()
    all_grades=[grade1, grade2, grade3]

    for grade in all_grades:
        for subjects in grade.values():
            if not subjects:
                return set()
    
    is_grade1 = set.intersection(*grade1.values())
    is_grade2 = set.intersection(*grade1.values())
    is_grade3 = set.intersection(*grade1.values())

    return is_grade1 & is_grade2 & is_grade3

grade1 = {"Alice": {"Math", "English"}, "Bob": {"Math", "Science"}}
grade2 = {"Charlie": {"Math", "History"}, "David": {"Math", "English"}}
grade3 = {"Eva": {"Math", "Music"}, "Frank": {"Math", "Science"}}
grade4 = {}
grade5 = {"Gina": {}, "Hank": {"Math","History"}}

print(common_subjects(grade1, grade2, grade3))  # Output: {"Math"}
print(common_subjects(grade1, grade2, grade4))  # Output: set()
print(common_subjects(grade1, grade2, grade3, grade5))  # Output: {"Math"}