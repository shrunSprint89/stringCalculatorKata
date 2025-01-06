# String Calculator TDD Kata

This repo implements the String Calculator TDD Kata as defined by Roy Osherove (https://osherove.com/tdd-kata-1/). The kata involves creating a string calculator that can handle basic string parsing and addition with various rules and edge cases.

## Getting Started

### Prerequisites

- Python 3.x
- pytest

### Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/string-calculator-kata.git
cd string-calculator-kata
```

### Running Tests

To run the tests:

```bash
pytest -v
```

### Using the Calculator

To use the string calculator in your code:

```python
from string_calculator import StringCalculator

calculator = StringCalculator()
result = calculator.Add("1,2,3")  # Returns 6
```

The Add method accepts a string input containing numbers separated by commas and returns their sum. See the kata rules for supported formats and special cases.
