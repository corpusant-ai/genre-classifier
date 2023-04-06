# 🎻 Genre Classifier

Train a classifier that accepts the name of a musician and predicts the most likely genre of their music out of the set:

`{ jazz, opera, country, electronic, metal, rap, classical, reggae }`

You will train this classifier to operate on top of a pretrained text encoder that converts artist names into embedding vectors. In support of this task, you will assemble a small dataset of artist names for each genre using GPT.

## Steps

1. Create a dataset of artists by genre and save to JSON. We suggest using the OpenAI GPT API and will provide you an access key.
```
python create_dataset.py --count 20 --output data.json
```

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
