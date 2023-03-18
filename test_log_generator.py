import numpy as np
import logging
from faker import Faker 
fake = Faker() 
import random
import os

# remove the file before it is created or the logging lib will append to existing
try:
    os.remove("testruns.log")
except FileNotFoundError :
    print("File not found")

logging.basicConfig(filename="testruns.log",format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

def test_log_generate():
    word_list = ["Testcase","test","verify","Validate","Check","Assert"] 
    logging.info("SUITE NAME: DEV_TEST_SUITE_01")
    for j in range(10):
        logging.info(f"TESTCASE ############ FEATURE0{j} "+fake.sentence(ext_word_list = word_list))
        pass_fail_arry_1 = np.random.randint(2, size=10)
        if  pass_fail_arry_1[j]:
            logging.info("=> STEP PASSED")
        else:
            logging.info("=> STEP FAILED")
        for i in range(0, 5): 
            logging.info(f"TC0{i} "+fake.sentence(ext_word_list = word_list)) 
            pass_fail_arry_2 = np.random.randint(2, size=3)
            for k in range(3):
                logging.info("=> DNSREQUEST")
                if  pass_fail_arry_2[k]:
                    logging.info("=> STEP PASSED")
                else:
                    logging.info("=> STEP FAILED")

test_log_generate()   
