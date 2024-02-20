# 🎻 Genre Classifier

Train a classifier that accepts the name of a musician and predicts the most likely genre of their music out of the set:

`{ jazz, opera, country, electronic, metal, rap, classical, reggae }`

You will train this classifier to operate on top of a pretrained text encoder that converts artist names into embedding vectors. 

## Steps

1. We've provided a data.json file, that includes a mapping of genre to a list of artists. Preprocess the data as you wish to get it ready for embedding computation.
   
2. Compute an embedding vector from each artist name and save to disk. We suggest using the text encoder from [open_clip](https://github.com/mlfoundations/open_clip) and saving as a pandas dataframe.
```
python compute_embeddings.py --input data.json --output embeddings.pkl
```

3. Visualize the embeddings in a 2D projection space using [umap](https://github.com/lmcinnes/umap). We provide the code for this.
```
python visualize_embeddings.py --input embeddings.pkl
```

4. Train a simple classifier to predict the genre from the embedding vector of the artist's name. It is up to you to pick an architecture, train, and evaluate the model.
```
python train_classifier.py --input embeddings.pkl
```
