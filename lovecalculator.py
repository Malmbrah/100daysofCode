def calculate_love_score(name1, name2):
    the_list_of_names = [name1.upper(), name2.upper()]
    string_true = "TRUE"
    string_love = "LOVE"
    the_char_of_the_names = []
    matched_chars_true = []
    matched_chars_love = []
   
    #Har lagt navnene inn i en liste, så bryter opp den og legger hver bokstav i egen liste
    for names in the_list_of_names:
        for letter in names:
            the_char_of_the_names.append(letter)
   
    #Går gjennom bokstav-listen og måler den opp mot "TRUE" og lagrer det i en egen liste
    for name_char in the_char_of_the_names:
        for char_of_string_true in string_true:
            if name_char == char_of_string_true:
                matched_chars_true.append(char_of_string_true)
   
    #Går gjennom bokstav-listen og måler den opp mot "LOVE" og lagrer det i en egen liste
    for name_char in the_char_of_the_names:
        for char_of_string_love in string_love:
            if name_char == char_of_string_love:
                matched_chars_love.append(char_of_string_love)
     
    print(str(len(matched_chars_true)) + str(len(matched_chars_love)))
   
               
       
calculate_love_score(name1 = "Jonathan Malmberg", name2 = "Live Tronstad")