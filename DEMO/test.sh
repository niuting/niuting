#!/bin/bash

st(){
    str1='-h192.168137'
    str2='--host192.168.13.7'
    str3='--if_ip'
    local value

    if [ $1 = $str1 ]; then
        value=`echo $str1`
    elif [ $1 = $str2 ]; then
        value=`echo $str2`
    elif [ $1 = $str3 ]; then
        value=`echo $str3`
    else  
        value='jklfgnb'
    fi
    echo $value
}

#str3='--if_ip192.168.13.7'
str3='--if_ip'
#echo "$str3" | grep -E "^a-------------if_ip|^--"
echo "$str3" | grep  "^--"
if [ $? = 0 ]; then
    echo $"______________"
    value=`st "--if_ip"`
    echo $value
    echo ${value:7}
fi

st "--if_ip192.168.13.7"

