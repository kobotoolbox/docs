# Seleccionar opciones desde una imagen
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/select_from_image.md" class="reference">23 Apr 2026</a>

Seleccionar opciones desde una imagen permite a los encuestados tocar o hacer clic directamente en **áreas específicas de un archivo SVG** en lugar de elegir de una lista de texto. Esta funcionalidad está disponible tanto en formularios web como en la aplicación Android KoboCollect.

Puedes usar esta funcionalidad para:

- Seleccionar una ubicación desde la imagen de una habitación o instalación
- Seleccionar una parte del cuerpo desde un diagrama del cuerpo humano
- Seleccionar áreas dañadas desde una foto de un edificio después de un desastre

Este artículo explica cómo crear una imagen SVG con áreas seleccionables y configurar tu XLSForm para que los encuestados puedan elegir opciones directamente desde la imagen.

![](images/select_from_image/select_image.png)


## Crear tu imagen seleccionable

Para crear una imagen con regiones seleccionables, debes usar un archivo **SVG (Scalable Vector Graphics)**.

<p class="note">
 Para obtener más información sobre los archivos SVG, consulta la <a href="https://developer.mozilla.org/en-US/docs/Web/SVG">documentación de SVG</a>. Recomendamos usar <a href="https://inkscape.org/">Inkscape</a>, un editor de gráficos vectoriales gratuito y de código abierto, para crear y editar archivos SVG.
</p>

Cada área seleccionable de la imagen debe incluir un atributo `id`. Estos valores de `id` deben coincidir exactamente con los valores correspondientes de la columna `name` en la hoja `choices` de tu XLSForm, por lo que deben seguir las mismas [convenciones de nomenclatura](https://support.kobotoolbox.org/es/option_choices_xls.html#best-practices-for-defining-choice-names).

Para crear tu archivo de imagen seleccionable:

1. Crea o edita un archivo `.svg`.
2. Agrega atributos `id` a cada elemento que quieras que sea seleccionable.
3. Guarda el archivo.

<p class="note">
<strong>Nota:</strong> En los formularios web, solo los elementos SVG <code>&lt;path&gt;</code> son compatibles como áreas seleccionables. Otras formas SVG, como rectángulos o círculos, pueden no funcionar correctamente. KoboCollect admite primitivas SVG adicionales.
</p>

## Configurar tu XLSForm

Para permitir que los encuestados seleccionen opciones desde tu imagen en XLSForm:

1. En la **hoja survey**, agrega una pregunta `select_one` o `select_multiple`.
2. Agrega una columna `appearance` e ingresa `image-map`.
3. Agrega una columna `image` e ingresa el nombre exacto del archivo SVG.
4. En la **hoja choices**, agrega la lista de opciones.
    - La columna `name` debe coincidir exactamente con los valores de `id` en tu archivo SVG.

**hoja survey**

| type | name | label | appearance | image |
|:---|:---|:---|:---|:---|
| select_one body | body_part | Which body part hurts the most? | image-map | body.svg |
| survey |

**hoja choices**

| list_name | name | label |
|:---|:---|:---|
| body | leg | Leg |
| body | arm | Arm |
| body | head | Head |
| choices |

## Cargar el archivo SVG en KoboToolbox

Después de crear tu archivo SVG y referenciarlo en tu XLSForm, debes cargarlo en tu proyecto.

Para importar archivos multimedia:

1. Inicia sesión en tu cuenta de KoboToolbox.
2. Abre tu proyecto.
3. Ve a **CONFIGURACIÓN > Multimedia.**
4. Carga el archivo SVG. Asegúrate de que el nombre del archivo coincida exactamente con lo que está escrito en la columna `image` de tu XLSForm.
5. Implementa o vuelve a implementar tu formulario para aplicar los cambios.

<p class="note">
Para obtener más información sobre cómo cargar archivos multimedia, consulta <a href="https://support.kobotoolbox.org/es/upload_media.html">Importar archivos multimedia a un proyecto</a>.
</p>