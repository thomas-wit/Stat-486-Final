# Stat-486-Final
Just an attempt to predict average reviews as well as implement a RAG model to recommend books with a little clustering thrown in

## This repository contains code for the following:
* Code to clean and create subsets of data (This will be commented out, comment back in to make data) (finalproj.ipynb)
* Code for the model fitting for rating prediction (finalproj.ipynb)
   -Will need to get the data from https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews
   - Just follow the script
   - Data was too large to include here

* Code for clustering (Xela code)
   - finalproj_xela.ipynb - use merged dataset
  
* Code for the RAG model (most is from the youtuber Pixegami from his tutorial)
    - All in the code for the rag model and streamlit is in the rag directory.
    - rag/rag-tutorial-v2/data has the pdf of the subset of books the model is trained on
    - The same directory also contains the needed code.
        * Will need to provide an api key (not going to let you take my $4) in get_embedding_function, query_data, and maybe config.py, though I'm not sure about that one
        * Also provide a directory path for the pdf in populated database
        * To train, run 'python populate_database.py --reset'
        * to run, run 'streamlit run query_data.py' 

