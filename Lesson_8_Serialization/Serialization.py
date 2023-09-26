import os
import json
import csv
import pickle


def scan_directory(dir_path):
	result = []
	for root, dirs, files in os.walk(dir_path):
		for file in files:
			file_path = os.path.join(root, file)
			file_info = {'path': file_path, 'parent': root, 'type': 'file', 'size': os.path.getsize(file_path)}
			result.append(file_info)
		for dir in dirs:
			dir_path = os.path.join(root, dir)
			dir_info = {'path': dir_path, 'parent': root, 'type': 'directory', 'size': get_total_size(dir_path)}
			result.append(dir_info)

	with open('result.json', 'w') as f:
		json.dump(result, f)

	with open('result.csv', 'w') as f:
		writer = csv.DictWriter(f, fieldnames=['path', 'parent', 'type', 'size'])
		writer.writeheader()
		writer.writerows(result)

	with open('result.pickle', 'wb') as f:
		pickle.dump(result, f)


def get_total_size(dir_path):
	total = 0
	for root, dirs, files in os.walk(dir_path):
		for file in files:
			file_path = os.path.join(root, file)
			total += os.path.getsize(file_path)
	return total
