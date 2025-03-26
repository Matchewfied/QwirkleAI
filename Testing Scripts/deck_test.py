from deck import Deck
from test_suite import Test, TestSuite
SUCCESS, FAILURE, ERROR, DNR = 0, 1, 2, 4

def main():
    starter_deck = [i for i in range(14)]
    deck = Deck(starter_deck, debug=True)


    ts = TestSuite()
    ts.cat_()




###############################
# Test Functinos
def verify_contents(*args, **kwargs) -> tuple:
    deck_contents, expected_contents = args[0], args[1]
    status, status_msg, after_state = SUCCESS, "", ""
    if expected_contents != deck_contents:
        status = FAILURE
        after_state = f"deck_contents: {str(deck_contents)}\n" \
                      f"expected_contents: {str(expected_contents)}"
        # Diagnose issue
        if len(expected_contents) != len(deck_contents):
            status_msg = "Lengths of contents do not match."
        else:
            idx = 0
            for i in range(len(expected_contents)):
                if expected_contents[i] != deck_contents[i]:
                    idx = i
                    break
            status_msg = f"First element mismatch at index {idx}. " \
                         f"deck_contents[{idx}] = {deck_contents[idx]} " \
                         f"| expected_contents[{idx}] = {expected_contents[idx]}"

    return status, status_msg, after_state





if __name__ == "__main__":
    main()