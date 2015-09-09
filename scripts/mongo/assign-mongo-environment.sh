#!/bin/bash -e

ctx source instance runtime_properties mongo_host $(ctx target node name)
ctx source instance runtime_properties mongo_port $(ctx target node properties port)
