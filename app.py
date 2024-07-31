from flask import Flask, request, render_template_string

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

html_template = '''
<!doctype html>
<html>
<head>
    <title>素数判定アプリ</title>
</head>
<body>
    <h1>素数判定アプリ</h1>
    <form method="post">
        <label for="number">数値を入力してください:</label>
        <input type="text" id="number" name="number">
        <input type="submit" value="判定">
    </form>
    {% if result is not none %}
        <h2>{{ number }} は {{ result }} 。</h2>
    {% endif %}
</body>
</html>
'''

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
    return render_template_string(html_template, result=result, number=number)

if __name__ == '__main__':
    app.run(debug=True)
