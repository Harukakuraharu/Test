import pytest
from main import get_unique_name, get_top3_name, get_duration
from data import mentors, courses, durations



@pytest.mark.parametrize(
        'list_name, expected', 
        [
            (mentors, 'Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий'),
            (['1', '2', '1', '1', '3', '4', '5'], '1, 2, 3, 4, 5')
            
        ]

) 
def test_unique_name(list_name, expected):
    assert get_unique_name(list_name) == expected





@pytest.mark.parametrize(
        'list_name, expected', 
        [
            (mentors, 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'),
        ]

)                
def test_top3_name(list_name, expected):
    assert get_top3_name(list_name) == expected





@pytest.mark.parametrize(
        'list_course, list_duration, expected', 
        [
            (courses, durations, 'Самый короткий курс(ы): Fullstack-разработчик на Python - 12 месяца(ев)\nСамый длинный курс(ы): Java-разработчик с нуля, Frontend-разработчик с нуля - 20 месяца(ев)'),
        ]

)  
def test_duration(list_course, list_duration, expected):
    assert get_duration(list_course, list_duration) == expected

