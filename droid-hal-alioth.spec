# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device alioth
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Poco F3

%define installable_zip 1

%define droid_target_aarch64 1

%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%include rpm/dhd/droid-hal-device.inc

%define makefstab_skip_entries /product /system /system_ext /vendor /dev/stune /dev/cpuset /sys/fs/pstore /dev/cpuctl

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

