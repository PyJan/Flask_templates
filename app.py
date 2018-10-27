from flask import Flask, render_template, url_for, request
from models import HedgeRatio, Schwartz97, GBM
from bokeh.embed import components
from bokeh.plotting import output_file, show
from wtforms import Form, StringField, SubmitField, FloatField, IntegerField


app = Flask(__name__)

app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176'

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
    statlinearfit = hedgeratio.getLinearFitCoef()
    stats = {
        'statspotstd': statspotstd,
        'statfwdstd': statfwdstd,
        'statratio': statratio,
        'statcorr': statcorr,
        'statlinearfit': statlinearfit
        }
    p = hedgeratio.createScatterPlot()
    p_line = hedgeratio.createHedgingPlot()
    script, div = components(p)
    script_line, div_line = components(p_line)
    return render_template('sim.html', corr=corr, numobserv=numobserv,
    spotstd=spotstd, fwdstd=fwdstd, script=script, div=div, stats=stats, 
    div_line=div_line, script_line=script_line)

@app.route('/schwartz97', methods=['GET','POST'])
def schwartz97():
    schwartz97 = Schwartz97()
    if request.method == 'POST':
        alpha=float(request.form['alpha']) 
        dt=float(request.form['dt'])
        sigma=float(request.form['sigma'])
        mu=float(request.form['mu'])
        S0=float(request.form['S0'])
        steps=int(request.form['steps'])
        numScen=int(request.form['numScen'])
        schwartz97.updateParameters(alpha, dt, sigma, mu, S0, steps, numScen)
    params = schwartz97.getParameters()
    schwartz97.calculateScenarios()
    script, div = components(schwartz97.createPlot())
    return render_template('sim_schwartz97.html', params=params, script=script, div=div)

class gbmForm(Form):
    mu = FloatField(label='mu', id='label')
    sigma = FloatField(label='sigma', id='sigma')
    S0 = FloatField(label='S0', id='S0')
    dt = FloatField(label='dt', id='dt')
    steps = IntegerField(label='steps', id='steps')
    numScen = IntegerField(label='numScen', id='numScen')

@app.route('/gbm', methods=['GET','POST'])
def gbm():
    gbm = GBM() # type: models.gbm.GBM
    gbmform = gbmForm(request.form, **gbm.getParameters())
    if request.method == 'POST':
        gbm.updateParameters(**gbmform.data)
    print(gbm.getParameters())
    gbm.calculateScenarios()
    script, div = components(gbm.createPlot())
    return render_template('sim_gbm.html', gbmform=gbmform, script=script, div=div)

if __name__ == '__main__':
    app.run(debug=True)