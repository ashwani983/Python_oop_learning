# Project Title

Python OOP's Learning

## Description

This project is a simple inventory management system that manages different types of items, specifically phones and keyboards. It allows users to create instances of these items, apply discounts, and manage their prices.

## Classes

- **Item**: The base class that contains common attributes and methods for all items.
- **Phone**: A subclass of `Item` that represents phone items.
- **Keyboard**: A subclass of `Item` that represents keyboard items.

## Usage

To use the project, you can create instances of the classes as follows:

```python
item1 = Item('Phone', 100)
item1.apply_discount()
print(item1.price)

phone1 = Phone('Iphone', 1000, 2, 1)
print(phone1.apply_increment(20))

keyboard1 = Keyboard('Dell', 100, 2, 1)
print(keyboard1.apply_increment(20))
```

## Installation

No specific installation instructions are required. Ensure you have Python installed to run the scripts.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License.
