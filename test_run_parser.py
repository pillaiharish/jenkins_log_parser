import re
import json

import logging
 
logging.getLogger().setLevel(logging.INFO)

record_buffer = []
dictionary2 = dict()
dictionary2["test_cases"] = []

def test_logs_parser(FILE_NAME): 

    with open(FILE_NAME,"r") as f:
        tc_flag,dns_flag,pass_flag,fail_flag= 0,0,0,0
        for num,line in enumerate(f):
            tc_flag = 1
            if "suite" in line:
                dictionary2["suite_name"] = (line.split("")[1]).split("")[0]
            if ("  TC" in line or "TESTCASE" in line) and tc_flag>0:
                tc_name = ""
                if "  TC" in line:
                    tc_name = "TC"+line.split("  TC")[1].strip("\n")
                elif "TESTCASE" in line:  
                    tc_name = line.split("TESTCASE")[1]
                dictionary2["test_cases"].append({"testcase":tc_name,"dnsrequests":dns_flag,"pass":pass_flag,"fail":fail_flag})
                tc_flag,dns_flag,pass_flag,fail_flag= 0,0,0,0
        
            if "=> DNSREQUEST" in line:
                dns_flag += 1
            if "=> STEP PASSED" in line:
                pass_flag += 1
            if "=> STEP FAILED" in line:
                fail_flag += 1
           
        logging.info("Total test cases: " + str(len(dictionary2["test_cases"])))
        json_object = json.dumps(dictionary2, indent = 4)

        return json_object

