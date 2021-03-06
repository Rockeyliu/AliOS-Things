#!/bin/bash
echo "Making SDL"
library_path=$1
host_os=$2
toolchan_path=$3
config_file=$4
origin_path="$(pwd)"
comp_path="$( cd "$(dirname "$0")" ; pwd -P )"
echo origin_path: $origin_path
echo comp_path: $comp_path

# include config.mk to import variables
python ./build/scripts/aos_configmk_convert.py ${config_file} ${config_file}.sh
source ${config_file}.sh
rm -f ${config_file}.sh

# enter into component path
cd $comp_path
if [ $? -ne 0 ]; then
    echo "cd fail!"
    exit 1
fi

# add your specific build command, and set the path of library generated by
# third party build tools
#cd cmake_test
#if [ ! -d "build" ]; then
#    mkdir build
#fi 
#cd build

if [ ! -f "Makefile" ]; then
    cmake .. -DCMAKE_C_COMPILER="$origin_path/${toolchan_path}gcc" -DCMAKE_CXX_COMPILER="$origin_path/${toolchan_path}g++" -DCMAKE_BUILD_FLAGS="$AOS_SDK_LDFLAGS" -DCMAKE_C_FLAGS="$AOS_SDK_CFLAGS --specs=nosys.specs" -DCMAKE_CXX_FLAGS="$AOS_SDK_CFLAGS --specs=nosys.specs"
fi
AOS_INCLUDES=$( echo "$AOS_SDK_INCLUDES" | sed -e 's;\-I./;\-I../../../../;g' )
make AOS_BUILD_FLAGS="$AOS_SDK_LDFLAGS" AOS_C_FLAGS="$AOS_SDK_CFLAGS --specs=nosys.specs" AOS_CXX_FLAGS="$AOS_SDK_CFLAGS --specs=nosys.specs" AOS_DEFINES="$AOS_SDK_DEFINES" AOS_GLOBAL_INCLUDES="$AOS_INCLUDES" prefix="$origin_path/$library_path"
#make 
#make install
#make arlib
echo "==================================="
#echo $AOS_SDK_CFLAGS
#echo $AOS_DEFINES
#echo $AOS_INCLUDES
#echo $AOS_SDK_LDFLAGS
#echo "AOS_INCLUDES=$AOS_SDK_INCLUDES" | sed -e 's;\-I./;\-I../../../../;g'
echo $library_path
echo $host_os
echo $toolchan_path
echo $config_file
echo "==================================="

libraries="./lib/libSDL.a"

# copy library to AliOS-Things library folder

#echo "copy to library path: $origin_path/$library_path"
mv $libraries $origin_path/$library_path
#if [ $? -ne 0 ]; then
#    echo "cp failed!"
#    exit 1
#fi
