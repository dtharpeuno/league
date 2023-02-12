import math
from dataclasses import dataclass
from typing import List

@dataclass
class Output:
    description: str
    data: str

class CSVFileToString:

    def __init__(self, *, file_data):
        self.cleaned_file_data = self.clean_file_data(
            data=file_data
        )

    @classmethod
    def clean_file_data(cls, *, data) -> str:
        """
        Used for claening intiial data that was extracte from
        the file upload
        :param: data: String extracted from csv file
        :return data
        """
        data = data.replace('\n', ',').split(',')
        return data

    @classmethod
    def convert_data_list(cls, *, data: str, convert=False) -> List:
        """
        Used for converting instance file data to a list
        If convert = True the eval operator converts the
        strings to integers
        :param: data: String extracted from csv file
        :return: List
        """
        if convert:
            return [eval(i) for i in data]
        return [i for i in data]

    @classmethod
    def create_matrix_object(cls, *, file_data: str):
        """
        Used as a factory for creating an instance
        of CSVFileToString
        :param: file_data: String extracted from csv file
        :return: CSVFileToString
        """
        return CSVFileToString(file_data=file_data)

    def output_sum_data(self) -> Output:
        """
        Returns the Output dataclass object
        with the sum of an integer converted list
        :return Output
        """
        return Output(
            description='Sum of integers',
            data=sum(self.convert_data_list(
                    data=self.cleaned_file_data,
                    convert=True
                )
            )
        )

    def output_flatten_data(self) -> Output:
        """
        Returns the Output dataclass object
        with the "flattened" string of instance
        file_data variable
        :return Output
        """
        return Output(
            description='Flattened string',
            data=','.join(self.cleaned_file_data)
        )

    def output_product_data(self) -> Output:
        """
        Returns the Output dataclass object
        with the product of an integer converted list
        using math module form standard lib
        :return Output
        """
        return Output(
            description='Product of list',
            data=math.prod(self.convert_data_list(
                    data=self.cleaned_file_data,
                    convert=True
                ))
        )

    def output_string_matrix_format(self) -> Output:
        """
        Returns the Output dataclass object
        with the initial data that was stored to instance from
        file upload read() method
        :return Output
        """
        return Output(
            description='Matrix formatted string',
            data=','.join(
                obj+'\n' if i % 3 == 0 and i != 0 else obj for i, obj in enumerate(self.cleaned_file_data, start=1)
                )
        )

    def output_inverted_matrix(self) -> Output:
        """
        Returns the Output dataclass object
        with the initial data that was stored to instance from
        file upload read() method
        :return Output
        """
        intitial_list = self.convert_data_list(
            data=self.cleaned_file_data
        )
        start, current, incrementer, list_mapping = 0, 0, 3, {}
        # build inital list so indexes exists for later insert
        final_list = [None] * len(intitial_list)

        # create dictionary of lists for mapping
        for i, _ in enumerate(intitial_list, start=1):
            if i % 3 == 0 and i != 0:
                list_mapping[start] = intitial_list[current:incrementer+current]
                start += 1
                current = i

        # iterate thru dictionary items and insert in correct
        # inverted index
        for index_key, item_list in list_mapping.items():
            pos_key = index_key
            for item in item_list:
                # insert item in correct index
                final_list.insert(pos_key, item)
                # remove newly created index since
                # index() makes a right-shift addition
                # of current items in list
                final_list.pop(pos_key+1)
                pos_key += incrementer

        return Output(
            description='Inverted matrix formatted string',
            data=','.join(
                obj+'\n' if i % 3 == 0 and i != 0 else obj for i, obj in enumerate(final_list, start=1)
                )
        )


if __name__ == "__main__":
    pass
