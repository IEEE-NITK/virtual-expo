---
layout: post
title: "Shockwave Dynamics Simulator"
description: "Project on the implementation of a scheme to simulate compressible flow to further understanding of shockwave interaction"
categories: piston
thumbnail: "shockwave-dynamics.jpeg"
---

### Project Members

- Erin Sam Joe

## Abstract

The second-order semidiscrete central-upwind scheme is used to model
compressible flow systems. The equations governing the flow are the equation of
mass conservation, energy conservation and the compressible Euler Equations. An
OpenMP parallelized numerical framework written in C++, controlled through
simple Python scripts by the use of pybind11, is in use to implement the
semidiscrete central-upwind scheme. The implementation is tested through a
number of classic examples with known solutions. The current form of the code is
only featured for uniform, quadrilateral cells, with zero gradient boundary
conditions.

## Objective

The main goal of the project was to develop an understanding and simulate shock-
interactions. This is to be done by implementing the second-order semidiscrete
central-upwind scheme introduced by Kurganov et al.

## Theory

Intercell numerical flux must be calculated for each edge of a mesh-cell (in the case
of a 3D mesh, this intercell numerical flux must be calculated for each surface of a
mesh). For a 2D mesh comprising of quadrilateral elements, there are 4 edges for
each mesh cell. The intercell numerical flux must be calculated for each edge using
the data of flow field variables (velocity, density and pressure) of the 2 mesh cells
that straddle a single edge.

For a 100 by 100 square mesh, comprising of quadrilateral elements, there are
10,000 mesh cells, each having 4 edges, and so a total of 40,000 edges for which the
intercell numerical flux must be calculated. If we want to increase the refinement of
the mesh to better capture the flow features, take for example a 500 by 500 square
mesh comprising of quadrilateral elements, a million edges are present for which
the intercell numerical flux must be calculted.

One should note that this calculation must be done for each time step.

When the refinement of the mesh is increased, the size of the time step must
decrease by at least the factor by which refinement is increased. For example, if we
were to decrease the size of the mesh by a factor of 5, the size of the time step must
be decreased by 5. In our case of increasing the refinement from a 100x100 mesh to
a 500x500 mesh, time step size (say if it were initially 0.001s) must be reduced to
0.0002s. So to simulate 0.001s, the refined mesh must be iterated 5 more times,
moving from what used to be 40,000 intercell numerical flux computations to 5

The reason for the preceding discussion is to highlight the importance of being able
to calculate a cheap intercell numerical flux.

### Reimann Solvers

To solve for the intercell numerical flux in the compressible Euler equations,
Reimann solvers are typically used. A variety of Reimann solvers exist — the exact
reimann solver, random-choice reimann solvers, approximate-state reimann
solvers, the HLL and HLLC reimann solvers, reimann solver of Roe, reimann solver
of Osher and many more with total variation diminishing (TVD) to prevent
numerical oscillations.

The exact reimann solver provides the exact values of the intercell flux, but requires
an iterative procedure to obtain the flux, which is very expensive (in terms of time
and computational effort). The remaining reimann solvers serve as approximate
means of solving for intercell flux by providing better computational efficiency at
the cost of accuracy.

### Semidiscrete Central-Upwind Scheme

The semidiscrete central-upwind scheme, bypasses the need for a reimann solver,
providing in itself a means of calculating the intercell numerical flux. This method
has been described in the papers by Kurganov et al.

Due to the lower computational cost and sufficient accuracy of the scheme, this
scheme has been chosen to implement to serve the goal of developing a code for
shock-wave interaction.

## Code Development

### Prototyping the scheme

A prototype of the scheme was first implemented using Python and tested using the
numerical experiments that were present in the paper on meshes of very low
refinements.

Highly refined meshes could not be used due to how long it took to run. The results
matched, bearing in mind the poor refinement of the mesh and are depicted below.
![img 1](/virtual-expo/assets/img/piston/SDCU_blog_1.png)
![img 2](/virtual-expo/assets/img/piston/SDCU_blog_2.png)
![img 3](/virtual-expo/assets/img/piston/SDCU_blog_3.png)

Python scripts were developed, as well as, all the numerical experiments present in
the paper were attempted [5].

### Refactoring

Once the code was sufficiently validated, the scheme was re-written in C++ to be
able to run faster. The main aim was to allow us to the code on more refined meshes.

Although the code ran faster, we wanted to see if we could take it to another step.

### OpenMP

OpenMP uses a portable, scalable
model that gives programmers a simple and flexible interface for developing parallel
applications for platforms ranging from the standard desktop computer to the
supercomputer.

OpenMP was then studied to parallelise code so that appropriate use of multi-core
processors could be fully utilised [3]. The version of the code without the OpenMP
primitives, ran serially on a single processor of the system's Intel i7 processor,
instead of making full use of all the 12 threads on which execution of the code could
be conducted.

The code was then modified to the present form — an OpenMP parallelized
numerical framework written in C++, controlled through simple Python scripts by
the use of pybind11, is in use to implement the semidiscrete central-upwind scheme
[6].
![img 4](/virtual-expo/assets/img/piston/SDCU_blog_4.png)

### Features

Now we detail some of the features of the code

- The entire scheme gets compiled to a shared library by the use of pybind11. This
allows the mesh to be easily controlled within a Python script or directly from a
Python terminal by the mesh class.
- 3 functions of the mesh class (apart from initialisation) can be availed by users:
  - Initialise the cells with one of the 19 configurations (all of which have been
    taken from the numerical experiments section of the paper by Kurganov et
    al.). The configuration passed as a parameter to the function initialise( )
  - Increment the cells by a time step size taken as an parameter to the function
    updateCells( )
  - Apply the boundary conditions. It would have been better to write this as
    part of the updateCells( ) functions, since one can easily forget it
  - Save the mesh data through the save( ) function. Flow field variables for all
    the cells gets written out as .csv files
- Post-processing of the data by running postProcess.py or by running 'make
saveAll' in the root folder of the project. The aim was to resemble OpenFOAM's
ability to post-process the data while the simulation is still running
- Viewing the latest data with an interactive 3D plot (made by matplotlib) to
monitor the current state of the simulation

## Results and Conclusion

An OpenMP parallelized numerical framework written in C++, controlled through
simple Python scripts by the use of pybind11, is in use to implement the
semidiscrete central-upwind scheme for second-order spatial accuracy and first-
order temporal accuracy.

The current form of the code is only featured for uniform, quadrilateral cells, with
zero gradient boundary conditions. The following results has been obtained using
the 6th configuration [1].

![img 5](/virtual-expo/assets/img/piston/SDCU_blog_5.png)
![img 6](/virtual-expo/assets/img/piston/SDCU_blog_6.png)
The above simulation took 5 whole days to run. Due to the lack of proper
computational resources to continue testing the code, the fact that my latop could
not fully function when utilizing all the processors for the simulation and the
matching results in the paper, it has been concluded that the code is valid and the
semidiscrete central-upwind scheme has been implmented.

## Future Work

The code can be further improved by refactoring into a highly parallelised form to be
run on a GPU. This GPU accelerated form, written in CUDA, tailor-made for a Turing
micro-architecture NVIDIA GPU is currently underway.

The accuracy of the code as a solver can be further improved increasing the order of
spatial and temporal accuracy.

Furthermore, the code can also be modified to solve for additional fields, like the
eletric field, magnetic field to incorporate EM effects. More modifications can be
made on this code-base to develop it for more ambitious applications.

## References

[1] Alexander Kurganov; Eitan Tadmor (2002). Solution of two-dimensional
Riemann problems for gas dynamics without Riemann problem solvers. , 18(5), 584–
608.

[2] Kurganov, Alexander; Noelle, Sebastian; Petrova, Guergana (2001). Semidiscrete
Central-Upwind Schemes for Hyperbolic Conservation Laws and Hamilton--Jacobi
Equations. SIAM Journal on Scientific Computing., 23(3), 707–740.

[3] [OpenMP Course by Intel](https://www.youtube.com/playlist?list=PLLX-Q6B8xqZ8n8bwjGdzBJ25X2utwnoEG)

[4] E. F. Toro (2009). Reimann solvers and numerical methods for fluid dynamics — a
practical introduction. Springer.

[5] [Python version of the code](https://github.com/ErinSam/Semidiscrete-Central-Upwind-Schemes)

[6] [C++ Implementation](https://github.com/ErinSam/Second-Order-Semidiscrete-Central-Upwind-Scheme)
