# Tipo de pregunta de firma
<a href="../collecting_signatures.html">Read in English</a> | <a href="../fr/collecting_signatures.html">Lire en français</a> | <a href="../ar/collecting_signatures.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/collecting_signatures.md" class="reference">29 Jul 2025</a>

Algunos formularios pueden requerir que se incluyan firmas con ellos. Puedes usar
la apariencia `signature` tanto en la aplicación de Android de Collect como en Enketo. El widget de dibujo
solo está disponible cuando usas Enketo para la recolección de datos.

## Aplicación de Android de Collect

Collect permite que se recolecte una firma digital directamente en la pantalla del
teléfono/tableta.

Para agregar esto a tu formulario:

1. Abre o descarga la versión XLS de tu formulario.
2. Crea la pregunta y establece el tipo como `image`
3. Establece la apariencia como `signature`

## Enketo

Las firmas digitales también funcionan en los formularios web de Enketo, donde tienes la opción
adicional de usar un widget de dibujo para recolectar firmas. En tu XLSForm simplemente agrega
`signature` o `draw` bajo la columna `appearance` para una pregunta de tipo `image`.

**hoja survey**

| type  | name | label            | appearance | hint                                       |
| :---- | :--- | :--------------- | :--------- | :----------------------------------------- |
| image | draw | Widget de dibujo | draw       | Tipo imagen con apariencia de dibujo       |
| image | sign | Widget de firma  | signature  | Tipo imagen con widget de firma            |
| survey |

[Sigue este enlace](https://enke.to/draw) para probar la diferencia entre los widgets de dibujo
y firma.

## Crear un tipo de pregunta de Firma en el editor de formularios

1. Crea una nueva pregunta y selecciona Foto como el tipo de pregunta.

![image](/images/collecting_signatures/new_question.jpg)

2. En la Configuración bajo Opciones de pregunta, haz clic en el menú desplegable de Apariencia y
   selecciona Firma.

![image](/images/collecting_signatures/signature.jpg)