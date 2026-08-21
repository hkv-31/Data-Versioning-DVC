# Data Versioning with DVC- Wine Quality Dataset

## Overview

This project demonstrates **data versioning using Data Version Control (DVC)** with the Wine Quality dataset.

Git versions the project files and DVC metadata, while DVC manages the actual dataset and its different versions.

## Dataset

**Wine Quality- Red Wine**

The dataset contains physicochemical measurements of red wine samples and a `quality` score.

Dataset path:

```text
data/winequality-red.csv
```

## Tools Used

- Python
- Pandas
- Git
- GitHub
- DVC

## Repository Structure

```text
Data-Versioning-DVC/
│
├── data/
│   ├── winequality-red.csv
│   └── winequality-red.csv.dvc
│
├── .dvc/
├── .dvcignore
├── README.md
└── requirements.txt
```

## DVC Workflow

### Initialize DVC

```bash
dvc init
```

### Track the dataset

```bash
dvc add data/winequality-red.csv
```

This creates:

```text
data/winequality-red.csv.dvc
```

The `.dvc` file is committed to Git instead of the actual dataset.

### Commit the dataset metadata

```bash
git add data/winequality-red.csv.dvc
git commit -m "Add wine dataset v1"
```

### Configure a DVC remote

For this project, a local directory is used as the DVC remote:

```bash
dvc remote add -d local dvc-storage
```

### Push the dataset

```bash
dvc push
```

The actual dataset is stored in the DVC remote while GitHub stores the DVC metadata.

## Dataset Versions

| Version | Change |
|---|---|
| V1 | Original Wine Quality dataset |
| V2 | Updated dataset after removing duplicate records |

To create a new version:

```bash
dvc add data/winequality-red.csv
git add data/winequality-red.csv.dvc
git commit -m "Update wine dataset v2"
dvc push
```

## Switching Between Dataset Versions

Git controls which `.dvc` metadata version is checked out.

```bash
git checkout <commit>
dvc checkout
```

To return to the latest version:

```bash
git checkout main
dvc checkout
```

`dvc checkout` synchronizes the working dataset with the DVC metadata for the selected Git revision.

## Git vs DVC

```text
Git
 ├── Code
 ├── README
 ├── Project files
 └── .dvc metadata
          │
          ↓
        DVC
          │
          ↓
   Actual dataset
          │
          ↓
     DVC Remote
```

Git provides the project and metadata history, while DVC manages the actual dataset versions.

## Useful Commands

```bash
dvc status
dvc add <file>
dvc push
dvc pull
dvc checkout

git status
git log --oneline
git add .
git commit -m "message"
git push
```

## Conclusion

This project demonstrates how DVC can be used alongside Git to version datasets without storing large data files directly in Git. Different dataset states can be associated with Git commits, while DVC stores and restores the corresponding dataset versions.
