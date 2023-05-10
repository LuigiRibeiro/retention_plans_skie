# This is a test lib retention_plans.
from retention_plans import check_retention
import datetime as dt


def test_retention_plans():
    list_tests = [
        (dt.date(2023, 5, 5), 'standard', True),
        (dt.date(2023, 5, 5), 'standard', False), # Force erro
        (dt.date(2023, 5, 5), 'gold', True),
        (dt.date(2023, 5, 5), 'platinum', True),
        (dt.date(2022, 4, 30), 'standard', False),
        (dt.date(2022, 4, 30), 'gold', False),
        (dt.date(2023, 4, 30), 'gold', True),
        (dt.date(2022, 4, 30), 'platinum', False),
        (dt.date(2010, 12, 31), 'standard', False),
        (dt.date(2010, 12, 31), 'gold', False),
        (dt.date(2010, 12, 31), 'platinum', False),
        (dt.date(2020, 12, 31), 'platinum', True),
    ]

    test_success = 0
    test_erro = 0

    for test in list_tests:
        if check_retention(test[0], test[1]) == test[2]:
            test_success += 1
        else:
            test_erro += 1

    print('Results test:')
    print(f'Success: {test_success}')
    print(f'Erro: {test_erro}')



if __name__ == '__main__':
    test_retention_plans()

