This repo contains the work I did on a recommendation system while learning Data Science.

Folder Structure:

Notebooks: Notebooks used in data processing and training

Reading: Papers and other study material pertaining to recommender systems

RecoM: Actual flask web app

Description of the notebooks

1. Movie_recommender_normal: This approach uses cosine similarity to recommend movies. Though reccommendations are satisfactory the size of the similarity matrix is too large (about 3.84 GB) to be commercially feasible

2. Movie_recommenderDL.ipynb: This approach uses Deep Learning with Matrix Factorization to recommend movies. Did not get satisfactory results

3. Movie_recommender_Decomposed.ipynb: Same cosine similarity approach but tried to bring down size of matrix using SVD. However at 100 components the model only captures 10% of features.

4. Movie_recommender_cast_metadata.ipynb: Cosine Similarity approach but used cast, director, genre as features. This works and produces smaller matrix

Currently developing a web app using the results of the 4th notebook 


