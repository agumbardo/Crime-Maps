import os
import time
import pandas as pd
import numpy as np
import google.auth
from google.cloud import bigquery
from google.cloud import bigquery_storage_v1beta1

def get_dataframe(dataset_id, table_id):
    start_time = time.time()
    name = "./data/" + dataset_id
    
    if not os.path.isdir("./data/"):
        os.mkdir("./data/")

    if dataset_id in os.listdir("./data"):
        df = pd.read_pickle(name)
        print("Loaded data from {} in {} s".format(name, time.time() - start_time))
        return df
    
    print("{} not found, generating dataframe from Big Query . . .".format(name))

    # Get reusable credentials, must export json
    # export GOOGLE_APPLICATION_CREDENTIALS="/Users/agumbardo/Documents/MIT/6.S080/Crime-Maps/gcloud.json"
    credentials, your_project_id = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )

    # Create "Client" objects
    client = bigquery.Client(credentials=credentials, project=your_project_id)
    storage_client = bigquery_storage_v1beta1.BigQueryStorageClient(credentials=credentials)

    table = bigquery_storage_v1beta1.types.TableReference()
    table.project_id = "bigquery-public-data"
    table.dataset_id = dataset_id
    table.table_id = table_id

    read_options = bigquery_storage_v1beta1.types.TableReadOptions()
    # read_options.selected_fields.append("species_common_name")

    session = storage_client.create_read_session(
        table,
        parent="projects/{}".format(your_project_id),
        read_options=read_options,
        format_=bigquery_storage_v1beta1.enums.DataFormat.ARROW,
        sharding_strategy=(
            bigquery_storage_v1beta1.enums.ShardingStrategy.LIQUID
        ),
    )

    stream = session.streams[0]
    position = bigquery_storage_v1beta1.types.StreamPosition(stream=stream)
    reader = storage_client.read_rows(position)
    df = reader.to_dataframe(session)
    df.to_pickle(name)
    print("Saved data to {} in {} s".format(name, time.time() - start_time))
    return df