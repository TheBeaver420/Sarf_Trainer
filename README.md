# Sarf Trainer

## About

- A quiz game which tests you on basic arabic morphology using a set list of words

## Features

- Customisable quiz timer
- Extendable wordlist
- Arabic morphology analysis and generation using CAMeL Tools
- Multiple-choice questions

## Requirements

- Python 3.12
- customtkinter 5.2.2
- camel-tools 1.6.0

## Installation

- Clone the repository and install the required packages:

```bash
pip install -r requirements.txt

```
## CAMeL Tools Setup

Sarf Trainer uses CAMeL Tools for Arabic morphological analysis and word generation.

### Install the MSA Morphology Database

First, list the available CAMeL Tools packages:

```bash
python -m camel_tools.cli.camel_data -l
```

Install the Modern Standard Arabic morphology database:

```bash
python -m camel_tools.cli.camel_data -i morphology-db-msa-r13
```

The application loads the database using:

```python
MorphologyDB.builtin_db()
```

### Verify Installation

Check that CAMeL Tools is installed correctly:

```bash
python -c "import camel_tools; print(camel_tools.__version__)"
```

The expected version is:

```text
1.6.0
```
## How to Run

Run the application from the `main.py` file:

```bash
py main.py
```
## Testing

### Unit Testing

Unit testing was carried out using Python's built-in unittest framework. Tests were created to check whether the Arabic conjugation generation function successfully returns a generated form for different grammatical inputs.

The tests can be run using:

python -m unittest discover -s tests -v
Conjugation Generation Tests

#### Passive Test
The following tests were carried out:

| Test          | Input                                                     | Expected Result                      | Result |
| ------------- | --------------------------------------------------------- | ------------------------------------ | ------ |
| Active voice  | `b*l`, present, 2nd person, masculine, singular, active  | A conjugated Arabic form is returned | Pass   |
| Passive voice | `b*l`, present, 2nd person, masculine, singular, passive | A conjugated Arabic form is returned | Fail   |

The active voice test successfully returned a generated Arabic form. The passive voice test returned an empty list ([]) instead of a generated form.

Further tests for passive forms were carried out:

| Test          | Input                                                     | Expected Result                      | Result |
| ------------- | --------------------------------------------------------- | ------------------------------------ | ------ |
| Passive voice  | `xrj`, present, 2nd person, masculine, singular, passive  | A conjugated Arabic form is returned | Fail   |
| Passive voice | `rbT`, present, 2nd person, masculine, singular, passive | A conjugated Arabic form is returned | Fail   |

The failed passive test helped identify a limitation in the current use of CAMeL Tools' morphological generation. This is documented further in the Known Issues section.

#### Multiple Form Generation Test

Following test was carried out:
 | Test          | Input                                                     | Expected Result                      | Result |
| ------------- | --------------------------------------------------------- | ------------------------------------ | ------ |
| Generate Words| Generate a list of 100 Words | 100 words Generated | Fail   |


Some forms of arabic words simply cannot be created for grammatical reasons so there will be new words generated to replace them
Test Structure

Tests are stored separately from the main application code in the tests directory:

Sarf_Trainer/
├── main.py
├── functions.py
├── screens.py
├── widgets.py
├── wordlist.py
└── tests/
    └── test_functions.py

## Known Issues

During testing, `smE` produced an unexpected morphological form. 
It inflected the wrong harakaat due to its grammar requiring it to have a different pattern.

This was investigated and found to be related to the behaviour of the
CAMeL Tools morphology database rather than an error in Sarf Trainer's
implementation. As the morphological generation is provided by the
external CAMeL Tools library, this behaviour cannot be directly corrected
within the application. 
Due to this issue, passive generation has been omitted from this project.

## Future Improvements


- Improve lemma selection when multiple morphological analyses are returned by CAMeL Tools.
- Store additional morphological information with each word to reduce reliance on automatic analysis.
- Expand the wordlist with additional Arabic roots and verb forms.
- Add more comprehensive automated unit testing.
- Improve handling of edge cases in Arabic morphological generation.
- Make it so the User has to enter the meaning of the words.