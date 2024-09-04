---

# Decimal to Binary and IP to Binary Converter

This project provides a Python script that converts decimal numbers and IPv4 addresses to their binary representations. The script uses command-line arguments for input and includes validation to ensure correct input formats and values.

## Features

- **decimal_to_binary**: Converts a decimal number (0-255) to an 8-bit binary string.
- **ip_to_binary**: Converts an IPv4 address to its binary representation, with each octet represented as an 8-bit binary string. Includes validation for correct IP address format and octet ranges.

## Functions

### decimal_to_binary

Converts a decimal number to its 8-bit binary representation.

#### Parameters
- `num` (int): A decimal number between 0 and 255.

#### Returns
- `binary_str` (str): The 8-bit binary representation of the input number.

### ip_to_binary

Converts an IPv4 address to its binary representation.

#### Parameters
- `ip_address` (str): A string representing an IPv4 address (e.g., '192.168.1.1').

#### Returns
- `binary_ip` (str): The binary representation of the input IP address, with each octet represented as an 8-bit binary string, separated by dots.

## Usage

1. Clone the repository or copy the script to your local machine.
2. Ensure you have Python installed (version 3.x recommended).
3. Use the script from the command line to convert a decimal number or IP address to binary.

### Example Commands

To convert a decimal number to binary:
```sh
python bin_calc.py decimal <number>
```
Example:
```sh
python bin_calc.py decimal 9
```
Output:
```
The binary representation of 9 is: 00001001
```

To convert an IP address to binary:
```sh
python bin_calc.py ip <ip_address>
```
Example:
```sh
python bin_calc.py ip 192.168.1.1
```
Output:
```
The binary representation of 192.168.1.1 is: 11000000.10101000.00000001.00000001
```

## License

This project is open-source and available under the MIT License. See the LICENSE file for more information.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---
