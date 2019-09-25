# LiveSplitRemote
Python remote for LiveSplit server

## Made for this
```
https://github.com/LiveSplit/LiveSplit.Server
```

### Example Connection

![connection example](example-pictures/Connection-example.svg "Connection")
You should have setup of at least two computers to benefit from a remote in the first place.
Computer 1 is used for streaming and running the LiveSplit timer;
Computer 2 is either the one you have next to your gaming setup as a remote & chat, or you are using it directly to play.

### Prerequisites
You need to have LiveSplit installed & configured with LiveSplit server before using this.
click library might not be installed by default.
You can install it via pip (as a root)
```
pip install click
```

### Installing
change the address & port as needed editing the LSR.py file

default is ```sock.connect(('192.168.3.120', 16834))```

To run you can use:
```
python LSR.py
```
