#!/usr/bin/expect -f


set port 22
set user root
set host localhost
set password root11
set timeout 5

spawn ssh -p$port $user@$host

expect "password:"
send "$password\r"

expect "*]#"
send "ssh-keygen -t rsa\r"

expect "*]:"
send "\n\r"

expect "*]:"
send "\n\r"

expect "*]:"
send "\n\r"

expect eof
exit
