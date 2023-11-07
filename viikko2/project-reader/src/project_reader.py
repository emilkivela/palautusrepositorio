from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        toml_dict = tomli.loads(content)
        data = toml_dict['tool']['poetry']
        print(data)
        dev_dependencies = list(data['group']['dev']['dependencies'].keys())
        name = data['name']
        description = data['description']
        license = data['license']
        authors = data['authors']
        dependencies = list(data['dependencies'].keys())
        return Project(name, description, license, authors, dependencies, dev_dependencies)
