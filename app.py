from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('input.html')


@app.route("/output", methods=['POST'])
def output():
    your_name = request.form['name']
    num = [0, 1]
    return redirect(url_for('redirect_test', name=your_name, num=num))


@app.route("/redirect_test", methods=['GET'])
def redirect_test():
    your_name = request.args.get('name', '')
    num = [0, 1]
    return render_template("output.html", name=your_name, num=num)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)