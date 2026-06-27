# Chiffrer vos formulaires
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/179faeb3c5a17b69406b0243ab9c22f7ca86aa44/source/encrypting_forms.md" class="reference">4 nov. 2024</a>


_Cette procédure est assez technique et s'adresse aux utilisateurs à l'aise avec des instructions techniques avancées. Elle requiert une attention particulière aux détails._

Les formulaires chiffrés fonctionnent en chiffrant les données sur le téléphone dès qu'elles sont enregistrées. Les données envoyées à KoboToolbox sont chiffrées et totalement inaccessibles à toute personne ne possédant pas la clé privée. Dans ce cas, KoboToolbox joue simplement le rôle d'un espace de stockage pour vos fichiers chiffrés — un endroit où importer vos données, puis les télécharger ultérieurement pour les déchiffrer en local
([à l'aide d'ODK Briefcase](http://blog.formhub.org/2013/06/27/formhub-supports-odk-briefcase/)).
Les soumissions étant chiffrées, toute fonctionnalité nécessitant un accès aux données — comme le mode Carte ou l'export de données — ne sera pas disponible dans KoboToolbox. Ce niveau de sécurité supplémentaire permet d'utiliser KoboToolbox pour collecter des données sensibles tout en respectant certains protocoles de protection des données.

## Fonctionnement

KoboCollect permet de chiffrer le contenu d'un formulaire dès qu'il est marqué comme finalisé et prêt à être envoyé depuis le téléphone. Pour utiliser cette fonctionnalité, vous devez disposer d'une clé de chiffrement publique à inclure dans le XLSForm, ainsi que d'une clé privée (que vous ne partagez jamais) utilisée par ODK Briefcase pour déchiffrer les données en local après les avoir téléchargées depuis KoboToolbox. La clé publique sert à chiffrer les données, tandis que la clé privée les déchiffre. Seule une personne possédant la clé privée peut déchiffrer les données chiffrées avec la clé publique. Pour en savoir plus sur l'infrastructure à clés publiques et privées,
[consultez cette page](https://en.wikipedia.org/wiki/Public-key_cryptography).

## Chiffrer des formulaires XLS

1. Créez votre formulaire dans KoboToolbox comme d'habitude. Téléchargez le formulaire depuis la liste des brouillons en tant que fichier XLS.

2. Dans le fichier téléchargé, accédez à l'**onglet settings**.

3. Ajoutez une colonne _submission_url_ et saisissez
   `https://kc.kobotoolbox.org/submission` ou
   `https://kc-eu.kobotoolbox.org/submission` (selon
   le serveur que vous utilisez).

5. Ajoutez une autre colonne _public_key_ (c'est-à-dire base64RsaPublicKey). Collez votre clé publique compatible.

    (Voir l'image ci-dessous pour référence)

    ![image](/images/encrypting_forms/column.png)

6. Importez le fichier XLS dans KoboToolbox. Vous pouvez soit l'importer dans la liste des brouillons de formulaires puis le déployer en tant que nouveau projet, soit l'importer directement dans votre liste de projets déployés. Une fois déployé, vous devriez voir un libellé indiquant « encrypted » à côté du nom de votre formulaire.

<p class="note">
  Veuillez noter que l'URL pour un utilisateur authentifié n'inclut plus <strong>votrenom d'utilisateur</strong> suite aux mises à jour récentes.
</p>

## Déchiffrer des formulaires

ODK Briefcase est utilisé pour télécharger les fichiers chiffrés depuis KoboToolbox et les déchiffrer en local sur votre ordinateur à l'aide d'une clé privée, garantissant ainsi un accès unique aux données. Pour que le déchiffrement avec ODK Briefcase soit réussi, assurez-vous de télécharger et d'installer les _Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 6_ depuis le
[site de téléchargement Java](https://www.oracle.com/java/technologies/javase-jce-all-downloads.html).
Ces fichiers sont nécessaires au bon fonctionnement du déchiffrement.

### Installer le JCE :

1. Décompressez l'archive zip téléchargée.

2. Naviguez dans l'arborescence du répertoire extrait et copiez les fichiers local_policy.jar et US_export_policy.jar dans le répertoire lib\security.

3. Collez ces fichiers dans le répertoire d'installation de l'environnement d'exécution Java (JRE) de votre ordinateur, en remplaçant les versions antérieures de ces fichiers.
    - Sur **Windows**, le JRE est généralement installé ici : C:\Program Files\Java\jre7\lib\security
    - Sur **OSX**, l'emplacement est /Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/lib/security

### Déchiffrer vos formulaires :

1. Téléchargez et ouvrez [ODK Briefcase](https://docs.getodk.org/briefcase-intro/).

2. Indiquez un **emplacement de stockage** sous l'onglet **Paramètres**.

3. Ouvrez l'onglet **Pull** et cliquez sur **Configure**.  
   ![image](/images/encrypting_forms/configure.png)

4. Saisissez ensuite les informations suivantes :

    - `https://kc.kobotoolbox.org` OU
      `https://kc-eu.kobotoolbox.org` (selon le serveur que vous utilisez)
    - Votre nom d'utilisateur
    - Votre mot de passe
    - Appuyez sur **Connect** une fois terminé  
      ![image](/images/encrypting_forms/connect.png)

<p class="note">
  Veuillez noter que les URL de serveur ci-dessus n'ont plus besoin d'inclure <strong>votrenom d'utilisateur</strong> suite aux mises à jour récentes.
</p>

5. Une liste de projets s'affiche. Sélectionnez le projet que vous souhaitez récupérer et appuyez sur **Pull**. Vous recevrez un message **Success** sous **Pull Status**.

6. Accédez maintenant à l'onglet **Export**.

7. Appuyez sur **Edit Default Configuration** pour vérifier que vous avez bien la **clé privée PEM** à l'**emplacement du fichier PEM**.  
   ![image](/images/encrypting_forms/private_key.png)  
   Si elle n'y figure pas, sélectionnez la **clé privée PEM** depuis le dossier où vous l'avez conservée en lieu sûr. (_Remarque : vous verrez également ici tous les projets qui ont été récupérés avec succès._)

8. Cochez maintenant le projet que vous souhaitez exporter et appuyez sur **Export**.

9. Les données sont exportées sous forme de fichier CSV ; vous pouvez désormais consulter les données déchiffrées.

## Générer des clés de chiffrement RSA

Pour générer les paires de clés publique-privée RSA, vous pouvez utiliser le logiciel OpenSSL, préinstallé sur OSX et Linux. Sur Windows, vous devez télécharger et installer le logiciel OpenSSL depuis
[ce site](http://slproweb.com/products/Win32OpenSSL.md). (_Remarque : installez Win64 OpenSSL v1.1.1c dans **C:** plutôt qu'à l'emplacement par défaut **C:\Program Files**_)

### Générer une clé RSA pour les formulaires chiffrés dans KoboToolbox

_Remarque : Nous recommandons vivement d'utiliser OpenSSL tel que décrit ci-dessous pour créer votre paire de clés publique/privée, car d'autres méthodes peuvent ne pas être prises en charge par le logiciel._

1. Ouvrez une fenêtre de commande Windows (« cmd »).

2. Saisissez la commande suivante : `cd C:\OpenSSL-Win32\bin` pour accéder au répertoire /bin dans le répertoire OpenSSL.

    ![image](/images/encrypting_forms/openssl_1.png)

3. Créez une clé privée de 2048 bits et enregistrez-la dans le fichier **MyPrivateKey.pem** en saisissant la commande suivante, puis appuyez sur **Entrée** :
   `openssl genpkey -out MyPrivateKey.pem -outform PEM -algorithm RSA -pkeyopt rsa_keygen_bits:2048`

    ![image](/images/encrypting_forms/openssl_2.png)

4. Extrayez ensuite la clé publique correspondant à la clé privée ci-dessus. Saisissez la commande suivante, puis appuyez sur **Entrée** :
   `openssl rsa -in MyPrivateKey.pem -inform PEM -out MyPublicKey.pem -outform PEM -pubout`

    ![image](/images/encrypting_forms/openssl_3.png)

5. Vous avez maintenant généré deux fichiers :

    - **MyPrivateKey.pem** — votre clé privée, que vous devez déplacer vers un emplacement sécurisé.
    - **MyPublicKey.pem** — votre clé publique, que vous pouvez partager avec toute personne avec qui vous souhaitez échanger des informations de manière sécurisée.

6. Ouvrez **MyPublicKey.pem** avec le Bloc-notes ou un autre éditeur de texte ; votre clé publique correspond à la très longue chaîne de caractères ininterrompue,

`e.g.:Tjhfur1K9+BRQ2USezIPbtyahbfuNqviI5Suhm8maA3JoELRHj9psjf/oNWoG87aFtKNbLrRaCEDP oFMDC9NEzWlv5L49BygeieMu/wg/rtMT0M0kgDbKxw5weJJgyb9P41aMsrqAAAAB3NzaC1yc2EAAAADAQAB AAABAQDfNoFX7bh3bfdW6lGfDht1Ea8PUBLKYjugbHN5jS7j5fHV6dexM+kzvITVgoyjhhKPXeCbaT62vD/ saTqJFXJzlysnZ24fqxNkjreO5K5EQ9c3ggwqML06+AKrFUSP5jpnyJJH8btNwKl6D5pG4ZseHwDUKzZtae xtPTNQz67kdYIKdtCkCsQHVsy4xvy/A0jzfK3xyOkG6j+L`

Cette chaîne est celle que vous devrez coller dans le champ public_key de l'**onglet settings** de votre fichier XLS.

**IMPORTANT** : assurez-vous de ne coller que la chaîne de la clé publique, sans espaces ni sauts de ligne !

**MyPrivateKey.pem** est le fichier que vous utiliserez lors de l'export des soumissions avec ODK Briefcase.

Remarque : lorsque vous tentez de modifier un formulaire chiffré, vous recevez le message suivant : « This form cannot be edited once it has been marked as finalized. It may by encrypted ».