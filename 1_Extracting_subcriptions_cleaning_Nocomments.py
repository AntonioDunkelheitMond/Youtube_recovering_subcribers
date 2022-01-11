#CREADO POR ANTONIO JUSTO
Lista = []
bandera = 0
bandera_no_descri_no_abonne = 0
# number of subcriptions
i = 1
with open("Kanalliste.txt", "r", encoding="UTF-8") as rf:
    with open("Kanalliste_nuevo.txt", "w", encoding="UTF-8") as wf:
        # we star looping throught all the lines in the file
        for x in rf:
            if not x.isspace():
                # the key flag abonnente is not present in some files so the flag
                # wont work thus we have to use other trick
                long = len(x)

                # this is our flag we assume that all subcriptions are followed by
                # a line with abonnente on it, but that is not true. We also use
                # the extructure number of videos: 207 Videos in which case there
                # is no abonnenten bc the subcriber made the subcriptions invisible
                if ("Abonnenten" in x) or ("Videos" in x and long <= 14):
                    # Since we entered here we assume that there a description
                    # next, thus we trigger this flag to 1 in orther to bypass
                    # the description
                    bandera = 1
                    # with this flag we indicate that we have entered this if,
                    # used for the next iteration
                    bandera_no_descri_no_abonne = 1
                    continue

                elif bandera == 1 and long > 60:
                    # iF WE ENTER HERE THUS THERE is A DESCRIPTION THUS THE NEXT
                    # LINE
                    # IS GUARATEED TO BE A SUBCRIPTION NAME THUS WE CHANGE THE
                    # FLAG TO ZERO, PREPARING TO WRITE THE NEXT LINE OF THE LOOP
                    bandera = 0  # we are ready to write
                    bandera_no_descri_no_abonne = 0
                    continue

                elif (bandera == 1 and long < 60 and
                      bandera_no_descri_no_abonne == 1):

                    # Esto está para pillar los nombre sin descripción
                    Lista.append(x)

                    bandera = 1
                    # We reset this flag
                    bandera_no_descri_no_abonne = 0
                    # We increment the number of subcriptions
                    i += 1
                    continue

                elif (bandera == 0 and long < 200):

                    Lista.append(x)

                    bandera = 1
                    # We also reset the flag here bc there is a possibility that
                    # there is no description
                    bandera_no_descri_no_abonne = 0
                    i += 1
                    continue

                else:
                    Lista.append(x)
                    # Since this is the weird case where we have to subcriptions
                    # names one after the other
                    bandera = 0
                    i += 1
                    bandera_no_descri_no_abonne = 0
                    continue

        # Number of subcriptions stored
        print(f"El numero de subcripciones son: {i} subcripciones")
        for y in Lista:
            wf.write(y)
            print(f"The number of characters are: {len(y)}")
            print(str(y), end="")

        # Number of subcriptions stored
        print(f"El numero de subcripciones son: {i} subcripciones")