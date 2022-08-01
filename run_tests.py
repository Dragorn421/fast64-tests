#!/usr/bin/env python3

import conf

from pathlib import Path
import subprocess


def run_blender(blend_file, python_script, args=[]):
    return subprocess.call(
        [
            str(conf.BLENDER),
            str(blend_file),
            "--background",
            "--python-exit-code",
            "1",
            "--python",
            str(python_script),
            "--",
        ]
        + args
    )


for test_dir in Path(conf.TESTS_FOLDER).iterdir():
    python_script = test_dir / "export.py"
    export_path = test_dir / "export"

    python_script.write_text(
        f"""\
import bpy

assert bpy.context.scene.ootDLExportUseCustomPath
bpy.context.scene.ootDLExportCustomPath = {str(export_path)!r}
bpy.ops.object.oot_export_dl()

bpy.ops.wm.quit_blender()
"""
    )

    test_blends = list(test_dir.glob("*.blend"))
    assert len(test_blends) == 1
    test_blend = test_blends[0]

    retcode = run_blender(test_blend, python_script)
    assert retcode == 0, retcode
