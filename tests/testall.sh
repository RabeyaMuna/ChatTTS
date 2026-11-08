#!/bin/sh

exitcode=0

for file in tests/*.py
do
    echo "Testing $file..."
    if python "$file"
    then
        echo "Test $file success"
    else
        echo "Error: $file exited with a non-zero status."
        exitcode=1
    fi
done

exit $exitcode
