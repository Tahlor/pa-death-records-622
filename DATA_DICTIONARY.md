# Data Dictionary

This release is a curated subset of Pennsylvania death records from the early 20th century.

## Naming and normalization

- `ImageFileName`: official image filename used as the stable record key.
- `image_path`: canonical source path used during curation.
- `SelfGivenName`, `SelfSurname`, `FatherGivenName`, `FatherSurname`, `MotherGivenName`, `MotherSurname`: generally reviewed names.
- Other fields may be standardized, normalized, or corrected for downstream use.
- Fields in the official release should not be assumed to be literal OCR copies.

## Core fields

- `ImageFileName`: filename for the source image.
- `image_path`: original source location of the image.
- `SelfNamePrefix`, `SelfGivenName`, `SelfSurname`, `SelfNameSuffix`: decedent name components.
- `SelfBirthPlace`: birthplace of the decedent.
- `FatherGivenName`, `FatherSurname`, `FatherBirthPlace`: father-related fields.
- `MotherGivenName`, `MotherSurname`, `MotherBirthPlace`: mother-related fields.
- `SelfName`, `FatherName`, `MotherName`: combined convenience fields.

## Usage guidance

- Use the official release as the source of truth for experiments.
- Treat the examples in the README as previews only.
- If you need the full image payload, download the release asset referenced from the GitHub Releases page.

## What is not in this repo

- No raw CSV exports are committed here.
- No image payload is committed here.
- No internal provenance bundle is committed here.
