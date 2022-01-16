# Youtube_recovering_subcribers
Automatic Youtube subcription. These two python files allow a new user to recover or move to anew gmail account while still being able to recover the subcriptions list. The first python file allow you to obtain a clean version with only the names of the channels you where subcribed to. The second file will allow you to automatically parse through the file and check if you are subbed to it and if not subribe and move to the next one. This code in fact works in three languages, Spanish, ENlgish and German. So you have to make sure that when the youtube browser is open by the bot it has one of these three languagues as explained in point 4.1º

Suscripción automatica de Youtube. Estos dos códigos te permiten recuperar tus subscriptores al cambiar de cuenta de youtube. El primer archivo .py te permiten limpiar y extraer los nombres de tus suscripciones y el segundo hace uso de Selenium para poder automaticamente  buscar y comprobar cada una de los nombres extraidos con el primer archivo y ver si estas suscrito. He implementado el código para tres idomas, Español, Alemán e Ingles. Aunque solo tengo la explicacion en 2 de ellos.

DISCLAIMER: The code it is not perfect, and there is a case where if a channel with the exact same name appear in the search results it wont sub to it, this is due to the way in which the code decides if you are subbed or not already to it. Currently i am working on a better way of doing it. Altough it is possible to subs to those manually later on, or opening in a new tab if you are quickly enough, this wont be a problem for the program.

DISCLAIMER: Pido disculptas por las posibles faltas de ortografía en ambos idiomas, las prisas no son buen compañero. Intentaré arreglarlos en el futuro.
            You are going to excuse me from all the possible grammar errors, not only in english but in both languagues, that i hasve made during the writing of this little wiki. I will try to fix them in the future.
            
++++++++++++++++++++++++++++++++++PASOS EN ESPAÑOL:++++++++++++++++++++++++++++++++++++++++++++++++++++

0º Para hacer funcionar ambos códigos necesitas que en tu virtual envrioment tener los siguiente paquetes a instalar con pip:
  pip install undetected-chromedriver
  pip install selenium
  pip install pathlib
1º Accede a tu cuenta y tu lista de suscripciones: https://www.youtube.com/feed/channels

2º Aquí la unica manera que yo he encontrado que me sirve es copìarlo todo, selecciona el nombre de la primera subcrcipcion que te aparezca y empiza con el raton a bajar seleccionando todo (sus descripciones vista etc), todo esto lo quitaremos con el primer código. Que funciona aunque es bastante burdo. 

3º Una vez seleccionadas todas las suscripciones, copia y pegalas a un .txt con el nombre: Kanalliste.txt, ese es el nombre que le dí en su momento y por pereza se ha quedado así, si quieres llamalo como quieras, pero tendrás que modificar el codigo que intentará abrilo para leerlo. o puede utilizar .rglob(*.txt) si deseas que coja el primer archivo aunque esto solo funcionará una vez.

4º Abré el primer archivo, este documento le he quitado los comentarios que puse mientras lo desarrollaba para pdoer ir limpiando y que de esta maneras sea más compacto, aunque basicamente lo que hacer es comprobar la longitud de la linea copiada y si es mas larga que un numero establecido considerado como razonable, alamacenara la linea en un nuevo archivo, de no ser as´ñi la descartá. Esto tiene el problema de que si el nombre d ela sucripción es más largo que ese numero de separación, este sucscripción se perderá, al igualq ue si se da el caso de que la descdipción de la suscripcion es muy corta, esta se almacerá en el archivo finl. Lo cual inrtroduce basura en nuestro .txt ya limpio. Ene l siguiente codigo de alguna manera solvento este problem, aunque cuando hize esta primera parte de este proyecto no conseguí distinguir entre lineas que son el nombre y las que son la descrición y que muy corta, por lo que no se filtran. Por lo que este primer codigo añade basura, y puede hacer perder ciertas suscripciones al final del todo. 

Tras haberlo corrido, se genera un segundo archivo que yo he llamado Kanalliste_nuevo.txt, este te vale y tiene ya la versión "limpia" con las suscripciones. Este primer codigo sólo lo tienes que hacer correr una vez.

4.1º Una consideración antes de pasar con el siguiente código es que se requiere que el driver de google se habra en uno de lso tres idiomas en los que he hecho funcionar este código, y son Español, Ingles y Alemán, para otros idiomas sera solo caso de añadir su condicional al if que toma la decision y crear para ello una variable que alamcene le trozso de string que hacemos apra buscar dentro del codigo fuente.

5º Abre 2_Subbing_bot_youtube_v14_GITHUB, y correlo, el código te pedirá que le des el gmail y contraseña para poder logearse en tu cuenta. Una vez hecho esto procederá ha chear la lista de susbcriciones generadas en el codigo anterior. El número máximo en teoria sond e 75 suscripones seguidas, aunque si dejas un intervalo de un par de horas te permite otro batch. Se generan los siguiente archivos:

+++file_subs_remaining_temp.txt = en caso de que cancele la ejecucion antes de acabar este arhchivo nos sirve de backup del momento antes de cancelarlo, asi evitandonos que la siguiente corrida dle codigo se empieze desde nuevo, por ello copia su contenido y peaglo en Kannaliste_nuevo.txt si se para el codigo.

+++Sub_failures.txt = suscripcioens que no se han podido subcribir por algun motivo u otro, auqi por ejemplo se captura toda esa basura de descipciones etc que no se filtraron, ademas de otras susciciciones que por un motivo u otro no puedieron ejecutarse, por lo que tendrás que despues suscribirte tu manualmente a estas.

+++Kanalliste_nuevo_remaining.txt  =al finalizar, este archivo posee las susbcriciones restantes tras alcanzar las 75. Se recomiendas un intervalode un par de horas de ejecucion de este primer archivo.

+++Kanalliste_nuevo.txt = cversión actualizar del original, que no es mas que una copia de +++Kanalliste_nuevo_remaining.txt tras finalizar correctamente.


6º Tras 75 suscripciones seguidas, tendrás que esperar un par de horas antes de correr el segundo arhivo de nuevo.

7º Alm finalizar todo comprueba Sub_failures.txt para ver entre al basura que suscricpioens no se puedieron suscribir para tu hacerlas manualmente.



+++++++++++++++++++++++++++++STEPS IN ENGLISH:+++++++++++++++++++++++++++++++++++++++++++++

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

+++Sub_failures.txt = here will be stored the channels that for one reason or another werent subbed to, or better said, these names didnt trigger the part of the code in charge of executing the action of subbing. Also, the rubbish that wasn't able to be cleaned (like wrong names, or very short descriptions) with the first python code will also appear in this file here.
   
+++Kanalliste_nuevo_remaining.txt = This will be saved once the code subbed to 75 channels, in case of early termination it will be blanck or it will have the version of the 
                                previuos susccesful run. It is worth noting, that after correctly executing the 75 subs, the Kanalliste_nuevo.txt will be overwritte with this                                   file.
                                
+++Kanalliste_nuevo.txt = this will be the updated version ready to be used. It should contain the same subs than the Kanalliste_nuevo_remaining.txt once it ran sussccesfully-
   
   6º Once 75 subcriptions have been reached, you will need to wait for a couple of hours so that the "youtube subcribtions counter" has been reset, and allows you to continue subbing to whole a new batch of subcriptions. Since currently youtube limits the amount of daily subcriptions. After subbing the code will refresh the page so you can check if the subcription was successful.
   
   7º You should check the Sub_failures.txt file to manually check and sub to those channels that the bot was not able to sub you to.
   
   
