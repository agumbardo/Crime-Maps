# Crime-Maps

## Dependencies
### Geopandas
conda install --channel conda-forge geopandas
### bokeh
conda install bokeh
### BigQuery
pip install --upgrade google-cloud-bigquery
pip install google-cloud-bigquery-storage
export GOOGLE_APPLICATION_CREDENTIALS="~/Documents/MIT/6.S080/Crime-Maps/gcloud.json"
conda install -c conda-forge pyarrow