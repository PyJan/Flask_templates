from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/child')
def child():
    return render_template('child.html')

@app.route('/simbase')
def simbase():
    return render_template('sim_base.html')

@app.route('/sim')
def sim():
    return render_template('sim.html')

if __name__ == '__main__':
    app.run(debug=True)