# Docker compose profiles directive

## Issue

I was trying to have smart separtion between different development environments for our project. Fox example only run selected services when developing frontend locally, or run different set of services when developing backend locally.

## Solution

For now we are using `docker-compose.override.yml`. But I found out there is `profiles` directive https://github.com/compose-spec/compose-spec/blob/master/spec.md#profiles
