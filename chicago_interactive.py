import geopandas as gp
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider, GeoJSONDataSource
from bokeh.plotting import figure
from bokeh.tile_providers import get_provider, Vendors

# bokeh serve --show chicago_interactive.py 

class MakeInteractiveMap:
    def __init__(self, gdf):
        start_month = 1
        self.gdf = gdf
        self.source = GeoJSONDataSource(geojson = gdf[gdf.month == start_month].to_json())

        # Create plot
        plot = figure(x_axis_type="mercator", y_axis_type="mercator",  plot_width=900, title="Chicago Crime")
        plot.add_tile(get_provider(Vendors.CARTODBPOSITRON_RETINA))
        plot.circle(x= 'x', y='y', source=self.source, radius=10, color='red')

        # Create slider
        self.slider = Slider(start=1, end=12, value=start_month, step=1, title='Month')
        self.slider.on_change('value', self.callback)

        # Arrange plots and widgets in layouts
        layout = column(plot, self.slider) 
        curdoc().add_root(layout)

    def callback(self, attr, old, new): 
        N = self.slider.value
        self.source.geojson = self.gdf[self.gdf.month == N].to_json()

gdf2018 = gp.read_file("test/test.geojson")
print(gdf2018.shape)
MakeInteractiveMap(gdf2018)
