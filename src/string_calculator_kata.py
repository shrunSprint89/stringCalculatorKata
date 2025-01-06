class StringCalculator:
    def Add(self, numbers) -> int:
        if numbers.startswith("//[") and "]" in numbers:
            delimiter_end = numbers.find("]")
            delimiter = numbers[3:delimiter_end]
            numbers = numbers[delimiter_end + 2:]
            number_list = self.__split_numbers(numbers, [delimiter])
            return self.__calculate_sum(number_list)
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers[4:]
            number_list = self.__split_numbers(numbers, [delimiter])
            return self.__calculate_sum(number_list)
        if numbers.isdigit():
            return int(numbers)
        if ',' in numbers or '\n' in numbers:
            number_list = self.__split_numbers(numbers, [",","\n"])
            return self.__calculate_sum(number_list)
        return 0

    def __calculate_sum(self, number_list):
        sum = 0
        for num in number_list:
            if int(num) <= 1000:
                sum += int(num)
        return sum
       
    def __split_numbers(self, numbers, delimiters):
        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ',')
        return numbers.split(',')