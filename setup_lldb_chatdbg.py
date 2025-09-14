#!/usr/bin/env python3
"""
Setup script to configure LLDB with ChatDBG
"""

import sys
import os

# Add the ChatDBG source directory to Python path
chatdbg_src_path = '/Users/anton/proj/ChatDBG/src'
if chatdbg_src_path not in sys.path:
    sys.path.insert(0, chatdbg_src_path)

# Now import and execute the ChatDBG LLDB module
try:
    exec(open('/Users/anton/proj/ChatDBG/src/chatdbg/chatdbg_lldb.py').read())
    print("ChatDBG loaded successfully in LLDB!")
except Exception as e:
    print(f"Failed to load ChatDBG: {e}")
    import traceback
    traceback.print_exc()
