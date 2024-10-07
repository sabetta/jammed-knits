These simulations were developed by M. Dimitriyev and S. Gonzalez.

For questions, email sgonzalez49@gatech.edu or visit matsumoto.gatech.edu for the contact information of current graduate students.

-------------
VERSION INFORMATION
Python code developed for v3.6.13 of the Python Programming Language, using v1.18.1 of NumPy and v1.4.1 of SciPy libraries as packaged in Anaconda3 (https://www.anaconda.com/)

This simulation was initially made for the manuscript: Singal, K., Dimitriyev, M.S., Gonzalez, S.E. et al. Programming mechanics in knitted materials, stitch by stitch. Nat Commun 15, 2622 (2024). https://doi.org/10.1038/s41467-024-46498-z

Modifications since that publication were made by S. Gonzalez.

-------------
RUNNING THE SIMULATIONS

To run, execute the following script in terminal: python3 simulation.py config_file_name.dat

To run, you must have an initialization file, named "Init_XXXX.dat", and a configuration file that is called in the terminal. The XXXX in the initialization file name can be subbed out for any number or string. That XXXX suffix is included in the configuration file to indicate the initialization file that is being called into the simulation. The initialization file must be in the same folder as the simulation code.

INITIALIZATION FILE
The initialization file has a list of inputs used to construct an initial Bezier curve for the stitch. Example initialization files for each fabric type have been provided. To create new initialization files, you can either add a small amount of random noise to the provided initialization file or use the output of one of the simulations of the same fabric type. To make a new init file from a simulation, copy the ResultsOut.dat output file of a simulation with a similar set of input parameters. 

If the simulation parameters are sufficiently far from those used in the initialization file, the simulation will struggle to find the minimum energy configuration. Markers of this include high total energies for rest configurations (>1J), or decreasing energy as the fabric is stretched. You can mitigate this by creating a series of initializations and simulations that slowly move the simulation inputs towards your desired set of parameters.


CONFIGURATION FILE
The configuration files include a list of fabric and yarn parameters. It also specifies the prefix of the output file name, the stretching direction, and the initialization file needed to start the simulation. A sample configuration file has been included, "sampleconfigfile.dat".

The configuration file also has infrastructure to tell the simulation the cell dimension to start and end stretching. The simulation is currently hard-coded to stop at a set stress value, but you can instead set a minimum and maximum stitch cell dimension through the configuration file. This infrastructure also supports changing the simulation to compress the stitch.

The initial step size the simulation takes to increase the cell dimension is also listed in the configuration file. A smaller step size gives more accuracy in characterizing the jammed regime. The simulation is currently hard-coded to increase the step size after reaching a certain strain value, but that portion of the code can be removed or commented out to maintain the same step size throughout the simulation run.

-------------
ASSOCIATED SCRIPTS

Bezier.py, ConnectingCurve.py, Crossover.py, and mathHelper.py are associated scripts that construct and update the Bezier curve splines used in the simulations. These codes must be in the same folder as the fabric simulations for the simulations to run. Initialized Bezier curves are provided via the initialization files.

-------------
SIMULATION MECHANICS
For an in-depth explanation of the physics utilized and code mechanics, see the SI of Singal, K., Dimitriyev, M.S., Gonzalez, S.E. et al. Programming mechanics in knitted materials, stitch by stitch. Nat Commun 15, 2622 (2024).

The simulations take a stitch constructed of Bezier curve splines, calculate the bending and compression energy along the curves, and iteratively change the shape of the curve to minimize the total energy for the specified stitch cell dimension. The unspecified stitch cell dimension can vary freely as an unclamped edge to reflect the Poisson ratio of the fabric. These simulations are static and would reflect stretching experiments done in the quasi-static regime.

BEZIER SPLINES
The Bezier curve splines constructed in the simulation are labelled according to subfigure (a) in "splinenotation.png". Subfigure (b) shows the total shape of the stitch from a top view (left) and angled perspective (right). 

MINIMIZATION SCHEME
Standard scipy.minimize is used to minimize the total energy, using the sequential least-squares ("SLSQP") method. Due to the large dimension of the energy landscape, the simulation can fall into local minima. 

****To increase the likelihood of finding a global minima, run the simulation multiple times for the same configuration parameters but change the initialization used to start the simulation.****

Typically, four initialization files for a single simulation provides good stability.

--------------
SIMULATION OUTPUTS
When a simulation code is started, it writes the input configuration file into an output configuration file. This allows you to delete the input configuration file and still keep track of the parameters for each simulation set. 

The simulations output ten files for each set of cell dimensions. 

"BendingDensityOut.dat", "BezierOut.dat", "BezierOutCourse.dat", and "BezierOutWale.dat" provide information about the final Bezier curve spline. "BezierOut.dat", "BezierOutCourse.dat", and "BezierOutWale.dat" list control points for the Bezier curves. See the print function in Bezier.py for how the control points are printed. See the simulation code for which splines are printed to which file.

"ResultsOut.dat" provides information that can be used to generate a new initialization. See the INITIALIZATION FILE section of this text for instructions. 

"ContactDensityOut.dat" and "ContactMapOut.dat" provide information about the contact energy density.

"EnergyOut.dat", "StretchOut.dat", and "CellPropsOut.dat" can be used to generate stress v strain data. "CellPropsOut.dat" has information on shearing via the join and cell angles. Currently, the simulation is hard-coded for uniaxial stretching or compression and these angles are set to zero. "EnergyOut.dat" has three entries: the contact energy, then the bending energy, then the total energy. "StretchOut.dat" has three entries: the length of yarn per stitch, the stitch cell x-dimension, and the stitch cell y-dimension.

-------------
ANALYZING RESULTS

To get force data from the energy v cell dimension, take a discrete, midpoint derivative. To transform the force into stress, divide by the cell dimension you weren't sweeping over at zero-force. To get strain from the cell dimension data, calculate (a_x-a_x0)/a_x0 where a_x is the x-dimension of the cell and a_x0 is the x-dimension of the cell at zero force. The same calculation can be made for the y-dimension.

Remember to run multiple initializations and choose the minimum energy simulation for a given stitch cell dimension before doing your stress strain analysis. This will give the best results.

A Mathematica code to analyze results is included in the simulationoutputs folder, "analyzesimdata.nb", along with all of the simulation outputs created during this study.

