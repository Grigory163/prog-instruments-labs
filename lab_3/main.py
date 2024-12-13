import re
import logging
from typing import Hashable

import pandas as pd

from checksum import calculate_checksum, serialize_result
from config import PATTERNS, CSV_PATH


def read_csv(path: str) -> pd.DataFrame:
    """
    Reading input .csv file into dataframe object
    :param path: (str) .csv file path
    :return raw_data: (pd.DataFrame) output dataframe object
    """
    try:
        raw_data: pd.DataFrame = pd.read_csv(path, sep=";", encoding="utf-16")
        return raw_data
    except Exception as e:
        logging.error(f'Can not read .csv file - {e}')


def check_row(row: pd.Series) -> bool:
    """
    Checking row valid using regular expressions
    :param row: (pd.Series) input row
    :return: (bool) True - valid, False - not valid
    """
    return all(re.match(PATTERNS[key], str(row[key])) for key in PATTERNS if key in row)


def good_row_indices(raw_data: pd.DataFrame) -> list[Hashable]:
    """
    Returning list of indices of invalid rows
    :param raw_data: (pd.DataFrame) input data from .csv file
    :return: (list[Hashable]) list of indices of invalid rows
    """
    return [index for index, row in raw_data.iterrows() if not check_row(row)]


if __name__ == "__main__":
    serialize_result(15, calculate_checksum(good_row_indices(read_csv(CSV_PATH))))

