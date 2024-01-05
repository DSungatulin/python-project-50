from gendiff.define_diff import generate_diff

def test_generate_diff():
    first_file = 'tests/fixtures/file1.json'
    second_file = 'tests/fixtures/file2.json'
    file_differences = generate_diff(first_file, second_file)
    correct_result = open('tests/fixtures/correct_comparison.txt', 'r')
    assert file_differences == correct_result.read()

def test_generate_diff_2():
    first_file = 'tests/fixtures/file1.json'
    second_file = 'tests/fixtures/file2_extended.json'
    file_differences = generate_diff(first_file, second_file)
    correct_result = open('tests/fixtures/extended_file_comparison.txt', 'r')
    assert file_differences == correct_result.read()
