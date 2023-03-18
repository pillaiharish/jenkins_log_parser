# jenkins_log_parser
jenkins console output parser which stores testcase pass fail in html report

The file test_log_generator.py is used to generate testruns.log file which contains dummy jenkins logs after a build is executed on jenkins. The parser logic for jenkins logs is written in file test_run_parser.py which outputs the data in a json object. This json object is used to create a report.html using jinja2. The jinja2 html report logic goes in report_json_to_html.py file. 


(.venv) root:jenkins_log_parser harishkumar$ git clone git@github.com:pillaiharish/jenkins_log_parser.git


(.venv) root:jenkins_log_parser harishkumar$ cd jenkins_log_parser/


(.venv) root:jenkins_log_parser harishkumar$ pyenv exec python -m venv .venv


(.venv) root:jenkins_log_parser harishkumar$ source .venv/bin/activate


(.venv) root:jenkins_log_parser harishkumar$ pip install requirements.txt


(.venv) root:jenkins_log_parser harishkumar$ python test_log_generator.py 


(.venv) root:jenkins_log_parser harishkumar$ python report_json_to_html.py
INFO:root:Total test cases: 60
INFO:root: HTML report generated successfully...

![newmov](https://user-images.githubusercontent.com/12826131/226104890-7b84a7e0-5930-400f-a0e8-239f2e223259.gif)



#https://user-images.githubusercontent.com/12826131/226104639-e4f3b5cb-3384-49f4-810d-30a63932f379.mov


