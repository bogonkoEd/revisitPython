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
    
    
def filter_into_jsonl(xlsx_file_path, output_dir, filter_column, filter_value):
    """Reads data from Excel file, filters it based on a specified column and value and saves as jsonl file
    Args:
        xlsx_file_path (str): Input Excel file path, output_dir (str): Output directory for JSON Lines file, filter_column (str): Column to filter
        filter_value (str): Value to filter by"""

    data_f = pd.read_excel(xlsx_file_path)
    filtered_data = data_f[data_f[filter_column] == filter_value]
    filtered_data_dict = filtered_data.to_dict(orient='records')

    jsonl_file_path = os.path.join(output_dir, f'{filter_value}.jsonl')
    with open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:
        for record in filtered_data_dict:
            jsonl_file.write(json.dumps(record, ensure_ascii=False) + '\n')