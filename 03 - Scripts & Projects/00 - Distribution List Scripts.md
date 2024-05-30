# Zero to Hero > 03 - Scripts & Projects
## 03 - Scripts & Projects > 01 - Distribution List Scripts

### Exchange / Office 365 | Adding & Removing | PowerShell Distribution List Changes 
```powershell
# Load the Distribution List ex& Members:

$GroupAlias = " "
$GroupMembersCurrent = Get-DistributionGroupMember $GroupAlias
$CSV = Import-CSV "C:\temp\list.csv"

# Removing ALL Users from the DL (Used in a swap)
ForEach ($Member in $GroupMembersCurrent) {
    Remove-DistributionGroupMember -Identity $GroupAlias -Member $member.PrimarySMTPAddress -Confirm:$false
    Write-Host "Removed User: " $Member.PrimarySMTPAddress
}

# Adding New Users to the DL by CSV
ForEach ($Member in $CSV){
    
    Add-DistributionGroupMember -Identity $GroupAlias -Member $member.PrimarySMTPAddress -Confirm:$false
    Write-Host "Added User(s): " $Member.PrimarySMTPAddress
}
```

#### Get Distribution List & Export Members
```powershell

$DLList=@('enterDLListsHere')

# For each element ($dl) in the list above ($DLList) 
# You can substitute the $DLList to Import-CSV & import many more files. See: Import-CSV

foreach ($dl in $DLList) { 
    Write-Host "
    DL Name:"$dl 
    "
    DL Members: "
    
    Get-DistributionGroupMember -identity $dl | Select-Object PrimarySMTPAddress,Alias | ft
}
```
#### Array of Users : Get Properties & Group Memberships
```powershell

$UserList = ('XUser','XUser','XUser','XUser','XUser','XUser','XUser','XUser')

foreach ($Username in $UserList){
   
   Write-Host("Username: " + $Username)
    Get-ADUser -Identity $Username -Properties * | Select -Property manager,managedBy,mailNickname,msExchHideFromAddressLists,enabled,description,msExchRecipientDisplayType,msExchRecipientTypeDetails,msExchRemoteRecipientType | ft
    Get-ADPrincipalGroupMembership -Identity $Username | ft              
}
```

Utilize this to change a wide set of properties or values or group memberships if need be.

#### Get Values of Users in AD / Exchange & Set to New Values from CSV (Work-in-Progress)
```powershell

$CSV = Import-CSV "C:\temp\list.csv" #CSV should already contain Name or PrimarySMTPAddress in the first column. Additional columns to be Attributes that need to be changed. i.e. Name;JobTitle;Description

foreach ($Username in $CSV){
   
   Write-Host("User Details: " + $Username + "," + $JobTitle + "," + $Description) 
    Get-ADUser -Identity $Username $CSV.
    Set-ADUser -Identity $Username -Properties 

}
```

#### Import Distribution List & Export Members w/ Properties

```powershell
$DLList = Import-CSV -path "C:\Scripts\ScriptInputs\DLMEMBERLIST.CSV"
    
foreach ($PRIMARY_EMAIL in $DLList){
   
   Get-DistributionGroupMember -Identity $PRIMARY_EMAIL.PRIMARY_EMAIL | Select-Object name,Alias,PrimarySMTPAddress,$PRIMARY_EMAIL.GroupName | Out-File -Append -filepath 'C:\Scripts\ScriptOutputs\output.csv'
    }

```

