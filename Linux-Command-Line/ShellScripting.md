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

### Case
```sh
case word in
    [pattern [| pattern]...) commands ;;]...
esac
```
- patterns used by case are the same as those used by pathname expansion
- Patterns are terminated with a ) character

| Pattern      | Description                                       |
| ------------ | ------------------------------------------------- |
| a)           | Matches if word equals a.                         |
| [[:alpha:]]) | Matches if word is a single alphabetic character. |
| ???)         | Matches if word is exactly three characters long. |
| *.txt)       | Matches if word ends with the characters .txt.    |
| *)           | Matches any value of word.                        |

- can also use | to combine patterns as an `or` conditional
- add the `;;&` notation to terminate each action to enable performing multiple actions

```sh
#!/bin/bash
# case4-2: test a character
read -n 1 -p "Type a character > "
echo
case "$REPLY" in
    [[:upper:]]) echo "'$REPLY' is upper case." ;;&
    [[:lower:]]) echo "'$REPLY' is lower case." ;;&
    [[:alpha:]]) echo "'$REPLY' is alphabetic." ;;&
    [[:digit:]]) echo "'$REPLY' is a digit." ;;&
    [[:graph:]]) echo "'$REPLY' is a visible character." ;;&
    [[:punct:]]) echo "'$REPLY' is a punctuation symbol." ;;&
    [[:space:]]) echo "'$REPLY' is a whitespace character." ;;&
    [[:xdigit:]]) echo "'$REPLY' is a hexadecimal digit." ;;&
esac
```

### for loops
- traditional shell form
```sh
for variable [in words]; do
 commands
done
```
```sh
#!/bin/bash

for i in 0 1 2 3 4; do
        echo "$i"
done
```


- C Language form
```sh
for (( expression1; expression2; expression3 )); do
 commands
done
```

```sh
#!/bin/bash
# simple_counter: demo of C style for command

for (( i=0; i<5; i=i+1 )); do
    echo $i
done
```

- expression1 initializes the variable i
- expression2 sets the condition for loop to run until
- expression3 increments the value of i by 1 each time the loop repeats

### Positional Parameters
- The shell provides a set of variables called positional parameters that contain the individual words on the command line. The variables are named 0 through 9.
  - 0 is script name
  - can be accessed like $0 $1 $2 etc.
- determine number of arguments: `$#` 
- to access many arguments use `shift`
  - cause each parameter to "move down one" each time it is executed

```sh
#!/bin/bash
# posit-param2: script to display all arguments
count=1
while [[ $# -gt 0 ]]; do
    echo "Argument $count = $1"
    count=$((count + 1))
    shift
done
```
- To handle many positional parameters at once use `"$@"`

### Parameter Expansion

Expansions to Manage Empty Variables
- expansion with defaults to manage empty variables
  - `${parameter:-default}`
- expansion with defaults to manage empty variables and assign default value to parameter if used
  - `${parameter:=default}`
- exit with an error if parameter is unset
  - `${parameter:?default}`
- expand to default if parameter exists, else return nothing
  - `${parameter:+default}`

Expansions That Return Variable Names
- to return the names of variables
  - `{!prefix*}`

String Operations
- expand into length of string contained in parameter
  - `${#parameter}`
- getting a slice of a string
  - `${parameter:offset:length}`
- remove portion of string matching a pattern
  - `${parameter#pattern}` or `${parameter##pattern}`
- a search-and-replace operation
  - `${parameter/pattern/string}`

Case Conversion
- using `declare` force a variable to always contain the desired format
  - `declare -u upper`
  - `declare -l lower`

### Arithmetic Evaluation and Expansion
`$((expression))`

| Operator | Description        |
| -------- | ------------------ |
| +        | Addition           |
| -        | Subtraction        |
| *        | Multiplication     |
| /        | Integer division   |
| **       | Exponentiation     |
| %        | Modulo (remainder) |

### Assignment
| Notation           | Description                    |
| ------------------ | ------------------------------ |
| parameter = value  | Simple assignment.             |
| parameter += value | parameter = parameter + value. |
| parameter++        | parameter = parameter + 1      |


### Logic
| Operator          | Description                      |
| ----------------- | -------------------------------- |
| <=                | Less than or equal to.           |
| >=                | Greater than or equal to.        |
| <                 | Less than.                       |
| >                 | Greater than.                    |
| ==                | Equal to.                        |
| !=                | Not equal to.                    |
| &&                | Logical AND.                     |
| `||`              | Logical OR.                      |
| expr1?expr2:expr3 | If expr1  then expr2; else expr3 |

### Arrays
Limited to one dimension
- single value: `name[subscript]=value`
- multiple values: `name=(value1 value2 ...)`
- subscript `@` can be used to access every element in an array
- number of array elements: `o ${#a[@]}`
- find subscript used in array: `${!array[@]}`
- appending to an array: `array+=value`
- delete an array: `unset array`
- sort an array : `($(for i in "${a[@]}"; do echo $i; done | sort))`
- Associative arrays (string indexes): `array["string"]=value`

