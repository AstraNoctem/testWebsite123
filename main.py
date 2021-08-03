from flask_frozen import Freezer, render_template
from myapplication import app

freezer = Freezer(app)

@app.route('/home')
def index():
  return render_template('index.html')


@app.route('/test')
def test():
  return render_template('test.html')

app.run(host='0.0.0.0', port=8080)
