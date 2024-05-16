from gendiff.generate_diff import generate_diff


def test_gendiff():
    file1_json = '/home/fedor/Hexlet/python-project-50/tests/fixtures/file3.json'
    file2_json = '/home/fedor/Hexlet/python-project-50/tests/fixtures/file4.json'
    result_stylish = open('/home/fedor/Hexlet/python-project-50/tests/fixtures/result_stylish.txt')
    result_plain = open('/home/fedor/Hexlet/python-project-50/tests/fixtures/result_plain.txt')
    result_json = open('/home/fedor/Hexlet/python-project-50/tests/fixtures/result_json.txt')
    assert generate_diff(file1_json, file2_json, format='stylish') == result_stylish.read()
    assert generate_diff(file1_json, file2_json, format='plain') == result_plain.read()
    assert generate_diff(file1_json, file2_json, format='json') == result_json.read()
    result_stylish.close()
    result_plain.close()
    result_json.close()






'''
тест на ошибочное расширение(txt)
тест на ошибочный форматор(wrong format)
'''