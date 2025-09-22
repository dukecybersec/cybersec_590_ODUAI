#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

# Import the compiled app module
import app

if __name__ == "__main__":
    app.init_db()
    app.app.run(host="0.0.0.0", port=5000, debug=False)
