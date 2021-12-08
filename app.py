from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/home_page')
@app.route('/home')
@app.route('/')
def hello_func():
    return 'welcome to My web!'

@app.route('/about')
def about_func():
    return 'About Me :)'

@app.route('/product')
def product_func():
    print('i am in product')
    return redirect(url_for('cakes_func'))

@app.route('/cakes')
def cakes_func():
    return redirect('/customize_cakes')

@app.route('/customize_cakes')
def customize_func():
    return 'welcome to customize cakes page'


if __name__ == '__main__':
    app.run(debug=True)
