# Files

## Assumptions
- Valheim server running on Linux via LGSM (https://linuxgsm.com/)

## Logs?
Directory listing of all the files which look like logs based on their names.

    vhserver@valheim-1:~$ find -regex ".*log.*"
    ./log
    ./log/script
    ./log/script/vhserver-steamcmd.log
    ./log/script/vhserver-script-2021-03-11-17:49:59.log
    ./log/script/vhserver-script-2021-03-11-20:15:58.log
    ./log/script/vhserver-script.log
    ./log/script/vhserver-script-2021-03-11-20:29:48.log
    ./log/script/vhserver-script-2021-03-11-17:54:22.log
    ./log/script/vhserver-script-2021-03-11-17:47:29.log
    ./log/server
    ./log/console
    ./log/console/vhserver-console-2021-03-11-17:54:22.log
    ./log/console/vhserver-console-2021-03-11-17:47:29.log
    ./log/console/vhserver-console.log
    ./log/console/vhserver-console-2021-03-11-20:15:58.log
    ./log/console/vhserver-console-2021-03-11-17:49:59.log
    ./log/console/vhserver-console-2021-03-11-20:29:48.log
    ./.bash_logout
    ./.local/share/Steam/logs
    connection_log_2456.txt
    appinfo_log.txt
    connection_log.txt
    configstore_log.txt
    stats_log.txt
    stderr.txt
    remote_steamcmd.txt
    shader_log.txt
    sitelicense_steamcmd.txt
    bootstrap_log.txt
    content_log.txt
    workshop_log.txt
    ./lgsm/functions/install_logs.sh
    ./lgsm/functions/core_logs.sh
    ./lgsm/functions/check_logs.sh

## Interesting logs

| Filename                 | Important?   | Contents                        | Notes                                                                |
|--------------------------|--------------|---------------------------------|----------------------------------------------------------------------|
| vhserver-steamcmd.log    | ?            | ?                               |                                                                      |
| vhserver-script.log      | ?            | ?                               | rotating log with date. Ex: vhserver-script-2021-03-11-20:15:58.log  |
| vhserver-console.log     | ?            | Player connection. Player death | rotating log with date. Ex: vhserver-console-2021-03-11-20:15:58.log |
| connection_log.txt       | ?            | ?                               |                                                                      |
| connection_log_2456.txt  | ?            | ?                               | Connection log but with running port appended (2456 in this case)    |
| appinfo_log.txt          | ?            | ?                               |                                                                      |
| configstore_log.txt      | ?            | ?                               |                                                                      |
| stats_log.txt            | ?            | ?                               |                                                                      |
| stderr.txt               | ?            | stderr                          |                                                                      |
| remote_steamcmd.txt      | ?            | ?                               |                                                                      |
| shader_log.txt           | Probably not | Shader logs?                    |                                                                      |
| sitelicense_steamcmd.txt | Probably not | ?                               |                                                                      |
| bootstrap_log.txt        | ?            | ?                               |                                                                      |
| content_log.txt          | ?            | ?                               |                                                                      |
| workshop_log.txt         | ?            | ?                               | Related to Steam Workshop?                                           |
| install_logs.sh          | ?            | ?                               | Shell script - should check what this does                           |
| core_logs.sh             | ?            | ?                               | Shell script - should check what this does                           |
| check_logs.sh            | ?            | ?                               | Shell script - should check what this does                           |

## Console logs | location - /home/vhserver/log/console
There are instances that says "Server: New peer connected,sending global keys". Followed by another log line "Got character ZDOID from Richard Flamel : 26869525:7"
**Characters are assigned an id each  time they connect to a server**
This is the first time a person connected. "03/12/2021 12:51:57: Got character ZDOID from FartMeister : 1351653627:1" and this is the second time they connected to the same server during the same session in which the server was on. "03/12/2021 12:54:37: Got character ZDOID from FartMeister : 1708501107:1"
- Session ids can be "negative" ex. 03/13/2021 09:28:37: Got character ZDOID from Richard Flamel : -402550596:10

### Character Deaths
When a character dies, it looks like this "03/13/2021 12:01:02: Got character ZDOID from Richard Flamel : 0:0" with the 0:0. The next entry in the console log will be the server assigning the character a new id.
