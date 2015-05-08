#!/bin/bash

cd ../
FILEPATH=`pwd`
FILENAME=$FILEPATH/lib
LOGNAME=$FILEPATH/log

typearray=()
contentarray=()         #将字段值存放在一个数组中


show_error_massage()
{
    local errormassage=$1
    local log=$2

    echo "Error : $errormassage" >> $log
    exit 0          #当输入字段名称有误时，即退出程序
}


judge_type()
{
    type=$1

    case $type in
        0)
            echo 'Integer'
            ;;
        1)
            echo 'String'
            ;;
        *) echo ''
            ;;
    esac
}


judge_content_type()
{
    local log=$1
    local i=0
    local str=""           #存放字段值

    if [ ${#contentarray[@]}  -eq ${#typearray[@]} ];then
        while [ -n ${contentarray[$i]} ] 
        do
            echo ${typearray[$i]} | grep ^Integer$
            if [ $? -eq 0 ];then
                expr match ${contentarray[$i]} "[0-9]*$"
                if [ $? -eq 0 ];then 
                    str=$str"   "${contentarray[$i]}
                else
                    show_error_massage '类型不匹配' $log
                fi
            fi

            echo ${typearray[$i]} | grep ^String$
            if [ $? -eq 0 ];then
                expr match ${contentarray[$i]} "[a-z|A-Z]*$"
                if [ $? -eq 0 ];then
                    str=$str"   "${contentarray[$i]}
                else
                    show_error_massage '类型不匹配' $log
                fi
            fi

            i=`expr $i + 1`
            if [ -z ${contentarray[i]} ];then
                break
            fi

        done

    else
        show_error_massage '参数个数不匹配' $log

    fi
    echo $str >> $file
}


del_fild_content()
{
    local content=$1
    local log=$2
    local i=1

    echo $fild | grep ':'
    #echo content=$content
    if [ $? -eq 0 ]
    then
        fildcontent=`echo $content | cut -d':' -f$i`
        while [ -n $fildcontent ]
        do
            contentarray[`expr $i-1`]=$fildcontent
            i=`expr $i + 1`
            fildcontent=`echo $content | cut -d':' -f$i`

            if [ -z $fildcontent ]
            then
                break
            fi

        done

    fi
    #echo 'contentarray '${contentarray[@]}
    judge_content_type $log           #判断字段值是否与字段类型匹配


}


del_fild_name()
{
    local fild=$1           #字段名称
    local separator=$2      #分隔符
    local log=$3            #日志文件名
    local str=""
    local i=1
    local fildone

    echo $fild | grep ':'
    if [ $? -eq 0 ]
    then
        fildone=`echo $fild | cut -d":" -f$i`
        while [ -n $fildone ]
        do
            echo $fildone | grep '('
            if [ $? -eq 0 ]
            then
                fild1=`echo $fildone | cut -d"(" -f1`
            else
                show_error_massage '缺少左括号' $log
            fi

            if [ $i == 1 ]  #若是第一次，行首不需要空格
            then
                str=$str$fild1
            else
                str=$str"   "$fild1  #(formate:字段名称（类型）   字段名称（类型）...)
            fi
            
            intermediate=`echo $fildone | cut -d"(" -f2` 

            echo $fildone | grep ')' 
            if [ $? -eq 0 ]
            then
                type=`echo $intermediate | cut -d')' -f1`
            else 
                show_error_massage "缺少右括号" $log
            fi

            type=`judge_type $type`
            len=`echo $type | wc -c`    #统计类型长度，若为一，类型为空
    
            if [ $len -gt 1 ]
            then
                str=$str'('$type')'
                typearray[`expr $i-1`]=$type     #将数据类型保存到一个数组中。
            else
                show_error_massage '数据类型错误' $log
                break
            fi
        
            i=`expr $i + 1`

            fildone=`echo $fild | cut -d":" -f$i`
            if [ -z $fildone ]
            then
                break
            fi

        done
    else
        show_error_massage 'user str format is Error' $log
        break
    fi
    #echo 'typrarray : '${typearray[@]}
    echo $str > $file   #将字段名写入文件（formate： 字段名(字段类型)   字段名(字段类型)。。。）
}


create_file()
{
    local ok=true
    local localpath=$1
    read -p "please input your filename : " filename
    file=$localpath/$filename

    while [ $ok = 'true' ]
    do
        if [ -e $file ]
        then
            read -p "the file name alread exist,please input another : " filename
            file=$localpath/$filename
        else
            ok=false

        fi
    done

    touch $file

    echo $file
}


create_fild_content()
{
    local file=$1
    local log=$2
    local separator=':'

    fildname=`cat $file | head -1`
    echo '字段： '$fildname
    read -p 'please input the value :(format: 字段值：字段值...；) : '  readline
    while [ -n readline ]
    do
        del_fild_content $readline $log
        read -p 'please input the value :(format: 字段值：字段值...；) : '  readline
        if [ -z $readline ]
        then
            break
        fi
    done

}


create_fild_name()
{
    local file=$1
    local log=$2
    local separator=':'
    
    echo "类型： 0：Integer， 1： String"
    read -p "please input the filed list (formate:字段名称(类型):字段名称（类型）...) : " fild
    
    del_fild_name $fild $separator $log

}


create_file_content()
{
    local file=$1
    local log=$2

    create_fild_name $file $log
    create_fild_content $file $log
}


#file=$(create_file)

printf "输入： 1. 文件名， 2.日志名\n"
file=`create_file $FILENAME`
#log=`create_file $LOGNAME`
#echo LOGNAME=$log
create_file_content $file $log
a
