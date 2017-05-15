# mars-sim-tools
These Python scripts assist in preparing data prior to a release, and are not used for the execution of the program itself.

tsv2xml (landmarks) converts a generated list of Martian landmarks from USGS to a simulation-compatible format, and adds human artifacts from Wikipedia and Google Mars. It filters the raw list to some criteria.

htmlgenerate generates HTML5 files for the inline user guide based on the XML files in the project.

transition is a simple percentage calculator to give us incentive to migrate faster from Swing to JavaFX. It doesn't change the source or data files in any way.
