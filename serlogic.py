from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/website.html')
def Contact():
    return render_template('index.html')

@app.route('/submit_email', methods=['POST'])
def submit_email():
    email = request.form.get('email')

    # Perform any desired processing or storage of the email data here

    return "Email submitted successfully!"

if __name__ == '__main__':
    app.run()
