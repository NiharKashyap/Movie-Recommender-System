from flask import Flask
from flask import render_template
import pandas as pd
import numpy as np
from tmdbv3api import TMDb
from tmdbv3api import Movie


tmdb = TMDb()
tmdb.api_key = '3a9f5aa1d4b3eebd503a6bb3e02cf23f'



class Predict:

    def __init__(self, mat):
        self.matrix = mat
    
    def get_title_from_index(self, index):
        return df[df.index==index]['movie_title'].values[0]
    
    def get_index_from_title(self, title):
        return df[df.movie_title==title].index[0]

    def get_recommendations(self, movie_index, name):
        
        similar_movies = list(enumerate(self.matrix[movie_index]))
        sorted_similar_movies = sorted(similar_movies, key = lambda x:x[1], reverse = True)[1:]
        i=0
        print("Top 5 similar movies to "+name+" are:\n")
        arr = []
        for element in sorted_similar_movies:
            #print(self.get_title_from_index(element[0]))
            arr.append(self.get_title_from_index(element[0]))
            i=i+1
            if i>19:
                return arr





app = Flask(__name__)
df = pd.read_csv('main_data.csv')
mat = np.load('Sim.npy')

@app.route('/')
def index():
    movie = Movie()
        
    data = list(df['movie_title'])

    #for title in data:
        #search = movie.search(title)
        #print(title + ' ' + search[0]['poster_path'])
    

    return render_template('home.html', data = data)

@app.route('/result/<name>')
def result(name):
    print(name)
    pred = Predict(mat)
    movie_index = pred.get_index_from_title(name)
    arr = pred.get_recommendations(movie_index, name)
    data = {'name':name, 'arr':arr}
    
    return render_template('result.html', data = data)