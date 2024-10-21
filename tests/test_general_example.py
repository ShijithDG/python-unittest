import pytest
from unittest.mock import patch
from src.general_example import GeneralExample

class TestGeneralExample:

    def test_flatten_dictionary(self):
        example = GeneralExample()
        input_data = {'key1': [3, 2, 1], 'key2': [42, 55, 10], 'key3': [0, 22]}
        expected_output = [0, 1, 2, 3, 10, 22, 42, 55]
        result = example.flatten_dictionary(input_data)
        assert result == expected_output

    @patch.object(GeneralExample, 'load_employee_rec_from_database')
    def test_fetch_emp_details(self, mock_load):
        # Mock the return value of load_employee_rec_from_database
        mock_load.return_value = ['emp001', 'Sam', '100000']
        
        example = GeneralExample()
        expected_output = {
            'empId': 'emp001',
            'empName': 'Sam',
            'empSalary': '100000'
        }
        
        result = example.fetch_emp_details()
        assert result == expected_output
