class StringCalculator:
    def Add(self, numbers) -> int:
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers[4:]
            number_list = numbers.split(delimiter)
            return self.__calculate_sum(number_list)
        if numbers.isdigit():
            return int(numbers)
        if ',' in numbers or '\n' in numbers:
            number_list = numbers.replace('\n', ',').split(',')
            return self.__calculate_sum(number_list)
        return 0

    def __calculate_sum(self, number_list):
        sum = 0
        for num in number_list:
            if int(num) <= 1000:
                sum += int(num)
        return sum
