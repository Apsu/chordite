import yaml
import pathlib
import pprint as pp

# pp = pprint.PrettyPrinter(indent = 4)

def analyze(layout_path: pathlib.Path):
	print(f"Analyzing {layout_path}")
	with open(layout_path) as layout_file:
		layout_data = yaml.load(layout_file, Loader=yaml.CLoader)

	pp.pprint(layout_data)
