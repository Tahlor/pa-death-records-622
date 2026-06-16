# Data Dictionary

This release is a curated subset of Pennsylvania death records from the early 20th century.

## Naming and normalization

- `ImageFileName`: official image filename used as the stable record key.
- `SelfGivenName`, `SelfSurname`, `FatherGivenName`, `FatherSurname`, `MotherGivenName`, `MotherSurname`: generally reviewed names.
- Other fields may be standardized, normalized, or corrected for downstream use.
- Fields in the official release should not be assumed to be literal OCR copies.

## Core fields

- `ImageFileName`: filename for the source image.
- `SelfNamePrefix`, `SelfGivenName`, `SelfSurname`, `SelfNameSuffix`: decedent name components.
- `SelfBirthPlace`: birthplace of the decedent.
- `FatherGivenName`, `FatherSurname`, `FatherBirthPlace`: father-related fields.
- `MotherGivenName`, `MotherSurname`, `MotherBirthPlace`: mother-related fields.
- `SelfName`, `FatherName`, `MotherName`: combined convenience fields.

## Usage guidance

- Use the official release as the source of truth for experiments.
- Treat the examples in the README as previews only.
- If you need the full image payload, download the release archive named `PA_DEATH_RECORDS_622_v1.tar.gz` once it is published.

## What is not in this repo

- No raw CSV exports are committed here.
- No image payload is committed here.
- No local filesystem paths are published here.
