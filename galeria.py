from flask import Flask, render_template, request, redirect, url_for
import requests as req  

app = Flask(__name__)

@app.route('/list')
def index():
    response = req.get('http://localhost:3000/api/listtasks')
    result = response.json()['quotes']
    return render_template('home.html', quotes = result)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/form')
def citas():
    return render_template('assigned-appointments.html')



@app.route('/addquote', methods={'POST'})
def addquote():
    if request.method == 'POST':
        title = request.form['title']
        tipe = request.form['tipe']
        address = request.form['address']
        rooms = request.form['rooms']
        price = request.form['price']
        area = request.form['area']
        addQuote = {"title":title,"tipe":tipe,"address":address,"rooms":rooms,"price":price,"area":area}
        response = req.post('http://localhost:3000/api/addtask', json = addQuote)       
        return redirect(url_for('index'))


if __name__== "__main__":
    app.run(debug=True)

