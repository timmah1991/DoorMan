import serial

# Device and configuration
serial_device = '/dev/serial/by-id/usb-Flipper_Devices_Inc._Flipper_Arull1n3_flip_Arull1n3-if00'  # Replace with your actual device
baud_rate = 230400  # Set the baud rate (check the device's documentation for the correct value)
timeout = 2  # Timeout for the serial connection in seconds

# Command to send
command = "subghz tx_from_file /ext/subghz/Dearborn.sub 100 0\n"  # Ensure newline character if required

try:
    # Open serial connection
    with serial.Serial(serial_device, baud_rate, timeout=timeout) as ser:
        print(f"Connected to {serial_device}")
        
        # Send the command
        ser.write(command.encode('utf-8'))
        print(f"Sent command: {command.strip()}")
        
        # Optional: Read the response (if the device sends one)
        response = ser.read_until(b'\n')  # Reads until a newline character
        print(f"Received response: {response.decode('utf-8').strip()}")

except serial.SerialException as e:
    print(f"Error connecting to serial device: {e}")