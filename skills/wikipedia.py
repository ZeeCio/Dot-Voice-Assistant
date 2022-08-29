from engine import DOT

dot = DOT()


def wiki_who_is(text):
    print("Searching...")
    query = text.split()
    # looping through the command for "who", "is"
    # and first and last name of searched person
    for i in range(0, len(query)):
        if i + 3 <= len(query) - 1 and query[i].lower() == "who" and query[i + 1].lower() == "is":
            return query[i + 2] + " " + query[i + 3]
