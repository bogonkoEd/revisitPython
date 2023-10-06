import functions
import os
from absl import flags, app

FLAGS = flags.FLAGS

flags.DEFINE_string(
    "archive_path", "data/dataset.tar.gz", "Path to the dataset archive"
)
flags.DEFINE_string(
    "output_directory", "language_specific_files", "Path to the output directory"
)
flags.DEFINE_string("output_dir", "jsonl_files", "Path to the output directory")
flags.DEFINE_string("filter_column", "partition", "Column to filter on")


def main(_):
    data_frame = functions.load_dataset(FLAGS.archive_path)
    os.makedirs(FLAGS.output_directory, exist_ok=True)
    functions.generate_language_excel_files(data_frame, FLAGS.output_directory)

    os.makedirs(FLAGS.output_dir, exist_ok=True)
    filters = [
        ("language_specific_files/en-en.xlsx", "test"),
        ("language_specific_files/en-de.xlsx", "dev"),
        ("language_specific_files/en-sw.xlsx", "train"),
    ]
    for path, filter_value in filters:
        functions.filter_into_jsonl(
            path, FLAGS.output_dir, FLAGS.filter_column, filter_value
        )

    functions.generate_translation_jsonl(data_frame, FLAGS.output_dir)

  
    functions.upload_files(FLAGS.output_dir, FLAGS.output_directory)
    


if __name__ == "__main__":
    app.run(main)
