'''
Author: Nihar Kashyap
Changelog:
Date: 15/7/21
Time: 12:50 AM
Changes: Session variable to store history,
        shows 6 from each history,
        won't add redundant history

'''


from flask import Flask
from flask import render_template
from flask.globals import session
import pandas as pd
import numpy as np
from tmdbv3api import TMDb
from tmdbv3api import Movie

from flask import Flask, redirect, url_for, request

tmdb = TMDb()
tmdb.api_key = '3a9f5aa1d4b3eebd503a6bb3e02cf23f'

movie_arr = []

class Predict:

    def __init__(self, mat):
        self.matrix = mat
        
        
    
    def get_title_from_index(self, index):
        return df[df.index==index]['movie_title'].values[0]
    
    def get_index_from_title(self, title):
        return df[df.movie_title==title].index[0]

    
    def staggered_recommendations(self, name):
        
        
        movie_arr = session['movie_arr']
        
        print(movie_arr)
        
        arr = []
        
        for movies in movie_arr:
            movie_index = self.get_index_from_title(movies)
            similar_movies = list(enumerate(self.matrix[movie_index]))
            sorted_similar_movies = sorted(similar_movies, key = lambda x:x[1], reverse = True)[1:]
            i=0
            print("Top 5 similar movies to "+name+" are:\n")
            
            for element in sorted_similar_movies:
            #print(self.get_title_from_index(element[0]))
                arr.append(self.get_title_from_index(element[0]))
                i=i+1
                if i>5:
                    break
        arr.reverse()
        
        print(arr)
        
        return arr
        
    '''
    def get_recommendations(self, movie_index, name):
        
        movie_arr.append(name)
        
        print(movie_arr)
        
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
    '''

class CollectData:
    
    def __init__(self, df):
        self.clicks = df
    
    def write_movie(self,title):
        self.clicks.loc[session['username']][title]+=1
        print('Current cLicks for {} {}'.format(title, self.clicks.loc[session['username']][title]))
        



app = Flask(__name__)

app.secret_key = "abc"  

df = pd.read_csv('main_data.csv')
user_mov = pd.read_csv('user_movie.csv')
user_mov.set_index('User', inplace=True) 
mat = np.load('Sim.npy')

@app.route('/')
def index():
    movie = Movie()
    if 'username' in session:
        print(session['username'])    
    data = list(df['movie_title'])
    
    
    #print(user_mov[user_mov['User']==session['username']])

    #for title in data:
        #search = movie.search(title)
        #print(title + ' ' + search[0]['poster_path'])
    

    return render_template('home.html', data = data)

@app.route('/result/<name>')
def result(name):
    print(name)
    
    if 'movie_arr' not in session:
        session['movie_arr'] = []
    
    if name not in session['movie_arr']:
    
        movie_list = session['movie_arr']
        movie_list.append(name)
        session['movie_arr'] = movie_list
        
    #cld = CollectData(user_mov)
    #cld.write_movie(name)
    pred = Predict(mat)
    #movie_index = pred.get_index_from_title(name)
    
    #arr = pred.get_recommendations(movie_index, name)
    
    arr = pred.staggered_recommendations(name)
    
    data = {'name':name, 'arr':arr}
    
    return render_template('result.html', data = data)




@app.route('/login',methods = ['POST', 'GET'])
def user_login():
    if request.method == 'POST':
      user = request.form['username']
      session['username'] = user
      return redirect(url_for('index'))
    else:
      return render_template('login.html')
    