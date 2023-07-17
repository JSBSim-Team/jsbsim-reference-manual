# JSBSim Reference Manual

This site is the home of the [JSBSim Reference Manual](https://jsbsim-team.github.io/jsbsim-reference-manual), a website hosted by GitHub Pages, based on [MkDocs](https://www.mkdocs.org/) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

<p align="center">
<img width="250" heigth="250" src="https://github.com/JSBSim-Team/jsbsim-logo/blob/master/logo_JSBSIM_globe.png">
</p>

[JSBSim](https://github.com/JSBSim-Team/jsbsim) is a multi-platform, general purpose object-oriented Flight Dynamics Model (FDM) written in C++. The FDM is essentially the physics & math model that defines the movement of an aircraft, rocket, etc., under the forces and moments applied to it using the various control mechanisms and from the forces of nature. JSBSim can be run in a standalone batch mode flight simulator (no graphical displays) for testing and study, or integrated with [FlightGear](https://www.flightgear.org/) or other flight simulator.
 
## Contribute

### Report bugs or request features.

If you want to report bugs or request features/new additions, please [open a new issue](https://github.com/JSBSim-Team/jsbsim-reference-manual/issues).

### Contribute to the documentation

If you want to contribute to the documentation, please [submit a pull request](https://github.com/JSBSim-Team/jsbsim-reference-manual/pulls)

For that, you will need to fork this repository and install [Python3](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installation/) on your computer.

1. Install the prerequisites mentioned above.

2. Clone the repository.
```bash
git clone https://github.com/JSBSim-Team/jsbsim-reference-manual.git
```

3. Create an isolated virtual environment.
```bash
cd jsbsim-reference-manual
python3 -m venv env # OR < py -m venv env > on Windows
```

4. Activate the virtual environment and install required PyPi packages.
```bash
source env/bin/activate # OR < .\env\Scripts\activate > on Windows
python3 -m pip install -r requirements.txt # OR < py -m pip install -r requirements.txt > on Windows
```

5. Build the site and make it available on a local server.
```bash
mkdocs serve
```

6. Browse to http://localhost:8000

MkDocs will then run a local web server at http://localhost:8000, rebuilding the site any time you make a change. You can exit at any time by pressing (`CTRL`+`C`).

You can also build the manual as a static site for offline use using the commands shown below:
```bash
export OFFLINE=true # OR < set OFFLINE=true > on Windows
export CI=false
mkdocs build
```
The built manual will be located in the *site/* directory. You will now be able to use the search feature offline.

When done, you can exit your virtual environment with the following command:
```bash
deactivate
```
