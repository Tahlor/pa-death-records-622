# Pennsylvania Death Records 622

Curated 622-image Pennsylvania death-record subset used in [arXiv:2509.09722](https://arxiv.org/abs/2509.09722).

This repository is a public landing page for the release. It keeps the tree small, shows representative preview renders, and points to a downloadable zip archive containing the full image set and release metadata.

## Download

Current release:

- [PA_DEATH_RECORDS_622_v1.0.1.zip](https://github.com/Tahlor/pa-death-records-622/releases/download/v1.0.1/PA_DEATH_RECORDS_622_v1.0.1.zip)
- [SHA256SUMS.txt](https://github.com/Tahlor/pa-death-records-622/releases/download/v1.0.1/SHA256SUMS.txt)

Release page:

- [v1.0.1 release notes](https://github.com/Tahlor/pa-death-records-622/releases/tag/v1.0.1)

## Files included in the release archive

The downloadable zip contains the full image set plus release metadata. Expected top-level paths inside the zip are:

- `images/` - 622 image files
- `data/official/5164_gts.csv` - official label CSV
- `examples/example_labels.csv` - small preview label table
- `CITATION.cff` - citation metadata
- `LICENSE.md` - repository/documentation license note
- `RELEASE_NOTES.md` - release summary and limitations
- `DATA_DICTIONARY.md` - field definitions and normalization notes

## Preview images

Representative preview renders are committed in the repo so the landing page shows actual images on GitHub.

<p align="center">
  <img src="examples/preview/0549-04785_blur_k11.jpg" width="220" alt="Blurred preview for record 41381_1220705043_0549-04785" />
  <img src="examples/preview/0549-04785_rotate_1deg.jpg" width="220" alt="Rotated preview for record 41381_1220705043_0549-04785" />
  <img src="examples/preview/0549-04785_gridwarp_std3.jpg" width="220" alt="Grid-warp preview for record 41381_1220705043_0549-04785" />
  <img src="examples/preview/0567-00432_highlighted.jpg" width="220" alt="Highlighted preview for record 41381_1220705043_0567-00432" />
</p>

## Example labels

The table below matches the previewed records.

| ImageFileName | SelfGivenName_orig | SelfGivenName_edt | SelfSurname_orig | SelfSurname_edt | SelfBirthPlace_orig | SelfBirthPlace_edt |
| --- | --- | --- | --- | --- | --- | --- |
| `41381_1220705043_0549-04785.jpg` | Mary Miller | Mary Miller | Scott | Scott | Phila | Philadelphia, Pennsylvania |
| `41381_1220705043_0567-00432.jpg` | Melora Kellogg | Melora Kellogg | Fleming | Fleming | New York State | New York |

See [examples/example_labels.csv](examples/example_labels.csv) for a CSV version of the same preview-label rows.

## Data fields

The official CSV uses paired `_orig` and `_edt` columns for names and places, plus a stable image key and archive-relative image path.

- [DATA_DICTIONARY.md](DATA_DICTIONARY.md)
- The official release CSV in the archive is the source of truth for experiments.

## Usage notes

- The examples in this README are previews only.
- The official release labels are curated and may include normalization or standardization in `_edt` fields.
- The release archive is the canonical public download.
- The public repo does not commit the full image payload.

## Citation

If you use this release, cite the paper and the release URL:

- [arXiv:2509.09722](https://arxiv.org/abs/2509.09722)
- [GitHub release v1.0.1](https://github.com/Tahlor/pa-death-records-622/releases/tag/v1.0.1)

## License and terms

Documentation in this repository is provided for public release reference.
The image scans and label data in the downloadable archive may remain subject to the source-record access terms that governed their collection.
This repository does not claim to relicense those source records.

## Contact and issues

Use [GitHub Issues](https://github.com/Tahlor/pa-death-records-622/issues) for questions or corrections.
