#!/bin/bash

#time： 2015/05/04

direction(){
    echo "Redis_HA backend API manager"
    echo "[-i|--iptbs IPTBS] the IP access list"
    echo "[-p|--port PORT] the port is instance port"
    echo "[-d|--dump DUMP] should be yes or no"
    echo "[-a|--aof AOF] should be yes or no"
    echo "[-m|--maxmem MAXMEM] the most big Within the save value"
    echo "[-h|--host HOST] ip address"
    echo "[-s|--service SERVICE] the backend API service url"
    echo "[-v|--verbose VERBOSE] show verbose information"
    echo "[--action ACTION] the action is api interfaces"
    echo "[--masterip MASTERIP] the ip address of the master"
    echo "[--masterport MASTERPORT] the port of the master"
    echo "[--slaveport SLAVEPORT] the port of the slave"
    echo "[--if_ip IF_IP] "
    echo "[--debug] the debug information"
    echo "[--help HELP] it's me"
    echo "redis_client.sh -s  http://113.107.161.240:3000 -i 192.168.1.1,10.20.0.0 -p 3025 -d yes -a no -m 0 -a init --debug"
    echo "redis_client.sh -s  http://113.107.161.240:3000 -h192.168.1.1,10.20.0.0 -p 3025 -v --debug"
}

if [ $# -lt 1 ];then
    direction
    exit 1
fi

TEMP=`getopt -o i:p:d:a:m:h::s:v\
    --long iptbs:,port:,dump:,aof:,maxmem:,host::,service:,action:,masterip:,masterport:,slaveport:,if_ip::,verbose,help --"$@"`
if [ $? != 0 ]; then
    echo "Terminating..." >&2
    exit 1
fi

eval set --"$TEMP"

grep_command(){
    local parameter=$1
    local value

    echo "$parameter" | grep -E "^--host|^-h|^--if_ip"
    if [ $? = 0 ]; then 
        echo "$parameter" | grep "^--host"
        if [ $? = 0 ]; then
            value=`echo ${parameter:6}`
        fi

        echo "$parameter" | grep "^-h"
        if [ $? = 0 ]; then
            value=`echo ${parameter:2}`
        fi

        echo "$parameter" | grep "^--if_ip"
        if [ $? = 0 ]; then 
            value=`echo ${parameter:7}`
        fi
    else
        str='@'
    fi

    echo $value
}

while true; do
    case $1 in
        -i|--iptbs)
            IPTBS=$2; shift 2 ;;

        -p|--port)
            PORT=$2; shift 2 ;;
        
        -d|--dump)
            DUMP=$2; shift 2 ;;

        -a|--aof)
            AOF=$2; shift 2 ;;

        -m|--maxmem)
            MAXMEM=$2; shift 2;;

        -s|--service)
            SERVICE=$2; shift 2 ;;

        -v|verbos)
            VERBOSE='v'; shift ;;

        --action)
            ACTION=$2; shift 2 ;;

        --masterip)
            MASTERIP=$2; shift 2 ;;

        --masterport)
            MASTERPORT=$2; shift 2 ;;

        --slaveport)
            SLAVEPORT=$2; shift 2 ;;

        --debug)
            DEBUG=1; shift ;;
        
        --help)
            HELP=1; shift ;;

        --)
            shift; break ;; 

        *)
            value=`grep_command() $1`
            echo "$parameter" | grep -E "^--host|^-h"
            if [ $? = 0 ]; then
                if [ -z $HOST ]; then
                    HOST='backend机器本身实例'
                else
                    HOST=$value; 
                fi
                shift  
            fi 

            echo "$parameter" | grep -E "^--if_ip"
            if [ $? = 0 ]; then 
                if [ -z $IF_IP ]; then
                    IF_IP='0.0.0.0'
                else
                    IF_IP=$value
                fi
                shift
            fi

            if [ $value = '@' ]; then
                echo "unknow argument $1"
                exit 1
            fi
            ;;
    esac
done

if [ x"$HELP" = x"1" ]; then
    direction
    exit 0
fi

if [ -z $ACTION ]; then
    echo "action argument must be include, use [-a action| --action action]"
    echo "the action is the interface of Redis Backend which in document"
    exit 1
fi

[ `echo "$DUMP" | grep -iE "yes|no"` ] || DUMP="默认值"         #grep -E 匹配扩展正则表达式
[ `echo "$AOF" | grep -iE "yes|no"` ] || AOF="默认值"

debug(){
    if [ x"$DEBUG" = x"1" ]; then
        echo "[DEBUG]action: "$ACTION
    fi
}

debug

if [ x"$VERBOSE" = x"v" ]; then
    CURL="curl -v"
else
    CURL="curl"
fi

init(){
    echo $"Initialize a redis instance with port $PORT"
    $CURL $VERBOSE $SERVICE/init?"iptbs=$IPTBS&port=$PORT&dump=$DUMP&aof=$AOF&&maxmem=$MAXMEM"
}

baseinfo(){

    echo $"Get the machine l basic information with port $PORT"
    $CURL $VERBOSE $SERVICE/baseinfo?"port=$PORT&host=$HOST"
}

initslave(){
    echo $"Will an initialization of the instance configuration as a slave"
    $CURL $VERBOSE $SERVICE/initslave?"masterip=$MASTERIP&masterport=$MASTERPORT&slaveport=$SLAVEPORT"
}

usage(){
    echo $"Get the native memory and disk information"
    $CURL $VERBOSE $SERVICE/usage
}

ports(){
     echo $"Get This machine is using the port number"
     $CURL $VERBOSE $SERVICE/ports?"if_ip=$IF_IP"
}

iptables(){
    echo $"Add IP access rules with port $PORT"
    $CURL $VERBOSE $SERVICE/ports?"iptbs=$IPTBS&port=$PORT"
}

show(){
    echo $"$ACTION"
    $CURL $SERVICE/"$ACTION"?"port=$PORT"
}

case "$ACTION" in
    init)
        init
        ;;

    baseinfo)
        baseinfo
        ;;

    initslave)
        initslave
        ;;

    usage)
        usage
        ;;

    ports)
        ports
        ;;

    iptables)
        iptables
        ;;

    *)
        show
        ;;

esac



