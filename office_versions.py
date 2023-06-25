versions = {
    "Office 2019": {"dir1": "cd /d %ProgramFiles%\Microsoft Office\Office16",
                    "dir2": "cd /d %ProgramFiles(x86)%\Microsoft Office\Office16",
                    "cmd1": r"for /f %x in ('dir /b ..\root\Licenses16\ProPlus2019VL*.xrm-ms') do cscript ospp.vbs /inslic:""..\root\Licenses16\%x""",
                    "cmd2": "cscript ospp.vbs /setprt:1688",
                    "cmd3": "cscript ospp.vbs /unpkey:6MWKP >nul",
                    "cmd4": "cscript ospp.vbs /inpkey:NMMKJ-6RK4F-KMJVX-8D9MJ-6MWKP",
                    "cmd5": "cscript ospp.vbs /sethst:e8.us.to",
                    "cmd6": "cscript ospp.vbs /act"},
    "Office 2016": {"dir1": "cd /d %ProgramFiles%\Microsoft Office\Office16",
                    "dir2": "cd /d %ProgramFiles(x86)%\Microsoft Office\Office16",
                    "cmd1": r"for /f %x in ('dir /b ..\root\Licenses16\proplusvl_kms*.xrm-ms') do cscript ospp.vbs /inslic:""..\root\Licenses16\%x""",
                    "cmd2": "cscript ospp.vbs /inpkey:XQNVK-8JYDB-WJ9W3-YJ8YR-WFG99",
                    "cmd3": "cscript ospp.vbs /unpkey:BTDRB >nul",
                    "cmd4": "cscript ospp.vbs /unpkey:KHGM9 >nul",
                    "cmd5": "cscript ospp.vbs /unpkey:CPQVG >nul",
                    "cmd6": "cscript ospp.vbs /sethst:e8.us.to",
                    "cmd7": "cscript ospp.vbs /setprt:1688",
                    "cmd8": "cscript ospp.vbs /act"
    }
}