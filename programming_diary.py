from interactions_with_db import InteractionsWithDb


class ProgrammingDiary:
    @classmethod
    def welcome(cls):
        print("\n\nWelcome to the programming diary!\n")

    @classmethod
    def users_selection(cls):
        print(
            "\nPlease select one of the following options:\n\n1 - Add new entry for today.\n2 - View entries.\n3 - Exit."
        )

        users_input = input("\nYour selection: ")

        return cls.value_selected(users_input)

    @classmethod
    def what_next(cls):
        users_input = input(
            "\nWhat do you want to do next?\n1 - See the menu again\n2 - Exit.\n\nSelect one of the above options:"
        )
        if users_input == "1":
            return cls.users_selection()
        if users_input == "2":
            cls.goodbye()
        else:
            print("\n\nYou've entered an invalid value. Please try again.\n")
            return cls.what_next()

    @classmethod
    def value_selected(cls, users_input):
        if users_input == "1":
            new_entry = input(
                "\nPlease add a new note by typing it after colon and then press Enter to save it do the database: "
            )
            try:
                InteractionsWithDb.insert_to_db(new_entry)
            except Exception as e:
                print(e)
                return
            print("\nThe entry was added to the database.")
            return cls.what_next()

        elif users_input == "2":
            all_entries = InteractionsWithDb.select_all_from_db()
            for entry in all_entries:
                print(str(entry)[1:-1])
            cls.what_next()
        elif users_input == "3":
            cls.goodbye()
        else:
            print("\n\nYou've entered an invalid value. Please try again.\n")
            return cls.users_selection()

    @classmethod
    def goodbye(cls):
        print("\nGoodbye, have a nice day!\n")
        return