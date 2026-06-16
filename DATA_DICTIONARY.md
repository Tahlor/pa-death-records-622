# Data Dictionary

This release is a curated subset of Pennsylvania death records from the early 20th century.
It is not a verbatim transcription of every source field.

## Field groups

- `ImageFileName`: stable record key for the image/label pair.
- `*_orig`: source text as entered or captured for curation.
- `*_edt`: curated or standardized text used for the official release.
- `image_path`: archive-relative path to the image file in the downloadable release.

## Column definitions

| Column | Definition |
| --- | --- |
| `ImageFileName` | Stable record key for the image; the matching file name in the release image folder is `<ImageFileName>.jpg`. |
| `SelfNamePrefix_orig` | Original prefix attached to the decedent name, if present. |
| `SelfNamePrefix_edt` | Curated prefix for the decedent name, if present. |
| `SelfGivenName_orig` | Original given name(s) for the decedent. |
| `SelfGivenName_edt` | Curated given name(s) for the decedent. |
| `SelfSurname_orig` | Original surname for the decedent. |
| `SelfSurname_edt` | Curated surname for the decedent. |
| `SelfNameSuffix_orig` | Original suffix attached to the decedent name, if present. |
| `SelfNameSuffix_edt` | Curated suffix for the decedent name, if present. |
| `SelfBirthPlace_orig` | Original birthplace text for the decedent. |
| `SelfBirthPlace_edt` | Curated/standardized birthplace text for the decedent. |
| `FatherGivenName_orig` | Original given name(s) for the father. |
| `FatherGivenName_edt` | Curated given name(s) for the father. |
| `FatherSurname_orig` | Original surname for the father. |
| `FatherSurname_edt` | Curated surname for the father. |
| `FatherBirthPlace_orig` | Original birthplace text for the father. |
| `FatherBirthPlace_edt` | Curated/standardized birthplace text for the father. |
| `MotherGivenName_orig` | Original given name(s) for the mother. |
| `MotherGivenName_edt` | Curated given name(s) for the mother. |
| `MotherSurname_orig` | Original surname for the mother. |
| `MotherSurname_edt` | Curated surname for the mother. |
| `MotherBirthPlace_orig` | Original birthplace text for the mother. |
| `MotherBirthPlace_edt` | Curated/standardized birthplace text for the mother. |
| `image_path` | Archive-relative image path used for traceability in the official release CSV. |
| `SelfName_orig` | Original combined decedent name field. |
| `SelfName_edt` | Curated combined decedent name field. |
| `FatherName_orig` | Original combined father name field. |
| `FatherName_edt` | Curated combined father name field. |
| `MotherName_orig` | Original combined mother name field. |
| `MotherName_edt` | Curated combined mother name field. |

## Normalization notes

- The `_edt` fields may standardize spelling, punctuation, or geographic wording.
- The official release keeps both the original and edited forms for transparency.
- The stable `ImageFileName` key is the primary join field between images and labels.

## Usage guidance

- Use the official release CSVs in the downloadable archive as the source of truth.
- Treat the README examples as previews only.
- Do not assume `_orig` fields are clean or normalized.
- Do not assume `_edt` fields are literal OCR copies.

## Public-release caveat

- The repository does not commit the full image payload.
- The repository does not expose private or local machine paths in its public-facing text.
