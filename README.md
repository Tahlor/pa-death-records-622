# Pennsylvania Death Records 622

This repository is the public landing page for the Pennsylvania death-record subset used in the ICDAR paper.

The repo intentionally does **not** contain the dataset payload. It provides:

- one cleanly named download target
- links to the official images
- links to the official labels
- example images
- example data
- a data dictionary
- usage notes for the fields and naming conventions

## Download

Use the single release asset below for the cleaned dataset package:

- `PA_DEATH_RECORDS_622_v1.tar.gz`

Release page:

`https://github.com/Tahlor/pa-death-records-622/releases`

## Official sources

- Images: `F:\labelbox\PA\pa_death_ems\5164\622`
- Official labels: cleaned release package
- Release landing page: `https://github.com/Tahlor/pa-death-records-622`

## Examples

The examples below are representative official records. They are shown for preview only; the source files are not committed in this repository.

### Example images

- `41381_1220705043_0549-01468.jpg`
- `41381_1220705043_0549-04785.jpg`
- `41381_1220705043_0567-00432.jpg`
- `41381_1220705043_0567-03648.jpg`

### Example data

| ImageFileName | SelfGivenName | SelfSurname | SelfBirthPlace |
| --- | --- | --- | --- |
| `41381_1220705043_0549-01468.jpg` | Raymond | Merrell | Phila |
| `41381_1220705043_0549-04785.jpg` | Mary Miller | Scott | Phila |
| `41381_1220705043_0567-00432.jpg` | Melora Kellogg | Fleming | New York State |
| `41381_1220705043_0567-03648.jpg` | Robert M | Phinney | Pa |

## Data dictionary

See [DATA_DICTIONARY.md](DATA_DICTIONARY.md) for field definitions and normalization notes.

## Important notes

- Names have been generally reviewed.
- Other fields may be standardized and may not be literal character-for-character matches to the source certificates.
- The official release should be treated as a curated research dataset, not a verbatim transcription of every source field.
