"""https://github.com/vrandezo/wikiglobe"""

from __future__ import division
import os
import json
import webbrowser
from http_server import GlobePlotServer
import numpy as np
from jinja2 import Environment, FileSystemLoader
from IPython.core.display import display, HTML
from pkg_resources import resource_filename


class GlobePlot(object):

    def __init__(self, lats=None, lons=None, data=None):
        self.lats, self.lons, self.data = \
            self._reshape_data(lats, lons, data)

    def _reshape_data(self, lats, lons, data):
        if lats.shape == lons.shape == data.shape:

            if lats.ndim == lons.ndim == data.ndim == 1:
                pass
            elif lats.ndim == lons.ndim == data.ndim == 2:
                y, x = data.shape
                data = np.reshape(data, y * x)
                lats = np.reshape(lats, y * x)
                lons = np.reshape(lons, y * x)
            else:
                err_msg = 'Can only handle one- and two-dimensional data.'
                raise ValueError(err_msg)

            data = self._normalize(data)

            return lats, lons, data
        elif lats == lons == data == None:
            return lats, lons, data
        else:
            raise ValueError('Arrays of different shape.')

    def append(self, lats, lons, data):
        lats, lons, data = self._reshape_data(lats, lons, data)
        self.lats = np.concatenate((self.lats, lats))
        self.lons = np.concatenate((self.lons, lons))
        self.data = np.concatenate((self.data, data))

    def _scale_linear(self, values, low=0.0, high=1.0):
        # https://gist.github.com/perrygeo/4512375
        mins = np.min(values)
        maxs = np.max(values)
        value_range = maxs - mins
        return high - (((high - low) * (maxs - values)) / value_range)

    def _normalize(self, values):
        maximum = np.max(values)
        return values / maximum

    def _convert_data(self):
        concat = np.transpose(np.array((self.lats, self.lons, self.data)))

        # filter... move this out of here
        # concat = concat[concat[:, 2] > 0]

        return concat.flatten().tolist()

    def _generate_html(self, data, title='Globe Plot',
                       creator='GlobePlot', creator_addr='http://...',
                       code_link='http://...'):
        base = resource_filename('globeplot', '')

        # base = os.path.split(base)[0]
        template_file = os.path.join(base, 'webgl_globe',
                                     'index_template_small.html')

        rendered_file = os.path.join(base, 'webgl_globe', 'index.html')
        data_list = json.dumps(data)

        html_path = os.path.split(template_file)[0]
        env = Environment(loader=FileSystemLoader(html_path))

        template = env.get_template(os.path.split(template_file)[1])
        html = template.render(title=title, data_list=data_list,
                               creator=creator, creator_addr=creator_addr,
                               code_link=code_link)

        with open(rendered_file, 'w') as f:
            f.write(html)

        return html

    def _show_in_browser(self):
        url = "http://localhost:8000"
        with GlobePlotServer() as _:
            webbrowser.open(url, new=2)

    def show(self, title='Globe Plot', creator='GlobePlot',
             creator_addr='http://...', code_link='http://...'):
        plt_data = self._convert_data()
        self._generate_html(plt_data, title=title, creator=creator,
                            creator_addr=creator_addr,
                            code_link=code_link)

        self._show_in_browser()

    def display(self, title='Globe Plot', creator='GlobePlot',
                creator_addr='http://...', code_link='http://...'):
        plt_data = self._convert_data()
        self._generate_html(plt_data, title=title, creator=creator,
                            creator_addr=creator_addr,
                            code_link=code_link)

        with GlobePlotServer() as _:
            return display(HTML('<iframe height=600 width=100%, src="http://localhost:8000/"></iframe>'))

    def export(self):
        # TODO: implement me
        pass
