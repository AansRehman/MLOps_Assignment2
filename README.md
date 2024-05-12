## Tasks
### 1. Data Extraction:
Utilize dawn.com and BBC.com as data sources.
Extract links from the landing page.
Extract titles, descriptions and urls(source links) from articles displayed on their homepages.
### 2. Data Transformation:
Preprocess the extracted text data, ensuring to clean and format the text appropriately for further analysis.
### 3. Data Storage and Version Control:
Store the processed data on Google Drive.
Implement Data Version Control (DVC) to track versions of the data, ensuring each version is accurately recorded as changes are made.
Try to version the metadata against each dvc push to the GitHub repo.
### 4. Apache Airflow DAG Development:
Write an Airflow DAG to automate the processes of extraction, transformation, and storage.
Ensure the DAG handles task dependencies and error management effectively.
Steps
#### Here are the detailed steps followed to complete the tasks:

### 1. Data Extraction:
Utilized Python libraries such as requests, BeautifulSoup, and pandas to extract data from dawn.com and BBC.com.
Wrote a Python script (bbc_scrapper.py and dawn_scrapper.py) to extract links, titles, and descriptions from the landing pages of both websites.
Implemented error handling to gracefully handle any issues during the extraction process.
Tested the extraction script to ensure it accurately retrieves the desired information from the websites.
### 2. Data Transformation:
Created Python scripts (cleaning_bbc_dataset.py and cleaning_dawn_dataset.py) to clean and preprocess the extracted text data.
Applied techniques such as text normalization, removal of special characters, removal of duplicated titles and tokenization to prepare the text for analysis.
Utilized pandas DataFrames to manipulate and transform the data efficiently.
Verified the transformation process by inspecting the cleaned data and comparing it with the original extracted data.
Merging of both cleaned dataset(bbc_scrapper_cleaned.csv and dawn_scrapper_cleaned.csv) into one file named as merged_data.csv
### 3. Data Storage and Version Control:
Configured Google Drive as the storage destination for the processed data. (pip install dvc[gdrive])
Installed and configured DVC to track versions of the data and manage dependencies. (dvc init)
Created a .dvc file to specify the data file (merged_data.csv) and its location in the Google Drive directory. (dvc add data/merged_data.csv)
Initialized a Git repository and linked it to a GitHub repository to track changes in the code and data files. (git add data/merged_data.csv.dvc)
Used Git to commit changes to the code and DVC to commit changes to the data files. (git commit)
Versioned the metadata against each dvc push to the GitHub repository, ensuring a complete record of changes. (Make some changes in data and check the changes are made)
### 4. Apache Airflow DAG Development:
- Downloading the wsl2 on windows
- Downloading the Ubuntu form Microsoft Store
- Install the WSL Ubuntu
- Downloading and Installing the Airflow on the Ubuntu.
- Running the Airflow
- Making the DAG
- Testing the DAG.

Developed an Airflow DAG (my_dag.py) to automate the data extraction, transformation, and storage processes.
Defined tasks for each step of the pipeline, including extract, transform, and load.
Configured task dependencies to ensure that tasks execute in the correct order.
Implemented error handling mechanisms such as retries and email notifications to handle any failures during task execution.
Tested the DAG locally to verify its functionality and troubleshoot any issues.
Deployed the DAG to the Airflow instance, scheduled it to run at regular intervals, and monitored its execution through the Airflow UI.

## Conclusion
By implementing Apache Airflow for MLOps, we have successfully automated the data pipeline, from extraction to storage, while ensuring version control and error management. This approach enhances efficiency and reproducibility in data processing workflows, enabling seamless integration of machine learning models with production systems.
The objective of this assignment is to implement Apache Airflow to automate the process of data extraction, transformation, and version-controlled storage.
