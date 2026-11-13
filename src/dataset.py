import pandas as pd

DATASET_PATH = "datasets/data.csv"


def load_dataset(): 
    dataset = pd.read_csv(DATASET_PATH)
    print("Dataset loaded successfully.")
    print(f"Number of examples: {len(dataset)}")

    print("\nClasses")
    print(f"{dataset["label"].value_counts()}")

    return dataset


if __name__ == "main()":
    load_dataset()