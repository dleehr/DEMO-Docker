#!/bin/bash

set -e

# This is a demo wrapper script to be run with docker-pipeline, getting the size of a file

# INPUTS
#
# CONT_INPUT_FILE

# OUTPUTS
#
# CONT_OUTPUT_FILE

# Test inputs
[ -z "$CONT_INPUT_FILE" ] && echo "Error: The CONT_INPUT_FILE variable must be set" && exit 1
[ -z "$CONT_OUTPUT_FILE" ] && echo "Error: The CONT_OUTPUT_FILE variable must be set" && exit 1

echo "Putting size of $CONT_INPUT_FILE into $CONT_OUTPUT_FILE"
stat -c '%s' $CONT_INPUT_FILE > $CONT_OUTPUT_FILE