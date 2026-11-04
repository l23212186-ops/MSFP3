"""
Práctica: Modelado y control del sistema musculoesquelético

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Christian Cid Pacheco
Número de control: 23212186
Correo institucional: l23212186@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""

import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
from scipy import signal 
import pandas as pd

t0, tend, dt, w, h = 0, 10, 1E-3, 7, 3.5
N = round(tend / dt) + 1
t = np.linspace(t0, tend, N)
amplitude = 1.0
period = 10.0
pulse_width_pct = 10.0  # 10% del periodo (1 segundo activo)
phase_delay = 1.0       # Retraso de fase de 1 segundo

pulse_duration = period * (pulse_width_pct / 100.0)
u = np.zeros_like(t)
mask = (t >= phase_delay) & ((t - phase_delay) % period < pulse_duration)
u[mask] = amplitude

Cs = 10E-6
Cp = 100E-6
alpha = 0.25

R_control = 100.0
num_ctrl = [R_control * Cs, 1.0 - alpha]
den_ctrl = [R_control * (Cp + Cs), 1.0]
sys_control = ctrl.tf(num_ctrl, den_ctrl)

R_caso = 10.0E3
num_caso = [R_caso * Cs, 1.0 - alpha]
den_caso = [R_caso * (Cp + Cs), 1.0]
sys_caso = ctrl.tf(num_caso, den_caso)

kP, kI = 0.021971, 41303.6113
pi_ctrl = ctrl.tf([kP, kI], [1, 0])
sys_pi = ctrl.feedback(ctrl.series(pi_ctrl, sys_caso), 1, sign=-1)

F = u
_, Fsx = ctrl.forced_response(sys_control, t, u)
_, Fsy = ctrl.forced_response(sys_caso, t, u) 
_, PID = ctrl.forced_response(sys_pi, t, Fsx)

clr1 = np.array([9, 21, 64]) / 255
clr2 = np.array([27, 44, 193]) / 255
clr3 = np.array([118, 146, 255]) / 255
clr4 = np.array([50, 205, 50]) / 255

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['mathtext.fontset'] = 'stix'

def plotsignals(t, F, Fsx, Fsy, PID, signal_type):
    fig = plt.figure(figsize=(w, h))
    ax = fig.add_subplot(111)

    # Configuración de ejes y bordes
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.tick_params(direction='in', which='both')

    if signal_type == "Caso":
        ax.plot(t, F, '-.', color=clr1, linewidth=1.5, label=r'$F(t)$')
        ax.plot(t, Fsx, '-', color=clr2, linewidth=1.5, label=r'$F(t)$: Control')
        ax.plot(t, Fsy, '--', color=clr3, linewidth=1.5, label=r'$F(t)$: Caso')
        ax.plot(t, PID, '--', color=clr4, linewidth=1.5, label=r'$PID(t)$: Tratamiento')

    # Leyenda superior horizontal orientada al exterior
    ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.02), ncol=2, 
              frameon=False, fontsize=9, prop={'family': 'Times New Roman', 'size': 10})

    ax.set_xlabel(r'$t [s]$', fontsize=11)
    ax.set_ylabel(r'$F_i(t)\ [V]$', fontsize=11)

    ax.set_xlim(0, 10)
    ax.set_xticks(np.arange(0, 11, 1))
    ax.set_ylim(-0.1, 1.1)
    ax.set_yticks(np.arange(-0.1, 1.2, 0.1))
    
    plt.tight_layout()

    filename = f"{signal_type}_python.pdf"
    fig.savefig(filename, format='pdf', bbox_inches='tight')
    print(f"Gráfica guardada exitosamente como: {filename}")
    plt.show()

if __name__ == "__main__":
    print("Ejecutando simulación del sistema musculoesquelético y generando gráficos...\n")
    plotsignals(t, F, Fsx, Fsy, PID, "Caso")
    
    print("\n¡Proceso finalizado con éxito!")