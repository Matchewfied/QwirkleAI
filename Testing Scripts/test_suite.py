from typing import Callable, Any

SUCCESS, FAILURE, ERROR, DNR = 0, 1, 2, 4


class Test:
    def __init__(self, name: str, desc: str, test_fn: Callable[..., Any], exceptions: tuple = ()):
        self.name = name
        self.desc = desc
        self.test_fn = test_fn
        self.exceptions = exceptions

    def get_name(self):
        return self.name

    def get_desc(self):
        return self.desc

    def display_name(self) -> None:
        print(self.name)

    def display_description(self) -> None:
        print(self.desc)

    def execute_test(self, *args, **kwargs) -> tuple:
        # If specific errors have been given, use try and except
        if not self.exceptions:
            result = self.test_fn(*args, **kwargs)
        else:
            try:
                result = self.test_fn(*args, **kwargs)
            except self.exceptions as e:
                result = (ERROR, e)

        return result


class TestSuite:

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.test_deck = {}
        self.context_data = {}
        self.current_context = None

    def process_context(self, context):
        complete_test_data = self.context_data[context]
        num_passed, num_failed, num_errored, num_dnr = 0, 0, 0, 0

        for idx, test_data in enumerate(complete_test_data):
            name, args, kwargs, result = test_data["name"], test_data["args"], test_data["kwargs"], test_data["result"]
            status_code, status_msg = result

            if status_code == 0:
                status = "[SUCCESS]"
                num_passed += 1
            elif status_code == 1:
                status = "[FAILURE]"
                num_failed += 1
            elif status_code == 2:
                status = "[ERROR]"
                num_errored += 1
            else:
                status = "[DNR]"
                num_dnr += 1

            results_str = status + " " + name + ": " + status_msg
            print(results_str)

        total = num_passed + num_failed + num_errored + num_dnr


    def display_stats(self):
        for context in self.context_data:
            self.process_context(context)

    def _run_test(self, test_name, *args, **kwargs) -> None:
        context = self.current_context
        if context is None:
            print("Current context is None. Please begin a context.")
            result = (DNR, "Context not provided.")
        elif test_name in self.test_deck:
            test = self.test_deck[test_name]
            if self.verbose:
                test.display_name()
                test.display_description()
            result = test.execute_test(*args, **kwargs)
        else:
            print("Test + " + test_name + " does not exist.")
            result = (DNR, "Test did not run.")

        test_data = {"name": test_name, "args": args, "kwargs": kwargs, "result": result}
        self.context_data[context].append(test_data)

    def _begin_context(self, name: str) -> None:
        if self.current_context is not None:
            print("Already in context named " + self.current_context)
            return
        if name in self.context_data:
            print("Please provide a name that is distinct from a previous context")
            return
        self.current_context = name
        self.context_data[name] = []

    def _end_context(self):
        self.current_context = None

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



