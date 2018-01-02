import logging
from flask import Flask, render_template
from flask_ask import Ask, session, statement, question

logging.getLogger('flask_ask').setLevel(logging.DEBUG)

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launch():
	session.attributes['secret_number'] = 0
	session.attributes['score'] = 0
	return question(render_template('game_instructions').reprompt(render_template('reprompt')))

@ask.intent('AMAZON.YesIntent')
def yes_handler():
	return question(render_template('challenge_text', secret_number=session.attributes['secret_number']).reprompt(render_template('reprompt')))

@ask.intent('NumberChallengeIntent', convert={'secret_number':int})
def number_challenge(secret_number):
	if secret_number == session.attributes['secret_number']:
		session.attributes['score'] += 1
		response = render_template('correct', score=session.attributes['score'])
	else:
		response = render_template('incorrect')

	session.attributes['secret_number'] += 1
	return question(response).reprompt(render_template('reprompt'))

@ask.intent('AMAZON.NoIntent')
def no_handler():
	return statement(render_template('opt_out', score=session.attributes['score']))

@ask.intent('AMAZON.CancelIntent')
def cancel():
	return statement(render_template('goodbye'))

@ask.intent('AMAZON.StopIntent')
def stop():
	return statement(render_template('goodbye'))

@ask.intent('AMAZON.HelpIntent')
def help():
	return statement(render_template('help'))

@ask.intent('AMAZON.StartOverIntent')
def startover():
	return launch()

@ask.session_ended
def session_ended():
	return '{}', 200

if __name__ == '__main__':
	app.run(debug=True)