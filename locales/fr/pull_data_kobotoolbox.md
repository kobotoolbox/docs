# Fonctionnalité Pull Data dans KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/202f8e0e134d0695913bf6c5d5b52449c5e61e5d/source/pull_data_kobotoolbox.md" class="reference">18 août 2025</a>

Cette opération se fait de préférence sur la version xls du formulaire.

-   Dans la partie survey du formulaire, ajoutez un champ calculate à votre enquête.
-   Donnez à ce champ le nom que vous souhaitez
-   Ensuite, dans sa colonne calculation, appelez la fonction pulldata(), en indiquant
    quel champ extraire de quelle ligne de quel fichier .csv. Cela peut être réalisé
    en écrivant comme suit
    `pulldata('nomducsv', 'entêtedecolonnepourextraireles données', 'colonneàvérifierpourcorrespondanceTEXTE', 'TEXTEàvérifier'`

    ![image](/images/pull_data_kobotoolbox/xls.png)

-   Notez que votre CSV doit avoir au moins deux colonnes et assurez-vous que la
    colonneàvérifierpourcorrespondanceTEXTE est toujours la première colonne à partir de la gauche
-   TEXTEàvérifier peut également être référencé à partir d'une question de champ antérieure en
    utilisant `${Question}` comme dans l'exemple ci-dessus
-   Une fois que vous avez terminé la mise à jour du xls, vous devrez importer votre formulaire
    depuis xls (ne le modifiez pas sur l'interface de création de formulaires), vous importerez ensuite votre CSV
    de la même manière que vous importeriez vos images.
-   Lorsque vous déployez votre fichier, le csv sera téléchargé dans les fichiers média

**Points à noter**

-   Cela fonctionnera à la fois sur l'application KoboCollect et Enketo (formulaire web).
-   Compressez un fichier .csv volumineux dans une archive .zip avant de l'importer.
-   Enregistrez le fichier .csv au format UTF-8 si les données préchargées contiennent des polices non anglaises
    ou des caractères spéciaux, cela permet à votre appareil Android de rendre le texte
    correctement.
-   Les champs de données extraits d'un fichier .csv sont considérés comme des chaînes de texte,
    utilisez donc les fonctions int() ou number() pour convertir un champ préchargé
    en forme numérique.
-   Si le fichier .csv contient des données sensibles que vous ne souhaitez peut-être pas importer sur
    le serveur, importez un fichier .csv vide dans le cadre de votre formulaire, puis remplacez-le
    par le vrai fichier .csv en copiant manuellement le fichier sur chacun de vos appareils.
-   Si vous rencontrez des messages d'erreur lors de l'utilisation de cette fonctionnalité, essayez de modifier le nom du fichier pour supprimer les traits de soulignement ou symboles.