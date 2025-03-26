from deck import Deck
from test_suite import TestSuite
import copy
SUCCESS, FAILURE, ERROR, DNR = 0, 1, 2, 4

def main():
    starter_deck = [i for i in range(14)]
    deck = Deck(starter_deck, debug=True)

    ts = TestSuite()
    ts.cat_('test-initial-contents', 'Checks that deck initializes correctly', verify_contents, (), deck.dg_listify_deck(), starter_deck)
    ts.cat_('test-draw', 'Checks that the draw method works correctly', test_draw_1, (), deck)
    ts.cat_('test-place-undoes-draw', 'Checks that place undoes the work of draw', test_draw_and_place, (), deck)
    ts.begin_context_()
    ts.run_test_('test-initial-contents')
    ts.run_test_('test-draw')
    ts.run_test_('test-place-undoes-draw')
    ts.display_context_results(display_failure_states=True)
    ts.end_context_()


###############################
# Test Functions
def test_draw_and_place(deck: Deck) -> tuple:
    status, status_msg, after_state = SUCCESS, "", ""
    deck_cp = copy.deepcopy(deck)
    expected_contents = deck_cp.dg_listify_deck()
    drawn = deck_cp.draw_(10)
    deck_cp.place_(drawn, flipped=True)

    deck_contents = deck_cp.dg_listify_deck()
    return verify_contents(deck_contents, expected_contents)



def test_draw_1(deck: Deck) -> tuple:
    status, status_msg, after_state = SUCCESS, "", ""
    deck_cp = copy.deepcopy(deck)
    drawn = deck_cp.draw_(1)
    card = drawn[0]
    size = deck_cp.get_size()
    if card != 13:
        status = FAILURE
        after_state = drawn
        status_msg = f"Drawn card {card} is not {13}"
        return status, after_state, status_msg
    elif size != 13:
        status = FAILURE
        after_state = str(deck_cp)
        status_msg = f"Size of deck is {size} when it should be {13}"
        return status, after_state, status_msg


    drawn = deck_cp.draw_(2)
    size = deck_cp.get_size()
    if drawn != [12, 11]:
        status = FAILURE
        after_state = drawn
        status_msg = f"Drawn cards {drawn} are not {[12, 11]}"
        return status, after_state, status_msg
    elif size != 11:
        status = FAILURE
        after_state = str(deck_cp)
        status_msg = f"Size of deck is {size} when it should be {11}"
        return status, after_state, status_msg

    return status, status_msg, after_state


def verify_contents(deck_contents: list, expected_contents: list) -> tuple:
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