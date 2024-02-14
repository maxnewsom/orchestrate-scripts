# orchestrate-scripts

This is a script written with python to determine how many POST commands are in a Sauce Labs test result. It uses Sauce Labs' Jobs API Endpoint. POST commands are the types of commands that the Sauce Orchestrate can impact. Sauce Orchestrate is a solution that can vastly improve automated test performance on the Sauce Labs cloud.

To use this script, you need to have Python installed on your machine, and you need to set a SESSION_ID variable

`export SESSION_ID=<sauce labs session id>`

You can then execute the script with
`python3 post_command.py`
