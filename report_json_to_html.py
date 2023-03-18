import json
from jinja2 import Environment, FileSystemLoader
import logging
from test_run_parser import test_logs_parser
import os

FILE_NAME = "testruns.log"

logging.getLogger().setLevel(logging.INFO)

def html_renderer(data):
    data = json.loads(data)

    # Define the Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))

    # Load the template file
    template = env.get_template('report.html')

    # Render the template with the JSON data
    html_output = template.render(data=data)

    # Write the HTML output to a file
    with open('report.html', 'w') as html_file:
        try:
            html_file.write(html_output) 
            logging.info(" HTML report generated successfully...")
        except:
            logging.error(" HTML report generation Failed")

if __name__ == "__main__":
    data = test_logs_parser(FILE_NAME)
    html_renderer(data)
