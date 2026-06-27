# Compartir proyectos con permisos a nivel de usuario

**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/managing_permissions.md" class="reference">23 abr 2026</a>

<iframe src="https://www.youtube.com/embed/WnCNuxgaMoQ?si=bktZdlug2uBKUyzq&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboToolbox te permite establecer diferentes niveles de acceso para usuarios en cada proyecto. Algunos usuarios pueden necesitar solo enviar o ver datos, mientras que otros requieren acceso más avanzado, como editar formularios, validar envíos o editar datos.

Este artículo explica cómo otorgar permisos a otros usuarios de KoboToolbox para colaborar en tus proyectos. Cubre permisos a nivel de usuario, permisos a nivel de fila y cómo copiar permisos de otro proyecto.

<p class="note">
Para obtener más información sobre cómo compartir tu proyecto con otros para la recolección de datos, consulta <a href="../es/data_through_webforms.html">Recolección de datos a través de formularios web</a>. Para obtener más información sobre la configuración a nivel de proyecto para compartir tus proyectos, consulta <a href="../es/project_sharing_settings.html">Compartir proyectos con configuraciones a nivel de proyecto</a>.
</p>

## Configurar permisos a nivel de usuario

Los permisos a nivel de usuario te permiten compartir datos del proyecto con otros usuarios de KoboToolbox y controlar su acceso a tu formulario o envíos.

Para configurar permisos a nivel de usuario:
1. Ve a la página **CONFIGURACIÓN** de tu proyecto de recolección de datos y haz clic en **Compartir**.
2. Debajo de la lista de usuarios con acceso actual, haz clic en **Agregar usuario**.
3. Ingresa el nombre de usuario del usuario con quien deseas compartir el formulario.
4. Selecciona el nivel de permiso deseado.
5. Haz clic en **CONCEDER PERMISOS**.

![Agregar un usuario](images/managing_permissions/add_user.png)

Los siguientes permisos están disponibles:
| **Permiso**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| Ver formulario               | El usuario puede previsualizar el formulario.                                  |
| Editar formulario      | El usuario puede editar el formulario.                                  |
| Ver envíos           | El usuario puede ver los datos enviados.           |
| Agregar envíos           | El usuario puede enviar datos usando el formulario.         |
| Editar envíos         | El usuario puede editar los datos enviados.           |
| Validar envíos | El usuario puede [aprobar o rechazar](../es/viewing_validating_data.html#validar-tus-datos) los datos enviados. |
| Eliminar envíos         | El usuario puede eliminar los datos enviados.        |
| Gestionar el proyecto      | El usuario puede hacer todo lo anterior y gestionar la configuración del proyecto.                  |

<p class="note">
<strong>Nota</strong>: Cuando se otorgan ciertos permisos, otros permisos también se otorgan automáticamente. Por ejemplo, si a un usuario se le otorga el permiso <strong>Agregar envíos</strong>, también se le otorgará automáticamente el permiso <strong>Ver formulario</strong>.
</p>

## Configurar permisos a nivel de fila

Los permisos a nivel de fila te permiten establecer permisos de visualización, edición, validación y eliminación de envíos según condiciones predefinidas. Estos permisos pueden ser:

- **Solo de usuarios específicos**: Los permisos basados en usuarios te permiten compartir datos del proyecto con otro usuario de KoboToolbox solo cuando son enviados por usuarios específicos. Esto puede ser útil para permitir que los recolectores de datos vean y editen sus propios envíos sin acceder a datos de otros recolectores.
- **Con base en una condición**: Los permisos basados en condiciones otorgan acceso a los datos del proyecto según la respuesta a una pregunta en tu formulario. Por ejemplo, esto se puede usar para compartir datos recolectados antes de una fecha determinada o para una región específica.

### Permisos basados en usuarios

Para agregar permisos basados en usuarios:

1. Abre tu proyecto y ve a la ventana **CONFIGURACIÓN**.
2. Ve a la sección **Compartir**.
3. Haz clic en **Agregar usuario** e ingresa el nombre de usuario del usuario con quien deseas compartir el proyecto.
4. Selecciona los permisos basados en usuarios que deseas permitir (**Ver**, **Editar**, **Eliminar** y/o **Validar**).
5. Debajo de cada permiso, ingresa el(los) nombre(s) de usuario de los usuarios cuyos envíos estás otorgando acceso al usuario. Los nombres de usuario deben estar separados por comas.
6. Haz clic en **Conceder permisos** para guardar tu configuración de permisos.

Una vez que hayas guardado tus permisos, el usuario con quien has compartido el proyecto podrá ver, editar, validar o eliminar los datos del proyecto enviados por los nombres de usuario especificados, dependiendo de los permisos seleccionados.

### Permisos basados en condiciones

Para agregar permisos basados en condiciones:

1. Abre tu proyecto y ve a la ventana **CONFIGURACIÓN**.
2. Ve a la sección **Compartir**.
3. Haz clic en **Agregar usuario** e ingresa el nombre de usuario del usuario con quien deseas compartir el proyecto.
4. Selecciona los permisos basados en condiciones que deseas permitir (**Ver**, **Editar**, **Eliminar** y/o **Validar**).
5. Abre el menú desplegable **Seleccionar...** para mostrar la lista completa de preguntas del formulario y selecciona la pregunta que debe usarse para filtrar qué envíos se comparten con el usuario.
6. En el lado derecho del signo igual (=), ingresa el valor de respuesta que debe cumplirse.
7. Haz clic en **Conceder permisos** para guardar tu configuración de permisos.
   
Una vez que hayas guardado tus permisos, el usuario podrá ver, editar, validar o eliminar envíos de datos del proyecto que cumplan con la condición especificada, dependiendo de los permisos seleccionados.

Los valores de respuesta deben seguir un formato específico para que la condición funcione:

| **Tipo de pregunta**    | **Formato**                                |
| :----------------- | :--------------------------------------------- |
| Fecha               | <code>AAAA-MM-DD</code> (ej., <code>1974-12-31</code>)                                  |
| Seleccionar una y Seleccionar varias      | Valor XML/nombre de opción (ej., <code>primer_grado</code> en lugar de <code>Primer grado</code>)                                   |
| Número y Decimal           | Un número entero o decimal específico            |

## Copiar permisos de otro proyecto

Para copiar permisos de equipo de otro proyecto:

1. Abre la ventana **Compartir** en la página **CONFIGURACIÓN** de tu proyecto.
2. Haz clic en "Copiar el equipo de otro proyecto".
3. Selecciona el proyecto del cual deseas copiar los permisos.

<p class="note">
<strong>Nota</strong>: Esto sobrescribirá cualquier configuración de uso compartido existente en el proyecto al que estás agregando los permisos.
</p>

## Solución de problemas

<details>
<summary><strong>Rastrear cambios realizados por otros usuarios</strong></summary>
KoboToolbox mantiene <a href="../es/activity_logs.html">registros de actividad</a> que muestran una línea de tiempo completa de las acciones de la cuenta y del proyecto. Los <strong>Registros del historial de la actividad del proyecto</strong> registran cada modificación dentro de un proyecto—cargas, ediciones, eliminaciones y envíos—para que puedas rastrear cambios, asignar responsabilidad e identificar cuándo comenzaron los problemas.
</details>
<br>
<details>
<summary><strong>Se solicita nombre de usuario y contraseña al enviar datos</strong></summary>
Si aparece una ventana emergente de inicio de sesión cuando intentas enviar, el proyecto está configurado para <a href="../es/project_sharing_settings.html">requerir autenticación</a> para la recolección de datos. En este caso, solo puedes enviar datos si tu cuenta tiene el permiso Agregar envíos. Ingresa tu nombre de usuario y contraseña de KoboToolbox para continuar.
</details>
<br>
<details>
<summary><strong>Los permisos basados en usuarios no parecen funcionar</strong></summary>
Los permisos basados en usuarios se aplican solo cuando <a href="../es/project_sharing_settings.html">se requiere autenticación</a> y cada envío lleva un nombre de usuario. Abre la ventana <strong>FORMULARIO</strong> del proyecto y desactiva "Permitir envíos a este formulario sin nombre de usuario ni contraseña" en <strong>Recolectar datos</strong>.
</details>
<br>
<details>
<summary><strong>Los registros antiguos ignoran las reglas a nivel de fila</strong></summary>
Los envíos realizados antes de que <a href="../es/project_sharing_settings.html">se requiriera autenticación</a> pueden no tener un nombre de usuario adjunto, por lo que las reglas basadas en usuarios no pueden filtrarlos.
</details>
<br>
<details>
<summary><strong>Los permisos basados en condiciones no coinciden con texto parcial</strong></summary>
El filtro debe incluir el valor de respuesta exacto. Por ejemplo, filtrar por <code>desarrollador</code> no coincidirá con <code>desarrollador_software</code>. Escribe el valor completo que esperas, o ajusta tu formulario para que se capture el valor exacto.
</details>
<br>
<details>
<summary><strong>Los permisos basados en condiciones fallan en preguntas de grupos de repetición</strong></summary>
Los filtros no pueden buscar dentro de un grupo de repetición porque un envío puede contener varias respuestas diferentes. Si necesitas esto, consulta la publicación del Foro de la comunidad <a href="https://community.kobotoolbox.org/t/condition-based-permissions-from-a-repeat-group-value/59449">Permisos basados en condiciones usando un valor de grupo de repetición</a> para una solución alternativa con hojas de cálculo.
</details>
<br>
<details>
<summary><strong>No se admiten múltiples condiciones</strong></summary>
Los permisos basados en condiciones aceptan solo una condición. Si necesitas establecer permisos basados en múltiples condiciones, considera crear un cálculo basado en condiciones en tu formulario que produzca un solo valor para filtrar.
</details>