```powershell
Function Now-Advanced {
    [CmdletBinding()]Param(
        [Parameter(Mandatory=$true,ValueFromPipelineByPropertyName=$true)]     
        [ValidatePattern("[a-z][a-z][0-9][0-9][0-9][0-9]")]

    $EmployeeID)
Process {Write-Host $EmployeeID}
}

##### Create a systemReport via PowerShell Function "Gather-Info" ########################################
##### Ideally you are creating a hash table that can be moved from $($location) to another location. ######
#Create a Get-Help f(x)
<#
.SYNOPSIS
This is a test.
.DESCRIPTION
Description field is also a test
.PARAMETER Name
Parameter name not needed
.Example
No examples
#>
Function Gather-Info {
[CmdletBinding()]
Param()

#Collect additional information about the computer from the input parameter:

    $IPv4Address=(Get-NetIPAddress).IPAddress #Note: See how we "Get-NetIPAddress" & THEN ".IPADDRESS"
    [array]$IPArray=$IPv4Address.split(" ")
    $PCName=(Get-CIMInstance -ClassName win32_ComputerSystem).Name
    $Make=(Get-CimInstance -ClassName Win32_ComputerSystem).Manufacturer
    $OS=(Get-CimInstance -ClassName Win32_OperatingSystem).Caption
    $Today=(Get-Date -Format MM/dd/yyyy)

    $ComputerInformation=@{
        ComputerName=$PCName;
        DateOfIP="$Today";
        IPAddress=$IPArray;
        OperatingSystem=$OS;
        Manufacturer="$Make";
        WaranteeExpiration=[DateTime]"06/30/2020"
    }
    return $ComputerInformation

}



```