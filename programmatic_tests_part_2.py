import eventManager
import event_manager as EM
import filecmp


def assert_test(received_value, expected_value, error_message=None):
    if error_message == None:
        error_message = "(Wrong value was: {})".format(received_value)

    assert received_value == expected_value, error_message


class Tests(object):
    @staticmethod
    def testSegelProvidedTest():
        events_lists = [{"name": "New Year's Eve", "id": 1, "date": EM.dateCreate(30, 12, 2020)}, \
                        {"name": "annual Rock & Metal party", "id": 2, "date": EM.dateCreate(21, 4, 2021)}, \
                        {"name": "Improv", "id": 3, "date": EM.dateCreate(13, 3, 2021)}, \
                        {"name": "Student Festival", "id": 4, "date": EM.dateCreate(13, 5, 2021)}, ]
        em = eventManager.printEventsList(events_lists, "./outputs/3.2.2_test_1.txt")
        for event in events_lists:
            EM.dateDestroy(event["date"])
        EM.destroyEventManager(em)

        assert_test(filecmp.cmp("./outputs/3.2.2_test_1.txt", "./expected_outputs/3.2.2_test_1.txt"), True)


    @staticmethod
    def testsPrintEventsListFunctionsWith2SameEarliestDates():
        events_lists = [{"name": "New Year's Eve", "id": 1, "date": EM.dateCreate(30, 12, 2020)}, \
                        {"name": "annual Rock & Metal party", "id": 2, "date": EM.dateCreate(21, 4, 2021)}, \
                        {"name": "Improv", "id": 3, "date": EM.dateCreate(13, 3, 2009)}, \
                        {"name": "Student Festival", "id": 4, "date": EM.dateCreate(13, 3, 2009)}]
        em = eventManager.printEventsList(events_lists, "./outputs/3.2.2_test_2.txt")
        for event in events_lists:
            EM.dateDestroy(event["date"])
        EM.destroyEventManager(em)

        assert_test(filecmp.cmp("./outputs/3.2.2_test_2.txt", "./expected_outputs/3.2.2_test_2.txt"), True)



TESTS = method_list = [getattr(Tests, func) for func in dir(Tests) if
                       callable(getattr(Tests, func)) and not func.startswith("__")]
