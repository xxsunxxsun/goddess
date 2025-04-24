from flask import Flask, request, render_template

app = Flask(__name__)

def calculate_tax(taxable_income):
    if taxable_income <= 540000:
        tax = taxable_income * 0.05
    elif taxable_income <= 1210000:
        tax = taxable_income * 0.12 - 37800
    elif taxable_income <= 2420000:
        tax = taxable_income * 0.20 - 134600
    elif taxable_income <= 4530000:
        tax = taxable_income * 0.30 - 376600
    else:
        tax = taxable_income * 0.40 - 829600
    return round(tax)

@app.route('/', methods=['GET', 'POST'])
def index():
    tax = None
    if request.method == 'POST':
        income = int(request.form['income'])
        dependents = int(request.form['dependents'])
        is_married = request.form.get('is_married') == 'yes'

        personal_exemption = 88000 * (1 + dependents + (1 if is_married else 0))
        standard_deduction = 240000 if is_married else 120000
        taxable_income = max(0, income - personal_exemption - standard_deduction)

        tax = calculate_tax(taxable_income)

    return render_template('index.html', tax=tax)

if __name__ == '__main__':
    app.run(debug=True)
