import json
from urllib.parse import quote

from tests.test_create_booking import test_data_json


def data_to_url(data: dict, prefix='', wrapper='{}'):

    url_components = list()
    for key, value in data.items():
        wrapped_key = wrapper.format(key)
        prefixed_key = quote(prefix + wrapped_key)
        # prefixed_key = prefix + wrapped_key
        if isinstance(value, dict) is False:
            url_components.append(f"{prefixed_key}={value}")
        else:
            url_components.append(f"{data_to_url(value, prefixed_key, '[{}]')}")
    return "&".join(url_components)

if __name__ == '__main__':
    data_ = json.load(open(test_data_json, 'r'))
    print(data_to_url(data_))
