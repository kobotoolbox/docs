# Almacenamiento de datos
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/592a15ee470fa144eeac9850c6b6a648c4755306/source/data_storage.md" class="reference">11 Sep 2023</a>


Ya sea que uses el [Servidor Global](https://kf.kobotoolbox.org/) o el
[Servidor con sede en la Unión Europea](https://eu.kobotoolbox.org/), los datos de
ambos servidores se almacenan en los servidores de Amazon Web Services (AWS).

Hay 2 tipos de datos almacenados en AWS: el formulario en sí y los archivos adjuntos
relacionados con cada envío. Los datos del formulario se guardan en la base de datos (DB)
y los archivos adjuntos se guardan en Simple Storage Service (S3). Los datos almacenados
en la base de datos nunca se eliminan a menos que los elimines tú mismo. Los
datos recolectados en S3 tampoco se eliminan, a menos que los elimines tú mismo o que
uses más espacio del permitido según las
[políticas de Kobo](../es/creating_account.md).

Puedes conservar hasta 10 exportaciones de datos a la vez por proyecto. Si creas una
exportación número 11, la más antigua se elimina y solo se conservan las 10 exportaciones
más recientes.

Para obtener más información sobre las medidas de seguridad de datos de KoboToolbox, consulta
este [Seguridad de datos en KoboToolbox](../es/is_my_data_safe.md).