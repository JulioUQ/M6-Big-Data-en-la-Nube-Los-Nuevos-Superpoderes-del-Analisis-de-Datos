# **Laboratorio 1: Introducción a AWS IAM**

## 1. ¿Qué es AWS IAM?

**AWS Identity and Access Management (IAM)** es el servicio de AWS que permite:

- Crear y administrar **usuarios**, **grupos** y **roles**
- Controlar **qué acciones** pueden realizar sobre **qué recursos**
- Gestionar credenciales de seguridad (contraseñas, claves de acceso, MFA)

IAM funciona bajo el principio de **mínimo privilegio**: cada usuario solo debe tener los permisos estrictamente necesarios.

---

## 2. Objetivos del laboratorio

En este laboratorio se aprende a:

1. Explorar usuarios y grupos de IAM ya creados
2. Analizar políticas de IAM asociadas a grupos
3. Asignar usuarios a grupos según un caso real
4. Localizar y usar la URL de inicio de sesión de IAM
5. Probar cómo las políticas afectan el acceso a servicios AWS

⏱ **Duración estimada**: 40 minutos

---
## 3. Restricciones del entorno

- El laboratorio tiene **permisos limitados**
- Algunos errores de tipo _“Not authorized”_ son **normales**
- Solo se permite usar los servicios necesarios para el laboratorio

---
## 4. Acceso a la consola de AWS

1. Seleccionar **Start Lab**
2. Esperar a que el indicador de AWS se ponga en **verde**
3. Abrir la **Consola de administración de AWS**
4. Mantener abiertas las instrucciones y la consola a la vez
---
## 5. Tarea 1: Analizar usuarios y grupos

### 5.1 Usuarios de IAM existentes

Usuarios creados previamente:
- `user-1`
- `user-2`
- `user-3`

**Estado inicial de los usuarios:**
- No tienen permisos directos
- No pertenecen a ningún grupo
- Todos tienen contraseña para la consola

---
### 5.2 Grupos de IAM existentes

Grupos creados:
- **EC2-Support**
- **S3-Support**
- **EC2-Admin**

---
### 5.3 Políticas asociadas a los grupos

#### 🔹 EC2-Support

- Política administrada: **AmazonEC2ReadOnlyAccess**
- Permite:
    - Ver información de EC2
    - No permite modificar recursos

- Uso típico: **soporte técnico**    
---
#### 🔹 S3-Support

- Política administrada: **AmazonS3ReadOnlyAccess**
- Permite
    - Listar buckets
    - Ver contenido de S3

- No permite:
    - Crear, modificar o borrar objetos

---
#### 🔹 EC2-Admin

- Política **insertada** (no administrada)
- Permite:
    - Ver instancias EC2
    - Iniciar y detener instancias

- Uso típico: **administrador de EC2**
---
## 6. Situación empresarial (caso práctico)

|Usuario|Grupo asignado|Permisos|
|---|---|---|
|user-1|S3-Support|Solo lectura en Amazon S3|
|user-2|EC2-Support|Solo lectura en Amazon EC2|
|user-3|EC2-Admin|Ver, iniciar y detener EC2|

---
## 7. Tarea 2: Agregar usuarios a los grupos

### 7.1 Asignaciones realizadas

- `user-1` → **S3-Support**
- `user-2` → **EC2-Support**
- `user-3` → **EC2-Admin**

📌 **Resultado esperado**:

- Cada grupo muestra **1 usuario**
- Los usuarios heredan permisos del grupo

---
## 8. Tarea 3: Inicio de sesión y pruebas

### 8.1 URL de inicio de sesión IAM

Formato:

```
https://857208194947.signin.aws.amazon.com/console
```

Se usa para iniciar sesión **como usuario IAM**, no como root.

---
## 9. Pruebas de acceso por usuario

### 🔹 user-1 (S3-Support)

**Credenciales:**

- Usuario: `user-1`
- Contraseña: `Lab-Password1`

**Resultados:**

- ✅ Puede acceder a **Amazon S3**
- ✅ Puede ver buckets (vacíos)
- ❌ No puede acceder a **EC2**
- ❌ Mensaje: _Not authorized_

✔️ Comportamiento correcto según permisos

---
### 🔹 user-2 (EC2-Support)

**Credenciales:**
- Usuario: `user-2`
- Contraseña: `Lab-Password2`

**Resultados:**
- ✅ Puede ver instancias EC2
- ❌ No puede detener la instancia `LabHost`
- ❌ No puede acceder a S3

✔️ Acceso de solo lectura confirmado

---
### 🔹 user-3 (EC2-Admin)

**Credenciales:**
- Usuario: `user-3`
- Contraseña: `Lab-Password3`

**Resultados:**
- ✅ Puede ver instancias EC2
- ✅ Puede detener la instancia `LabHost`
- ❌ No tiene permisos sobre S3

✔️ Acceso administrativo validado

---
## 10. Envío del laboratorio

1. Seleccionar **Submit**
2. Esperar al menos **5 minutos**
3. Revisar calificaciones en **Grades**
4. Consultar detalles en **Submission Report**
5. Finalizar con **End Lab**

---
## 11. Conclusión (RESUMEN FINAL)

### ✅ El laboratorio queda correctamente resuelto cuando:

- Los usuarios están asignados a los grupos correctos
- Cada usuario tiene **solo los permisos esperados**
- Se verifica el principio de **mínimo privilegio**
- Se confirma el efecto real de las políticas IAM

### 📚 Aprendizajes clave

- Diferencia entre políticas administradas e insertadas
- Uso práctico de grupos IAM
- Control granular de acceso a AWS    
- Validación de permisos mediante pruebas reales


---

