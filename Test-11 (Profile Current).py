import serial
import time
import os

# Define the log file directory
log_dir = r"C:\Users\ggarchev\Desktop\LoG device"


# Function to get the next log filename
def get_next_log_filename(log_dir, base_filename="log", extension=".txt"):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)  # Create directory if it doesn't exist

    i = 1
    while True:
        filename = f"{base_filename}{i}{extension}"
        full_path = os.path.join(log_dir, filename)
        if not os.path.exists(full_path):
            return full_path
        i += 1


# Function to log UART data
def log_uart_data(port, baudrate, log_dir, commands, expected_responses):
    ser = None

    try:
        ser = serial.Serial(port, baudrate, timeout=0)  # Timeout set to 0 for non-blocking mode
        print(f"Connected to {port} at {baudrate} baud.")

        if ser.is_open:
            print(f"Serial port {port} is open.")

            # Clear any existing data from the buffer
            ser.flushInput()

            log_file_path = get_next_log_filename(log_dir)

            with open(log_file_path, 'a') as log_file:
                print(f"Logging to file: {log_file_path}")

                for i in range(1, len(commands) + 1):
                    actual_command = commands[i]  # Get command by index

                    # Apply delays for specific commands
                    if i in [11, 14]:
                        time.sleep(2)
                        print(f"Applying 2-second delay for command {i}: {actual_command}")
                    else:
                        time.sleep(0.7)
                        print(f"Applying 1-second delay for command {i}: {actual_command}")

                    # Send the actual command to the device
                    print(f"Sending command {i}: {actual_command}")
                    full_command = (actual_command + '\r\n').encode('utf-8')
                    ser.write(full_command)
                    ser.flush()  # Ensure command is sent

                    # Wait for the expected response
                    response = ""
                    timeout = 3  # Set a timeout for waiting for the response
                    start_time = time.time()

                    while (time.time() - start_time) < timeout:
                        if ser.in_waiting > 0:
                            response += ser.read(ser.in_waiting).decode('utf-8')
                            expected_response_list = expected_responses[i]

                            # Check for the expected response(s)
                            if isinstance(expected_response_list, list):
                                if any(expected_response in response for expected_response in expected_response_list):
                                    print(f"One of the expected responses received. Proceeding to next command.")
                                    break
                            else:
                                if expected_response_list in response:
                                    print(f"Expected response received for command {i}.")
                                    break
                        time.sleep(0.1)  # Short sleep to prevent busy waiting

                    # Check for success response (but keep the script running)
                    if "-----Save settings to XML-----" in response:
                        print("Success condition met.")

                    # If the response does not match any expected responses, log it
                    if not any(expected_response in response for expected_response in expected_response_list):
                        print(f"None of the expected responses received or incorrect for command {i}.")
                        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        log_entry = f"{timestamp} - Command Sent: {actual_command}\n{timestamp} - Incorrect Response: {response.strip()}\n"
                        log_file.write(log_entry)
                        log_file.flush()

                    # Log the correct response only if it's not the "Save settings" condition
                    if "-----Save settings to XML-----" not in response:
                        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        log_entry = f"{timestamp} - Command Sent: {actual_command}\n{timestamp} - Response: {response.strip()}\n"
                        log_file.write(log_entry)
                        log_file.flush()

                print("All commands executed. Stopping script.")  # Only stop after all commands

        else:
            print(f"Failed to open serial port {port}.")

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if ser and ser.is_open:
            ser.close()  # Ensure the serial port is closed
            print("Serial port closed.")


# Main block to call the log_uart_data function
if __name__ == "__main__":
    commands = {

        1: 't svc atn buttons ok',
        2: 't svc atn buttons left',
        3: 't svc atn buttons left',
        4: 't svc atn buttons ok',
        5: 't svc atn buttons right',
        6: 't svc atn buttons right',
        7: 't svc atn buttons right',
        8: 't svc atn buttons down',
        9: 't svc atn buttons ok',
        10: 't svc atn buttons ok',
        11: 't svc atn buttons func1',
        12: 't svc atn buttons down',
        13: 't svc atn buttons ok',
        14: 't svc atn buttons func1',
        15: 't svc atn buttons down',
        16: 't svc atn buttons ok',
        17: 't svc atn buttons up',
        18: 't svc atn buttons up',
        19: 't svc atn buttons up',
        20: 't svc atn buttons up',
        21: 't svc atn buttons up',
        22: 't svc atn buttons up',
        23: 't svc atn buttons func1',
        24: 't svc atn buttons down',
        25: 't svc atn buttons ok',
        26: 't svc atn buttons right',
        27: 't svc atn buttons right',
        28: 't svc atn buttons right',
        29: 't svc atn buttons func1',
        30: 't svc atn buttons down',
        31: 't svc atn buttons ok',
        32: 't svc atn buttons right',
        33: 't svc atn buttons right',
        34: 't svc atn buttons right',
        35: 't svc atn buttons right',
        36: 't svc atn buttons func1',
        37: 't svc atn buttons down',
        38: 't svc atn buttons ok',
        39: 't svc atn buttons right',
        40: 't svc atn buttons right',
        41: 't svc atn buttons right',
        42: 't svc atn buttons right',
        43: 't svc atn buttons right',
        44: 't svc atn buttons func1',
        45: 't svc atn buttons down',
        46: 't svc atn buttons ok',
        47: 't svc atn buttons right',
        48: 't svc atn buttons right',
        49: 't svc atn buttons right',
        50: 't svc atn buttons right',
        51: 't svc atn buttons func1',
        52: 't svc atn buttons down',
        53: 't svc atn buttons ok',
        54: 't svc atn buttons right',
        55: 't svc atn buttons right',
        56: 't svc atn buttons right',
        57: 't svc atn buttons ok',
        58: 't svc atn buttons func1',
        59: 't svc atn buttons func1'
    }

    expected_responses = {
        1: ["RECEIVE INTERNAL MSG CAROUSEL TASK = 54", "RECEIVE INTERNAL MSG CAROUSEL TASK = 47"],
        2: "RECEIVE INTERNAL MSG CAROUSEL TASK = 6",
        3: "RECEIVE INTERNAL MSG CAROUSEL TASK = 6",
        4: ["RECEIVE INTERNAL SYS MENU TASK = 58", "RECEIVE INTERNAL SYS MENU TASK = 51"],
        5: "RECEIVE INTERNAL SYS MENU TASK = 8",
        6: "RECEIVE INTERNAL SYS MENU TASK = 8",
        7: "RECEIVE INTERNAL SYS MENU TASK = 8",
        8: "RECEIVE INTERNAL SYS MENU TASK = 4",
        9: "RECEIVE INTERNAL SYS MENU TASK = 12",
        10: "OPEN WINDOW ZEROING HANDLER !!!!!!!!!!",
        11: "RECEIVE INTERNAL SYS MENU TASK = 51",
        12: "RECEIVE INTERNAL SYS MENU TASK = 4",
        13: "RECEIVE INTERNAL SYS MENU TASK = 12",
        14: "RECEIVE INTERNAL SYS MENU TASK = 51",
        15: "RECEIVE INTERNAL SYS MENU TASK = 4",
        16: "one = 1 two = 0",
        17: "RECEIVE INTERNAL SYS MENU TASK = 2",
        18: "RECEIVE INTERNAL SYS MENU TASK = 2",
        19: "RECEIVE INTERNAL SYS MENU TASK = 2",
        20: "RECEIVE INTERNAL SYS MENU TASK = 2",
        21: "RECEIVE INTERNAL SYS MENU TASK = 2",
        22: "RECEIVE INTERNAL SYS MENU TASK = 2",
        23: "one = 0 two = 0",
        24: "RECEIVE INTERNAL SYS MENU TASK = 4",
        25: "RECEIVE INTERNAL SYS MENU TASK = 12",
        26: "RECEIVE INTERNAL SYS MENU TASK = 8",
        27: "RECEIVE INTERNAL SYS MENU TASK = 8",
        28: "RECEIVE INTERNAL SYS MENU TASK = 8",
        29: "RECEIVE INTERNAL SYS MENU TASK = 13",
        30: "RECEIVE INTERNAL SYS MENU TASK = 4",
        31: "RECEIVE INTERNAL SYS MENU TASK = 12",
        32: "RECEIVE INTERNAL SYS MENU TASK = 8",
        33: "RECEIVE INTERNAL SYS MENU TASK = 8",
        34: "RECEIVE INTERNAL SYS MENU TASK = 8",
        35: "RECEIVE INTERNAL SYS MENU TASK = 8",
        36: "RECEIVE INTERNAL SYS MENU TASK = 13",
        37: "RECEIVE INTERNAL SYS MENU TASK = 4",
        38: "RECEIVE INTERNAL SYS MENU TASK = 12",
        39: "RECEIVE INTERNAL SYS MENU TASK = 8",
        40: "RECEIVE INTERNAL SYS MENU TASK = 8",
        41: "RECEIVE INTERNAL SYS MENU TASK = 8",
        42: "RECEIVE INTERNAL SYS MENU TASK = 8",
        43: "RECEIVE INTERNAL SYS MENU TASK = 8",
        44: "RECEIVE INTERNAL SYS MENU TASK = 13",
        45: "RECEIVE INTERNAL SYS MENU TASK = 4",
        46: "RECEIVE INTERNAL SYS MENU TASK = 12",
        47: "RECEIVE INTERNAL SYS MENU TASK = 8",
        48: "RECEIVE INTERNAL SYS MENU TASK = 8",
        49: "RECEIVE INTERNAL SYS MENU TASK = 8",
        50: "RECEIVE INTERNAL SYS MENU TASK = 8",
        51: "RECEIVE INTERNAL SYS MENU TASK = 13",
        52: "RECEIVE INTERNAL SYS MENU TASK = 4",
        53: "RECEIVE INTERNAL SYS MENU TASK = 12",
        54: "RECEIVE INTERNAL SYS MENU TASK = 8",
        55: "RECEIVE INTERNAL SYS MENU TASK = 8",
        56: "RECEIVE INTERNAL SYS MENU TASK = 8",
        57: "RECEIVE INTERNAL SYS MENU TASK = 12",
        58: "RECEIVE INTERNAL SYS MENU TASK = 13",
        59: "-----Save settings to XML-----"
    }

    # Call the function and pass both `commands` and `expected_responses`
    log_uart_data(port="COM4", baudrate=115200, log_dir=log_dir, commands=commands,
                  expected_responses=expected_responses)
