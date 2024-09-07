# KOL Data Standardization (KOL Profiling)

KOL (Key Opinion Leader) Data Standardization project is an ETL utility which is used to provide the standardized data of the KOLs by gathering data from various sources (in batches), map it to translations and transform it for the end user consumption.

## Requirement

KOL (Key Opinion Leader) is essentially a highly experienced and reputed health care professional whose opinion is valued in a specific industry. Pharma companies appoints several medical representatives that approach these KOLs who would drive the prescription of a particular drug. They do this by influencing a wide network of doctors that can prescribe a given drug to the patients.

A suitable KOL would depend on various attributes like:

-   How much years of experience does the KOL has
-   How good is the KOLs network, how many others HCPs refer cases to him in critical situations
-   How much states or countries does the KOL treat patients.
-   Was the KOL involved in the early trials and researches for the disease.
    All these attributes make the job of finding the perfect KOL difficult for the pharma companies. Unless and otherwise there exists a standardized way to retrieve KOL data. This is where the KOL Profiling tool comes into picture.

## Data Source

Dummy data has been generated for this KOL Data Standardization project. It utilizes the Faker library of Python to create several batches of KOL data which is then provided to the ETL pipeline. You can use the below jupyter notebook to generate the input data:

`0. data_generation.ipynb`

## ETL Process

-   **Data Extraction (1. data_extraction.ipynb):** This script loads the various KOL input data batches into the memory and prepares it for the Landing area (Area where the data is stored for all the batches, waiting for data transformation process). The input data once loaded is checked for null values with following constraints:
    -   The mdm_id should not be null.
    -   The first name of the KOL should not be null.
-   **Data Transformation (2. data_transformation.ipynb):** This script loads the landing stage dataset into the memory and applies some business rules and logic onto it, making it ready for the Staging area (Area where the refined KOL data is stored, waiting for further final checks before sending it to the Reporting layer or to the end-users for analysis). The business rules include:
    -   Merge the data of same KOLs (data points with same mdm_id) and ensure that the latest batch data is updated for all columns except degree and speciality.
    -   Since, a KOL can have multiple degrees and multiple specialities, concat these datapoints across the landing stage batches.
    -   Based on the master tables, apply name-id mappings to degree, speciality, and profile status.
    -   Handle null values on other columns
-   **Data Loading (3. data_loading.ipynb):** This script loads the staging area dataset into the memory and further prepares 3 separate datasets:
    -   KOL speciality map: A mapping table which stores KOL's mdm_id and their specialities.
    -   KOL degree map: A mapping table which stores KOL's mdm_id and their degrees.
    -   KOL data: Basic information relatd to the KOLs

After this ETL process, the data stored in the reporting area can be used to empower a KOL Data Management platform or can be further used for KOL data analysis.
