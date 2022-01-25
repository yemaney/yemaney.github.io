# Shell Scripting

A shell script is a file containing a series of commands. The shell reads the file and carries out the commands as if they have been entered directly on the command line.

### How to Write a Shell Script
1. Write a script. Shell scripts are ordinary files, so they are made with a text editor. Preferably with syntax highlightin.
2. Make the script executable.
3. Put the script somewhere the shell can find i

### Script file format

```sh
#!/bin/bash
# This is out first script

echo 'Hello World!'
```
Comments designated by # symbol can also be at the end of a code line.

### Executable Permission
```sh
chmod 755 hello_world
```

### Script File Location
With the permissions set, we can now execute our script. For the script to run, we must precede the script name with an explicit path.
```sh
./hello_world
```
To use script without stating the path. You will have to add it to a directory that is registered in the PATH variable.

```sh 
export PATH=~/bin:"$PATH"
```
### Good Locations for Scripts
- personal use: ~/bin
- everyone: ~/usr/local/bin
- sys admin: ~/usr/local/sbin

### More Formatting Tricks

- If a command has both  long and short option, use the short option
- If command is long, readability can be enhanced by spreading it over several lines and indenting
    - Using line continuation backslash \
---
### variables and constants
variables are mutable, constants are immutable
`variable=value` : no spaces in-between name of variable and its value
`CONSTANT=VALUE` : CONSTANTS in al caps, if you want to enforce immutability, must make it read only. `declare -r CONSTANT=VALUE`
### parameter expansion
- Use `parameter expansion` if a variable is going be used more than once in a file
```sh
name="yemane"
echo="This is ${name} using path expansion twice with variable ${name}"
```
### Here Document
In the format of ...
```sh
command << _EOF_
text
_EOF_
```
- single and double quotes within here documents 
lose their special meaning to the shell.
### Shell Functions
Shell functions are "mini-scripts" that are located inside other scripts and can act as autonomous programs.
```sh
# formal form
function name {
    commands
    return
}

# simpler and preferred form
name () {
    commands
    return
}
```
Thr following script demonstrates the use of functions
```sh
#!bin/bash

function step2 {
    echo "Step 2"
    return
}

# Main program starts here

echo "Step 1"
step2
echo "Step 2"
```
### Local Variables
- Global variables are available throughout the the programm
- Local variables are accessible only within the shell function they   are defined in

```sh
#!/bin/bash

foo=0 # global variable foo

func () {
    local foo # variable foo local to func
    foo=1
    echo "funct_1: foo = $foo"
}

echo "global: foo = $foo"
func
```