from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/tutor-register', methods=['GET', 'POST'])
def tutor_register():
    if request.method == 'POST':
        name = request.form['name']
        highest_degree = request.form['highest_degree']
        phone = request.form['phone']
        email = request.form['email']
        # Here, you would typically send this data to the admin or store it in a database
        return redirect(url_for('thank_you'))
    return render_template('tutor_register.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)

