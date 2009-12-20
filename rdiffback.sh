#!/bin/sh

# Where the backups go, this is an sshfs mount for me
DESTINATION="/home/sontek/backups/"
LOG="/var/log/backup/"
TIMESTAMP=`date +%m%d_%H%M`

# How long to keep backup history (6 months)
MAXAGE="6M"

# Options from man page
OPTIONS="--force --print-statistics --exclude **.iso"

# Make sure $DESTINATION exists
if [ ! -d "$DESTINATION" ]; then
    echo "Error: '$DESTINATION' does not exist!!"
    exit 1
fi

# Check if rdiff-backup exists
if ! which rdiff-backup; then
    echo "You need to install rdiff-backup"
    exit 1
fi

# Just put all the folders you want backed here.
for SOURCE in "/home/sontek/dotfiles/"
do
    if [ ! -d "$DESTINATION/$SOURCE" ]; then
        echo "Creating folder $DESTINATION/$SOURCE"
        mkdir -p "$DESTINATION/$SOURCE"
    fi

    echo "Backup: rdiff-backup $OPTIONS $SOURCE $DESTINATION/$SOURCE"
    rdiff-backup $OPTIONS "$SOURCE" "$DESTINATION/$SOURCE"

    # It went well, remove stuff older than MAXAGE
    if [ "$?" -eq 0 ]; then
        echo "Cleanup: rdiff-backup --force --remove-older-than $MAXAGE
        $DESTINATION/$SOURCE"
        rdiff-backup --force --remove-older-than $MAXAGE "$DESTINATION/$SOURCE"
    else
        echo $? > $LOG/fail$TIMESTAMP.log
    fi
done
