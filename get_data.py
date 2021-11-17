import pandas as pd


def inergrate_data(annotation_file, insertion_file):
    annotation_data = pd.read_csv(annotation_file)
    insertion_data = pd.read_csv(insertion_file)

    insertion_data = insertion_data.drop(insertion_data.columns[0], axis=1).drop_duplicates()

    sample_list_datatable = insertion_data.drop_duplicates(subset=['sample', 'gene'])[['sample', 'gene']]

    return sample_list_datatable, insertion_data
