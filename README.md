# Schrodinger_Numerical
Examples of Numerical Solution of the Schrödinger equation for simple potentials as finite difference boundary value problem.

Based on the method proposed by D. Truhlar, Journal Computational Physics 10 (1972) 123-132
https://www.sciencedirect.com/science/article/pii/0021999172900940 


The method is explained in the included pdf file.
This numerical mehod shows how the differential equation problem is transformed into a linear algebra problem.
Also provides a simple way to obtain energy levels and their wave functions for single particle quantum problems.

An interactive python implementation of this same method for the case of the harmonic oscillator is available here
https://liu-group.github.io/1D-PDE-BV/


A key practical aspect is the choice of units before the numerical integration. 
For some simple potentials it is possible to easily select a dimensionless system of units which allows a general solution, as in the harmonic oscillator example. 
In general this is not possible or not practical and a typical choice of units is atomic units, as defined here:
https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Physical_Chemistry_(LibreTexts)/08%3A_Multielectron_Atoms/8.01%3A_Atomic_and_Molecular_Calculations_are_Expressed_in_Atomic_Units


