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


def preprocess_dataset(
    *,
    input: str = "data.json",
) -> None:
    """
    Preprocess / clean up the raw data
    """
    print("✨🔧 Implement me! 🔧✨")


if __name__ == "__main__":
    argh.dispatch_command(preprocess_dataset)
