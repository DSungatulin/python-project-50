# Difference Calculator

[![Actions Status](https://github.com/DSungatulin/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DSungatulin/python-project-50/actions)
[![Python CI](https://github.com/DSungatulin/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/DSungatulin/python-project-50/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/68219a8b96085a1216e9/maintainability)](https://codeclimate.com/github/DSungatulin/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/68219a8b96085a1216e9/test_coverage)](https://codeclimate.com/github/DSungatulin/python-project-50/test_coverage)


## Description
This program compares two files and shows the difference between that files.
It supports different data formats (JSON, YAML).
It also supports three formats of output: stylish, plain and JSON.


## Requirements

* Python 3.10+
* Poetry 1.7+
* Pip 22.0+

## Installation

1. Clone the repo

```bash
git clone https://github.com/DSungatulin/python-project-50
```
2. Install application

```bash
make install
make build
make package-install
```

## Usage

To view help, use the follwoing command:
```
gendiff -h
```
To use the program, use the following command:

```
gendiff [-f FORMAT] first_file second_file
```

`FORMAT` is the output format. It supporsts `stylish`, `plain` and `json` formats. Default format is `stylish`.

`first_file`, `second_file` are the files to compare.

## Usage examples

### Help view
![](https://github.com/DSungatulin/python-project-50/work_examples/blob/main/help_view_example.gif)

### Flat JSON file comparison
![](https://github.com/DSungatulin/python-project-50/work_examples/blob/main/flat_json_comparison_example.gif)

### Flat YAML file comparison
![](https://github.com/DSungatulin/python-project-50/work_examples/blob/main/flat_yaml_comparison_example.gif)

### Nested JSON file comparison
![](https://github.com/DSungatulin/python-project-50/work_examples/blob/main/nested_json_comparison_example.gif)

### Nested YAML file comparison
![](https://github.com/DSungatulin/python-project-50/work_examples/blob/main/nested_yaml_comparison_example.gif)

### Plain output format
![](https://github.com/DSungatulin/python-project-50/work_examples/blob/main/plain_format_example.gif)

### JSON output format
![](https://github.com/DSungatulin/python-project-50/work_examples/blob/main/json_format_example.gif)
