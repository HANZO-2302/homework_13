

import json
import csv
import pickle


def read_json(filepath):
	with open(filepath, 'r') as f:
		return json.load(f)


def write_json(data, filepath):
	with open(filepath, 'w') as f:
		json.dump(data, f)


def read_csv(filepath):
	with open(filepath, 'r') as f:
		return list(csv.DictReader(f))


def write_csv(data, filepath):
	with open(filepath, 'w') as f:
		writer = csv.DictWriter(f, fieldnames=data[0].keys())
		writer.writeheader()
		writer.writerows(data)


def read_pickle(filepath):
	with open(filepath, 'rb') as f:
		return pickle.load(f)


def write_pickle(data, filepath):
	with open(filepath, 'wb') as f:
		pickle.dump(data, f)


