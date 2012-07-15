#!/bin/bash

git diff --name-only -z HEAD HEAD~1 | xargs -d '\n'
