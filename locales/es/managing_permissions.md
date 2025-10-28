# Compartir proyectos con permisos a nivel de usuario/a
<a href="../managing_permissions.html">Read in English</a> | <a href="../fr/managing_permissions.html">Lire en français</a> | <a href="../ar/managing_permissions.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/2d936225c821d33163324c6fe6093fa30da3c5fa/source/managing_permissions.md" class="reference">29 ago 2025</a>

<iframe src="https://www.youtube.com/embed/WnCNuxgaMoQ?si=bktZdlug2uBKUyzq" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboToolbox te permite establecer diferentes niveles de acceso para los/as usuarios/as en cada proyecto. Algunos/as usuarios/as pueden necesitar solo enviar o visualizar datos, mientras que otros/as requieren acceso más avanzado, como editar formularios, validar envíos o editar datos.

Este artículo explica cómo otorgar permisos a otros/as usuarios/as de KoboToolbox para colaborar en tus proyectos. Cubre permisos a nivel de usuario/a, permisos a nivel de fila y cómo copiar permisos de otro proyecto.

<p class="note">
Para obtener más información sobre cómo compartir tu proyecto con otros/as para la recolección de datos, consulta <a href="data_through_webforms.html">Recolectar datos a través de formularios web</a>. Para obtener más información sobre la configuración a nivel de proyecto para compartir tus proyectos, consulta <a href="project_sharing_settings.html">Compartir proyectos con configuración a nivel de proyecto</a>.
</p>

## Configurar permisos a nivel de usuario/a

Los permisos a nivel de usuario/a te permiten compartir datos del proyecto con otros/as usuarios/as de KoboToolbox y controlar su acceso a tu formulario o envíos.

Para configurar permisos a nivel de usuario/a:
1. Ve a la página **SETTINGS** de tu proyecto de recolección de datos y haz clic en **Sharing**.
2. Debajo de la lista de usuarios/as con acceso actual, haz clic en **Add user**.
3. Ingresa el nombre de usuario/a del/de la usuario/a con quien deseas compartir el formulario.
4. Selecciona el nivel de permiso deseado.
5. Haz clic en **GRANT PERMISSIONS**.

![Adding a user](images/managing_permissions/add_user.png)

Los siguientes permisos están disponibles:
| **Permiso**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| View form               | El/la usuario/a puede previsualizar el formulario.                                  |
| Edit form      | El/la usuario/a puede editar el formulario.                                  |
| View submissions           | El/la usuario/a puede visualizar los datos enviados.           |
| Add submissions           | El/la usuario/a puede enviar datos usando el formulario.         |
| Edit submissions         | El/la usuario/a puede editar los datos enviados.           |
| Validate submissions | El/la usuario/a puede [aprobar o rechazar](record_validation.md) los datos enviados. |
| Delete submissions         | El/la usuario/a puede eliminar los datos enviados.        |
| Manage project      | El/la usuario/a puede hacer todo lo anterior y administrar la configuración del proyecto.                  |

<p class="note">
<strong>Nota</strong>: Cuando se otorgan ciertos permisos, otros permisos también se otorgan automáticamente. Por ejemplo, si se otorga a un/a usuario/a el permiso <strong>Add submissions</strong>, también se le otorgará automáticamente el permiso <strong>View form</strong>.
</p>

## Configurar permisos a nivel de fila

Los permisos a nivel de fila te permiten establecer permisos de visualización, edición, validación y eliminación de envíos basados en condiciones predefinidas. Estos permisos pueden ser:

- **Solo de usuarios/as específicos/as**: Los permisos basados en usuarios/as te permiten compartir datos del proyecto con otro/a usuario/a de KoboToolbox solo cuando son enviados por usuarios/as específicos/as. Esto puede ser útil para permitir que los/as recolectores/as de datos visualicen y editen sus propios envíos sin acceder a datos de otros/as recolectores/as.
- **Basados en una condición**: Los permisos basados en condiciones otorgan acceso a los datos del proyecto según una respuesta a una pregunta en tu formulario. Por ejemplo, esto se puede usar para compartir datos recolectados antes de una fecha determinada o para una región específica.

### Permisos basados en usuarios/as

Para agregar permisos basados en usuarios/as:

1. Abre tu proyecto y navega a la ventana **SETTINGS**.
2. Ve a la sección **Sharing**.
3. Haz clic en **Add user** e ingresa el nombre de usuario/a del/de la usuario/a con quien deseas compartir el proyecto.
4. Selecciona los permisos basados en usuarios/as que deseas permitir (**View**, **Edit**, **Delete** y/o **Validate**).
5. Debajo de cada permiso, ingresa el/los nombre(s) de usuario/a de los/as usuarios/as cuyos envíos estás otorgando acceso al/a la usuario/a. Los nombres de usuario/a deben estar separados por comas.
6. Haz clic en **Grant permissions** para guardar tu configuración de permisos.

Una vez que hayas guardado tus permisos, el/la usuario/a con quien has compartido el proyecto podrá visualizar, editar, validar o eliminar los datos del proyecto enviados por los nombres de usuario/a especificados, dependiendo de los permisos seleccionados.

### Permisos basados en condiciones

Para agregar permisos basados en condiciones:

1. Abre tu proyecto y navega a la ventana **SETTINGS**.
2. Ve a la sección **Sharing**.
3. Haz clic en **Add user** e ingresa el nombre de usuario/a del/de la usuario/a con quien deseas compartir el proyecto.
4. Selecciona los permisos basados en condiciones que deseas permitir (**View**, **Edit**, **Delete** y/o **Validate**).
5. Abre el menú desplegable **Select…** para mostrar la lista completa de preguntas del formulario y selecciona la pregunta que debe usarse para filtrar qué envíos se comparten con el/la usuario/a.
6. En el lado derecho del signo igual (=), ingresa el valor de respuesta que debe cumplirse.
7. Haz clic en **Grant permissions** para guardar tu configuración de permisos.
   
Una vez que hayas guardado tus permisos, el/la usuario/a podrá visualizar, editar, validar o eliminar envíos de datos del proyecto que cumplan con la condición especificada, dependiendo de los permisos seleccionados.

Los valores de respuesta deben seguir un formato específico para que la condición funcione:

| **Tipo de pregunta**    | **Formato**                                |
| :----------------- | :--------------------------------------------- |
| Date               | <code>YYYY-MM-DD</code> (ej., <code>1974-12-31</code>)                                  |
| Select One y Select Many      | Valor XML/nombre de opción (ej., <code>first_grade</code> en lugar de <code>First grade</code>)                                   |
| Number y Decimal           | Un número entero o decimal específico            |

## Copiar permisos de otro proyecto

Para copiar permisos de equipo de otro proyecto:

1. Abre la pestaña **Sharing** en la página **SETTINGS** de tu proyecto.
2. Haz clic en "Copy team from another project".
3. Selecciona el proyecto del cual deseas copiar los permisos.

<p class="note">
<strong>Nota</strong>: Esto sobrescribirá cualquier configuración de uso compartido existente en el proyecto al que estás agregando los permisos.
</p>

## Solución de problemas

<details>
<summary><strong>Rastrear cambios realizados por otros/as usuarios/as</strong></summary>
KoboToolbox mantiene <a href="activity_logs.html">Registros de actividad</a> que muestran una línea de tiempo completa de las acciones de la cuenta y del proyecto. Los <strong>Registros de historial del proyecto</strong> registran cada modificación dentro de un proyecto—cargas, ediciones, eliminaciones y envíos—para que puedas rastrear cambios, asignar responsabilidad e identificar cuándo comenzaron los problemas.
</details>
<br>
<details>
<summary><strong>Se solicita nombre de usuario/a y contraseña al enviar datos</strong></summary>
Si aparece una ventana emergente de inicio de sesión cuando intentas enviar, el proyecto está configurado para <a href="project_sharing_settings.html">requerir autenticación</a> para la recolección de datos. En este caso, puedes enviar datos solo si tu cuenta tiene el permiso Add submissions. Ingresa tu nombre de usuario/a y contraseña de KoboToolbox para continuar.
</details>
<br>
<details>
<summary><strong>Los permisos basados en usuarios/as no parecen funcionar</strong></summary>
Los permisos basados en usuarios/as se aplican solo cuando <a href="project_sharing_settings.html">se requiere autenticación</a> y cada envío lleva un nombre de usuario/a. Abre la ventana <strong>FORMULARIO</strong> del proyecto y desactiva "Allow submissions to this form without a username and password" en <strong>Collect data</strong>.
</details>
<br>
<details>
<summary><strong>Los registros antiguos ignoran las reglas a nivel de fila</strong></summary>
Los envíos realizados antes de que <a href="project_sharing_settings.html">se requiriera autenticación</a> pueden no tener un nombre de usuario/a adjunto, por lo que las reglas basadas en usuarios/as no pueden filtrarlos.
</details>
<br>
<details>
<summary><strong>Los permisos basados en condiciones no coinciden con texto parcial</strong></summary>
El filtro debe incluir el valor de respuesta exacto. Por ejemplo, filtrar por <code>developer</code> no coincidirá con <code>software_developer</code>. Escribe el valor completo que esperas, o ajusta tu formulario para que se capture el valor exacto.
</details>
<br>
<details>
<summary><strong>Los permisos basados en condiciones fallan en preguntas de grupos repetidos</strong></summary>
Los filtros no pueden buscar dentro de un grupo repetido porque un envío puede contener varias respuestas diferentes. Si necesitas esto, consulta la publicación del Foro de la comunidad <a href="https://community.kobotoolbox.org/t/condition-based-permissions-from-a-repeat-group-value/59449">Permisos basados en condiciones usando un valor de grupo repetido</a> para una solución alternativa con hojas de cálculo.
</details>
<br>
<details>
<summary><strong>No se admiten múltiples condiciones</strong></summary>
Los permisos basados en condiciones aceptan solo una condición. Si necesitas establecer permisos basados en múltiples condiciones, considera crear un cálculo basado en condiciones en tu formulario que produzca un solo valor para filtrar.
</details>