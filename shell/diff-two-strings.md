# How to diff 2 or more strings

## Issue
I want to run diff on 2 strings

## Solution
https://stackoverflow.com/a/454549/3627387
```console
diff  <(echo "$string1" ) <(echo "$string2")
```

## What we learned
1. How to run shasum on files on macOS
   ```console
   $ diff <(shasum -a 256 go1.15.8.linux-amd64.tar.gz) <(echo "d3379c32a90fdf9382166f8f48034c459a8cc433730bc9476d39d9082c94583b  go1.15.8.linux-amd64.tar.gz")
   ```
   **Note**: there are 2 spaces between sum and file
