# 🔐 CREDENCIALES Y CLAVE DE ACCESO INSTITUCIONAL
**Empresa Titular:** Asesorías Pedagógicas S.A.S.  
**Plataforma:** Plataforma Curricular Multiárea de Derechos Básicos de Aprendizaje (DBA 1° a 11°)  
**Fecha de Actualización:** 14 de Octubre de 2026  

---

## 🔑 Clave de Acceso Oficial

| Parámetro | Valor Oficial |
| :--- | :--- |
| **Contraseña / Clave Institucional:** | `Asesorias2026*` |
| **Entidad:** | Asesorías Pedagógicas S.A.S. |
| **Archivo de Seguridad:** | [`auth-gatekeeper.js`](file:///D:/WILMER_FERRER/JSON/DBA_Antigravity/auth-gatekeeper.js) |
| **Archivo Principal del Portal:** | [`index.html`](file:///D:/WILMER_FERRER/JSON/DBA_Antigravity/index.html) |

---

## 📋 Instrucciones de Uso

1. Al abrir el archivo [`index.html`](file:///D:/WILMER_FERRER/JSON/DBA_Antigravity/index.html) en cualquier navegador moderno (Edge, Chrome, Firefox, Safari), aparecerá la pantalla de bloqueo de bienvenida institucional de **Asesorías Pedagógicas S.A.S.**.
2. Ingrese la clave exacta:
   ```text
   Asesorias2026*
   ```
   *(Respete las mayúsculas iniciales y el asterisco final).*
3. Presione la tecla **Enter** o haga clic en **«Ingresar a la Plataforma Curricular»**.
4. Una vez autorizado, la sesión se mantendrá activa automáticamente mientras la pestaña permanezca abierta.

---

## 🛠️ ¿Dónde se Encuentra Configurada la Contraseña?

La clave se encuentra definida en la línea 9 del archivo de seguridad [`auth-gatekeeper.js`](file:///D:/WILMER_FERRER/JSON/DBA_Antigravity/auth-gatekeeper.js):

```javascript
const AUTH_CONFIG = {
  ACCESS_KEY: "Asesorias2026*", // <-- Clave institucional modificable
  SESSION_KEY: "asesorias_pedagogicas_auth_session"
};
```

Si en el futuro requiere cambiar la contraseña:
1. Abra [`auth-gatekeeper.js`](file:///D:/WILMER_FERRER/JSON/DBA_Antigravity/auth-gatekeeper.js) con cualquier editor de texto o código.
2. Modifique el valor de `ACCESS_KEY`.
3. Actualice este documento [`CREDENCIALES_ACCESO.md`](file:///D:/WILMER_FERRER/JSON/DBA_Antigravity/CREDENCIALES_ACCESO.md) para conservar siempre el registro.
