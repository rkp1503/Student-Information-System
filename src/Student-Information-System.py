"""
Author: Rayla Kurosaki

GitHub Username: RaylaKurosaki1503

File: Student-Information-System.py
"""

import os
import sys

from constructors.Student import Student
from phases import phase1
from phases import phase2
from phases import phase3
from phases import phase4


def get_path_to_excel_file(path: str) -> str:
    if not (os.path.exists(path)):
        raise Exception(f"The path '{path}' does not exist.")
    if not path.endswith(".xlsx"):
        file: str = path.split('\\')[-1]
        raise Exception(f"The file '{file}' is not an Excel file.")
    return path


if __name__ == '__main__':
    student: Student = Student()
    path_to_excel_file: str = get_path_to_excel_file(sys.argv[1])
    phase1.add_data(student, path_to_excel_file)
    phase2.modify_data(student, path_to_excel_file)
    phase3.perform_computations(student, path_to_excel_file)
    phase4.print_data(student)
    pass