## restful-booker practice project

This project aims to be a practice of designing and executing API test cases.
The service exposing an API can be found here: https://restful-booker.herokuapp.com/apidoc/index.html

### Setup

Firstly, make a virtual environment:
`python -m venv your_venv`

Secondly, install dependencies:
`pip install -r requirements.txt`

The packages you just installed are contained within `your_venv` virtual environment.

Everything should be set up to run tests:
`pytest tests`

**Note:** There are 7 tests out of 12 expected to fail every test run. Each of these failing cases has a documented cause in the comments, so make sure to read them beforehand.

#### Other ideas (realizable or not):

- (tests) concurrent requests (load/performance, using `locust` or other framework)
- (tests) parsing content to check if it matches our `Accept` header (we can't entirely rely `Content-Type` header from response)
- (tests) checking types of fields from received content (i.e. if API responded with a `null` instead of `int`)
- (misc) logging attached to requests and responses, to analyze flow and not having to run debug mode in IDE
- (misc) reporting: `pytest-html`, `allure` (if one isn't allergic to Java)