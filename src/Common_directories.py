"""Common file paths for leading to other resources are defined here"""

import os

src_directory = os.path.dirname(os.path.abspath(__file__))
base_project_directory = os.path.split(src_directory)[0]
test_directory = os.path.join(base_project_directory, "test")
test_files_directory = os.path.join(test_directory, "test_files")
res_directory = os.path.join(base_project_directory, "res")
