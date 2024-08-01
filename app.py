from flask import Flask, request, render_template

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    number = None
    if request.method == 'POST':
        number = int(request.form['number'])
        if is_prime(number):
            result = "素数です"
        else:
            result = "素数ではありません"
    return render_template('index.html', result=result, number=number)

if __name__ == '__main__':
    app.run(debug=True)

