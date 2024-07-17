from flask import Flask, render_template,request
import time
app = Flask('__main__')

@app.route('/')
def home():

    return render_template('forest-fire.html')

@app.route('/submit', methods=['POST'])
def submit():
    temp = request.form.get('temperature')
    humid = request.form.get('humidity')
    oxy = request.form.get('oxygen')
    time.sleep(0.5)
    return render_template('forest-fire.html', show_popup = True , temperature = temp,humidity = humid, oxygen = oxy)
    return f"Temp: {temp} Humid: {humid} Oxygen : {oxy}"
if __name__ == '__main__' :
    app.run(debug=True)