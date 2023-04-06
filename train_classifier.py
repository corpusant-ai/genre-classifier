import argh

from create_dataset import GENRES


def train_classifier(
    *,
    input_file: str,
    seed: int = 42,
) -> None:
    """
    Train a classifier that predicts an artist's genre from the embedding
    vector of their name.
    """
    print("✨🔧 Implement me! 🔧✨")


if __name__ == "__main__":
    argh.dispatch_command(train_classifier)
