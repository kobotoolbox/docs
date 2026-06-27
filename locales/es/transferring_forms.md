# Importar formularios en KoboCollect
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/7def5f54e2441b05b4a2163e682bdd146fa781e1/source/transferring_forms.md" class="reference">24 Sep 2025</a>

Puede haber ocasiones en las que estés en el campo sin conexión a internet, pero aún necesites cargar la última versión de los formularios (es decir, los últimos formularios implementados en el servidor) en tu dispositivo. También es posible que no puedas cargar los envíos al servidor debido a una pantalla rota. En ambos casos, necesitarás transferir manualmente los formularios y/o envíos usando otro dispositivo. Este artículo de ayuda te mostrará cómo hacerlo.

Necesitarás los siguientes elementos para seguir las instrucciones que se describen a continuación:

-   Un dispositivo Android que tenga la [aplicación Android KoboCollect](https://support.kobotoolbox.org/es/kobocollect_on_android_latest.html) con la última versión del formulario implementado. (Se recomienda [obtener la última versión](https://support.kobotoolbox.org/es/data_collection_kobocollect.html#downloading-forms) del formulario implementado en el dispositivo haciendo clic en **Descargar formulario** desde tu **aplicación Android KoboCollect**.)
-   Un dispositivo Android que no tenga la última versión del formulario (o incluso ningún formulario).
-   Ambos dispositivos Android deben tener la aplicación KoboCollect ya instalada.
-   Computadora personal (de escritorio o portátil).
-   Cable USB que conecte el dispositivo a la computadora personal.

**Paso 1:** Enciende tu computadora personal (no se necesita conexión a internet en este paso). Una PC es necesaria en esta fase para copiar los formularios y datos de un dispositivo Android con la última versión del formulario a otro.

**Paso 2:** Conecta el dispositivo Android (con el formulario y los datos más recientes que deseas transferir) a la PC mediante el cable USB.

**Paso 3:** A continuación, sigue la ruta que se ilustra a continuación para extraer las carpetas requeridas con los formularios y datos (según la versión de la aplicación instalada):

<p class="note">
  En este ejemplo, estamos conectando un Galaxy S10+ (un dispositivo Android) a Windows 11, por eso ves <strong>Este equipo</strong> y <strong>Galaxy S10+</strong>. Estos nombres pueden variar si usas otro sistema operativo o dispositivo Android.
</p>

-   Para la aplicación Android KoboCollect versión 2021.2 y posteriores:
    -   Si la aplicación Android KoboCollect está instalada en la memoria del teléfono:
        `Este equipo\Galaxy S10+\Phone\Android\data\org.koboc.collect.android\files\projects`
    -   Si la aplicación Android KoboCollect está instalada en la memoria externa:
        `Este equipo\Galaxy S10+\sdcard\Android\data\org.koboc.collect.android\files\projects`
-   Para la aplicación Android KoboCollect (versión mayor que v1.26.0):
    -   Si la aplicación Android KoboCollect está instalada en la memoria del teléfono:
        `Este equipo\Galaxy S10+\Phone\Android\data\org.koboc.collect.android\files`
    -   Si la aplicación Android KoboCollect está instalada en la memoria externa:
        `Este equipo\Galaxy S10+\sdcard\Android\data\org.koboc.collect.android\files`
-   Para la aplicación Android KoboCollect (versión menor que v1.26.0):
    -   Si la aplicación Android KoboCollect está instalada en la memoria del teléfono:
        `Este equipo\Galaxy S10+\Phone\odk`
    -   Si la aplicación Android KoboCollect está instalada en la memoria externa:
        `Este equipo\Galaxy S10+\sdcard\odk`

**Paso 4:** Una vez que estés en la carpeta **projects**, la carpeta **files** o la carpeta **odk** _(según la versión de la aplicación Android KoboCollect que estés usando)_, deberías ver una carpeta con un nombre similar (como se muestra a continuación):

![Imagen de ejemplo](images/transferring_forms/sample_1_folder.png)

**Paso 5:** Entra en esta carpeta y **COPIA** todos los elementos (como se muestra en la imagen a continuación):

![Imagen de ejemplo de subcarpetas](images/transferring_forms/sub_folders.png)

**Paso 6:** Ahora, conecta el otro dispositivo Android al que deseas copiar los datos a la PC mediante el cable USB.

**Paso 7:** Una vez más, sigue la ruta que se ilustra a continuación (según la versión de la aplicación instalada):

-   Para la aplicación Android KoboCollect versión 2021.2 y posteriores:
    -   Si la aplicación Android KoboCollect está instalada en la memoria del teléfono:
        `Este equipo\Galaxy S10+\Phone\Android\data\org.koboc.collect.android\files\projects`
    -   Si la aplicación Android KoboCollect está instalada en la memoria externa:
        `Este equipo\Galaxy S10+\sdcard\Android\data\org.koboc.collect.android\files\projects`
-   Para la aplicación Android KoboCollect (versión mayor que v1.26.0):
    -   Si la aplicación Android KoboCollect está instalada en la memoria del teléfono:
        `Este equipo\Galaxy S10+\Phone\Android\data\org.koboc.collect.android\files`
    -   Si la aplicación Android KoboCollect está instalada en la memoria externa:
        `Este equipo\Galaxy S10+\sdcard\Android\data\org.koboc.collect.android\files`
-   Para la aplicación Android KoboCollect (versión menor que v1.26.0):
    -   Si la aplicación Android KoboCollect está instalada en la memoria del teléfono:
        `Este equipo\Galaxy S10+\Phone\odk`
    -   Si la aplicación Android KoboCollect está instalada en la memoria externa:
        `Este equipo\Galaxy S10+\sdcard\odk`

**Paso 8:** Una vez que estés en la carpeta **projects**, la carpeta **files** o la carpeta **odk** _(según la versión de la aplicación Android KoboCollect que estés usando)_, deberías ver una carpeta con un nombre similar (como se muestra a continuación):

![Imagen de ejemplo](images/transferring_forms/sample_2_folder.png)

**Paso 9:** Entra en esta carpeta y **PEGA** los elementos copiados:

![Imagen de ejemplo de subcarpetas](images/transferring_forms/sub_folders.png)

Una vez completado este proceso, abre la **aplicación Android KoboCollect** desde el dispositivo (en el que has pegado los formularios y datos). Ahora puedes usar este dispositivo para continuar con la recolección de datos y cargar los envíos al servidor.

<p class="note">
  Si los formularios y datos no son visibles, puedes intentar reiniciar tu dispositivo. Esto podría hacer que los formularios y datos sean visibles en la aplicación.
</p>

## Resolución de problemas

-   Al conectar el dispositivo Android original con el formulario y los datos que deseas copiar a la PC, es posible que a veces veas no solo una carpeta, sino varias (como se muestra en la imagen a continuación):
    ![Imagen de ejemplo de varias carpetas](images/transferring_forms/sample_many_folders.png)
    Esto puede resultar confuso y dificulta la selección del proyecto correcto que deseas copiar. Aunque lleva tiempo, tendrás que revisar todas las carpetas para identificar la carpeta correcta con el proyecto que buscas. También puedes eliminar las carpetas que ya no sean necesarias. Por ejemplo, si un proyecto ha sido eliminado de la aplicación, es posible que aún aparezca como carpeta cuando se accede al dispositivo desde la computadora. Si estás seguro de que un proyecto ya no es relevante, eliminar la carpeta lo borrará por completo.

-   Del mismo modo, al conectar el teléfono móvil Android sin la última versión del formulario (o incluso sin ningún formulario) a la PC, a veces verás no solo una carpeta sino varias (como se muestra en la imagen a continuación):
    ![Imagen de ejemplo de varias carpetas](images/transferring_forms/sample_many_folders.png)
    _Si el dispositivo ya tiene una versión anterior del formulario:_ Tendrás que identificar la carpeta correcta que contiene el proyecto que buscas. Después de identificar la carpeta correcta, debes pegar aquí todas las subcarpetas que copiaste.

_Si el dispositivo no tiene ninguna versión del formulario:_ Si tu dispositivo no tiene ninguna versión del formulario, pero aún ves varias carpetas, esto podría deberse a proyectos anteriores que fueron eliminados previamente de la aplicación. Como se describió anteriormente, eliminar un proyecto de la aplicación no necesariamente elimina estas carpetas. Puedes eliminar todas las carpetas innecesarias para liberar espacio. Actualiza la vista saliendo de la carpeta y volviendo a ella (es decir, la carpeta del proyecto, la carpeta files o la carpeta odk, según la versión de la aplicación Android KoboCollect que estés usando). Ahora deberías ver una sola carpeta. Una vez que hayas hecho clic en esta carpeta, puedes pegar todas las subcarpetas que copiaste anteriormente (es decir, forms, instances, etc.).

    _Si la aplicación KoboCollect está recién instalada en el dispositivo:_ Si acabas de instalar la aplicación KoboCollect en tu dispositivo, es posible que no veas ninguna carpeta sin antes configurar los ajustes del servidor, como se describe en el artículo de ayuda [Configuración de la aplicación KoboCollect](kobocollect_on_android_latest).

-   Si has copiado los formularios y datos de un dispositivo Android a otro y estás listo para enviar los envíos desde el dispositivo al servidor, pero aún tienes problemas para enviarlos, puedes consultar las sugerencias de configuración del servidor que se describen en el artículo de ayuda [Configuración de la aplicación KoboCollect](kobocollect_on_android_latest).