from data import mentors, courses, durations


def get_full_name(mentors):
    """Получить имена всех преподавателей"""

    all_list = []
    for m in mentors:
        all_list.extend(m)
    all_names_list = []
    for mentor in all_list:
        name = mentor.split(' ')[0]
        all_names_list.append(name)

    return all_names_list



def get_unique_name(mentors):
    """Уникальные имена преподавателей"""

    all_names_list = get_full_name(mentors)
	
    unique_names = set(all_names_list)
    all_names_sorted = sorted(list(unique_names))
    all_names_sorted=', '.join(all_names_sorted)
    return all_names_sorted


def get_top3_name(mentors):
    """Топ-3 уникальных имен преподавателей"""

    unique_names = (get_unique_name(mentors)).split(', ')
    all_names = get_full_name(mentors)
    popular = []
    for name in unique_names:
        popular.append([name, all_names.count(name)]) 
    popular.sort(key=lambda x:x[1], reverse=True)
    top_3 = popular[0:3]
    return f'{top_3[0][0]}: {top_3[0][1]} раз(а), {top_3[1][0]}: {top_3[1][1]} раз(а), {top_3[2][0]}: {top_3[2][1]} раз(а)'



def get_duration(courses, durations):
    """Названия и продолжительность самого короткого и самого длинного курсов"""

    courses_list = []
    for course, time in zip(courses, durations):
       course_dict = {
    'title' : course,
    'duration': time
  }
       courses_list.append(course_dict)

    min_ = min(durations)
    max_ = max(durations)
    maxes = []
    minis = []
    for ind, durations_ind in enumerate(durations):
       if durations_ind == max_:
            maxes.append(ind)
       elif durations_ind == min_:
            minis.append(ind)
    courses_min = []
    courses_max = []
    for id in minis:
        courses_min.append(courses_list[id].get('title'))
    for id in maxes:
        courses_max.append(courses_list[id].get('title'))
    return f"""Самый короткий курс(ы): {', '.join(courses_min)} - {min_} месяца(ев)
Самый длинный курс(ы): {", ".join(courses_max)} - {max_} месяца(ев)"""



# if __name__ == '__main__':
#     print(get_unique_name(mentors))
#     print(get_top3_name(mentors))
#     print(get_duration(courses, durations))