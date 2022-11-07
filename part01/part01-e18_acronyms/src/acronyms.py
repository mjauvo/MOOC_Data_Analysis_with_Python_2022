#!/usr/bin/env python3

# Takes a string as a parameter and returns a list of acronyms, ie. words
# that have a length at least two, and all their characters are in uppercase.
def acronyms(s):
    cleaned_up_and_splitted = s.strip().replace(")", "").replace("(", "").replace(",", "").replace(".", "").split()
    acronym_list = []

    for word in cleaned_up_and_splitted:
        if len(word) > 1 and word.isupper():
            acronym_list.append(word)

    return acronym_list

def main():
    s = "For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."
    print(acronyms(s))


if __name__ == "__main__":
    main()
