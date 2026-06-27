# Tipo de pregunta Firma

Algunos formularios pueden requerir que se incluyan firmas. Puedes usar la apariencia `signature` tanto en la aplicación KoboCollect como en Enketo. El widget draw solo está disponible cuando usas Enketo para la recolección de datos.

## Aplicación KoboCollect

KoboCollect permite recolectar una firma digital directamente en la pantalla del teléfono o tableta.

Para agregar esto a tu formulario:

1. Abre o descarga la versión XLS de tu formulario.
2. Crea la pregunta y configura el tipo como `image`
3. Configura la apariencia como `signature`

## Enketo

Las firmas digitales también funcionan en los formularios web de Enketo, donde tienes la opción adicional de usar un widget draw para recolectar firmas. En tu XLSForm, simplemente añade `signature` o `draw` en la columna `appearance` para una pregunta de tipo `image`.

**hoja survey**

| type  | name | label            | appearance | hint                             |
| :---- | :--- | :--------------- | :--------- | :------------------------------- |
| image | draw | Draw widget      | draw       | Image type with draw appearance  |
| image | sign | Signature widget | signature  | Image type with signature widget |
| survey |

[Sigue este enlace](https://enke.to/draw) para probar la diferencia entre los widgets draw y signature.

## Crear un tipo de pregunta Firma en el Formbuilder

1. Crea una nueva pregunta y selecciona Foto como el tipo de pregunta.

![image](/images/collecting_signatures/new_question.jpg)

2. En Configuraciones, en Opciones de preguntas, haz clic en el menú desplegable Apariencia y selecciona signature (firma).

![image](/images/collecting_signatures/signature.jpg)