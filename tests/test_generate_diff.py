from gendiff.diff_determinant import generate_diff


def test_generate_diff():
    first_file = 'tests/fixtures/flat_files/file1.json'
    second_file = 'tests/fixtures/flat_files/file2.json'
    file_differences = generate_diff(first_file, second_file)
    correct_result = open(
        'tests/fixtures/comparison_results/correct_flat_comparison.txt', 'r'
    )
    assert file_differences == correct_result.read()
    
    first_file = 'tests/fixtures/flat_files/file1.yml'
    second_file = 'tests/fixtures/flat_files/file2.yml'
    file_differences = generate_diff(first_file, second_file)
    correct_result = open(
        'tests/fixtures/comparison_results/correct_flat_comparison.txt', 'r'
    )
    assert file_differences == correct_result.read()
