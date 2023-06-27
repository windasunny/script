# Net Tool Script

This script retrieves and displays the network status and TCP/UDP packet transmission, reception, and listening information on the system.

### Prerequisites

Ensure that you have sufficient permissions to retrieve network status and packet information before executing the script.
This script is only compatible with Linux and Unix-like systems. Please adjust and test according to your system and requirements.

### Installing

requirement
```
    make requirement
```

### Running

```
    python3 main.py -h
```

### Usage

#### Netstat
show all connected host:port
```
    python3 main.py netstat list  # just can use in Linux OS
```

##### TCP package
listen or check if a host:port is active.
```
    python3 main.py tcp connect -H {host} -P {port}
    python3 main.py tcp listen -H {host} -P {port}
```

### Contribution

If you have any questions, suggestions, or improvements, please open an Issue or contact me.
