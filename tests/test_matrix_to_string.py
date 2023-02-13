import math
from unittest import TestCase
from api.matrix_to_string import CSVFileToString

class MatrixToStringTest(TestCase):

    def test_clean_file_data(self):

        file_data_from_upload = '1,2,3\n4'

        cleaned_data = CSVFileToString.clean_file_data(data=file_data_from_upload)

        self.assertTrue(type(cleaned_data) is list)
        cleaned_string = ['1', '2', '3', '4']

        self.assertEqual(cleaned_data, cleaned_string)

    def test_convert_data_is_integers(self):

        file_data_from_upload = '1,2,3\n4'

        cleaned_data = CSVFileToString.clean_file_data(data=file_data_from_upload)

        converted_data = CSVFileToString.convert_data_list(data=cleaned_data,  convert=True)

        self.assertTrue(type(cleaned_data) is list)
        self.assertTrue(all(type(obj) is int for obj in converted_data))

    def test_get_product_of_integers(self):

        file_data_from_upload = '1,2,3\n4'

        csv_obj = CSVFileToString.create_matrix_object(file_data=file_data_from_upload)

        output = csv_obj.output_product_data()

        self.assertEqual(output.description, 'Product of list')
        self.assertEqual(output.data, math.prod([1, 2, 3, 4]))

    def test_get_sum_of_integers(self):

        file_data_from_upload = '1,2,3\n4'

        csv_obj = CSVFileToString.create_matrix_object(file_data=file_data_from_upload)

        output = csv_obj.output_sum_data()

        self.assertEqual(output.description, 'Sum of integers')
        self.assertEqual(output.data, sum([1, 2, 3, 4]))

    def test_get_flattened_string_of_data(self):

        file_data_from_upload = '1,2,3\n4'

        csv_obj = CSVFileToString.create_matrix_object(file_data=file_data_from_upload)

        output = csv_obj.output_flatten_data()

        self.assertEqual(output.description, 'Flattened string')
        self.assertEqual(output.data, '1,2,3,4')