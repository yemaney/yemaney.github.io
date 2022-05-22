# week 3 : remote connections to vm

- In order for to connect to a remote server. The server must have a program that is always listening to connections.

## commands

- `ip a` - show all IP addresses
- `clear` - clear screen
- `which` - display path to a program
- `users` - shortname of all logged in users
- `w` - more information on every user logged in
- `sudo apt install openssh-server` - install ssh server (if not)

## ssh into VirtualBox

- make sure virtual box machine is attached ot bridge adapter to enable easy ssh
    - `Settings > Network > adapter 1 > attached to > Bridged adapter`

- connect ith ssh
  - `ssh -l <user> <ip>`
  - enter users password

- virtualbox command line
  - add `export PATH="$PATH:/c/Program Files/Oracle/VirtualBox"` to .bashrc
  - `vboxmanage startvm <vmname> --type headless` start the vm in headless mode
  - `vboxmanage list runningvms` list running vms
  - `vboxmanage list vms` list all vms
  - `vboxmanage controlvm <vmname> poweroff` power off headless vm

## vi Basics
- `i` - change to insert mode
- `ESC`- change to command mode
- `arrow keys` - navigation
- `:wq` - save and quit
- `:q!` - quite without saving
- `:w`- save without exiting