from flask import Flask, render_template

app = Flask(___name___)

@app.route('/edit')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80890)