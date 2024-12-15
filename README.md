# Genome Project: Gene Family Classification

## Overview

This project builds a classification model trained on human coding DNA sequences (CDS) to predict gene families. The model is then tested on sequences from chimpanzees and dogs to compare prediction accuracies across species. The main goal is to develop a gene family classifier and evaluate its generalizability across different species.

## Project Structure

The repository contains the following key components:

1. **data/** - Contains datasets used to train and test the model.
2. **data_extraction.py** - A Python script that extracts human genome data from Ensembl using the BioMart API. The script retrieves gene metadata and coding DNA sequences, and saves them in a FASTA file format for further processing.
3. **genome_nlp_0.ipynb** - A Jupyter notebook that processes the extracted human genome data, trains a classification model, and evaluates its performance on human, dog, and chimpanzee datasets.
4. **environment.yml** - An environment file listing the required dependencies for running the project.

## Data Extraction: `data_extraction.py`

The `data_extraction.py` script uses the [BioMart](http://www.ensembl.org/biomart) API to retrieve gene metadata and coding DNA sequences (CDS) for the human genome. The following steps are performed:

1. **Connect to BioMart**: Connects to the Ensembl BioMart server to access the human genome dataset (`hsapiens_gene_ensembl`).
2. **Metadata Retrieval**: Retrieves metadata attributes including:
   - Ensembl Gene ID
   - Ensembl Transcript ID
   - Gene Name
   - Gene Description
   - Source of Transcript
3. **Sequence Retrieval**: Retrieves coding DNA sequences (CDS) for the genes.
4. **Data Storage**: The retrieved metadata and sequences are processed and stored in a FASTA file format (`human_cds_sequences.fasta`).

## Model Training: `genome_nlp_0.ipynb`

The `genome_nlp_0.ipynb` Jupyter notebook processes the extracted human genome data and trains a classification model. The model is trained only on the **human dataset**. The key steps in the notebook include:

1. **Data Preprocessing**: Data cleaning, tokenization, and vectorization of the DNA sequences for model input.
2. **Model Training**: A classification model is trained using the processed human DNA sequences. The model predicts gene families based on these sequences.
3. **Model Evaluation**: After training, the model's performance is evaluated on sequences from different species (chimpanzee and dog). The evaluation compares the prediction accuracy across species, assessing the model's ability to generalize to other species' data.

## Dataset

The datasets used in this project are genomic data from three species:
- **Human** (used for training the model)
- **Chimpanzee** (used for evaluating prediction accuracy)
- **Dog** (used for evaluating prediction accuracy)

The data is located in the `data/` directory.

## Setup and Installation

To set up the project environment, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd Genome_Project

2. Create a new conda environment using the provided environment.yml:
    ```bash
    conda env create -f environment.yml
    conda activate <environment-name>

3. Install additional dependencies (if any) with:
    ```bash
    pip install -r requirements.txt

## Usage
## Running the Data Extraction

To extract human genome data and save it to a FASTA file, run the data_extraction.py script:
    ```bash
    python data_extraction.py

This will generate a human_cds_sequences.fasta file containing the extracted sequences.
## Running the Model

Open the genome_nlp_0.ipynb notebook in Jupyter and execute the cells to train and evaluate the model. The notebook will guide you through the steps of processing the data and training the classification model. The model will be evaluated on the chimpanzee and dog datasets for comparison.
    ```bash
    jupyter notebook genome_nlp_0.ipynb

License

This project is licensed under the MIT License - see the LICENSE file for details.
