from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired,ValidationError
from keysecret import keys
from sandbox import *
from scattertext_url import *
import os

app = Flask(__name__, instance_path=keys['path'])
app.config['SECRET_KEY'] = keys['secret']

bootstrap = Bootstrap(app)
moment = Moment(app)

class AddressForm(FlaskForm):
    address = StringField('', [InputRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddressForm()
    if form.validate_on_submit():
        session['address'] = form.address.data
        return redirect(url_for('results'))

    return render_template('index.html', form=form, address=session.get('address'))

@app.route('/select')
def select():
    return render_template('select.html', address=session.get('choice'))

@app.route('/results')
def results():

    viz_info = Viz(session['address'])
    session['viz'] = viz_info.scatter_viz()

    input_info = InputModel(session['address'])
    session['title'] = input_info.title()
    session['source'] = input_info.source()
    session['image'] = input_info.image()

    class_info = GetBias(session['address'])
    session['bias_image'] = class_info.image()

    output_info = News(session['address']).choose_news()
    session['story_title1'] = output_info['title'][0]
    session['story_title2'] = output_info['title'][1]
    session['story_title3'] = output_info['title'][2]

    session['story_source1'] = output_info['source'][0]
    session['story_source2'] = output_info['source'][1]
    session['story_source3'] = output_info['source'][2]

    session['story_url1'] = output_info['url'][0]
    session['story_url2'] = output_info['url'][1]
    session['story_url3'] = output_info['url'][2]

    session['story_image1'] = output_info['image'][0]
    session['story_image2'] = output_info['image'][1]
    session['story_image3'] = output_info['image'][2]

    session['story_bias1'] = output_info['bias'][0]
    session['story_bias2'] = output_info['bias'][1]
    session['story_bias3'] = output_info['bias'][2]

    output2_info = Wiki(session['address']).choose_wiki()
    session['wiki_title1'] = output2_info['title'][0]
    session['wiki_title2'] = output2_info['title'][1]
    session['wiki_title3'] = output2_info['title'][2]

    session['wiki_url1'] = output2_info['url'][0]
    session['wiki_url2'] = output2_info['url'][1]
    session['wiki_url3'] = output2_info['url'][2]


    return render_template('results.html', address=session.get('address'),

    viz=session.get('viz'),

    title=session.get('title'), source=session.get('source'), image=session.get('image'), bias=session.get('bias_image'),

    story_title1=session.get('story_title1'), story_title2=session.get('story_title2'), story_title3=session.get('story_title3'),
    story_source1=session.get('story_source1'), story_source2=session.get('story_source2'), story_source3=session.get('story_source3'),
    story_url1=session.get('story_url1'), story_url2=session.get('story_url2'), story_url3=session.get('story_url3'),
    story_image1=session.get('story_image1'), story_image2=session.get('story_image2'), story_image3=session.get('story_image3'),
    story_bias1=session.get('story_bias1'), story_bias2=session.get('story_bias2'), story_bias3=session.get('story_bias3'),

    wiki_title1=session.get('wiki_title1'), wiki_title2=session.get('wiki_title2'), wiki_title3=session.get('wiki_title3'),
    wiki_url1=session.get('wiki_url1'), wiki_url2=session.get('wiki_url2'), wiki_url3=session.get('wiki_url3'),
    )

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/scattertext')
def scatter():
    return render_template('scattertext.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
