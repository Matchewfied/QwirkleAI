from typing import Callable, Any

SUCCESS, FAILURE, ERROR, DNR = 0, 1, 2, 4

ALL_PASSED_PHRASES = ["Wooh!", "That's what I'm talking about!"]


class Test:
    def __init__(self, name: str, desc: str, test_fn: Callable[..., Any], exceptions: tuple = (), *args, **kwargs):
        self.name = name
        self.desc = desc
        self.test_fn = test_fn
        self.exceptions = exceptions
        self.args = args
        self.kwargs = kwargs

    def get_name(self):
        return self.name

    def get_desc(self):
        return self.desc

    def get_args(self):
        return self.args

    def get_kwargs(self):
        return self.kwargs

    def display_name(self) -> None:
        print(self.name)

    def display_description(self) -> None:
        print(self.desc)

    def execute_test(self) -> tuple:
        # If specific errors have been given, use try and except
        if not self.exceptions:
            status, status_msg, after_state = self.test_fn(self.args, self.kwargs)
        else:
            try:
                status, status_msg, after_state = self.test_fn(self.args, self.kwargs)
            except self.exceptions as e:
                status, status_msg, after_state = ERROR, e, ""

        return status, status_msg, after_state


class TestSuite:

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.test_deck = {}
        self.context_data = {}
        self.current_context = None

    def process_context(self, context: str, display_failure_states=False) -> None:
        complete_test_data = self.context_data[context]
        num_passed, num_failed, num_errored, num_dnr = 0, 0, 0, 0
        failure_states = []

        for idx, test_data in enumerate(complete_test_data):
            name, args, kwargs, result = test_data["name"], test_data["args"], test_data["kwargs"], test_data["result"]
            status_code, status_msg, after_state = result

            if status_code == 0:
                status = "[SUCCESS]"
                num_passed += 1
            elif status_code == 1:
                status = "[FAILURE]"
                num_failed += 1
                if display_failure_states:
                    failure_states.append((name, args, kwargs, after_state))
            elif status_code == 2:
                status = "[ERROR]"
                num_errored += 1
            else:
                status = "[DNR]"
                num_dnr += 1

            print(f"{status} {name}: {status_msg}")

        total = num_passed + num_failed + num_errored + num_dnr

        print(f"{context} Results:")
        if display_failure_states and len(failure_states) > 0:
            for failure in failure_states:
                name, args, kwargs, after_state = failure
                print(f"Displaying after state for failed test {name}")
                print(after_state)
                print(f"args: {args}")
                print(f"kwargs: {kwargs}")
        print(f"Ran {total} tests.")
        if num_passed == total:
            print(f"All tests passed!")
        else:
            print(f"{num_passed} tests passed.")
            print(f"{num_failed} tests failed.")
            print(f"{num_errored} tests threw an error.")
            print(f"{num_dnr} tests did not run.")

    def display_context_results(self, context: str, display_failure_states: bool = False) -> None:
        self.process_context(context, display_failure_states=display_failure_states)

    def display_all_context_results(self, display_failure_states: bool = False) -> None:
        for context in self.context_data:
            self.display_context_results(context, display_failure_states=display_failure_states)

    def run_test_(self, test_name) -> None:
        context = self.current_context
        args, kwargs = "", ""
        if context is None:
            result = (DNR, "Context not provided.", "")
        elif test_name in self.test_deck:
            test = self.test_deck[test_name]
            if self.verbose:
                test.display_name()
                test.display_description()
            args = test.get_args()
            kwargs = test.get_kwargs()
            result = test.execute_test()
        else:
            result = (DNR, "Test did not run.", "")

        test_data = {"name": test_name, "result": result, "args": args, "kwargs": kwargs}
        self.context_data[context].append(test_data)

    def begin_context_(self, name: str = 'default') -> None:
        if self.current_context is not None:
            print(f"Already in context named {self.current_context}")
            return
        if name in self.context_data:
            print(f"{name} is a former context. Please provide a name that is distinct from a previous context.")
            return
        self.current_context = name
        self.context_data[name] = []

    def end_context_(self):
        self.current_context = None

    def set_verbose_(self, verbose: bool) -> None:
        self.verbose = verbose

    def add_test_(self, test: Test) -> None:
        name = test.get_name()
        if name in self.test_deck:
            print(f"Warning: A test named {name} already existed. It was overwritten.")
        self.test_deck[name] = test

    def create_and_add_test_(self, name: str, desc: str, test_fn: Callable[..., Any], exceptions: tuple = (), *args, **kwargs) -> None:
        test = Test(name, desc, test_fn, exceptions, args, kwargs)
        self.add_test_(test)

    def cat_(self, name: str, desc: str, test_fn: Callable[..., Any], exceptions: tuple = (), *args, **kwargs):
        self.create_and_add_test_(name, desc, test_fn, exceptions, args, kwargs)

    def remove_test_(self, test_name: str) -> None:
        if test_name in self.test_deck:
            del self.test_deck[test_name]