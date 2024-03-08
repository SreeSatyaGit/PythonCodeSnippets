import sys
if sys.argv[1] == '-server':
    import server
if sys.argv[1] == '-client':
    import client