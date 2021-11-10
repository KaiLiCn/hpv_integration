import pandas as pd


def inergrate_data(annotation_file, insertion_file):
    annotation_data = pd.read_csv(annotation_file)
    insertion_data = pd.read_csv(insertion_file)

    return annotation_data, insertion_data
