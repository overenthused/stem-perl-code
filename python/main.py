class Faculty:
    """
    Object which holds two pandas Series, one which holds the 2014 census data and one which holds
    the 2016 check-in data.
    """
    def __init__(self, c14=None, c16=None):
        self.c14 = c14
        self.c16 = c16


def match_faculty(df1, df2, col1, col2):
    """
    Match strings from a column of one dataframe to a column of another.
    Return a list of Faculty who have matches on both lists.

    :param df1: pandas DataFrame.
    :param df2: pandas DataFrame.
    :param col1: str. Used to choose column in df1
    :param col2: str. Used to choose column in df2
    :return: list of Faculty
    """
    emails_string = ""
    matched_faculty = []
    matches = 0
    dmatches = 0
    for i, email in enumerate(df1[col1]):  # Iterates through every single pair to check for duplicates
        count = 0
        for j, email2 in enumerate(df2[col2]):
            if type(email) == str and type(email2) == str:
                if email.strip().lower() == email2.strip().lower():
                    count += 1
                    if count == 1:
                        matches += 1
                        new_fac = Faculty(c14=df2.iloc[j], c16=df1.iloc[i])
                        matched_faculty.append(new_fac)
                    elif count > 1:
                        dmatches += 1
        if count == 0:
            emails_string = emails_string + email + "\n"  # TODO: Analyze duplicates
    return matched_faculty


def q_map(name, value=None, series=None):
    """
    Maps raw data from a certain variable name to legible or workable outputs.
    :param name: str. Variable name to be mapped
    :param value: str. Optional, value to match.
    :param series: Optional, series to be indexed with name
    :return: Mapped value.
    """
    if series is not None:
        value = series[name]
    if name == "Q37":
        if value == "1":
            return "Assistant Professor"
        elif value == "2":
            return "Associate Professor"
        elif value == "3":
            return "Tenured Professor"
        elif value == "4":
            return "Senior Professor"
        elif value == "5":
            return "Professor, Non-tentured track"
        elif value == "6":
            return "Postdoctoral Associate/Fellow"
        elif value == "7":
            return "Graduate Student"
        elif value == "12":
            return "Other"
        else:
            return "Error: Value Not Found"
