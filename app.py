import io
import json
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from flask import Flask, jsonify, render_template, request, send_file
from flask.json import jsonify
from flask_cors import CORS
from load_data import data_loads

app = Flask(__name__)
CORS(app)
def required_data():
    countries = data_loads()
    # responce=df.to_json()

    # return jsonify(responce)
    mylist=[]
    for country in countries:
        mydict = {} # initialize an empty dictionary to store data for each country
        mydict['id']=country['id']
        mydict['iso2code']=country['iso2Code']
        mydict['name']=country['name']
        mydict['region']=country['region']['value']
        mydict['incomelevel']=country['incomeLevel']['value']
        mydict['lendingType']=country['lendingType']['value']
        mydict['capitalCity']=country['capitalCity']
        mylist.append(mydict) # append the dictionary to mylist
    df= pd.DataFrame(mylist)
    return df

def filter_aggregate():
        #filter out entries with "aggregate" value and return the rest
    df_data=required_data()
    df_data['region'].value_counts()
    df_data[df_data['region']=='Aggregates']
    df_data=df_data.drop(df_data[df_data['region']=='Aggregates'].index)
    return df_data

def filter_single_regions(name):
    #filter out entries with "region name" value and return the data in regards to the region
    df=required_data()
    df['region'].value_counts()
    df[df['region']!=name]
    df=df.drop(df[df['region']!=name].index)
    return df

def visualize_regions(name):
    # get countries or a region then plot the income levels agnaist the region
    data=filter_single_regions(name)
    data.shape
    plt.figure(figsize=(10,8))
    sns.set(style="darkgrid")
    _ = sns.countplot(x="incomelevel", data=data)
    _ = plt.ylabel('Number of Countries')
    _ = plt.xlabel('Income Level')
    # plt.show()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image
    
def regions_names(name):

    if (name=="EAP"):
        return "East Asia & Pacific"
    elif (name=="LAC"):
        return "Latin America & Caribbean "
    elif (name=="ECA"):
        return "Europe & Central Asia"
    elif (name=="MENA"):
        return "Middle East & North Africa"
    elif (name=="SA"):
        return "South Asia"
    elif (name=="NA"):
        return "North America"
    elif (name=="SSA"):
        return "Sub-Saharan Africa "
    else:
        return "wrong region name"


@app.route("/")
def records():
    all_records=filter_aggregate()

    return all_records.to_json(index='id')



@app.route("/regions", methods=['GET'])
def africa():
    if request.method == 'GET':
        get_name=request.args.get('name')
        assign_name=regions_names(get_name)
        africa_data=filter_single_regions(assign_name)
        return africa_data.to_json()
    else:
        
        return "region name required"

@app.route("/plots")
def plot_visual():
    if request.method == 'GET':
        get_name=request.args.get('name')
        assign_name=regions_names(get_name)
        visual_name=visualize_regions(assign_name)
        return send_file(visual_name, attachment_filename='plot.png',
                     mimetype='image/png')
    else:
        return "error occured"


if __name__ == '__main__':
    
        app.run(host='127.0.0.1', port=5000)
