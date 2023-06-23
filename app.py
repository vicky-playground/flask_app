from flask import Flask, request, jsonify, render_template

# create the flask app
app = Flask(__name__)

# home page
@app.route('/')
def home():
    return render_template('home.html')

# define the logic for reading the inputs from the home page 
@app.route('/result', methods=['POST'])
def result():
    input = request.form.get('url')
    return render_template('result.html', display=input)

if __name__ == "__main__":
    app.run(debug=True)
