import nucleus
from flask import Flask, request, session, render_template



app = Flask(__name__)
app.secret_key = 'super secret key'


def percentage(percentile):
    return int(percentile * 100)
app.jinja_env.globals.update(percentage=percentage) 


@app.route('/')
def insights():
    if not 'token' in session:
        session['token'] = nucleus.get_token()

    if request.method == 'POST':
        person = nucleus.personality_insights(request.form['username'], request.session['token'])
        return render_template('insights.html', person=person)

    return render_template('index.html', person=nucleus.personality_insights('SkullTech101'))


@app.route('/inside')
def inside():
    return render_template('inside.html')


if __name__=='__main__':
    app.run()
