# Almacenamiento de datos
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/592a15ee470fa144eeac9850c6b6a648c4755306/source/data_storage.md" class="reference">11 Sep 2023</a>

Ya sea que estés usando el [Servidor Global](https://kf.kobotoolbox.org/) o el
[Servidor con sede en la Unión Europea](https://eu.kobotoolbox.org/), los datos de
ambos servidores se almacenan en servidores de Amazon Web Services (AWS).

Hay 2 tipos de datos almacenados en AWS: el formulario en sí y los archivos adjuntos
relacionados con cada envío. Los datos del formulario se guardan en la base de datos (DB)
y los archivos adjuntos se guardan en Simple Storage Service (S3). Los datos almacenados
en la base de datos nunca se eliminan a menos que tú mismo/a elimines los datos. Los
datos recolectados en S3 tampoco se eliminan nunca, a menos que tú mismo/a los elimines o
termines usando más espacio del que se te permite según las
[políticas de Kobo](creating_account.md).

Puedes mantener hasta 10 exportaciones de datos a la vez por proyecto. Si creas una undécima
exportación, la más antigua se elimina y solo se conservan las 10 exportaciones más recientes.

Para obtener más información sobre las medidas de seguridad de datos de KoboToolbox, consulta este
otro [artículo de ayuda](is_my_data_safe.md).