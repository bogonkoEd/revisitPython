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

def generate_translation_jsonl(dataframe, output_dir):
    """ Combines translations from a DataFrame and saves them as (.jsonl) file.
         Args:
        dataframe (pandas.DataFrame): DataFrame containing translation data. output_dir (str): Directory to save the combined file."""

    locales = dataframe['locale'].unique()

    combined_data_list = []

    for locale in locales:

        if locale == 'en-US':

            continue

        locale_data = dataframe[dataframe['locale'] == locale]
        combined_data = pandas.merge(en_data, locale_data, on='id', how='inner')
        combined_data_list.extend(combined_data.to_dict('records'))

    jsonl_file_path = os.path.join(output_dir, 'combined_translation.jsonl')

    with open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:

        for record in combined_data_list:
            
            jsonl_file.write(json.dumps(record, ensure_ascii=False) + '\n')
