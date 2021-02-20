# JSBSim Reference Manual

This site is the home of the [JSBSim Reference Manual](https://jsbsim-team.github.io/jsbsim-reference-manual), a website hosted by GitHub Pages, based on [Jekyll](https://jekyllrb.com).

<p align="center">
<img width="250" heigth="250" src="https://github.com/JSBSim-Team/jsbsim-logo/blob/master/logo_JSBSIM_globe.png">
</p>

[JSBSim](https://github.com/JSBSim-Team/jsbsim) is a multi-platform, general purpose object-oriented Flight Dynamics Model (FDM) written in C++. The FDM is essentially the physics & math model that defines the movement of an aircraft, rocket, etc., under the forces and moments applied to it using the various control mechanisms and from the forces of nature. JSBSim can be run in a standalone batch mode flight simulator (no graphical displays) for testing and study, or integrated with [FlightGear](https://www.flightgear.org/) or other flight simulator.
 
## Contribute
### Report bugs or request features.
If you want to report bugs or request features/new additions, please [open a new issue](https://github.com/JSBSim-Team/jsbsim-reference-manual/issues).
### Contribute to the documentation
If you want to contribute to the documentation, please [submit a pull request](https://github.com/JSBSim-Team/jsbsim-reference-manual/pulls)

For that, you will need to fork this repository and install [Jekyll](https://jekyllrb.com) on your computer.
1. Install all [prerequisites](https://jekyllrb.com/docs/installation/).
2. Install the jekyll and bundler gems.
```bash
gem install jekyll bundler
```
3. Clone the repo
```bash
git clone https://github.com/JSBSim-Team/jsbsim-reference-manual.git
```
4. In the directory `./jsbsim-reference-manual/docs`, install gems from our `Gemfile` using Bundler
```bash
bundle config set --local path 'vendor/bundle'
bundle install
```
5. Build the site and make it available on a local server
```bash
bundle exec jekyll serve
```
6. Browse to http://localhost:4000

Jekyll will then run a local web server at http://localhost:4000, rebuilding the site any time you make a change (except if you make changes to `_config.yml` at which point you will have to interrupt (`CTRL`+`C`) and restart `bundle exec jekyll serve`
