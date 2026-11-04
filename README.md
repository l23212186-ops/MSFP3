[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=l23212186-ops/MSFP3)

# Práctica — Modelado y control del sistema musculoesquelético

Repositorio académico de la asignatura **Modelado de Sistemas Fisiológicos**, correspondiente al programa de **Ingeniería Biomédica** del Tecnológico Nacional de México / Instituto Tecnológico de Tijuana. Esta práctica integra modelado mecánico de tejidos viscoelásticos, analogías electromecánicas fuerza-voltaje, análisis temporal y de estabilidad, diseño de controladores PID, simulación computacional (*in silico*) y verificación entre plataformas de software.

El caso de estudio representa las propiedades mecánicas de un compartimento del **sistema musculoesquelético** mediante un modelo mecánico viscoelástico (elementos activos, elásticos y viscosos) y su circuito eléctrico equivalente. Se busca analizar y comparar la respuesta temporal del desplazamiento $x(t)$ ante una fuerza aplicada $F(t)$, contrastando la dinámica de un **individuo sano (control)** contra un caso simulado de **atrofia muscular (caso)**, tanto en lazo abierto como en lazo cerrado con un controlador PID.

**Docente:** Dr. Paul Antonio Valle Trujillo  
**Correo:** paul.valle@tectijuana.edu.mx  
**Departamento:** Ingeniería Eléctrica y Electrónica  
**Institución:** Tecnológico Nacional de México / Instituto Tecnológico de Tijuana  
**Asignatura:** Modelado de Sistemas Fisiológicos  
**Programa:** Ingeniería Biomédica  
**Estudiante:** Christian Cid Pacheco · 23212186 · l23212186@tectijuana.edu.mx  

**Repositorio de la asignatura:** https://github.com/DrPaulValle/MSF-IBF1020  
**Sede:** Blvd. Alberto Limón Padilla s/n, Tijuana, C. P. 22454, B. C., México.

---

<a id="contenido"></a>
## Contenido

1. [Resumen](#resumen)
2. [Competencia y objetivos](#objetivos)
3. [Relación con el temario](#temario)
4. [Modelo físico y analogía electromecánica](#analogia)
5. [Formulación matemática](#modelo)
6. [Análisis temporal y de estabilidad](#analisis)
7. [Señales de entrada y condiciones de simulación](#senales)
8. [Implementación en MATLAB, Simulink y Simscape](#matlab)
9. [Control en lazo cerrado y sintonización PID](#pid)
10. [Reproducción en Python](#python)
11. [Resultados y verificación cruzada](#resultados)
12. [Diagrama biológico](#diagrama-biologico)
13. [Flujo de trabajo](#flujo)
14. [Actividades del estudiante](#actividades)
15. [Estructura del repositorio](#estructura)
16. [Requisitos](#requisitos)
17. [Reproducibilidad y entregables](#reproducibilidad)
18. [Referencias](#referencias)

---

<a id="resumen"></a>
## Resumen

La práctica tiene como propósito **analizar, simular y controlar un modelo mecánico del sistema musculoesquelético** empleando herramientas computacionales y técnicas de control clásico. Las propiedades viscoelásticas del tejido muscular y tendinoso se describen mediante una combinación de elemento contráctil activo ($F_0$), elemento elástico en serie ($C_s$), elemento elástico en paralelo ($C_p$) y amortiguador viscoso ($R$). A partir de la **analogía fuerza-voltaje**, este sistema mecánico se convierte en su circuito eléctrico equivalente.

Se derivan las ecuaciones diferenciales y la función de transferencia $G(s) = X(s)/F(s)$ para evaluar la respuesta dinámica ante una entrada de fuerza impulsiva. Se evalúan y comparan dos condiciones: un **individuo sano (control)** y un paciente con **atrofia muscular (caso)**, cuya alteración se modela mediante el incremento de la resistencia viscosa $R$. Posteriormente, se incorpora un **controlador PID en lazo cerrado** actuando sobre el caso atrófico, tomando como referencia la respuesta del individuo sano, para reducir la diferencia entre ambas respuestas. Todos los resultados se simulan *in silico* y se verifican de forma cruzada en MATLAB/Simulink, Simscape Electrical y Python.

Esta es una **práctica de simulación *in silico* y verificación cruzada**: permite comprender el modelado biomecánico, las transformaciones entre dominios físicos y el diseño de estrategias de regulación sobre patologías neuromusculares.

**Palabras clave:** sistema musculoesquelético; atrofia muscular; analogía fuerza-voltaje; viscoelasticidad; controlador PID; MATLAB; Simulink; Simscape Electrical; Python; simulación *in silico*.

[Volver al contenido](#contenido)

---

<a id="objetivos"></a>
## Competencia y objetivos

### Competencia a desarrollar

Modelizar sistemas fisiológicos mediante analogías entre sistemas físicos, ecuaciones diferenciales y funciones de transferencia para analizar su comportamiento dinámico y diseñar estrategias de control mediante técnicas de control clásico. En particular, analizar un modelo mecánico simplificado del sistema musculoesquelético, construir su circuito eléctrico equivalente mediante la analogía fuerza-voltaje, comparar la respuesta de un individuo sano (control) con un caso simulado de atrofia muscular (caso) y diseñar una estrategia de control *in silico* orientada a reducir las diferencias entre ambas respuestas.

### Objetivo general

Formular el modelo matemático y el circuito equivalente de un compartimento musculoesquelético viscoelástico, simular su respuesta temporal ante una fuerza aplicada en condiciones de salud y patología (atrofia muscular), y diseñar un sistema de control PID en lazo cerrado *in silico* que aproxime la dinámica del paciente a la de la referencia sana.

### Objetivos específicos

- Identificar los componentes mecánicos del músculo (elemento contráctil, elástico serie, elástico paralelo y amortiguador) y sus variables asociadas.
- Construir el circuito eléctrico equivalente aplicando rigurosamente las reglas de la analogía fuerza-voltaje.
- Derivar la función de transferencia $G(s) = X(s)/F(s)$ para los escenarios de control y caso.
- Determinar la localización de los polos, la estabilidad y el error en estado estacionario de ambos escenarios.
- Simular la respuesta al impulso en lazo abierto mediante MATLAB, Simulink, Simscape Electrical y Python.
- Diseñar y sintonizar un controlador PID utilizando la herramienta `Tune` de Simulink para minimizar la señal de error $e(t) = x_{\mathrm{control}}(t) - x_{\mathrm{caso}}(t)$.
- Diseñar el circuito analógico del controlador PID equivalente con amplificadores operacionales y verificar su respuesta en Simscape Electrical.
- Elaborar un diagrama biológico en BioRender que vincule las estructuras anatómicas musculares con las propiedades mecánicas y eléctricas.
- Documentar el código, archivos de simulación, figuras y resultados en un repositorio académico en GitHub.

[Volver al contenido](#contenido)

---

<a id="temario"></a>
## Relación con el temario

La práctica integra contenidos correspondientes a tres unidades de la asignatura **Modelado de Sistemas Fisiológicos (IBF-1020)**:

| Unidad | Área | Contenidos aplicados |
|---|---|---|
| I | Sistemas de control retroalimentados | Diagramas de bloques, retroalimentación negativa, respuesta temporal ante impulsos, análisis de error y criterios de estabilidad |
| II | Modelado matemático | Analogía mecánica (fuerza-voltaje), modelado del sistema musculoesquelético, transformadas de Laplace y funciones de transferencia |
| III | Controladores | Modos de control P, I, D, diseño de controladores PID, sintonización de ganancias y controladores analógicos con OpAmps |

El enfoque combina **Biomecánica, Ingeniería de Control, Electrónica Analógica, Ciencias de la Computación y Fisiología Muscular**.

[Volver al contenido](#contenido)

---

<a id="analogia"></a>
## Modelo físico y analogía electromecánica

El compartimento musculoesquelético se describe mediante el modelo de Hill-Khoo: la fuerza contráctil activa $F_0(t) = \alpha F(t)$ ($0 < \alpha < 1$) opera en paralelo con la amortiguación viscosa del tejido $R$. En serie se encuentra la elasticidad tendinosa y del elemento elástico en serie $C_s$, mientras que la elasticidad pasiva del sarcolema y tejido conjuntivo circundante se representa mediante el elemento en serie/paralelo $C_p$.

| Sistema mecánico | Variable / Elemento | Sistema eléctrico equivalente | Interpretación fisiológica |
|---|---|---|---|
| Fuerza $F(t)$ | Variable de entrada | Voltaje $V(t)$ | Fuerza total transmitida por el compartimento |
| Velocidad $\frac{dx(t)}{dt}$ | Variable interna | Corriente $I(t)$ | Velocidad de deformación / contracción |
| Desplazamiento $x(t)$ | Variable de salida | Carga eléctrica $q(t)$ | Elongación / acortamiento muscular total |
| Amortiguador | $R$ | Resistencia $R$ | Fricción viscosa interna y resistencia pasiva |
| Compliancia mecánica | $C_s, C_p$ | Capacitancia $C_s, C_p$ | Elasticidad de tendones ($C_s$) y sarcolema/tejido pasivo ($C_p$) |
| Masa | $M$ | Inductancia $L$ | Inercia de la masa muscular (despreciada en este orden) |

> **Regla de conversión:** En la analogía fuerza-voltaje, los elementos mecánicos conectados en paralelo se convierten en elementos eléctricos en serie, y los elementos mecánicos en serie se transforman en conexiones en paralelo.

### Parámetros para la simulación *in silico*

| Parámetro | Control (Individuo sano) | Caso (Atrofia muscular) | Unidad eléctrica | Interpretación biomecánica |
|---|---:|---:|---|---|
| $F(t)$ | $1$ | $1$ | $\mathrm{V}$ | Entrada de fuerza impulsiva ($1\,\mathrm{N}$) |
| $\alpha$ | $0.25$ | $0.25$ | Adimensional | Factor de ganancia contráctil activa |
| $C_s$ | $10\times10^{-6}$ | $10\times10^{-6}$ | $\mathrm{F}$ ($10\,\mu\mathrm{F}$) | Compliancia elástica en serie |
| $C_p$ | $100\times10^{-6}$ | $100\times10^{-6}$ | $\mathrm{F}$ ($100\,\mu\mathrm{F}$) | Compliancia elástica en paralelo |
| $R$ | $100$ | $10\,000$ | $\Omega$ ($100\,\Omega$ / $10\,\mathrm{k}\Omega$) | Amortiguamiento viscoso tisular |

La atrofia muscular se modela mediante el incremento drástico del término viscoso/resistivo $R$ (de $100\,\Omega$ a $10\,\mathrm{k}\Omega$), lo cual altera la velocidad de respuesta, disipación de energía y deformación elástica del músculo.

[Volver al contenido](#contenido)

---

<a id="modelo"></a>
## Formulación matemática

### 1. Ecuaciones del sistema mecánico y circuito equivalente

Equilibrando las fuerzas en los nodos de desplazamiento $x(t)$ y $x_1(t)$ y aplicando las relaciones constitutivas:

$$F_0(t) = \alpha F(t),$$

$$R \frac{d}{dt}[x(t) - x_1(t)] + \frac{x_1(t)}{C_s} = F_0(t),$$

$$F(t) = \frac{x(t)}{C_p} + \frac{x_1(t)}{C_s}.$$

### 2. Función de transferencia

Aplicando la transformada de Laplace con condiciones iniciales nulas $x(0) = 0, x_1(0) = 0$:

$$G(s) = \frac{X(s)}{F(s)} = \frac{C_p (R C_s s + 1 - \alpha)}{R C_s s + 1 + \frac{C_p}{C_s}}.$$

Sustituyendo $\alpha = 0.25$, la función de transferencia toma la forma general:

$$\boxed{G(s) = \frac{X(s)}{F(s)} = C_p \frac{R C_s s + 0.75}{R C_s s + \left(1 + \frac{C_p}{C_s}\right)}.}$$

Para la relación $C_p/C_s = 100\,\mu\mathrm{F} / 10\,\mu\mathrm{F} = 10$, se tiene el denominador $R C_s s + 11$.

[Volver al contenido](#contenido)

---

<a id="analisis"></a>
## Análisis temporal y de estabilidad

### 1. Error en estado estacionario

Para una entrada de fuerza en escalón unitario $F(s) = 1/s$, aplicando el teorema del valor final:

$$x(\infty) = \lim_{s\to 0} s X(s) = \lim_{s\to 0} G(s) = \frac{0.75 C_p}{1 + \frac{C_p}{C_s}} = \frac{0.75 \times 100\times 10^{-6}}{11} \approx 6.818\,\mu\mathrm{m}.$$

El valor final es independiente de $R$, lo que indica que la atrofia muscular altera la respuesta transitoria y la velocidad de deformación, pero no el valor final de deformación pasiva en estado estacionario.

### 2. Polos y estabilidad

El polo del sistema se ubica en:

$$s_{\mathrm{polo}} = -\frac{1 + \frac{C_p}{C_s}}{R C_s} = -\frac{11}{R C_s}.$$

- **Sano (Control, $R = 100\,\Omega$):** $s_{\mathrm{polo}} = -\frac{11}{100 \times 10^{-5}} = -11\,000\,\mathrm{rad/s}$. Respuesta sumamente rápida.
- **Atrofia (Caso, $R = 10\,\mathrm{k}\Omega$):** $s_{\mathrm{polo}} = -\frac{11}{10^4 \times 10^{-5}} = -110\,\mathrm{rad/s}$. La respuesta se ralentiza significativamente.

Dado que en ambos casos $s_{\mathrm{polo}} < 0$, el sistema es **estrictamente estable** (de primer orden equivalente en velocidad/desplazamiento).

[Volver al contenido](#contenido)

---

<a id="senales"></a>
## Señales de entrada y condiciones de simulación

El intervalo nominal de simulación es $0 \le t \le 10\,\mathrm{s}$ con un paso de integración de $\Delta t = 10^{-3}\,\mathrm{s}$.

| Señal | Definición para la simulación | Propósito |
|---|---|---|
| Impulso unitario | $F(t) = \delta(t)$ (Aproximación por pulso de corta duración) | Evaluar la respuesta natural y transitoria ante un impacto de fuerza |
| Escalón unitario | $F(t) = 1$ para $t \ge 0$ | Evaluar la deformación final en estado estacionario |

[Volver al contenido](#contenido)

---

<a id="matlab"></a>
## Implementación en MATLAB, Simulink y Simscape

Se comparan tres representaciones computacionales equivalentes:

| Implementación | Descripción | Aspecto por verificar |
|---|---|---|
| Ecuaciones diferenciales, Simulink | Bloques de suma, ganancias e integradores | Consistencia con el equilibrio mecánico |
| Función de transferencia, Simulink | Bloque $G(s) = X(s)/F(s)$ | Respuesta dinámico-frecuencial del modelo |
| Circuito equivalente, Simscape Electrical | Red de componentes $R$, $C_s$, $C_p$ y fuente $V(t)$ | Concordancia entre el dominio eléctrico y el mecánico |

### Ejecución desde el cuaderno MATLAB

El cuaderno `.mlx` ejecuta el modelo de Simulink e extrae las señales al *Workspace*:
1. **Entrada de Fuerza:** $F(t)$.
2. **Salida Control (Sano):** $x_{\mathrm{control}}(t)$.
3. **Salida Caso (Atrofia):** $x_{\mathrm{caso}}(t)$.
4. **Salida Caso Controlado (PID):** $x_{\mathrm{PID}}(t)$.

[Volver al contenido](#contenido)

---

<a id="pid"></a>
## Control en lazo cerrado y sintonización PID

### 1. Retroalimentación negativa

Se toma la respuesta del individuo sano $x_{\mathrm{control}}(t)$ como señal de referencia para el caso atrófico $x_{\mathrm{caso}}(t)$. La señal de error es:

$$e(t) = x_{\mathrm{control}}(t) - x_{\mathrm{caso}}(t).$$

La ley del controlador PID ideal es:

$$u(t) = k_P e(t) + k_I \int_0^t e(\tau)\,d\tau + k_D \frac{de(t)}{dt}.$$

### 2. Sintonización

Utilizando la herramienta `Tune` de Simulink sobre el modelo de la planta en caso de atrofia, se obtienen las ganancias $k_P, k_I, k_D$ necesarias para acelerar la respuesta del paciente y reducir la discrepancia transitoria con la referencia sana.

### 3. Realización analógica con OpAmps

El controlador PID se implementa analógicamente utilizando amplificadores operacionales en configuración inversora. Las relaciones para la elección de componentes comerciales son:

$$k_P = \frac{R_r}{R_e}, \qquad k_I = \frac{1}{R_e C_r}, \qquad k_D = C_e R_r.$$

[Volver al contenido](#contenido)

---

<a id="python"></a>
## Reproducción en Python

El script `modelo_musculoesqueletico.py` reproduce la simulación de manera independiente en Python utilizando las librerías `scipy.signal`, `numpy` y `matplotlib`:

1. Definición del vector de tiempo $t \in [0, 10]\,\mathrm{s}$.
2. Definición de las funciones de transferencia $G_{\mathrm{control}}(s)$ y $G_{\mathrm{caso}}(s)$.
3. Cálculo de la respuesta al impulso (`scipy.signal.impulse`).
4. Construcción del sistema en lazo cerrado con el controlador PID.
5. Generación y exportación de figuras en formato PDF.

[Volver al contenido](#contenido)

---

<a id="resultados"></a>
## Resultados y verificación cruzada

Convención gráfica de curvas:
- **Amarillo:** Entrada de fuerza aplicada, $F(t)$.
- **Azul:** Respuesta del individuo sano / Control, $x_{\mathrm{control}}(t)$.
- **Rojo / Naranja:** Respuesta del caso con atrofia muscular en lazo abierto, $x_{\mathrm{caso}}(t)$.
- **Verde:** Respuesta del paciente con atrofia controlado mediante PID, $x_{\mathrm{PID}}(t)$.

### Archivos de resultados

| Entrada | MATLAB/Simulink | Python | Simscape Electrical |
|---|---|---|---|
| Impulso | `impulse_matlab.pdf` | `impulse_python.pdf` | `impulse_simscape.pdf` |
| Escalón | `step_matlab.pdf` | `step_python.pdf` | `step_simscape.pdf` |

[Volver al contenido](#contenido)

---

<a id="diagrama-biologico"></a>
## Diagrama biológico

El diagrama biológico elaborado en BioRender establece la correspondencia entre los componentes anatómicos y las variables del modelo:

- **Elemento Contráctil ($F_0$):** Sarcómeros y puentes cruzados de actina-miosina.
- **Elemento Elástico Serie ($C_s$):** Tendón y bandas Z.
- **Elemento Elástico Paralelo ($C_p$):** Epimisio, perimisio, endomisio y sarcolema.
- **Amortiguador Viscoso ($R$):** Fricción del líquido sarcoplásmico y viscosidad tisular.

[Volver al contenido](#contenido)

---

<a id="flujo"></a>
## Flujo de trabajo

```mermaid
flowchart TD
    A[Modelo mecanico viscoelastico Hill-Khoo] --> B[Analogia fuerza-voltaje]
    B --> C[Circuito electrico equivalente RLC]
    C --> D[Leyes de Kirchhoff y equilibrio mecanico]
    D --> E[Ecuaciones diferenciales y Funcion de Transferencia Gs]
    E --> F[Analisis de polos, estabilidad y error]
    D --> G[Simulink: Ecuaciones diferenciales]
    E --> H[Simulink: Funcion de Transferencia]
    B --> I[Simscape Electrical: Circuito equivalente]
    G --> J[Respuesta en lazo abierto: Control vs Caso]
    H --> J
    I --> J
    E --> K[PID con retroalimentacion negativa]
    K --> L[Sintonizacion Tune y lazo cerrado]
    E --> M[Python: Simulacion independiente]
    L --> M
    L --> N[Diseno de controlador analogico con OpAmps]
    J --> O[Verificacion cruzada entre plataformas]
    L --> O
    M --> O
    O --> P[README, figuras y evidencias en GitHub]
