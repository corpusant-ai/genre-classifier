import argh


def compute_embeddings(
    *,
    input_file: str,
    output_file: str = "embeddings.pkl",
) -> None:
    """
    Given a JSON of artists per genre, compute an embedding vector
    for each artist's name, and save a dataframe containing the
    artist name, genre, and embedding vector.
    """
    print("✨🔧 Implement me! 🔧✨")


if __name__ == "__main__":
    argh.dispatch_command(compute_embeddings)
