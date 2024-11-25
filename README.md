---

# Decimal, IP to Binary, and Binary to IP Converter

This project provides a Python script to convert:
1. Decimal numbers to their 8-bit binary representation.
2. IPv4 addresses to their binary representation.
3. Binary IP addresses back to standard dotted-decimal IPv4 format.

The script uses command-line arguments for input and includes validation to ensure correct input formats and values.

## Features

- **decimal_to_binary**: Converts a decimal number (0-255) to an 8-bit binary string.
- **ip_to_binary**: Converts an IPv4 address to its binary representation, with each octet as an 8-bit binary string.
- **binary_to_ip**: Converts a binary IP address to its standard IPv4 dotted-decimal format.

## Functions

### decimal_to_binary

Converts a decimal number to its 8-bit binary representation.

#### Parameters
- `num` (int): A decimal number between 0 and 255.

#### Returns
- `binary_str` (str): The 8-bit binary representation of the input number.

---

### ip_to_binary

Converts an IPv4 address to its binary representation.

#### Parameters
- `ip_address` (str): A string representing an IPv4 address (e.g., `192.168.1.1`).

#### Returns
- `binary_ip` (str): The binary representation of the input IP address, with each octet as an 8-bit binary string, separated by dots.

---

### binary_to_ip

Converts a binary IP address to its dotted-decimal IPv4 format.

#### Parameters
- `binary_ip` (str): A binary IP address, with four 8-bit binary octets separated by dots (e.g., `11000000.10101000.00000001.00000001`).

#### Returns
- `ip_address` (str): The standard dotted-decimal IPv4 representation (e.g., `192.168.1.1`).

---

## Usage

1. Clone the repository or copy the script to your local machine.
2. Ensure Python is installed (version 3.x recommended).
3. Run the script from the command line to perform conversions.

### Example Commands

#### Convert a decimal number to binary:
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

#### Convert an IP address to binary:
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

#### Convert a binary IP address to dotted-decimal format:
```sh
python bin_calc.py binary <binary_ip>
```
Example:
```sh
python bin_calc.py binary 11000000.10101000.00000001.00000001
```
Output:
```
The dotted-decimal representation of 11000000.10101000.00000001.00000001 is: 192.168.1.1
```

---

## License

This project is open-source and available under the MIT License. See the LICENSE file for more information.

---

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

--- 
