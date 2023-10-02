import functions


def main():
    dataset_path = "data/dataset.tar.gz"
    data_frame = functions.load_dataset(dataset_path)


if __name__ == "__main__":
    main()
