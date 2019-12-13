import geopandas as gp

def clean_bounds(OUTPUT_NAME):
    # https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Community-Areas-current-/cauq-8yn6
    bounds = gp.read_file("comm_areas.geojson").rename({"community": "name"}, axis=1)

    filt = ["name", "shape_area", "shape_len", "geometry"]
    bounds = bounds[filt]

    web_merc = {'init': 'epsg:3857'}
    bounds = bounds.to_crs(web_merc)

    bounds.to_file(OUTPUT_NAME)
