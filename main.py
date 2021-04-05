from flask import Flask, session, redirect, request, render_template
import datetime
import display
import threading
import time

app = Flask(__name__)
app.secret_key = 'lmao'

display_text="ff"

one_way = ["Pori", "Aland", "Turku"]
two_way = ["Oulu", "Kokkola", "Vaasa", "Pori", "Turku", "Helsinki", "Hamina"]
locations = ["Oulu", "Kokkola", "Vaasa", "Pori", "Aland", "Turku", "Helsinki", "Hamina"]

@app.route("/")
def index():
   now = datetime.datetime.now()
   hour = now.strftime("%H")
   minute = now.strftime("%M")
   hour_int = int(hour)
   hour_int = hour_int + 2
   if hour_int >= 24:
       hour_int = hour_int - 24
   hour = str(hour_int)
   timeString = hour + ":" + minute
   #timeString = now.strftime("%H:%M")
   try:
       session
   except NameError:
        #var_exists = False
        print("Session does not exist")
        information = ""
   else:
        #var_exists = True
        information = session.get('information')
        origin = session.get('origin')
        destination = session.get('destination')
        ID = session.get('ID')
        arriving = session.get('arriving')
        leaving = session.get('leaving')
        d_arriving = session.get('d_arriving')
        #print("Session exists")
        
   templateData = {
      'title' : 'Tour-Tag',
      'time': timeString,
      'arriving': '21:00',
      'leaving': '4:00',
      'location': locations[0],
      'information': information,
      'origin': origin,
      'destination': destination,
      'arriving': arriving,
      'd_arriving': d_arriving,
      'leaving': leaving,
      'ID': ID
      }
   return render_template('index.html', **templateData)

@app.route("/leader")
def my_form():
    return render_template('leader.html')

@app.route('/leader', methods=['POST'])
def my_form_post():
    if not request.form.get('origin') is None:
        session['origin'] = request.form.get('origin')
    if not request.form.get('destination') is None:
        session['destination'] = request.form.get('destination')
    if not request.form.get('information') is None:
        session['information'] = request.form.get('information')
    if not request.form.get('ID') is None:
        session['ID'] = request.form.get('ID')
        global display_text
        display_text = session.get('ID')
        print(display_text)
    #session['information'] = request.form['information']
    #session['origin'] = request.form['origin']
    #session['destination'] = request.form['destination']
    #print(information)
    #return information
    return render_template('leader.html')
    #return redirect(url_for('b'))

@app.route("/boatdriver")
def boatdriver():
    return render_template('boatdriver.html')

@app.route('/boatdriver', methods=['POST'])
def my_form_post_2():
    if not request.form.get('arriving') is None:
        session['arriving'] = request.form.get('arriving')
    if not request.form.get('leaving') is None:
        session['leaving'] = request.form.get('leaving')
    if not request.form.get('d_arriving') is None:
        session['d_arriving'] = request.form.get('d_arriving')
    return render_template('boatdriver.html')

def run_server():
    if __name__ == "__main__":
        app.run(host='192.168.0.102', port=80, debug=False, threaded=True)

def LCD():
    #display.static_text(display_text,16)
    while 1:
        """
        for i in range(100):
            if i <10:
                a = 7
            else:
                a = 0
            display.static_text(display_text, 14, a)
            print(display_text)
            time.sleep(1)
        """
        if len(display_text) <= 2:
            if len(display_text) == 1:
                a = 7
            else:
                a = 0
            display.static_text(display_text, 14, a)
        else:
            display.scrolling_text(display_text, 14, 0.1)
        time.sleep(0.1)
#run_server()

x = threading.Thread(target=run_server)
y = threading.Thread(target=LCD)
#x.setDaemon(True)
#y.setDaemon(True)
x.start()
y.start()
