# Validación de registros
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/d5cdd698b4a91c3c45216f5a0f91ff7f0704a495/source/record_validation.md" class="reference">19 Jun 2020</a>

Un/a propietario/a de proyecto ahora puede otorgar un permiso de "Puede validar" a otros/as usuarios/as. Los/as usuarios/as con este permiso pueden ver un registro, editarlo si es necesario y asignar un estado al registro en cuestión. Asignar un estado a un registro/envío en particular eleva los estándares de recolección de datos para equipos con más de un/a encuestador/a.

## ¿Cuáles son los estados que puedes asignar a un registro?

Las etiquetas de estado de validación disponibles incluyen:

* **En espera**: El registro está bajo revisión.
* **Aprobado**: Los datos dentro de este registro son precisos.
* **Marcado para eliminación**: Los datos dentro de este registro deben eliminarse del conjunto de datos.

## Descripción general de la funcionalidad

* Este nuevo permiso agrega una columna "Validado" a la tabla de datos de tu proyecto.

    ![image](/images/record_validation/validated.png)

* Los/as usuarios/as pueden filtrar la vista de tabla según el estado de validación o cualquier otra pregunta de selección única. Por ejemplo, puedes usar estos filtros para ver los envíos asociados con un/a encuestador/a en particular, en el Distrito X. Es posible usar más de un filtro a la vez.

    ![image](/images/record_validation/filter.png)

* Establece un estado de validación para múltiples registros, o todos, a la vez.

    Para actualizar múltiples registros, simplemente selecciona los registros haciendo clic en la casilla de verificación a la izquierda del registro, y luego haz clic en "Actualizar seleccionados" para seleccionar el nuevo estado.

    Para actualizar todos los registros en la página, selecciona la casilla de verificación en la parte superior izquierda; o para actualizar todos los registros en tu conjunto de datos, selecciona el texto azul que dice "Seleccionar todos los XXX". Luego, haz clic en "Actualizar seleccionados" para seleccionar el nuevo estado.

    ![image](/images/record_validation/select.png)