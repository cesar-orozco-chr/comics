from web import db
from flask import render_template, flash, redirect, url_for
from web.characters import characters


collection = db.marvel_raw.characters

@characters.route('/')
def display_characters():
    character_list = collection.find()
    return render_template('home.html', characters=character_list)


@characters.route('/character/details/<char_name>')
def character_details(char_name):
    c = collection.find_one({'name':char_name})
    comics = c['comics']['items']
    series = c['series']['items']
    stories = c['stories']['items']
    events = c['events']['items']
    return render_template('details.html', c=c, 
                            comics=comics,
                            series=series,
                            stories=stories,
                            events=events)

@characters.route('/navbar')
def test_navbar():
    return render_template('navbar.html')