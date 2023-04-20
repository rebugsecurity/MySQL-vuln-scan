#imports:
import nmap

# Defining the target IP address or hostname
target = "192.168.1.100" # this is an example target

# Create an Nmap scanner object
scanner = nmap.PortScanner()

# Perform a CVE-based vulnerability scan on MySQL port (default is 3306)
scanner.scan(target, '3306', arguments="--script mysql-vuln-cve2012-2122")

# Check if the target is up and the MySQL port is open
if 'tcp' in scanner[target] and 3306 in scanner[target]['tcp'] and \
    scanner[target]['tcp'][3306]['state'] == 'open':
    # Check if CVE-2012-2122 Vulnerability is detected
    if 'mysql-vuln-cve2012-2122' in scanner.all_hosts():
        print(f"Target {target} is vulnerable to CVE-2012-2122")
    else:
        print(f"Target {target} is not vulnerable to CVE-2012-2122")
else:
    print(f"Target {target} is down or MySQL port is closed")