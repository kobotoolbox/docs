# Usar servicios REST
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/7ca46b8455887292b012aeb709e7e244245bf6b9/source/rest_services.md" class="reference">7 jul 2023</a>


**Cómo vincular tus datos a otros servidores o servicios usando los Servicios REST**

KoboToolbox cuenta con una serie de funcionalidades avanzadas integradas basadas en nuestras bibliotecas de código abierto, que incluyen complementos útiles para casos de uso avanzados.

Puedes vincular los datos recolectados con KoboToolbox a otros servidores o servicios que tengas a través de los Servicios REST. Los Servicios REST admiten los formatos JSON o XML y autenticación básica. Además, es posible enviar solo un subconjunto de campos.

En caso de fallo, la tarea en segundo plano intentará enviar los datos 3 veces (la primera vez después de 60 segundos, la segunda después de 600 segundos y la tercera después de 6.000 segundos). Puedes activar las notificaciones por correo electrónico para recibir un informe de fallos.

Ten en cuenta que tus datos se envían al servidor externo únicamente al momento de la creación. No se envía nada cuando se editan los datos.

A continuación encontrarás algunos videos tutoriales sobre el uso de los Servicios REST:

1. Creación

    [![Creación](/images/rest_services/thumbnail_1.jpg)](https://fast.wistia.net/embed/iframe/6i2hw2gcr1 "Creación")

2. Subconjunto de campos (Los campos se agregan presionando "Enter" o "Tab")

    [![Subconjunto de campos](/images/rest_services/thumbnail_2.jpg)](https://fast.wistia.net/embed/iframe/u6su0atm2w "Subconjunto de campos")

3. Fallo/Reintento

    [![Fallo / Reintento](/images/rest_services/thumbnail_3.jpg)](https://fast.wistia.net/embed/iframe/7my5eab5lm "Fallo / Reintento")

4. Envoltorio personalizado (Solo disponible con formato JSON)

    [![Envoltorio personalizado](/images/rest_services/thumbnail_4.jpg)](https://fast.wistia.net/embed/iframe/pd0czyksbx "Envoltorio personalizado")