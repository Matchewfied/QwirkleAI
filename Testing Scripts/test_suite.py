from typing import Callable, Any


class Test:
    def __init__(self, name: str, desc: str, test_fn: Callable[..., Any]):
        self.name = name
        self.desc = desc
        self.test_fn = test_fn

    def get_name(self):
        return self.name

    def get_dec(self):
        return self.desc

    def display_name(self) -> None:
        print(self.name)

    def display_description(self) -> None:
        print(self.desc)

    def execute_test(self, *args, **kwargs) -> None:
        self.test_fn(*args, **kwargs)


class TestSuite:

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.test_deck = {}

    def run_test(self, test_name, *args, **kwargs):
        if
        if test_name in self.test_deck:
            self.test_deck[test_name].execute_test(*args, **kwargs)
        else:
            print("Test + " + test_name + " does not exist")

    def run_all_tests(self):

    def _set_verbose(self, verbose: bool) -> None:
        self.verbose = verbose
    def _add_test(self, test: Test) -> None:
        name = test.get_name()
        if name in self.test_deck:
            print("Warning: A test by " + str(test.name) + " already existed. It was overwritten.")
        self.test_deck[name] = test

    def _remove_test(self, test_name: str) -> None:
        if test_name in self.test_deck:
            del self.test_deck[test_name]



