from gendiff import generate_diff


def test_generate_diff_flat_json():
    file1 = './tests/fixtures/file1.json'
    file2 = './tests/fixtures/file2.json'
    expected_result = open('./tests/fixtures/test_gendiff_flat_json.txt', 'r').read()
    assert expected_result == generate_diff(file1, file2)
