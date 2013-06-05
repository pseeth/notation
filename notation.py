import sys
sys.path.insert(0, ".")

from flask import Flask, request, session, g, redirect, url_for, abort
from flask import render_template, flash, _app_ctx_stack, jsonify
from ly.tokenize import *

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def home(name=None):
    return render_template('index.html')

@app.route('/parse', methods = ['POST'])
def parse():
	raw = request.form['rawinput']
	tokenizer = MusicTokenizer()
	output = []
	dur = 4
	for token in tokenizer.tokens(raw):
		if isinstance(token, MusicTokenizer.PitchDuration):
			if token.dur == '':
				dur = 1
			else:
				dur = token.dur
			note = token.step
			if "is" in note:
				note = note[0].upper() + "#"
			if "es" in note:
				note = note[0].upper() + "b"
			output.append((dur, [note]))
	return jsonify(notes=[{'duration':out[0], 'keys': out[1]} for out in output])

if __name__ == '__main__':
	app.debug = True
	app.run()
