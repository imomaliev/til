# DIRENV\_DIR environment variable

## Question
For some reason `DIRENV_DIR` has appended `-` before `$PWD`
```console
echo $DIRENV_DIR
-$PWD
```

## Answer
https://github.com/direnv/direnv/commit/b18b1f59a9eed1b3d7cb2f06980da3f94dad0155#diff-221dbe7605813b08a9a1f12ea8a612f2006f9376d0699dcf6538dca1aa30c668
https://github.com/direnv/direnv/commit/d7778d14384a7c459351cc212b56dacd8b7f0470


## What we learned
1. We need to strip "-" from DIRENV_DIR before using it
   ```console
   echo ${DIRENV_DIR#-}
   ```
1. There is "named directories" concept in zsh but I still need to properly understand it.
