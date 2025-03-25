from deck import Deck

def main():
    starter_deck = [i for i in range(14)]
    deck = Deck(starter_deck, debug=True)
    deck.dg_display_deck()




if __name__ == "__main__":
    main()