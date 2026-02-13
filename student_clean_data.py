students=[
    
    {"id":1, "name": "anamika","marks":80},
    {"id":2, "name": "amit","marks":68},
    {"id":3, "name": "ranchod das","marks":18},
    {"id":13, "name": "aman","marks":56},
    {"id":13, "name": "aman","marks":85},
    {"id":12, "name": "anika","marks":89},
    {"id":15, "name": "harjot","marks":58},
    {"id":16, "name": "aman","marks":69},
    {"id":5, "name": "aman","marks":71},
    {"id":14, "name": "aman","marks":28}

    ]
print("\n\tOriginal Data\n\n ",students)
unique_students=[]
seen_ids=set()
for students in students:
    if students["id"] not in seen_ids:
        unique_students.append(students)
        seen_ids.add(students["id"])
print("\n \tAfter Removing Duplicates:\n\n", unique_students)

cleaned_students=[s for s in unique_students if s["marks"]>=0]
print("\n \tAfter Removing Invalid Marks:\n\n",cleaned_students)

passed_students =[s for s in cleaned_students if s["marks"]>=45]
print("\n \tPassed students:\n\n",passed_students)
total_marks= sum(s["marks"]for s in cleaned_students)
average = total_marks/len(cleaned_students)
print("\n\tAverage Marks:", average)

