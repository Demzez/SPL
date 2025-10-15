def count_subject_hours():
    subjects = {}

    with open("subjects.txt", "r", encoding="utf-8") as file:
        for line in file:

            parts = line.split(':')
            subject_name = parts[0].strip()
            hours_str = parts[1]


            total_hours = 0
            for part in hours_str.split():
                if '(' in part:
                    hours = part.split('(')[0]
                    total_hours += int(hours)

            subjects[subject_name] = total_hours

    print(subjects)


count_subject_hours()