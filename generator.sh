#!/bin/bash

# Define log file names

generator_log="logs/generator.log"

# Run the Python script with the necessary flags and capture the output
output=$(python main.py \
    --archive_path "data/dataset.tar.gz" \
    --output_directory "language_specific_files" \
    --output_dir "jsonl_files" \
    --filter_column "partition")

# Append the output to the log file
echo "$output" >> "$generator_log"

# Count the number of generated files and save it to the generator_log
language_specific_files_count=$(ls -1 "language_specific_files" | wc -l)
jsonl_files_count=$(ls -1 "jsonl_files" | wc -l)
echo "Number of files generated in 'language_specific_files': $language_specific_files_count" >> "$generator_log"
echo "Name of generated files in 'language_specific_files': $(ls -1 "language_specific_files")" >> "$generator_log"
echo "Number of files generated in 'jsonl_files': $jsonl_files_count" >> "$generator_log"
echo "Name of generated files in 'jsonl_files': $(ls -1 "jsonl_files")" >> "$generator_log"
