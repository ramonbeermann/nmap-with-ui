from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    output = None
    if request.method == 'POST':
        target = request.form.get('target')
        options = request.form.get('options', '')
        if target:
            cmd = ['nmap'] + options.split() + [target]
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                output = result.stdout
            except subprocess.CalledProcessError as e:
                output = e.stdout + e.stderr
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
