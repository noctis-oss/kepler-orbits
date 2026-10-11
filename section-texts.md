# Keplerian Orbits — the text of every section

Optional. Lab 12 of *Git & GitHub for Scientific Computing and Writing* asks only for
the line the book's table gives under each heading (its equation and parameters).
For the complete paper, paste each block below over the `% TODO` under its heading,
one section per commit, on the branch the lab names. The `% FIGURE n` lines are the
placeholders the figure tasks replace.

Keep the line breaks as they are: Git compares lines. The second line of the
introduction, `classical problems of mechanics.`, is the line the revision cites
and the co-author rewrites, which is where the planned conflict happens.

This is the text of the reference repository at `v1.0-submitted`; the revision
(issue #9) is at the end.

## Introduction

```latex
The motion of a planet around a central body is one of the
classical problems of mechanics.
This paper derives the orbit from Newton's laws, computes the same orbit
numerically, and checks that the two descriptions agree.
The numerical data are written by a short Python script, and every figure
is drawn from a formula or from those data by its own script.
```

## 1. The Gravitational Model

```latex
A body of negligible mass moves under the gravity of a central mass $M$.
Newton's law of gravitation and his second law give
\begin{equation}
  \ddot{\mathbf r} = -\frac{\mu}{r^3}\,\mathbf r, \qquad \mu = GM,
\end{equation}
where $\mathbf r$ is the position relative to the central body and $r = |\mathbf r|$.
Throughout the paper we use units in which $\mu = 1$.
```

## 2. The Analytical Orbit

```latex
The solutions of (1) are conic sections with the central body at a focus.
For a bound orbit with semi-major axis $a$ and eccentricity $e < 1$,
\begin{equation}
  r(\theta) = \frac{a(1-e^2)}{1 + e\cos\theta},
\end{equation}
where $\theta$ is measured from the periapsis.
```

## 3. From the Equation to a Plot

```latex
With $x = r\cos\theta$ and $y = r\sin\theta$, equation (2) becomes a curve
in the plane.
Figure~\ref{fig:analytical} shows it for $a = 1$ and $e = 0.6$:
the periapsis is at $r = a(1-e) = 0.4$ and the apoapsis at $r = a(1+e) = 1.6$.

% FIGURE 1
```

## 4. Exploring Eccentricity

```latex
The eccentricity sets the shape of the orbit.
For $e = 0$ the orbit is a circle of radius $a$; as $e$ grows toward 1
the orbit becomes more elongated and the periapsis approaches the focus.
Figure~\ref{fig:eccentricity} compares $e = 0$, $0.3$, $0.6$ and $0.8$ for $a = 1$.

% FIGURE 2
```

## 5. The Same Problem as a Dynamical System

```latex
Equation (1) is a second-order system.
With the state vector $\mathbf X = (x, y, v_x, v_y)$ it becomes
\begin{equation}
  \dot{\mathbf X} = \left(v_x,\; v_y,\; -\frac{\mu x}{r^3},\; -\frac{\mu y}{r^3}\right),
\end{equation}
a first-order system that a numerical method can advance step by step.
```

## 6. Generating the Orbit with Python

```latex
The script \texttt{generate\_kepler\_data.py} integrates (3) with the
classical fourth-order Runge--Kutta method.
It starts at the periapsis of the orbit in Figure~\ref{fig:analytical},
\begin{equation}
  x_0 = a(1-e) = 0.4, \qquad v_{y0} = \sqrt{\frac{\mu(1+e)}{a(1-e)}} = 2,
\end{equation}
and takes 720 steps over one period, $T = 2\pi\sqrt{a^3/\mu} = 2\pi$.
It writes the trajectory to \texttt{kepler\_orbit.csv}.
The script uses only the Python standard library.
```

## 7. Plotting the CSV Data

```latex
The numerical orbit is a list of points, not a formula.
Figure~\ref{fig:numerical} draws the 721 points of \texttt{kepler\_orbit.csv}
as one curve.

% FIGURE 3
```

## 8. Analytical vs. Numerical Orbit

```latex
If the integrator and the initial state are right, the two descriptions
of the orbit coincide.
Figure~\ref{fig:comparison} draws both: over the whole revolution the
largest difference in radius is about $10^{-7}$, far below the width of a line.

% FIGURE 4
```

## 9. Kepler's Second Law

```latex
The angular momentum per unit mass, $h = |\mathbf r \times \dot{\mathbf r}|$,
is conserved in a central field.
The radius therefore sweeps area at a constant rate,
\begin{equation}
  \frac{dA}{dt} = \frac{h}{2} = \text{constant},
\end{equation}
so the body moves fastest at the periapsis and slowest at the apoapsis.
```

## 10. Kepler's Third Law

```latex
Integrating (5) over one period gives $\pi a b = hT/2$, and with
$b = a\sqrt{1-e^2}$ and $h = \sqrt{\mu a(1-e^2)}$,
\begin{equation}
  T^2 = \frac{4\pi^2}{\mu}\,a^3.
\end{equation}
The period depends only on the semi-major axis.
```

## 11. A Peano–Baker Perspective

```latex
A linear system $\dot{\mathbf x} = A(t)\,\mathbf x$ has the solution
$\mathbf x(t) = \Phi(t,t_0)\,\mathbf x(t_0)$.
The state-transition matrix $\Phi(t,t_0)$ is the sum of the Peano--Baker series,
\begin{equation}
  \Phi(t,t_0) = I + \int_{t_0}^{t} A(s_1)\,ds_1
  + \int_{t_0}^{t} A(s_1)\int_{t_0}^{s_1} A(s_2)\,ds_2\,ds_1 + \cdots
\end{equation}
```

## 12. Peano–Baker and the Kepler Problem

```latex
Linearized about a reference orbit, a small change in the state obeys
\begin{equation}
  \delta\dot{\mathbf X} = A(t)\,\delta\mathbf X,
\end{equation}
where $A(t)$ is the Jacobian of (3) evaluated along the reference orbit.
The state-transition matrix of (8) tells how an error in the initial state
grows along the orbit.
```

## 13. From Equations to Computation

```latex
The same orbit appeared three times: as an equation, as a function that
advances a state, and as data in a file.
Each view checks the others; the comparison in Figure~\ref{fig:comparison}
is where an error in any of them would show.
```

## Summary

```latex
We derived the Keplerian orbit, integrated the equations of motion
numerically, and drew both from a formula and from data.
The two agree to $10^{-7}$ over a full period.
The data, the figures and this paper are reproduced by the commands
in \texttt{README.md}.
```

## Revision (issue #9)

Section 10, after the third-law equation (Figure 5):

```latex
Figure~\ref{fig:third-law} plots $T^2$ against $a^3$ for six orbits.

% FIGURE 5
```

Section 12, after its paragraph (Figure 6):

```latex
This paper does not sum the series.
It integrates (8) numerically with RK4, together with the reference orbit and
an orbit started $0.001$ faster.
Figure~\ref{fig:variation} shows that the first-order prediction follows the
perturbed orbit.

% FIGURE 6
```

`plot-notes.txt`:

```text
Figure 6 integrates the first-order variational equation along the
reference orbit with RK4. It is not a truncated Peano-Baker series.

Figure 5 plots values that kepler_third_law.csv evaluates from the
analytical law; it does not measure integrated periods.
```

The references (`refs.bib`), the citation in the first sentence and the bibliography
commands are in Appendix E.6–E.7 of the book.
