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
    
def generate_language_excel_files(data_frame, output_dir):

"""Combines data from 'en-US' and other locales and saves as Excel files.
    Args:
        data_frame (pd.DataFrame): DataFrame containing data for various locales.
        output_dir (str): Directory to save the generated Excel files."""
        
    locales = data_frame['locale'].unique()

    if 'en-US' in locales:

        en_data = data_frame[data_frame['locale'] == 'en-US']
        output_file_path = os.path.join(output_dir, 'en-en.xlsx')
        en_data.to_excel(output_file_path, index=False)

    for locale in locales:

        if locale == 'en-US':

            continue  
        
        locale_data = data_frame[data_frame['locale'] == locale]
        en_us_data = data_frame[data_frame['locale'] == 'en-US'][['id', 'utt', 'annot_utt']]
        combined_data = pandas.merge(en_us_data, locale_data, on='id', how='inner')

        output_file_path = os.path.join(output_dir, f'en-{locale}.xlsx')
        combined_data.to_excel(output_file_path, index=False)