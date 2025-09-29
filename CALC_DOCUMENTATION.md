# Arithmetic Calculator Documentation

## Overview

The `calc.py` file contains a comprehensive command-line arithmetic calculator written in Python. It provides a user-friendly interface for performing basic mathematical operations and evaluating complex mathematical expressions.

## File Structure

### Main Components

1. **ArithmeticCalculator Class** - Core calculator functionality
2. **Menu System** - User interface and navigation
3. **Input Validation** - Error handling and data validation
4. **Main Program Loop** - Application control flow

## Class: ArithmeticCalculator

### Purpose
The `ArithmeticCalculator` class encapsulates all mathematical operations and maintains calculation history.

### Attributes
- `history` (list): Stores a record of all performed calculations

### Methods

#### Basic Operations
- `add(a, b)` - Performs addition: a + b
- `subtract(a, b)` - Performs subtraction: a - b
- `multiply(a, b)` - Performs multiplication: a × b
- `divide(a, b)` - Performs division: a ÷ b (with zero-division protection)
- `power(a, b)` - Performs exponentiation: a^b
- `modulo(a, b)` - Performs modulo operation: a % b (with zero-modulo protection)

#### Advanced Features
- `evaluate_expression(expression)` - Safely evaluates complex mathematical expressions
- `show_history()` - Displays all previous calculations
- `clear_history()` - Removes all calculation history

### Error Handling
- Division by zero prevention
- Invalid expression detection
- Input validation using regular expressions
- Safe expression evaluation with restricted globals

## User Interface Functions

### `display_menu()`
**Purpose**: Shows the main calculator menu with all available options
**Output**: Formatted menu with numbered choices (0-9)

### `get_number(prompt)`
**Purpose**: Safely gets numeric input from the user
**Parameters**: 
- `prompt` (str): Message to display to the user
**Returns**: float - Valid numeric value
**Features**: Continuous validation loop until valid number is entered

### `main()`
**Purpose**: Main program loop that controls the calculator flow
**Features**:
- Menu-driven interface
- Choice handling for all calculator operations
- Error handling for user interruptions
- Graceful exit handling

## Features Summary

### ✅ Supported Operations
- **Basic Arithmetic**: +, -, ×, ÷
- **Advanced Math**: Power (^), Modulo (%)
- **Expression Evaluation**: Complex expressions with parentheses
- **History Management**: View and clear calculation history

### ✅ Safety Features
- Zero division protection
- Input validation and sanitization
- Safe expression evaluation
- Error messages for invalid operations

### ✅ User Experience
- Clear, formatted menu system
- Descriptive error messages
- Calculation history tracking
- Keyboard interrupt handling (Ctrl+C)

## Usage Examples

### Basic Operations
```
Choice 1: Addition
Enter first number: 5
Enter second number: 3
Result: 5.0 + 3.0 = 8.0
```

### Expression Evaluation
```
Choice 7: Evaluate Expression
Enter mathematical expression: (10-5)^2 + 3*4
Result: (10-5)^2 + 3*4 = 37.0
```

### History Management
```
Choice 8: Show History
--- Calculation History ---
1. 5.0 + 3.0 = 8.0
2. (10-5)^2 + 3*4 = 37.0
```

## Technical Details

### Dependencies
- `sys` - System operations and exit handling
- `re` - Regular expression validation
- Built-in Python functions for mathematical operations

### Input Validation
- Regular expression pattern: `^[0-9+\-*/().%^]+$`
- Restricted `eval()` execution with empty `__builtins__`
- Number format validation for user inputs

### Security Considerations
- Safe expression evaluation prevents code injection
- Limited character set for mathematical expressions
- No access to built-in functions during expression evaluation

## Error Types and Handling

| Error Type | Cause | Handling |
|------------|-------|----------|
| `ValueError` | Division by zero, invalid expression | Display error message, continue program |
| `KeyboardInterrupt` | User presses Ctrl+C | Graceful exit with goodbye message |
| `General Exception` | Unexpected errors | Display error message, continue program |

## Program Flow

1. **Initialization**: Create calculator instance
2. **Menu Display**: Show available options
3. **User Input**: Get user choice
4. **Operation Execution**: Perform selected calculation
5. **Result Display**: Show calculation result
6. **History Update**: Add to calculation history
7. **Loop**: Return to menu (unless exit chosen)

## Code Quality Features

- **Object-Oriented Design**: Clean class structure
- **Error Handling**: Comprehensive exception management
- **Input Validation**: Robust user input checking
- **Documentation**: Clear docstrings and comments
- **Modularity**: Separated concerns for easy maintenance

## Running the Calculator

### Prerequisites
- Python 3.x installed
- Terminal/Command prompt access

### Execution
```bash
python calc.py
```

### Exit Options
- Choose option `0` from menu
- Press `Ctrl+C` for immediate exit

---

*This documentation covers the complete functionality of the arithmetic calculator implementation in `calc.py`.*
