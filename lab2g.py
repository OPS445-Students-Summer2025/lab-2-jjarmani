#!/usr/bin/env python3
# Author: Sing Man Wong
# Author ID: 170543235
# Date Created: 2025/05/16

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')
