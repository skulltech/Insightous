import nucleus
from flask import Flask, request, session, render_template



app = Flask(__name__)
app.secret_key = 'super secret key'


@app.route('/insights')
def insights():
	if not 'token' in session:
		session['token'] = nucleus.get_token()

	if request.method == 'POST':
		person = nucleus.personality_insights(request.form['username'], request.session['token'])
		return render_template('insights.html', person=person)

    return render_template('insights.html', person=None)



if __name__=='__main__':
    app.run()
