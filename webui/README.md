# Nmap Web UI

This directory provides a minimal Flask application that exposes a simple web
interface for running `nmap` scans.

## Usage

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start the application:

   ```bash
   python app.py
   ```

3. Open a browser and visit `http://localhost:5000`. Enter the target host and
   any additional Nmap options. The scan results will be displayed on the page.

`nmap` must be installed and available on the system path for scans to run
successfully.

