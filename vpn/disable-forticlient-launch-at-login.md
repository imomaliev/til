# How to disable FortiClient launch at login

## Issue

FortiClient is automatically added to launch at login, and there is no simple way to disable this

## Solution

```console
$ sudo vim /Library/LaunchAgents/com.fortinet.forticlient.fct_launcher.plist
# edit <key>RunAtLoad</key> to <false/> value
```

## Links

https://forum.fortinet.com/tm.aspx?m=97324
