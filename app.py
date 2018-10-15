from flask import Flask, render_template, url_for, request
from models import HedgeRatio
from bokeh.embed import components
from bokeh.plotting import output_file, show

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
    hedgeratio = HedgeRatio()
    if request.method=='POST':
        corr = request.form.get('corr')
        spotstd = request.form.get('spotstd')
        fwdstd = request.form.get('fwdstd')
        numobserv = request.form.get('numobserv')
        hedgeratio.updateParameters(float(corr), float(spotstd), float(fwdstd), int(numobserv))
    else:
        corr, spotstd, fwdstd, numobserv = hedgeratio.getParameters()
    hedgeratio.runSimulation()
    statspotstd, statfwdstd = hedgeratio.calculateSTDs()
    statratio = hedgeratio.calculateHedgeRatio()
    statcorr = hedgeratio.calculateCorr()
    stats = {
        'statspotstd': statspotstd,
        'statfwdstd': statfwdstd,
        'statratio': statratio,
        'statcorr': statcorr
        }
    p = hedgeratio.createScatterPlot()
    script, div = components(p)
    return render_template('sim.html', corr=corr, numobserv=numobserv,
    spotstd=spotstd, fwdstd=fwdstd, script=script, div=div, stats=stats)

if __name__ == '__main__':
    app.run(debug=True)