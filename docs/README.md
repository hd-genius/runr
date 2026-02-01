# Table of Contents
- [Table of Contents](#table-of-contents)
- [What is Runr](#what-is-runr)
- [Installation](#installation)
  - [Manual Installation](#manual-installation)
- [Usage](#usage)
  - [Get help](#get-help)
  - [List available scripts](#list-available-scripts)
  - [Run a script](#run-a-script)
- [Contributing](#contributing)

# What is Runr

Runr is command line utility that allows you to run your scripts from anywhere on your system. It is designed to be simple and flexible. It is still under development. New features are still being added and existing features will be improved over time.

# Installation

Installers and other distribution methods are still being developed. There is currently only one supported method to install Runr: **manually**.

## Manual Installation

*This method is very involved. For brevity's sake, this tutorial assumes you are familiar with adding environment variables, editing your user's PATH, and opening zip archives.*

Visit the [current release page](). From there, download Runr for your operating system and the `plugins.zip` file.

Extract the Runr zip file. Place the folder that was extracted in the location of your choice. This can be pretty much anywhere on your system as long as you have read, write, and execute access without needing elevated permissions (e.g. sudo or admin).

Add the location of the extracted folder to your user's PATH so that the runr executable (either `runr` or `runr.exe`) can be run from anywhere on your system.

Create a folder to serve as Runr's home for it's files. This can reside anywhere that you'd like as long as your user has full access to it without elevated privileges. Add a new environment named `RUNR_HOME` variable for your user that points to this folder.

Extract the plugins.zip archive that you downloaded in the first step. Move all of the files that were extracted to a folder named `plugins` at the root of your `RUNR_HOME` folder.

Create a folder in any location that you would like where your user as full access without needing elevated privileges. Create a new environment variable for your user called `RUNR_SCRIPTS`. The value of this variable should be the path to the folder that you just created. **Do not set this variable system wide unless you are sure about what you are doing.** For the very large majority of user's, it's important that this folder and environment variable are unique for each user on your system. Setting this variable system wide will force every user to use the exact same set of scripts. If so, you may have edit privileges and folder ownership for this to work at all.

# Usage

This section only covers the most common commands that you will use in Runr. For a comprehensive list of commands and their usage you can read the [help file]() or use Runr's [help command]().

## Get help

`runr --help` or `runr -h`

If you need help at anytime you can always use the help command. This will print out useful information about how to use Runr and the different arguments that it accepts.


## List available scripts

`runr --list` or `runr -l`

This command will print a list of all available scripts that you can use through Runr.

## Run a script

`runr my-script`

To run any script that is listed by the available scripts command you can run the above command, but replace 'my-script' with the name of the script you wish to use.

# Contributing

Contributions are always welcome! Whether you are requesting a new feature, reporting a bug, or submitting a pull request, all help is greatly appreciated. This project is currently only being maintained by myself so it may take some time for me to get back with you.
