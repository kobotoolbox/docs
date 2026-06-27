# Journalisation d'audit (type de métaquestion)

La journalisation d'audit peut être un outil utile pour surveiller le comportement des enquêteurs, identifier les questions qui prennent le plus de temps à répondre, mieux comprendre comment les enquêteurs naviguent dans un formulaire donné, et voir quels enquêteurs prennent généralement plus de temps pour soumettre leurs réponses.

<p class="note">Cette fonctionnalité nécessite d'analyser manuellement des fichiers CSV.</p>

La métaquestion de journalisation d'audit est un type de question uniquement disponible avec [l'application Android KoboCollect](kobocollect_on_android_latest.md).

Pour ajouter un type de métaquestion `audit` à un formulaire et consulter les données finalisées, veuillez suivre les étapes ci-dessous :

1. Dans un fichier XLSForm, ajoutez `audit` de la même manière que vous le feriez pour toute autre métaquestion. Importez ensuite le fichier de formulaire dans votre projet et déployez le formulaire.

**onglet survey**

| type  | name  | label                  |
| :---- | :---- | :--------------------- |
| start | start |                        |
| end   | end   |                        |
| audit | audit |                        |
| text  | Q1    | Q1. What is your name? |
| survey |

2. Collectez des données à l'aide de [l'application Android KoboCollect](kobocollect_on_android_latest.md) et envoyez les formulaires finalisés au serveur. KoboCollect enregistre les journaux d'audit de chaque soumission dans un fichier CSV, qui est sauvegardé et importé sur le serveur de la même façon qu'une photo jointe.

3. Une fois les données soumises, ouvrez votre projet dans le navigateur et accédez à **DONNÉES**, puis **Téléchargements**. Sélectionnez **Fichier média (ZIP)** comme type d'export, puis cliquez sur **Nouvel export**. Une fois le téléchargement disponible, cliquez sur le fichier pour le télécharger sur votre ordinateur.

![image](/images/audit_logging/zip_export.png)

4. Une fois le fichier ZIP extrait et ouvert, cliquez sur le fichier intitulé « audit.csv » pour consulter les journaux d'audit. Il est important de noter que le fichier CSV utilise le temps [Unix Epoch](https://www.unixtimestamp.com/index.php), de sorte que les journaux sont enregistrés en millisecondes.

5. Étant donné que les horodatages sont enregistrés pour chaque soumission individuelle, vous aurez probablement besoin de copier les valeurs dans un nouveau tableur pour effectuer une analyse approfondie sur l'ensemble des soumissions (par exemple, par enquêteur ou par question). La consolidation de plusieurs fichiers CSV peut être réalisée à l'aide de [nombreux outils gratuits ou en écrivant un script](https://www.google.com/search?q=merge+many+CSV). Pour obtenir des informations plus détaillées sur la structure des journaux et les types d'événements, consultez la documentation d'ODK sur [Logging Enumerator Behavior](https://docs.getodk.org/form-audit-log/#).

N'hésitez pas à publier un message sur notre [Forum communautaire](https://community.kobotoolbox.org/) pour partager votre approche ou script préféré pour utiliser cette fonctionnalité, afin que d'autres utilisateurs puissent s'en inspirer.