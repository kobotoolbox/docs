# Liste des types de questions
<a href="../question_types.html">Read in English</a> | <a href="../es/question_types.html">Leer en español</a> | <a href="../ar/question_types.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/3993133bcf0aafda0b0978709534175cb583e049/source/question_types.md" class="reference">28 oct. 2024</a>

Le tableau ci-dessous fournit un résumé général de chacun des types de réponse disponibles pour une utilisation dans votre XLSForm et l'interface de création de formulaires :

| Type de question                 | Icône                                         | Saisie de réponse                                                                                      |
| :------------------------------- | :-------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| integer                          | <i class="k-icon k-icon-qt-number"></i>       | Saisie d'un nombre entier.                                                                             |
| decimal                          | <i class="k-icon k-icon-qt-decimal"></i>      | Saisie décimale.                                                                                       |
| range                            | <i class="k-icon k-icon-qt-range"></i>        | Saisie de plage (y compris notation).                                                                  |
| text                             | <i class="k-icon k-icon-qt-text"></i>         | Réponse en texte libre.                                                                                |
| select_one [options]             | <i class="k-icon k-icon-qt-select-one"></i>   | Question à choix multiples ; une seule réponse peut être sélectionnée.                                 |
| select_multiple [options]        | <i class="k-icon k-icon-qt-select-many"></i>  | Question à choix multiples ; plusieurs réponses peuvent être sélectionnées.                            |
| select_one_from_file [file]      | <i class="k-icon k-icon-qt-select-one"></i>   | Choix multiples à partir d'un fichier ; une seule réponse peut être sélectionnée.                      |
| select_multiple_from_file [file] | <i class="k-icon k-icon-qt-select-many"></i>  | Choix multiples à partir d'un fichier ; plusieurs réponses peuvent être sélectionnées.                 |
| rank [options]                   | n/a                                           | Question de classement ; ordonner une liste.                                                           |
| note                             | <i class="k-icon k-icon-qt-note"></i>         | Afficher une note à l'écran, ne prend aucune saisie. Raccourci pour type=text avec readonly=true.     |
| geopoint                         | <i class="k-icon k-icon-qt-point"></i>        | Collecter une seule coordonnée GPS.                                                                    |
| geotrace                         | <i class="k-icon k-icon-qt-line"></i>         | Enregistrer une ligne de deux coordonnées GPS ou plus.                                                 |
| geoshape                         | <i class="k-icon k-icon-qt-area"></i>         | Enregistrer un polygone de plusieurs coordonnées GPS ; le dernier point est identique au premier point.|
| date                             | <i class="k-icon k-icon-qt-date"></i>         | Saisie de date.                                                                                        |
| time                             | <i class="k-icon k-icon-qt-time"></i>         | Saisie d'heure.                                                                                        |
| datetime                         | <i class="k-icon k-icon-qt-date-time"></i>    | Accepte une saisie de date et d'heure.                                                                 |
| image                            | <i class="k-icon k-icon-qt-photo"></i>        | Prendre une photo ou importer un fichier image.                                                        |
| audio                            | <i class="k-icon k-icon-qt-audio"></i>        | Effectuer un enregistrement audio ou importer un fichier audio.                                        |
| background-audio                 | <i class="k-icon k-icon-background-rec"></i>  | L'audio est enregistré en arrière-plan pendant le remplissage du formulaire.                           |
| video                            | <i class="k-icon k-icon-qt-video"></i>        | Effectuer un enregistrement vidéo ou importer un fichier vidéo.                                        |
| file                             | <i class="k-icon k-icon-qt-file"></i>         | Saisie de fichier générique (txt, pdf, xls, xlsx, doc, docx, rtf, zip)                                |
| barcode                          | <i class="k-icon k-icon-qt-barcode"></i>      | Scanner un code-barres ou un code QR                                                                   |
| calculate                        | <i class="k-icon k-icon-qt-calculate"></i>    | Effectuer un calcul ; voir la section Calcul ci-dessous.                                               |
| acknowledge                      | <i class="k-icon k-icon-qt-acknowledge"></i>  | Invite de confirmation qui définit la valeur sur « OK » si elle est sélectionnée.                      |
| hidden                           | <i class="k-icon k-icon-qt-hidden"></i>       | Un champ sans élément d'interface utilisateur associé qui peut être utilisé pour stocker une constante.|
| xml-external                     | <i class="k-icon k-icon-qt-external-xml"></i> | Ajoute une référence à un fichier de données XML externe.                                              |

Pour plus d'informations sur les types de réponse, veuillez consulter
[xlsform.org](http://xlsform.org/).

De plus, les types spécifiques à KoboToolbox peuvent également être utilisés depuis l'interface de création de formulaires :

| Type de question de l'interface de création de formulaires | Icône                                            | Saisie de réponse                                                         |
| :---------------------------------------------------------- | :----------------------------------------------- | :------------------------------------------------------------------------ |
| Rating                                                      | <i class="k-icon k-icon-qt-rating"></i>          | Comparer différents éléments en utilisant une échelle commune.            |
| Ranking                                                     | <i class="k-icon k-icon-qt-ranking"></i>         | Comparer une liste de différents objets les uns par rapport aux autres.   |
| Question Matrix                                             | <i class="k-icon k-icon-qt-question-matrix"></i> | Créer un groupe de questions qui s'affichent dans un format matriciel.    |

<p class="note">Les <a class="reference" href="/calculate_questions.html">questions de calcul</a> ne sont pas affichées dans votre formulaire, mais sont exécutées automatiquement pendant que vous répondez à votre formulaire.</p>

<p class="note">Le <a class="reference" href="matrix_response.html">type de matrice de questions</a> est uniquement pris en charge dans Enketo et avec le thème Grille défini. </p>