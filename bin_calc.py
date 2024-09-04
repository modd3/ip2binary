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

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python bin_calc.py decimal <number>")
        print("  python bin_calc.py ip <ip_address>")
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
        else:
            print("Unknown mode. Use 'decimal' or 'ip'.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()