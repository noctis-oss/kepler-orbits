"""Generate the reproducible Kepler data for the paper (standard library only)."""
from __future__ import annotations

import csv
from math import pi, sqrt
from pathlib import Path

OUTPUT = Path(__file__).resolve().parent
MU = 1.0
A = 1.0
E = 0.6
STEPS = 720
DT = 2.0 * pi / STEPS
DELTA_VY = 0.001


def derivative(state: tuple[float, ...]) -> tuple[float, ...]:
    x, y, vx, vy, xp, yp, vxp, vyp, dx, dy, dvx, dvy = state
    radius2 = x*x + y*y
    radius = sqrt(radius2)
    inv_r3 = 1.0 / (radius2 * radius)
    inv_r5 = inv_r3 / radius2
    radius2_p = xp*xp + yp*yp
    inv_r3_p = 1.0 / (radius2_p * sqrt(radius2_p))
    ax = -MU*x*inv_r3
    ay = -MU*y*inv_r3
    ax_p = -MU*xp*inv_r3_p
    ay_p = -MU*yp*inv_r3_p
    a_xx = -MU*inv_r3 + 3.0*MU*x*x*inv_r5
    a_xy = 3.0*MU*x*y*inv_r5
    a_yy = -MU*inv_r3 + 3.0*MU*y*y*inv_r5
    return (vx, vy, ax, ay, vxp, vyp, ax_p, ay_p,
            dvx, dvy, a_xx*dx + a_xy*dy, a_xy*dx + a_yy*dy)


def rk4(state: tuple[float, ...], step: float) -> tuple[float, ...]:
    k1 = derivative(state)
    k2 = derivative(tuple(v + step*k/2 for v, k in zip(state, k1)))
    k3 = derivative(tuple(v + step*k/2 for v, k in zip(state, k2)))
    k4 = derivative(tuple(v + step*k for v, k in zip(state, k3)))
    return tuple(v + step*(a + 2*b + 2*c + d)/6
                 for v, a, b, c, d in zip(state, k1, k2, k3, k4))


def write_csv(name: str, header: list[str], rows: list[list[float]]) -> None:
    with (OUTPUT/name).open('w', encoding='utf-8', newline='') as target:
        writer = csv.writer(target)
        writer.writerow(header)
        writer.writerows([[f'{value:.9f}' for value in row] for row in rows])


def main() -> None:
    periapsis = A*(1.0-E)
    periapsis_speed = sqrt(MU*(1.0+E)/(A*(1.0-E)))
    state = (periapsis, 0.0, 0.0, periapsis_speed,
             periapsis, 0.0, 0.0, periapsis_speed + DELTA_VY,
             0.0, 0.0, 0.0, DELTA_VY)
    orbit = []
    variation = []
    for index in range(STEPS + 1):
        t = index*DT
        x, y, vx, vy, xp, yp, _vxp, _vyp, dx, dy, _dvx, _dvy = state
        orbit.append([t, x, y, vx, vy])
        variation.append([t, x, y, xp, yp, x+dx, y+dy])
        if index < STEPS:
            state = rk4(state, DT)
    write_csv('kepler_orbit.csv', ['t','x','y','vx','vy'], orbit)
    write_csv('kepler_variation.csv',
              ['t','x_reference','y_reference','x_perturbed','y_perturbed',
               'x_linearized','y_linearized'], variation)
    semimajor_axes = [0.50, 0.75, 1.00, 1.25, 1.50, 2.00]
    write_csv('kepler_third_law.csv', ['a','a_cubed','T_squared'],
              [[a, a**3, 4*pi*pi*a**3/MU] for a in semimajor_axes])
    print(f'Generated {len(orbit)} orbit rows, {len(variation)} variation rows, '
          f'{len(semimajor_axes)} period rows.')


if __name__ == '__main__':
    main()
