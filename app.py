from flask import Flask, render_template, request

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factorization(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    factors = None
    number = None
    if request.method == "POST":
        try:
            number = int(request.form.get("number"))
            if is_prime(number):
                result = "素数です"
            else:
                result = "素数ではありません"
                factors = prime_factorization(number)
        except ValueError:
            result = "有効な数値を入力してください"
    
    return render_template("index.html", result=result, factors=factors, number=number)

if __name__ == "__main__":
    app.run(debug=True)


