class StringCalculator:
    def Add(self, numbers) -> int:
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers[4:]
            number_list = numbers.split(delimiter)
            sum = 0
            for num in number_list:
                sum += int(num)
            return sum
        if numbers.isdigit():
            return int(numbers)
        if ',' in numbers or '\n' in numbers:
            number_list = numbers.replace('\n', ',').split(',')
            sum = 0
            for num in number_list:
                sum += int(num)
            return sum
        return 0
