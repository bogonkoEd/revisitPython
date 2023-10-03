import functions
import os


def main():
    dataset_path = "data/dataset.tar.gz"
    data_frame = functions.load_dataset(dataset_path)
    output_dir = 'language_specific_files'
    os.makedirs(output_dir, exist_ok=True)
    functions.generate_language_excel_files(data_frame, output_dir)

    out_dir = 'jsonl_files'
    os.makedirs(out_dir, exist_ok=True)
    filter_column = 'partition'
    sw_value = 'dev'
    en_value = 'test'
    de_value = 'train'
    en_path = 'language_specific_files/en-en.xlsx'
    de_path = 'language_specific_files/en-de-DE.xlsx'
    sw_path = 'language_specific_files/en-sw-KE.xlsx'
    functions.filter_into_jsonl(en_path, out_dir, filter_column, en_value)
    functions.filter_into_jsonl(de_path, out_dir, filter_column, de_value)
    functions.filter_into_jsonl(sw_path, out_dir, filter_column, sw_value)

    functions.generate_translations(data_frame, out_dir)


if __name__ == "__main__":
    main()
