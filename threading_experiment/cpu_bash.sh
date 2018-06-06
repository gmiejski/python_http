#!/bin/bash

function myfunc()
{
    sum=0
    echo "Starting"
    for (( i=1; i<=1000000; i++))
	do
        sum=$(($sum + 1))
    done
    echo "Finished"
}


myfunc &
pid1=$!
myfunc &
pid2=$!
myfunc &
pid3=$!
( echo $$; echo $BASHPID )
echo $pid1
echo $pid2
echo $pid3

while :
do
    main=`ps -p $$ -o %cpu,%mem`
    echo $pid1 has $main
    a=`ps -p $pid1 -o %cpu,%mem`
    echo $pid1 has $a
    a=`ps -p $pid2 -o %cpu,%mem`
    echo $pid2 has $a
    a=`ps -p $pid3 -o %cpu,%mem`
    echo $pid3 has $a
    ss=`lsof -p $pid1 -t`
#    echo
    if [ -z  $ss ] ; then
          exit 0
    fi

done