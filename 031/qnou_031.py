#!/usr/bin/env python3

import sys
#Words with q but no u: ['Colloq', 'IQ', 'Iraq', 'Iraqi', 'q', 'Qatar', 'QED', "q's", 'seq']
qnou_ls = list()
def qnou(s):
    qnou_s = s.lower().replace("qu", "")
    if "q" in qnou_s:
        qnou_ls.append(s)


for line in sys.stdin:
    qnou(line.strip())

print("Words with q but no u:", qnou_ls)
