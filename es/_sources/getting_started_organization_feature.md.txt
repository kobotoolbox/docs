# Usar la función de gestión de equipos
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/7f800b38e7b07803e7abd456195dd5519b03240e/source/getting_started_organization_feature.md" class="reference">3 Oct 2025</a>


La nueva función de gestión de equipos te permite centralizar la gestión de proyectos y usuarios para mejorar la supervisión y la colaboración en equipos grandes y distribuidos. Cuando agregas usuarios a tu equipo en KoboToolbox, tendrás acceso para ver y gestionar sus proyectos. Los usuarios de tu equipo tendrán acceso a las cuotas de uso de tu plan Teams o Enterprise, y la propiedad de sus proyectos será transferida a tu equipo.

Este artículo incluye:

-   Propiedad de proyectos, roles y vistas de proyectos para equipos
-   Cómo invitar usuarios a unirse a tu equipo y asignar roles
-   Cómo eliminar usuarios de tu equipo

<p class="note">
  <b>Nota:</b> Esta función actualmente solo está disponible para usuarios con planes <a class="reference external" href="https://www.kobotoolbox.org/teams/">Teams</a> y <a class="reference external" href="https://www.kobotoolbox.org/enterprise/">Enterprise</a>.
</p>

## Propiedad de proyectos

Un aspecto clave de la función de gestión de equipos es que la propiedad de los proyectos está centralizada dentro de tu equipo.

-   Cualquier proyecto nuevo creado por un usuario de tu equipo es automáticamente propiedad de tu equipo.
-   Cuando un usuario se une a un equipo en KoboToolbox, todos los proyectos de su propiedad serán transferidos al equipo.

Al centralizar la propiedad de los proyectos, la función de gestión de equipos te brinda mayor supervisión y una gestión de equipos más eficaz.

<p class="note">
  <b>Nota:</b> Esta función solo afecta la propiedad de los proyectos. No afecta los permisos para compartir proyectos. Los permisos de uso compartido configurados anteriormente no se verán afectados cuando la propiedad del proyecto se transfiera a un equipo. Si tienes permisos de gestión para un proyecto, seguirás teniendo esos permisos y podrás compartir el proyecto como de costumbre. Para más información, consulta <a class="reference external" href="https://support.kobotoolbox.org/es/managing_permissions.html">Compartir proyectos con permisos a nivel de usuario/a</a>.
</p>

## Roles para equipos

Existen tres roles diferentes para los miembros de un equipo, cada uno con funciones y capacidades específicas.

1. **Propietario:** El propietario puede ver y gestionar todos los proyectos y usuarios del equipo, así como el plan y la configuración. Cada equipo en KoboToolbox puede tener un solo propietario.
   - **Vistas y gestión de proyectos:** El propietario puede ver todos los proyectos del equipo y tiene permisos completos de gestión de proyectos.
   - **Transferencias de propiedad de proyectos:** El propietario puede [transferir la propiedad](https://support.kobotoolbox.org/es/project_sharing_settings.html#transferring-ownership-of-a-project) de cualquier proyecto del equipo a un usuario externo al equipo.
   - **Gestión de usuarios:** El propietario puede agregar o eliminar miembros del equipo y asignar diferentes roles.
   - **Gestión del plan y el uso:** El propietario puede gestionar el plan y la configuración del equipo, y ver la página de uso.

2. **Administradores:** Los administradores pueden ver y gestionar todos los proyectos y usuarios del equipo, así como la configuración. Cada equipo puede tener un número ilimitado de administradores.
   - **Vistas y gestión de proyectos:** Los administradores pueden ver todos los proyectos del equipo y tienen permisos completos de gestión de proyectos.
   - **Gestión de usuarios:** Los administradores pueden agregar o eliminar miembros del equipo y asignar diferentes roles.
   - **Gestión del plan y el uso:** Los administradores pueden gestionar la configuración del equipo y ver la página de uso.

3. **Miembros:** Los miembros del equipo siguen teniendo acceso completo a su cuenta de KoboToolbox con el beneficio de las cuotas de uso de su equipo. Los miembros pueden crear nuevos proyectos y usar todas las funcionalidades de KoboToolbox como antes. Los equipos pueden tener un número ilimitado de miembros.

<p class="note">
  <b>Nota:</b> Los usuarios solo pueden pertenecer a un equipo a la vez.
</p>

## Vistas de proyectos

El propietario y los administradores del equipo tienen acceso a la vista **Proyectos del equipo** y a su propia vista personal **Mis proyectos**.

-   De forma predeterminada, se mostrará tu vista **Mis proyectos**. Si haces clic en el menú desplegable de vistas de proyectos, puedes cambiar a la vista **Proyectos del equipo**.
-   La vista **Proyectos del equipo** incluye todos los proyectos de todos los usuarios del equipo.

Los miembros del equipo solo tienen acceso a su vista personal **Mis proyectos**, que incluye los proyectos que crearon y los proyectos compartidos con ellos. No tienen acceso a la vista **Proyectos del equipo**.

![image](/images/getting_started_organization_feature/organizations_project_views.gif)

<br/>

## Invitar usuarios a unirse a tu equipo

El propietario y los administradores del equipo pueden invitar usuarios a unirse al equipo, dándoles acceso a las cuotas de uso del equipo y centralizando la gestión de proyectos.

Para invitar usuarios a unirse a tu equipo en KoboToolbox:

1. Ve a tu **Configuración de la cuenta**.
2. Navega a la página **Miembros** en **EQUIPO**.
3. Haz clic en el botón **Invitar miembros**.
4. Ingresa el **nombre de usuario** o la **dirección de correo electrónico** de la persona que deseas invitar a tu equipo y asígnale un **rol**. Haz clic en **Enviar invitación**.
   - Las invitaciones no están restringidas a usuarios con el dominio de correo electrónico de tu organización. Puedes invitar a usuarios con cualquier dirección de correo electrónico válida.
5. El usuario recibirá una invitación por correo electrónico para unirse a tu equipo. Si el usuario aún no tiene una cuenta de KoboToolbox, se le invitará a crear una.
6. Cuando acepte la invitación, obtendrá acceso a tu equipo según el rol que se le haya asignado. Todos los proyectos que eran propiedad del usuario anteriormente serán transferidos a tu equipo.

![image](/images/getting_started_organization_feature/organizations_inviting_a_user.gif)

<br/>

Una invitación para unirse a un equipo expirará **14 días** después de ser enviada. Puedes **reenviar la invitación** directamente desde el menú <i class="k-icon k-icon-more"></i> **Otras acciones** de la vista **Miembros**. También puedes **cancelar una invitación** usando la opción **Eliminar invitación** en el menú <i class="k-icon k-icon-more"></i> **Otras acciones**.

![image](/images/getting_started_organization_feature/organizations_resend_invitation.gif)

<br/>

<p class="note">
  <b>Nota:</b> Si tienes proyectos existentes cuya propiedad no deseas transferir a tu equipo, te recomendamos que crees una cuenta separada y transfieras la propiedad de esos proyectos a la nueva cuenta antes de aceptar la invitación para unirte al equipo.
</p>

## Asignar y gestionar roles

El propietario y los administradores del equipo pueden asignar y cambiar los roles de los usuarios de su equipo en la vista **Miembros**.

-   Cuando cambias el rol de un **miembro** a **administrador**, le otorgas acceso a la vista Proyectos del equipo, así como permisos de gestión de proyectos y roles. También le otorgas acceso para gestionar la configuración y ver la página de uso.

![image](images/getting_started_organization_feature/organizations_changing_roles.png)

## Eliminar un usuario de tu equipo

El propietario y los administradores del equipo pueden eliminar usuarios del equipo. Cuando se elimina a un usuario de tu equipo, ya no tendrá acceso a los proyectos propiedad del equipo ni a las cuotas de uso del equipo.

Para eliminar un usuario de tu equipo:

1. Ve a tu **Configuración de la cuenta**.
2. Navega a la página **Miembros** en **EQUIPO**.
3. Haz clic en el icono <i class="k-icon k-icon-more"></i> **Otras acciones** del usuario que deseas eliminar.
4. Selecciona **Eliminar**.
5. Confirma y completa la acción haciendo clic en **Eliminar miembro**.

![image](/images/getting_started_organization_feature/organizations_removing_a_member.gif)

<br/>

## Transferir la propiedad de tu equipo

Cada equipo en KoboToolbox puede tener un solo propietario. El propietario fue determinado previamente por tu organización cuando se suscribió al plan.

Para transferir la propiedad de tu equipo a otro usuario, [comunícate con nuestro equipo de soporte](support@kobotoolbox.org).