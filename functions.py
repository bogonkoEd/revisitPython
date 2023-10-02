import json
import tarfile
import pandas

"""The tarfile module makes it possible to read and write tar archives"""


def load_dataset(dataset_path):
    """Function to Read data from the Massive Dataset."""
    data = []

    with tarfile.open(dataset_path, mode="r:gz") as data_archive:
        for member in data_archive.getmembers():
            if member.isfile() and member.name.endswith(".jsonl"):
                jsonl_data = data_archive.extractfile(member).read().decode("utf-8")
                for line in jsonl_data.split("\n"):
                    if line:
                        data.append(json.loads(line))

    data_frame = pandas.DataFrame(data)

    return data_frame
