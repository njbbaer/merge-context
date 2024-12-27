# merge-context

A command-line utility that merges multiple code files into a single document, useful for providing pastable context to a language model.

## Usage

Create an input file listing the patterns of files to include/exclude:

```text
*.py
!tests/*.py
config/*.json
```

Prefix patterns with ! to exclude matches. Both relative and absolute paths are supported.

Run the script:

```shell
python merge.py -i input.txt -o output.md
```

The output will be a markdown file containing the contents of all matching files, in a convenient format for providing to a language model.
