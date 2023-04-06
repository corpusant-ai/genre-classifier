import argh

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


def create_dataset(
    *,
    count_per_genre: int = 20,
    output: str = "data.json",
) -> None:
    """
    Create a dataset of artist names per genre and save to a JSON file.
    """
    print("✨🔧 Implement me! 🔧✨")


if __name__ == "__main__":
    argh.dispatch_command(create_dataset)
