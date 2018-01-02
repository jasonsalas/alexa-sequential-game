# alexa-sequential-game
Ask Alexa on Amazon Echo (Dot) to respond to an ongoing series of questions with just two functions.

### Overview
This is a simple demo of an Alexa skill for the Amazon Echo family of smartspeakers using [Flask-Ask](http://flask-ask.readthedocs.io/en/latest/) to handle repeated question-answer interaction. My favorite skill is [Cinema Playground Screen Test](https://www.amazon.com/Screen-Test-Movie-Quote-Quiz/dp/B01MUAESMO), so this emulates the multi-step process of asking questions and incrementing the score.

Basically, the HTTP app persists the user's response and their score in the _session.attributes_ dictionary, looped over in the *number_challenge* function. A simple "yes" or "no" response bridges the data.
