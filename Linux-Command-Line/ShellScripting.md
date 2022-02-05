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
    return 0 # shell functions can return an exit status by including an integer argument to the return command
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
### If Statement
```sh
#!/bin/bash
x=5

if ["$x" -eq 5]; then # quotes ensure it is always a string, avoiding errors
    echo "x equals 5"
else
    echo "x does not equal 5"
fi
```
### test
The test command performs a variety of checks and comparisons. It has two equivalent expression. It returns an exit status of 0 if true, and 1 if false.
- test *expression*
- [expression]

Compound command
- [[expression]]
  - string1 =~ regex ; adds regex support
### (( ))—Designed for Integers
(( )) is used to perform arithmetic truth tests.
### Combining Expressions
| Operation | test | [[ ]] and (( )) |
| --------- | ---- | --------------- |
| AND       | -a   | &&              |
| OR        | -o   | `||`            |
| NOT       | !    | !               |
### Control Operators: Another Way to Branch
bash provides two control operators that can perform branching. The &&
(AND) and || (OR) operators work like the logical operators in the [[ ]] compound command.

- With the && operator, command1 is executed, and command2 is executed if, and only if, command1 is successful.
-  With the || operator, command1 is executed and command2 is executed if, and only if, command1 is unsuccessful

### Reading Keyboard Input
-  read assigns fields from standard input to the specified variables. 
- `read [-options] [variable...]`

```sh
#!/bin/bash

echo -n "Enter one or more values > "

read var1 var2 

echo "var1 = '$var1'"
echo "var2 = '$var2'"
```
- If read receives fewer than the expected number, the extra variables are empty `''`
-  an excessive amount of input results in the final variable containing all of the extra input
-  - If no variable name is supplied, the shell variable REPLY contains the line of data.

| Option | Description                                                                                                                                       |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| -a     | array Assign the input to array, starting with index zero.                                                                                        |
| -d     | delimiter The first character in the string delimiter is used to indicate the end of input, rather than a newline character.                      |
| -e     | Use Readline to handle input. This permits input editing in the same manner as the command line.                                                  |
| -i     | string Use string as a default reply if the user simply presses enter. Requires the -e option.                                                    |
| -n     | num Read num characters of input, rather than an entire line.                                                                                     |
| -p     | prompt Display a prompt for input using the string prompt.                                                                                        |
| -r     | Raw mode. Do not interpret backslash characters as escapes.                                                                                       |
| -s     | Silent mode. Do not echo characters to the display as they are typed. This is useful when inputting passwords and other confidential information. |
| -t     | seconds Timeout. Terminate input after seconds. read returns a non-zero exit status if an input times out.                                        |
| -u     | fd Use input from file descriptor fd, rather than standard input.                                                                                 |

### IFS
- shell normally performs word splitting using white spaces 
  - behavior is configured by shell variable IFS

### Menus
```sh
#!/bin/bash
# read-menu: a menu driven system information program
clear
echo "
Please Select:
1. Display System Information
2. Display Disk Space
3. Display Home Space Utilization
0. Quit
"
read -p "Enter selection [0-3] > "
echo "You have chosen $REPLY"
```

### while loop
- `while commands; do commands; done`

```sh
#!/bin/bash
# while-count: display a series of numbers
count=1

while [[ "$count" -le 5 ]]; do
    echo "$count"
    count=$((count + 1))
done
echo "Finished."
```
bash provides two builtin commands that can be used to control program 
flow inside loops
- break: immediately terminate the loop, and resume with next statement
- continue: skip remainder of loop, and resume with next iteration of the loop

### until loop
```sh
#!/bin/bash
# until-count: display a series of numbers
count=1

until [[ "$count" -gt 5 ]]; do
    echo "$count"
    count=$((count + 1))
done
echo "Finished."
```
- An until loop continues until it receives a zero exit status.