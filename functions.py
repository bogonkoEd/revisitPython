import os
import json
import tarfile
import pandas


def load_dataset(dataset_path):
    """Function to Read data from the Massive Dataset."""

    def _jsonl_generator():
        with tarfile.open(dataset_path, mode="r:gz") as data_archive:
            for member in data_archive.getmembers():
                if member.isfile() and member.name.endswith(".jsonl"):
                    with data_archive.extractfile(member) as file:
                        for line_bytes in file:
                            line = line_bytes.decode("utf-8").strip()
                            if line:
                                yield json.loads(line)

    data = _jsonl_generator()

    data_frame = pandas.DataFrame(data)

    return data_frame


def generate_translation_jsonl(data_frame, output_dir):
    """Combines translations from a DataFrame and saves them as (.jsonl) file."""

    locales = data_frame["locale"].unique()
    combined_data_list = []

    for locale in locales:
        if locale == "en-US":
            continue
        en_data = data_frame[data_frame["locale"] == "en-US"][
            ["id", "utt", "annot_utt"]
        ]
        locale_data = data_frame[data_frame["locale"] == locale]
        combined_data = pandas.merge(en_data, locale_data, on="id", how="inner")
        combined_data_list.extend(combined_data.to_dict("records"))

    jsonl_file_path = os.path.join(output_dir, "combined_translation.jsonl")

    with open(jsonl_file_path, "w", encoding="utf-8") as jsonl_file:
        for record in combined_data_list:
            jsonl_file.write(json.dumps(record, ensure_ascii=False) + "\n")


def generate_language_excel_files(data_frame, output_dir):
    """Combines data from 'en-US' and other locales and saves as Excel files."""

    locales = data_frame["locale"].unique()

    if "en-US" in locales:
        en_data = data_frame[data_frame["locale"] == "en-US"]
        output_file_path = os.path.join(output_dir, "en-en.xlsx")
        en_data.to_excel(output_file_path, index=False)

        for locale in locales:
            if locale == "en-US":
                continue

            locale_data = data_frame[data_frame["locale"] == locale]
            en_us_data = data_frame[data_frame["locale"] == "en-US"][
                ["id", "utt", "annot_utt"]
            ]
            combined_data = pandas.merge(en_us_data, locale_data, on="id", how="inner")
            output_file_path = os.path.join(output_dir, f"en-{locale}.xlsx")
            combined_data.to_excel(output_file_path, index=False)


def filter_into_jsonl(xlsx_file_path, output_dir, filter_column, filter_value):
    """Reads data from Excel file, filters it based on a specified column and value and saves as jsonl file."""

    data_frame = pandas.read_excel(xlsx_file_path)
    filtered_data = data_frame[data_frame[filter_column] == filter_value]
    filtered_data_dict = filtered_data.to_dict(orient="records")

    jsonl_file_path = os.path.join(output_dir, f"{filter_value}.jsonl")
    with open(jsonl_file_path, "w", encoding="utf-8") as jsonl_file:
        for record in filtered_data_dict:
            jsonl_file.write(json.dumps(record, ensure_ascii=False) + "\n")
