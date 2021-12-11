import pandas as pd
import numpy as np
import logging


class LoadData:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self, delimiter=","):
        """ 
        """
        logging.info("Loading data from {}".format(self.file_path))
        try:
            extension_mappings = {
                "csv": pd.read_csv,
                "xlsx": pd.read_excel,
                "xls": pd.read_excel,
                "txt": pd.read_csv,
                "tsv": pd.read_csv,
            }
            special_delimiters = {
                "txt": "\t",
                "tsv": "\t",
            }
            ext = self.file_path.split(".")[-1]
            if ext in extension_mappings:
                read_func = extension_mappings[ext]
                sep = (
                    special_delimiters[ext] if ext in special_delimiters else delimiter
                )
                return read_func(self.file_path, sep=sep)
            else:
                raise Exception(f"File Type '.{ext}' not supported ")

        except Exception as e:
            logging.error("Error loading data: {}".format(e))
            raise e

    def _check_data(self):
        logging.info("Checking data")
        try:
            data = self.load_data()
            if data.shape[0] < 5:
                raise Exception("Data is too small")

            if data.shape[1] < 1:
                raise Exception("Data is too small")
        except Exception as e:
            logging.error("Error checking data: {}".format(e))
            raise e

    def _give_column_names(self):
        logging.info("Giving column names")
        try:
            # check if column names are given
            data = self.load_data()
            if data.columns.size == 0:
                # give default column names
                data.columns = ["col" + str(i) for i in range(1, data.shape[1] + 1)]
            return data

        except Exception as e:
            logging.error("Error giving column names: {}".format(e))
            raise e

    def ImportFile(self):
        try:
            data = self.load_data()
            self._check_data()
            data = self._give_column_names()

            return data
        except Exception as e:
            logging.error("Error importing file: {}".format(e))
            raise e
