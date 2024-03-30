# <h1>API Automation using Python Pytest<h1>
- This is generic API Automation framework using Python Pytest.

## <h2>Setup:<h2>
- Download and install Python3 from [here](https://www.python.org/downloads/) (Ignore the step if you already have python installed)
- Clone this repo, navigate to API-Testing-Python-Pytest folder.
- Execute requirements.txt file to install all the dependent python libraries using following command and make it pass without any error: pip install -r requirements.txt

## <h2>Running the tests:<h2>
- Run below command to execute all the tests. This will generate log file (with name: log-<YYMMDD_HHMMSS>.log) at current location.
pytest -vs Test\test_requests.py
- Run below command to execute and generate pytest html report: 
pytest -vs --capture sys Test\test_requests.py --html=report.html
