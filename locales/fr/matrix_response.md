# Type de réponse Matrice de questions
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/matrix_response.md" class="reference">29 juil. 2025</a>

Le type de réponse Matrice de questions permet aux utilisatrices et utilisateurs de créer un groupe de questions qui s'affichent dans un format matriciel, où chaque cellule de la matrice représente une question distincte. Pour utiliser ce type de réponse, définissez le nombre de lignes et de colonnes que vous souhaitez dans votre ensemble matriciel et attribuez une étiquette ou un nom à chaque ligne et colonne. Chaque colonne peut être un type de question différent. Dans la capture d'écran ci-dessus, les deux premières colonnes sont des questions à choix unique, et la troisième colonne est une question numérique.

![image](/images/matrix_response/matrix_example.png)

<p class="note">Ce type de réponse <strong>fonctionne uniquement avec Enketo</strong>, en utilisant la <strong>mise en page Grid-theme</strong>. Les formulaires sont définis sur une mise en page à page unique par défaut -- pour la modifier, trouvez le bouton « layout » dans la barre d'outils de l'interface de création de formulaires, sélectionnez « grid-theme », enregistrez cette modification et redéployez votre formulaire pour que ces changements soient actifs.</p>

<p class='note'>Enketo prend en charge uniquement jusqu'à <code>10</code> colonnes dans les versions antérieures à <code>2.8.0</code>, jusqu'à <code>13</code> à partir de la version <code>2.8.0</code> incluse.</p>

## Créer une Matrice de questions dans l'interface de création de formulaires

1. Accédez à votre interface de création de formulaires et cliquez sur « Add question »
2. Sélectionnez « Question Matrix »

    ![image](/images/matrix_response/question_matrix.png)

3. Cliquez sur l'icône d'engrenage dans chaque colonne pour définir le type de question.

    ![image](/images/matrix_response/question_type.png)

4. Sélectionnez le type de question

5. Ajoutez l'étiquette de colonne et l'étiquette de réponse

    ![image](/images/matrix_response/label_response.png)

6. Sélectionnez l'icône d'engrenage dans « Row » pour définir l'étiquette de ligne

    ![image](/images/matrix_response/row.png)

## Créer une Matrice de questions dans XLSForm

Vous pouvez également créer une Matrice de questions dans un XLSForm en suivant les instructions décrites dans les images ci-dessous :

**feuille survey**

| type             | name | label                                      | required | `kobo--matrix_list` |
| :--------------- | :--- | :----------------------------------------- | :------- | :----------------   |
| begin_kobomatrix | M1   | Items                                      |          | assets              |
| select_one yn    | Q1   | Q1. Quels biens possédez-vous à la maison  | TRUE     |                     |
| integer          | Q2   | Q2. Nombre de biens                        | TRUE     |                     |
| end_kobomatrix   |      |                                            |          |                     |
| survey |

**feuille choices**

| list_name | name | label   |
| :-------- | :--- | :------ |
| assets    | car  | Voiture |
| assets    | bike | Vélo    |
| assets    | tv   | TV      |
| yn        | yes  | Oui     |
| yn        | no   | Non     |
| choices |

**feuille settings**

| style                        |
| :--------------------------- |
| theme-grid no-text-transform |
| settings |

<p class="note">Cette méthode utilise <code>begin_kobomatrix</code>,
<code>end_kobomatrix</code> et <code>kobo--matrix_list</code>.</p>

En suivant les étapes ci-dessus, vous devriez voir la matrice de questions illustrée dans la capture d'écran ci-dessous (dans [Enketo](data_through_webforms.md) uniquement) :

![image](/images/matrix_response/preview.png)

Il est également possible d'inclure des conditions `relevant` et `constraint` dans la matrice comme suit :

**feuille survey**

| type             | name | label                                      | required | `kobo--matrix_list` | relevant      | constraint |
| :--------------- | :--- | :----------------------------------------- | :------- | :----------------   | :------------ | :--------- |
| begin_kobomatrix | M1   | Items                                      |          | assets              |               |            |
| select_one yn    | Q1   | Q1. Quels biens possédez-vous à la maison  | TRUE     |                     |               |            |
| integer          | Q2   | Q2. Nombre de biens                        | TRUE     |                     | ${Q1} = 'yes' | . > 2      |
| end_kobomatrix   |      |                                            |          |                     |               |            |
| survey |