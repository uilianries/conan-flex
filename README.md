[![Build Status](https://travis-ci.org/uilianries/conan-flex.svg?branch=release/2.6.4)](https://travis-ci.org/uilianries/conan-flex)
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
[![Download](https://api.bintray.com/packages/uilianries/conan/flex%3Auilianries/images/download.svg?version=2.6.4%3Astable)](https://bintray.com/uilianries/conan/flex%3Auilianries/2.6.4%3Astable/link)


# conan-flex

![Conan flex](conan-flex.png)

This is **flex**, the fast lexical analyzer generator.

**flex** is a tool for generating scanners: programs which recognize lexical patterns in text.

[Conan.io](https://conan.io) package for [flex](https://github.com/westes/flex) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/uilianries/conan/flex%3Auilianries).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.

## Upload packages to server

    $ conan upload flex/2.6.4@uilianries/stable --all

## Reuse the packages

### Basic setup

    $ conan install flex/2.6.4@uilianries/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    flex/2.6.4@uilianries/stable

    [options]
    flex:shared=True # False

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

### Constraints

flex is **NOT** supported on Windows. If you are looking for it, see [here](https://sourceforge.net/projects/winflexbison/).

### License
[BSD](LICENSE)
