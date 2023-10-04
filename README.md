# Computer-Graphics: ICS 3C - Group 12 CAT 1

## About
This Python3 development project establishes an environment for data processing and file manipulation. It structures a PyCharm project, imports a massive dataset, and accomplishes three main tasks. It creates language-specific files and a comprehensive translation dataset ensuring clean file management with GitHub integration.

## Tasks
1. Build a Python3 project with the structure of projects in PyCharm.
2. Import the MASSIVE Dataset mentioned in the Data File above. In this dataset, the pivot language is English. Given that all the ids of the languages are matching, generate an `en-xx.xlxs` file for all the languages using the id, utt, and annot_utt.
3. For English (en), Swahili (sw), and German (de), generate separate `jsonl` files with test, train, and dev datasets respectively.
4. Generate one large `json` file showing all the translations from English (en) to xx with id and utt for all the train sets. Pretty print your json file structure.

## Python Files
- `functions.py`: Contains functions to answer the questions for generating files from Excel to Jsonl.
- `main.py`: The main program file that loads, processes, and analyzes data.

## Data Produced
- `Excel_Files`: The output excel files that contain id's of all languages.
- `JSONL_Files`: The `jsonl` files that contain the pretty printed `jsonl` formatted for each language.
- `JSONL_Output`: Contains DE, SW, and EN `jsonl` files.
- `translations.json`: Large `json` file showing all the translations from en to xx with id and utt for all the train sets.

## Usage
To run the project, follow these steps:
1. Activate the Virtual Environment: Activate the Python virtual environment with `source venv/bin/activate` to work within an isolated environment for this project.
2. Run the Main Script: Use the command `python main.py` to execute the project's main Python script, which performs various data processing tasks.
3. Check Output: After running the script, find the generated files in the project directory, including Excel, JSON, and CSV files, depending on the tasks completed.



## Authors
- 137192 Eddy Bogonko
- 137938 Martin Mwangi
- 136603 Jane Daisy
- 146013 Amanda Karani
- 139991 Glen Musa

## License
This project currently does not contain any licenses.