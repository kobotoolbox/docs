# Servicios REST
<a href="../rest_services.html">Read in English</a> | <a href="../fr/rest_services.html">Lire en français</a> | <a href="../ar/rest_services.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/7ca46b8455887292b012aeb709e7e244245bf6b9/source/rest_services.md" class="reference">7 Jul 2023</a>

**Cómo vincular tus datos a otros servidores o servicios usando Servicios REST**

KoboToolbox tiene una serie de funcionalidades avanzadas integradas basadas en nuestras bibliotecas de código abierto, que incluyen complementos útiles para casos de uso avanzados.

Puedes vincular tus datos recolectados con KoboToolbox a otros servidores o servicios que poseas a través de Servicios REST. Los Servicios REST admiten formatos JSON o XML, y autenticación básica. Además, es posible enviar solo un subconjunto de campos.

En caso de fallo, la tarea en segundo plano intentará 3 veces enviar los datos (la primera vez después de 60 segundos, la segunda vez después de 600 segundos, y la tercera vez después de 6,000 segundos). Se pueden habilitar notificaciones por correo electrónico para recibir un reporte de fallo.

Ten en cuenta que tus datos se envían al servidor externo solo al momento de la creación. No se envía nada cuando los datos son editados.

Aquí hay algunos videos tutoriales para usar Servicios REST:

1. Creación

    [![Creación](/images/rest_services/thumbnail_1.jpg)](https://fast.wistia.net/embed/iframe/6i2hw2gcr1 "Creation")

2. Subconjunto de campos (Los campos se agregan presionando "Enter" o "Tab")

    [![Subconjunto de campos](/images/rest_services/thumbnail_2.jpg)](https://fast.wistia.net/embed/iframe/u6su0atm2w "Subset of fields")

3. Fallo/Reintento

    [![Fallo / Reintento](/images/rest_services/thumbnail_3.jpg)](https://fast.wistia.net/embed/iframe/7my5eab5lm "Failure / Retry")

4. Envoltura personalizada (Solo disponible con formato JSON)

    [![Envoltura personalizada](/images/rest_services/thumbnail_4.jpg)](https://fast.wistia.net/embed/iframe/pd0czyksbx "Custom Wrapper")