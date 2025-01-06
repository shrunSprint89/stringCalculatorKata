class StringCalculator:
    def Add(self, numbers) -> int:
        if numbers.isdigit():
            return int(numbers)
        if ',' in numbers:
            number_list = numbers.split(',')
            sum = 0
            for num in number_list:
                sum += int(num)
            return sum
        return 0
