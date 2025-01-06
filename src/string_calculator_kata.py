class StringCalculator:
    def Add(self, numbers) -> int:
        if numbers.isdigit():
            return int(numbers)
            
        return 0
