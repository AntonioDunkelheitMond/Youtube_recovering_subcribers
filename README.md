# Youtube_recovering_subcribers
Automatic Youtube subcription. These two python files allow a new user to recover or move to anew gmail account while still being able to recover the subcriptions list. The first python file allow you to obtain a clean version with only the names of the channels you where subcribed to. The second file will allow you to automatically parse through the file and check if you are subbed to it and if not subribe and move to the next one. This code in fact works in three languages, Spanish, ENlgish and German. So you have to make sure that when the youtube browser is open by the bot it has one of these three languagues as explained in point 4.1º

Suscripción automatica de Youtube. Estos dos códigos te permiten recuperar tus subscriptores al cambiar de cuenta de youtube. El primer archivo .py te permiten limpiar y extraer los nombres de tus suscripciones y el segundo hace uso de Selenium para poder automaticamente  buscar y comprobar cada una de los nombres extraidos con el primer archivo y ver si estas suscrito. He implementado el código para tres idomas, Español, Alemán e Ingles. /La explicación se encuentra únicamente en Ingles, en el futuro añadiré la versión traducida a Español. 

DISCLAIMER: The code it is not perfect, and there is a case where if a channel with the exact same name appear in the search results it wont sub to it, this is due to the way in which the code decides if you are subbed or not already to it. Currently i am working on a better way of doing it. Altough it is possible to subs to those manually later on, or opening in a new tab if you are quickly enough, this wont be a problem for the program.


PASOS:

0º Make sure you pip install the following packages installed: 
  pip install undetected-chromedriver
  pip install selenium
  pip install pathlib
  
1º Go to: https://www.youtube.com/feed/channels

2º Scroll all the way down selecting all the text and the subcriptions. This will copy the name of the youtuber, its description, numbers of subcribers etc.

3º Paste the copied text into the file: Kanalliste.txt, and close it.

4º Open the python file: 1_Extracting_subcriptions_cleaning_Nocomments and run it. This will clean and leave mostly just the name of the channels your are subcribed to. It is not perfect so fails to remove some very short descriptions, but it doesn't really matter. Once it has ran, a new file named Kanalliste_nuevo.txt will appear on the current directory. In this file will appear all the names ready to be use by the next python file. THIS CODE WILL ONLY BE NEEDED TO BE RUN ONCE, ONCE YOU HAVE EXTRACTED THE NAMES AND YOU HAVE MADE SURE THAT THE CODE RAN CORRECTLY, DONT RUN IT AGAIN.

4.1º For the next steps it is worth noting that you have to open the browser in one of the three languagues, Spanish, English or Deutsch. If that is not the case, you can go to the second file 2_Subbing_bot_youtube_v14_GITHUB to the line 12, an in the sleep comand put 10 instead of 1, this will give you 10 seconds, so when it runs, you will have to change the langugue of the youtube pop up righ on the top right corner of the pop up. This will allow you to run the code correctly. 

5º Open the python file: 2_Subbing_bot_youtube_v14_GITHUB, and run it. Here the program will ask you to provide your gmail account and password so it can do the subbing. In theory there is a limitation of only 75 sub per day by youtube. Altough it is possible to sub to more channels if your run it in intervals of a couple hours. Once you have ran the code, several files will be created:

+++file_subs_remaining_temp.txt = incase of the program terminating or failing to end correctly this file will provide a backup of the a current updated list of the remaining                                       subcriptions, this file will be really helpful.

+++Sub_failures.txt = here will be stored the channels that for one reason or another wasnt subbed, or better said, didnt trigger the part of the code in charge of executing                            the action of subbing. Also, the rubbish that wasn't able to clean like wrong names, or very short descriptions will also appear here.
   
+++Kanalliste_nuevo_remaining.txt = This will be saved once the code subbed to 75 channels, in case of early termination it will be blanck or it will have the version of the 
                                previuos susccesful run. It is worth noting, that after correctly executing the 75 subs, the Kanalliste_nuevo.txt will be overwritte with this                                   file.
                                
+++Kanalliste_nuevo.txt = this will be the updated version ready to be used. It should contain the same subs than the Kanalliste_nuevo_remaining.txt once it ran sussccesfully-
   
   6º Once 75 subcriptions were reach, you need to wait a couple hour so the youtube "counter" allows you to sub to a new batch since currently youtube limit the amount of daily subcriptions. After subbing it will refresh the page so you can see if the subcription wast permitted or you have already surpass the daily limit, in which case it wont show you the "Subcribed gray button".
   
   
   
