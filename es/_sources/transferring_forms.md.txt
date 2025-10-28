# Transferir formularios y datos manualmente de un dispositivo Android a otro
<a href="../transferring_forms.html">Read in English</a> | <a href="../fr/transferring_forms.html">Lire en français</a> | <a href="../ar/transferring_forms.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/7def5f54e2441b05b4a2163e682bdd146fa781e1/source/transferring_forms.md" class="reference">24 Sep 2025</a>

Puede haber ocasiones en las que estés en el campo sin conexión a internet,
pero aún necesites cargar la última versión de los formularios (es decir, los últimos
formularios desplegados en el servidor) a tu dispositivo. También es posible que no puedas cargar
los envíos de formularios al servidor debido a una pantalla rota. En ambos escenarios,
necesitarás transferir manualmente formularios y/o envíos utilizando otro dispositivo.
Este artículo de ayuda te mostrará cómo hacerlo.

Necesitarás los siguientes elementos para seguir las instrucciones descritas a continuación:

-   Un dispositivo Android que tenga la [aplicación de Android de KoboCollect](kobocollect_on_android_latest.md) con la última versión del formulario desplegado. (Se
    recomienda [obtener la última versión](https://support.kobotoolbox.org/es/data_collection_kobocollect.html#downloading-forms) del formulario desplegado en el dispositivo
    haciendo clic en **Descargar formulario** desde tu **aplicación de Android de KoboCollect**.)
-   Un dispositivo Android que no tenga la última versión del formulario (o incluso
    ningún formulario en absoluto).
-   Ambos dispositivos Android deben tener la aplicación de Android de KoboCollect ya instalada.
-   Computadora personal (de escritorio o portátil).
-   Cable USB que conecte el dispositivo y la computadora personal.

**Paso 1:** Abre tu computadora personal (no se necesita conexión a internet aquí).
Una PC es necesaria en esta fase para copiar los formularios y datos de un dispositivo Android
con la última versión del formulario a otro.

**Paso 2:** Ahora, conecta el dispositivo Android (con el último formulario y datos que
deseas transferir) a la PC usando el cable USB.

**Paso 3:** Luego, sigue la ruta ilustrada a continuación para extraer las carpetas
requeridas con los formularios y datos (dependiendo de qué versión de la aplicación esté instalada):

<p class="note">
  En este ejemplo, estamos conectando Galaxy S10+ (un dispositivo Android) a Windows
  11, por eso estás viendo <strong>Este equipo</strong> y
  <strong>Galaxy S10+</strong>. Estos pueden diferir si estás usando otro sistema operativo y
  dispositivo Android.
</p>

-   Para la aplicación de Android de KoboCollect versión 2021.2 y superior:
    -   Si la aplicación de Android de KoboCollect está instalada en la memoria del teléfono:
        `Este equipo\Galaxy S10+\Teléfono\Android\data\org.koboc.collect.android\files\projects`
    -   Si la aplicación de Android de KoboCollect está instalada en la memoria externa:
        `Este equipo\Galaxy S10+\sdcard\Android\data\org.koboc.collect.android\files\projects`
-   Para la aplicación de Android de KoboCollect (versión superior a v1.26.0):
    -   Si la aplicación de Android de KoboCollect está instalada en la memoria del teléfono:
        `Este equipo\Galaxy S10+\Teléfono\Android\data\org.koboc.collect.android\files`
    -   Si la aplicación de Android de KoboCollect está instalada en la memoria externa:
        `Este equipo\Galaxy S10+\sdcard\Android\data\org.koboc.collect.android\files`
-   Para la aplicación de Android de KoboCollect (versión inferior a v1.26.0):
    -   Si la aplicación de Android de KoboCollect está instalada en la memoria del teléfono:
        `Este equipo\Galaxy S10+\Teléfono\odk`
    -   Si la aplicación de Android de KoboCollect está instalada en la memoria externa:
        `Este equipo\Galaxy S10+\sdcard\odk`

**Paso 4:** Una vez que estés en la carpeta **projects**, carpeta **files**, o la
carpeta **odk** _(dependiendo de la versión de la aplicación de Android de KoboCollect que estés
usando)_, deberías ver una carpeta con un nombre similar (como se muestra a continuación):

![Imagen de muestra](images/transferring_forms/sample_1_folder.png)

**Paso 5:** Ingresa a esta carpeta y **COPIA** todos los elementos (como se muestra en la imagen
a continuación):

![Imagen de muestra de subcarpetas](images/transferring_forms/sub_folders.png)

**Paso 6:** Ahora, conecta el otro dispositivo Android al que deseas copiar los datos
con la PC usando el cable USB.

**Paso 7:** Una vez más, sigue la ruta ilustrada a continuación (dependiendo de qué
versión de la aplicación esté instalada):

-   Para la aplicación de Android de KoboCollect versión 2021.2 y superior:
    -   Si la aplicación de Android de KoboCollect está instalada en la memoria del teléfono:
        `Este equipo\Galaxy S10+\Teléfono\Android\data\org.koboc.collect.android\files\projects`
    -   Si la aplicación de Android de KoboCollect está instalada en la memoria externa:
        `Este equipo\Galaxy S10+\sdcard\Android\data\org.koboc.collect.android\files\projects`
-   Para la aplicación de Android de KoboCollect (versión superior a v1.26.0):
    -   Si la aplicación de Android de KoboCollect está instalada en la memoria del teléfono:
        `Este equipo\Galaxy S10+\Teléfono\Android\data\org.koboc.collect.android\files`
    -   Si la aplicación de Android de KoboCollect está instalada en la memoria externa:
        `Este equipo\Galaxy S10+\sdcard\Android\data\org.koboc.collect.android\files`
-   Para la aplicación de Android de KoboCollect (versión inferior a v1.26.0):
    -   Si la aplicación de Android de KoboCollect está instalada en la memoria del teléfono:
        `Este equipo\Galaxy S10+\Teléfono\odk`
    -   Si la aplicación de Android de KoboCollect está instalada en la memoria externa:
        `Este equipo\Galaxy S10+\sdcard\odk`

**Paso 8:** Una vez que estés en la carpeta **projects**, carpeta **files**, o la
carpeta **odk** _(dependiendo de la versión de la aplicación de Android de KoboCollect que estés
usando)_, deberías ver una carpeta con un nombre similar (como se muestra a continuación):

![Imagen de muestra](images/transferring_forms/sample_2_folder.png)

**Paso 9:** Ingresa a esta carpeta y **PEGA** los elementos copiados:

![Imagen de muestra de subcarpetas](images/transferring_forms/sub_folders.png)

Una vez que esto esté completo, abre la **aplicación de Android de KoboCollect** desde el dispositivo
(donde has pegado los formularios y datos). Ahora puedes usar este dispositivo para
continuar con la recolección de datos y cargar los envíos al servidor.

<p class="note">
  Si los formularios y datos no son visibles, puedes intentar reiniciar tu dispositivo.
  Esto podría hacer que los formularios y datos sean visibles en la aplicación.
</p>

## Solución de problemas:

-   Al conectar el dispositivo Android original con el formulario y datos que deseas
    copiar a la PC, a veces puedes ver no solo una carpeta, sino varias
    carpetas (como se muestra en la imagen a continuación):
    ![Imagen de muestra de muchas carpetas](images/transferring_forms/sample_many_folders.png)
    Esto es confuso y hace que sea difícil seleccionar el proyecto correcto que
    deseas copiar. Aunque consume tiempo, necesitarás revisar todas las
    carpetas para identificar la carpeta correcta con el proyecto que estás buscando.
    También podrías eliminar cualquier otra carpeta que ya no sea necesaria. Por
    ejemplo, si un proyecto ha sido eliminado de la aplicación, aún puede aparecer
    como una carpeta cuando se accede al dispositivo a través de la computadora. Si estás
    seguro/a de que un proyecto ya no es relevante, eliminar la carpeta lo eliminará
    completamente.

-   De manera similar, al conectar el teléfono móvil Android sin la última
    versión del formulario (o incluso sin ningún formulario en absoluto) a la PC, a veces verás
    no solo una carpeta sino varias carpetas (como se muestra en la imagen a continuación):
    ![Imagen de muestra de muchas carpetas](images/transferring_forms/sample_many_folders.png)
    _Si el dispositivo ya tiene una versión anterior del formulario:_ Necesitarás identificar
    la carpeta correcta que tiene el proyecto que estás buscando. Después de
    identificar la carpeta correcta, debes pegar todas las subcarpetas que
    has copiado aquí.

    _Si el dispositivo no tiene ninguna versión del formulario en absoluto:_ Si tu dispositivo no
    tiene ninguna versión del formulario, pero aún ves varias carpetas, esto podría ser
    de proyectos anteriores que fueron eliminados previamente en la aplicación. Como se describió
    anteriormente, eliminar un proyecto de la aplicación no necesariamente elimina estas
    carpetas. Puedes eliminar todas las carpetas innecesarias para limpiar el espacio.
    Actualiza tu vista saliendo de la carpeta y regresando a ella (es decir, carpeta
    project, o carpeta files, o la carpeta odk dependiendo de la versión de la aplicación de Android de KoboCollect que estés usando). Ahora deberías ver una sola carpeta. Una
    vez que hayas hecho clic en esta carpeta, ahora puedes pegar todas las subcarpetas
    que copiaste previamente (es decir, forms, instances, etc.).

    _Si la aplicación de KoboCollect está recién instalada en el dispositivo:_ Si has
    instalado recientemente la aplicación de KoboCollect en tu dispositivo, es posible que no veas ninguna carpeta
    sin antes configurar los ajustes del servidor, como se describe en el artículo de ayuda
    [Recolección de datos en la aplicación de KoboCollect)](kobocollect_on_android_latest).

-   Si has copiado los formularios y datos de un dispositivo Android a otro y
    estás listo/a para enviar los envíos desde el dispositivo al servidor, pero aún
    tienes problemas para enviarlos, puedes consultar las sugerencias de configuración
    del servidor que se han descrito en el artículo de ayuda ["Recolección de datos en la aplicación de KoboCollect")](kobocollect_on_android_latest).