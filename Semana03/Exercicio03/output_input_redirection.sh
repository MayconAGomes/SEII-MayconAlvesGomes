#!/bin/bash

echo Hello World > hello.txt
cat hello.txt
echo Good day to you > hello.txt
cat hello.txt
rm hello.txt
echo Hello World >> hello.txt
cat hello.txt
echo Good day to you >> hello.txt
cat hello.txt

wc -w hello.txt
wc -w < hello.txt
cat << EOF
I will
write some
text here
EOF
wc -w <<< "Hello there wordcount!"


