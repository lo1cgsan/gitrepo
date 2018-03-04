#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib

print(hashlib.md5('informatyka'.encode('utf-8')).hexdigest())
print(hashlib.sha1('informatyka'.encode('utf-8')).hexdigest())
print(hashlib.sha256('informatyka'.encode('utf-8')).hexdigest())
