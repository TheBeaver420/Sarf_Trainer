# Sarf Trainer

## About

- A quiz game which tests you on basic arabic morphology using a set list of words
## Features

- Customisable quiz timer
- Customisable wordlist
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

The application was tested using Python unit tests to verify the functionality
of the Arabic morphology and word generation features.

| Test | Expected | Result |
|---|---|---|
| `ktb` transliteration | `كتب` | PASS |
| Morphological analysis | Correct analysis | PASS |
| Word generation | Correct form | PASS |
| `smE` generation | Expected form | LIMITATION |

## Known Issues

During testing, `smE` produced an unexpected morphological form. 
It inflected the wrong harakaat due to its grammar requiring it to have a different pattern.

This was investigated and found to be related to the behaviour of the
CAMeL Tools morphology database rather than an error in Sarf Trainer's
implementation. As the morphological generation is provided by the
external CAMeL Tools library, this behaviour cannot be directly corrected
within the application.


## Future Improvements

