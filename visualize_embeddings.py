import argh
import numpy as np
import pandas as pd
import plotly_express as px
import umap


def visualize_embeddings(
    *,
    input: str,
    seed: int = 42,
) -> None:
    """
    Plot embeddings from a pickled dataframe containing the following columns:

        - artist: Name of the artist
        - genre: Labeled genre of the artist
        - features: Embedding vector of the artist's name
    """
    df = pd.read_pickle(input)
    embeddings = np.array(df["features"].values.tolist())  # (batch, embed_dim)
    coords = umap.UMAP(random_state=seed).fit_transform(embeddings)  # (batch, 2)

    fig = px.scatter(
        df,
        x=coords[:, 0],
        y=coords[:, 1],
        color="genre",
        size=np.ones(len(df)) * 0.01,
        hover_name="artist",
    )
    fig.show()


if __name__ == "__main__":
    argh.dispatch_command(visualize_embeddings)
