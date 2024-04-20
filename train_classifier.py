import argh
import torch
import numpy as np
import pandas as pd

GENRES = [
    "jazz",
    "opera",
    "country",
    "electronic",
    "metal",
    "rap",
    "classical",
    "reggae",
]

class Dataset(torch.utils.data.Dataset):
    def __init__(self, df):
        self.features = df["features"].values.tolist()
        self.labels = df["genre_id"].values.tolist()

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, i):
        return self.features[i], self.labels[i]

def train_classifier(
    *,
    input: str,
    seed: int = 42,
) -> None:
    """
    Train a classifier that predicts an artist's genre from the embedding
    vector of their name.
    """
    # Fix seed
    np.random.seed(seed)
    torch.manual_seed(seed)

    # Load data
    df = pd.read_pickle(input)

    # Add genre ID as a number
    df["genre_id"] = df["genre"].apply(lambda x: GENRES.index(x))

    # Shuffle
    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)

    
    # Split train / test
    test_frac = 0.2
    train_df = df[int(test_frac * len(df)) :].copy()
    test_df = df[: int(test_frac * len(df))].copy()

    batch_size = 32
    data_loader = torch.utils.data.DataLoader(
        Dataset(train_df),
        batch_size=batch_size,
        shuffle=True,
    )

    print("✨🔧 Implement me! 🔧✨")


if __name__ == "__main__":
    argh.dispatch_command(train_classifier)
