#!/usr/bin/env python3
import sys
import os
import subprocess
import json
import tempfile
import shutil
from pathlib import Path

def setup_libreoffice_macro():
    """Set up LibreOffice to allow macro execution"""
    config_dir = Path.home() / '.config' / 'libreoffice' / '4' / 'user'
    config_dir.mkdir(parents=True, exist_ok=True)
    
    registrymodifications = config_dir / 'registrymodifications.xcu'
    
    config_content = '''<?xml version="1.0" encoding="UTF-8"?>
<oor:items xmlns:oor="http://openoffice.org/2001/registry" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<item oor:path="/org.openoffice.Office.Common/Security/Scripting"><prop oor:name="MacroSecurityLevel" oor:op="fuse"><value>0</value></prop></item>
</oor:items>'''
    
    registrymodifications.write_text(config_content)

def recalculate_excel(filepath, timeout=30):
    """Recalculate Excel formulas using LibreOffice"""
    setup_libreoffice_macro()
    
    abs_path = os.path.abspath(filepath)
    
    # Create a temporary copy to work with
    with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp:
        tmp_path = tmp.name
    
    shutil.copy2(abs_path, tmp_path)
    
    try:
        # Use LibreOffice to open and recalculate
        cmd = [
            'libreoffice',
            '--headless',
            '--calc',
            '--convert-to', 'xlsx',
            '--outdir', os.path.dirname(abs_path),
            tmp_path
        ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        # Move the converted file back
        converted = os.path.join(os.path.dirname(abs_path), os.path.basename(tmp_path))
        if os.path.exists(converted):
            shutil.move(converted, abs_path)
            return {"status": "success", "message": "Formulas recalculated"}
        else:
            return {"status": "error", "message": "Conversion failed"}
            
    except subprocess.TimeoutExpired:
        return {"status": "error", "message": f"Timeout after {timeout}s"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "Usage: recalc.py <excel_file> [timeout]"}))
        sys.exit(1)
    
    filepath = sys.argv[1]
    timeout = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    
    result = recalculate_excel(filepath, timeout)
    print(json.dumps(result, indent=2))
