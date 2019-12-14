# Crime-Maps
## About

Interactive tool for visualizing crime data!

---

## Dependencies

### Geopandas
`conda install --channel conda-forge geopandas`

### bokeh
`conda install bokeh`

### BigQuery (to fetch data)
`pip install --upgrade google-cloud-bigquery`

`pip install google-cloud-bigquery-storage`

`conda install -c conda-forge pyarrow`

You must have a google api key. Generate your own or use the one I provide (`gcloud.json`). Then run `export GOOGLE_APPLICATION_CREDENTIALS="/Users/agumbardo/Documents/MIT/6.S080/Crime-Maps/gcloud.json"` using the correct path

---

## Use

### chicago.ipynb

Notebook where a bunch of the datacleaning was done. Running certain cells will output a interactive crime map within the notebook or in a seperate html file.

### fetch_data.py

Creates a pandas dataframe by querying the Kaggle Chicago crime dataset using Google BigQuery
___

### To run the website 

`python3 website.py`


## Authors
Adam Gumbardo, Vedaant Kukadia and Van Coykendall
