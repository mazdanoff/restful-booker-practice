import os

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
tests_path = os.path.join(project_path, "tests")
test_data_path = os.path.join(tests_path, "test_data")
test_data_json = os.path.join(test_data_path, "create_booking.json")
test_data_xml = os.path.join(test_data_path, "create_booking.xml")
test_data_url = os.path.join(test_data_path, "create_booking.txt")
