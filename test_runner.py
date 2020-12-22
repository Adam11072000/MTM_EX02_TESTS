import traceback
import filecmp
import os

import programmatic_tests_part_1 as tests1
import programmatic_tests_part_2 as tests2
import eventManager

INPUTS_PATH = "./inputs/"
EXPECTED_OUTPUTS_PATH = "./expected_outputs/"
OUTPUTS_PATH = "./outputs/"


def does_matching_output_exists(file_name):
    return os.path.exists(EXPECTED_OUTPUTS_PATH + file_name)


def get_valid_input_names_to_run():
    raw_files = os.listdir(INPUTS_PATH)
    return filter(does_matching_output_exists, raw_files)


def did_test_succeed(input_name):
    return filecmp.cmp(EXPECTED_OUTPUTS_PATH + input_name, OUTPUTS_PATH + input_name)


def print_input_file_test_failure(input_name):
    print("Expected: <a href='/ex02/staging/{STAGING_ID}/expected_outputs/" + input_name + "'>expected_" + input_name + "</a>, but got instead: <a href='/ex02/staging/{STAGING_ID}/outputs/" + input_name + "'>{}</a>".format(input_name))

def print_test_error(err):
    print("Test encountered an exception. Exception details:\n{}".format(traceback.format_exc()).replace(" ", "&nbsp;"))

def run_input_file_test(input_name):
    eventManager.fileCorrect(INPUTS_PATH + input_name, OUTPUTS_PATH + input_name)
    return did_test_succeed(input_name)

def run_test(test):
    test_result = True
    if type(test) == str:
        input_name = test
        print("+ Running test: <b>{}</b> ... ".format(input_name))
        try:
            test_result = run_input_file_test(input_name)
        except Exception as err:
            print_test_error(err)
            test_result = False

        if not test_result:
            print_input_file_test_failure(input_name)
    else:
        try:
            pass
        except AssertionError as err:
            pass
        except Exception as err:
            pass

    if test_result:
        print("[OK]")
    else:
        print("[Failed]")

    print("<hr>", end="")


if __name__ == "__main__":
    input_names = get_valid_input_names_to_run()

    if not os.path.exists(OUTPUTS_PATH):
        os.mkdir(OUTPUTS_PATH)
    for input_path in input_names:
        run_test(input_path)

    # TODO: python tests
    for test in tests1.TESTS:
        pass
