from flask import Flask, render_template, url_for, request

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

@app.route('/sim', methods=['GET', 'POST'])
def sim():
    corr, spotstd, fwdstd = 0.8, 2, 3
    if request.method=='POST':
        corr = request.form.get('corr')
        spotstd = request.form.get('spotstd')
        fwdstd = request.form.get('fwdstd')
    return render_template('sim.html', corr=corr, spotstd=spotstd, fwdstd=fwdstd)

if __name__ == '__main__':
    app.run(debug=True)