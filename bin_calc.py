import sys

def decimal_to_binary(num):
    """Convert a decimal number to its 8-bit binary representation."""
    if not (0 <= num <= 255):
        raise ValueError("Number must be between 0 and 255.")
    
    binary = []
    remainder = num
    deci = [2 ** i for i in range(7, -1, -1)]  # 2^7 to 2^0
    for base in deci:
        if remainder >= base:
            binary.append('1')
            remainder -= base
        else:
            binary.append('0')
    binary_str = ''.join(binary)
    return binary_str

def ip_to_binary(ip_address):
    """Convert an IPv4 address to its binary representation."""
    octets = ip_address.split('.')
    
    if len(octets) != 4:
        raise ValueError("IP address must consist of exactly four octets.")
    
    binary_octets = []
    for octet in octets:
        try:
            num = int(octet)
            if not (0 <= num <= 255):
                raise ValueError(f"Octet {octet} is out of range. Must be between 0 and 255.")
            binary_octets.append(decimal_to_binary(num))
        except ValueError:
            raise ValueError(f"Invalid octet: {octet}")
    
    binary_ip = '.'.join(binary_octets)
    return binary_ip

def binary_to_decimal(binary_str):
    """Convert an 8-bit binary string to its decimal equivalent."""
    if len(binary_str) != 8 or not all(char in '01' for char in binary_str):
        raise ValueError("Binary string must be 8 bits long and contain only 0s and 1s.")
    return int(binary_str, 2)

def binary_to_ip(binary_ip):
    """Convert a binary IP address to its standard dotted-decimal IPv4 format."""
    octets = binary_ip.split('.')
    
    if len(octets) != 4:
        raise ValueError("Binary IP address must consist of exactly four 8-bit octets.")
    
    decimal_octets = []
    for binary_octet in octets:
        try:
            decimal_octets.append(str(binary_to_decimal(binary_octet)))
        except ValueError:
            raise ValueError(f"Invalid binary octet: {binary_octet}")
    
    return '.'.join(decimal_octets)

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python bin_calc.py decimal <number>")
        print("  python bin_calc.py ip <ip_address>")
        print("  python bin_calc.py binary <binary_ip>")
        return

    mode = sys.argv[1]
    value = sys.argv[2]

    try:
        if mode == 'decimal':
            num = int(value)
            if 0 <= num <= 255:
                print(f"The binary representation of {num} is: {decimal_to_binary(num)}")
            else:
                print("Number must be between 0 and 255.")
        elif mode == 'ip':
            print(f"The binary representation of {value} is: {ip_to_binary(value)}")
        elif mode == 'binary':
            print(f"The dotted-decimal representation of {value} is: {binary_to_ip(value)}")
        else:
            print("Unknown mode. Use 'decimal', 'ip', or 'binary'.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
