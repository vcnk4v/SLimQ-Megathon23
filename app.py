from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello():
    return render_template('hello.html')


@app.route('/homepage', methods=['POST', 'GET'])
def home():
    return render_template('homepage.html')


@app.route('/chat', methods=['POST', 'GET'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user_input']
        print(user_input)

        return render_template('homepage.html', user_input=user_input)
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True)



