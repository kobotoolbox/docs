# Stockage des données
<a href="../data_storage.html">Read in English</a> | <a href="../es/data_storage.html">Leer en español</a> | <a href="../ar/data_storage.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/592a15ee470fa144eeac9850c6b6a648c4755306/source/data_storage.md" class="reference">11 Sep 2023</a>

Que vous utilisiez Le serveur KoboToolbox mondial](https://kf.kobotoolbox.org/) ou Le serveur KoboToolbox Union européenne](https://eu.kobotoolbox.org/), les données des deux serveurs sont stockées sur les serveurs Amazon Web Services (AWS).

Il existe 2 types de données stockées sur AWS : le formulaire lui-même et les pièces jointes liées à chaque soumission. Les données du formulaire sont enregistrées dans la base de données (DB) et les pièces jointes sont enregistrées dans Simple Storage Service (S3). Les données stockées dans la base de données ne sont jamais supprimées, sauf si vous supprimez les données vous-même. Les données collectées sur S3 ne sont jamais supprimées non plus, sauf si vous les supprimez vous-même ou si vous finissez par utiliser plus d'espace que ce qui vous est autorisé selon les [politiques de Kobo](creating_account.md).

Vous pouvez conserver jusqu'à 10 exports de données à la fois par projet. Si vous créez un 11ème export, le plus ancien est supprimé et seuls les 10 exports les plus récents sont conservés.

Pour plus d'informations sur les mesures de sécurité des données de KoboToolbox, veuillez consulter cet autre [article d'aide](is_my_data_safe.md).