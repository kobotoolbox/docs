# Styliser vos formulaires web dans le Formbuilder
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/alternative_enketo.md" class="reference">23 avr. 2026</a>

<iframe src="https://www.youtube.com/embed/wLWiw473YSQ?si=tJbKl-VzjZkDPivR&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Vous pouvez personnaliser la mise en page et l'apparence visuelle de vos [formulaires web](https://support.kobotoolbox.org/fr/data_through_webforms.html) à l'aide de thèmes intégrés. Ces thèmes vous permettent de contrôler la façon dont les questions sont affichées, que ce soit sur une seule page, sur plusieurs pages ou organisées dans une mise en page en grille compacte.

Les thèmes de formulaires s'appliquent uniquement aux formulaires web et ne sont pas disponibles dans KoboCollect. Cet article explique comment appliquer un thème de formulaire web dans le Formbuilder et comment configurer les largeurs de questions lors de l'utilisation du thème Grille.

## Ajouter un thème de formulaire web dans le Formbuilder

Pour ajouter un thème de formulaire web à votre formulaire dans le Formbuilder :

1. Cliquez sur <i class="k-icon-settings"></i> **Mise en page & Paramètres** en haut à droite de l'écran.
2. Dans la section **Style du formulaire**, sélectionnez le thème que vous souhaitez appliquer à votre formulaire.

![Style du formulaire](images/alternative_enketo/access.png)

Les thèmes suivants sont disponibles pour personnaliser vos formulaires :

![Thèmes](images/alternative_enketo/preview.png)

<p class="note">
<strong>Note :</strong> Vous pouvez également combiner les styles <strong>Pages multiples</strong> et <strong>Thème de grille</strong>.
</p>

## Configurer les largeurs de questions pour le thème Grille

Dans les formulaires web, le thème Grille vous permet d'afficher les questions sur plusieurs colonnes, rendant votre formulaire plus compact et visuellement organisé. La configuration de ces colonnes, y compris leur nombre et leur largeur, est contrôlée en attribuant des `valeurs-w` à chaque question dans ses paramètres **Apparence (avancée)**. 

<p class="note">
 Pour un aperçu complet de l'utilisation du thème Grille, consultez ce <a href="https://ee.kobotoolbox.org/n41GqUkf">tutoriel sur le thème Grille</a> et cet <a href="https://docs.google.com/spreadsheets/d/1qKmxPTA4B0vihU6GsKgi1CJE2Db2FfE7KZpOig4nTEI/edit?gid=0#gid=0">exemple d'XLSForm</a>.   
</p>

Pour spécifier la largeur relative de chaque question dans une ligne :

1. Ouvrez les paramètres de la question en cliquant sur <i class="k-icon-settings"></i> **Paramètres** à droite de la question. Cela vous amènera à l'onglet **Options de la question**.
2. Dans **Apparence (avancée)**, attribuez des valeurs d'apparence (par exemple, `w1`, `w2`, `w3`) pour spécifier la largeur relative de la question dans une ligne.

Les lignes s'étendront toujours automatiquement sur toute la largeur de la page. Par exemple, une ligne contenant une question avec une valeur d'apparence `w2` et une autre avec `w1` divisera la ligne en deux tiers et un tiers, respectivement. 

<p class="note">
<strong>Note :</strong> La largeur par défaut pour un groupe ou un groupe répété est de quatre colonnes (<code>w4</code>), donc un groupe avec <code>w4</code> peut contenir un maximum de quatre questions <code>w1</code> dans une seule ligne. La <code>valeur-w</code> d'une question est relative à la <code>valeur-w</code> de son groupe. Appliquez les <code>valeurs-w</code> uniquement aux groupes ou répétitions de niveau supérieur : bien que leur application aux groupes ou répétitions imbriqués soit possible, l'affichage peut ne pas être optimal.
</p>