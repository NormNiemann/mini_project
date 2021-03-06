#Import necessary libraries
from flask import Flask, request, jsonify, render_template
import json
import requests
from pprint import pprint


app = Flask(__name__)

beer_url_template = 'https://api.openbrewerydb.org/breweries'
brewery_type_template = 'https://api.openbrewerydb.org/breweries?by_type={variableName}'

@app.route('/', methods=['GET', 'POST'])  #login page
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return "Beer is good!"
    return render_template('login.html', error=error) #html template and return

#Establish default route
@app.route('/home')
def hello():
    return "Beer is good!"

#Return general information about breweries in the US
@app.route('/beer',  methods=['GET'])
def beer():
    response = requests.get(beer_url_template).json()
    beer = {'Brewery': [],'BreweryID': [],'Type': [],'State': []}
    for x in response:
        beer['Brewery'].append(x['name'])
        beer['BreweryID'].append(x['id'])
        beer['Type'].append(x['brewery_type'])
        beer['State'].append(x['state'])
    return jsonify(beer)
    if resp.status_code == 404:
        return 'Error, page does not exist!'


#Allow the user to search for brewery information by brewery type, e.g. by 'micro' breweries
@app.route('/type/<type_name>',  methods=['GET'])
def brewery(type_name):
    type_url = brewery_type_template.format(variableName = type_name)
    resp = requests.get(type_url)
    beer = {'Brewery': [],'BreweryID': [],'Type': [],'State': []}
        #resp = requests.get(beer_url).json()
    jsondata = resp.json()
    for x in jsondata:
        beer['Brewery'].append(x['name'])
        beer['BreweryID'].append(x['id'])
        beer['Type'].append(x['brewery_type'])
        beer['State'].append(x['state'])
    return jsonify(beer)
    #brewery = {'BreweryType': jsondata['brewery_type']}
    #brewery_type_template = 'https://api.openbrewerydb.org/breweries?by_type={type}'
    #brewery = {'typename' : jsondata ['brewery_type']}
    #for x in resp:
        #brewery['Type'].append(x['brewery_type'])
    #return jsonify(brewery)/*
    #brewery_type = 'micro'
    if resp.status_code == 404:
        return 'Error, page does not exist!', 404


        #pprint(beer)


if __name__=="__main__":
    app.run(port=8080, debug=True)
