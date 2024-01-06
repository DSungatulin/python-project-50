from gendiff.define_diff import generate_diff

def test_generate_diff():
    first_file = 'tests/fixtures/file1.json'
    second_file = 'tests/fixtures/file2.json'
    file_differences = generate_diff(first_file, second_file)
    correct_result = open('tests/fixtures/correct_comparison.txt', 'r')
    assert file_differences == correct_result.read()
    
    first_file = 'tests/fixtures/file1.yml'
    second_file = 'tests/fixtures/file2.yml'
    file_differences = generate_diff(first_file, second_file)
    correct_result = open('tests/fixtures/correct_comparison.txt', 'r')
    assert file_differences == correct_result.read()
