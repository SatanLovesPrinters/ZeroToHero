### Utilizes RemotePSSession to uninstall software across a wide range of devices.

```powershell
$computerNames = Get-Content C:\Scripts\serverInput.txt

$appName = "AppName"

$yourAccount = (Get-Credential)

ForEach ($computerName in $computerNames) {
    Invoke-Command -ComputerName $computerName -Credential $yourAccount -ScriptBlock {
        Get-WmiObject Win32_product | Where {$_.name -eq $appName} | ForEach {
            $_.Uninstall()
        }
    }
}
```
