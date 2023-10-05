#!/bin/bash

# Run the Python script with the necessary flags
python main.py \
    --archive_path "data/dataset.tar.gz" \
    --output_directory "language_specific_files" \
    --output_dir "jsonl_files" \
    --filter_column "partition"  \