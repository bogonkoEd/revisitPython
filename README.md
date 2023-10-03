### Readme

This repository contains the code for the Python3 Development Environment assessment.

## Python3 Development Environment

To set up the Python3 Development environment, follow these steps:

1. Install Python3 and PyCharm.
2. Clone this repository to your local machine.
3. Open the project in PyCharm.
4. Install the following dependencies:
    * pandas
    * openpyxl
    * json

## Running the code

To run the code, follow these steps:

1. Open a terminal and navigate to the root directory of the project.
2. Run the following command:


./generator.sh


This will generate the following files:

* en-xx.xlsx: An Excel file containing the translations for all languages.
* en.jsonl, sw.jsonl, de.jsonl: JSONL files containing the test, train, and dev sets for English, Swahili, and German, respectively.
* train.json: A JSON file containing all the translations from en to xx for all the train sets.

## Functions

The following functions are used in the code:

* load_dataset(): Loads the MASSIVE Dataset from the given data file.
* generate_specific_lang(): Generates a JSONL file for the specified language.
* translation_jsonl(): Generates a JSON file containing all the translations from en to xx for all the train sets.
* filter(): Filters the given dataset based on the specified criteria.

## Pandas

Pandas is used to get a DataFrame from the MASSIVE Dataset and read it into one file at a time.

## JSON

JSON is used to store the generated JSONL files.

## Google Drive Backup Folder

The generated files are uploaded to the Google Drive Backup Folder.

## GitHub

The code changes are uploaded to GitHub.

## Example usage

To generate the en-sw.xlsx file, run the following command:


./generator.sh -l sw


To generate the en.jsonl file, run the following command:


./generator.sh -l en



To generate the train.json file, run the following command:


./generator.sh -t train


## Conclusion

This repository contains the code for the Python3 Development Environment assessment. The code is well-documented and easy to use.