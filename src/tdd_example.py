class TDDExample():
    def __init__(self):
        pass

    def reverse_string(self, input_str: str) -> str:
        """
        Reverses order of characters in string input_str.
        """
        reversed_string = ''.join(reversed(input_str))
        return reversed_string

    def find_longest_word(self, sentence: str) -> str:
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        
        my_list = sentence.split()
        string_length = 0
        word = ''
        for i in range(len(my_list)):
            print(my_list[i])
            if big < len(my_list[i]):
                big = len(my_list[i])
                word = my_list[i]
        return word

    def reverse_list(self, input_list: list) -> list:
        """
        Reverses order of elements in list input_list.
        """
        # input_list[::-1]
        length = len(input_list) // 2
        for i in range(length):
            temp = input_list[i]
            input_list[i] = input_list[len(input_list) - i - 1]
            input_list[len(input_list) - i - 1] = temp
        return input_list

    def count_digits(self, input_list: list, number_to_be_counted: int) -> int:
        """
        Return count of digits
        
        """
        # count = input_list.count(number_to_be_counted) 
        number_count = 0
        for i in range(len(input_list)):
            if number_to_be_counted == input_list[i]:
                number_count += 1
        return number_count