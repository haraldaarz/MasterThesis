import subprocess

def get_masscan_output(args):
    # Run the masscan tool and capture its output in a variable
    p = subprocess.Popen(['masscan'] + args, stdout=subprocess.PIPE)

    # Read from the stdout stream
    output = []
    while True:
        line = p.stdout.readline()
        if line:
            # Convert the line to a string
            line = line.decode()
            # Use the strip method to remove unwanted parts of the output
            line = line.strip()
            if 'rate: ' in line:
                # Add only the lines that contain the information you want to the output list
                output.append(line)
        else:
            break
    
    # Return the output as a string
    return '\n'.join(output)

# Example usage:
output = get_masscan_output(['-p80,443', '192.168.1.0/24', '--rate=10000'])
print(output)