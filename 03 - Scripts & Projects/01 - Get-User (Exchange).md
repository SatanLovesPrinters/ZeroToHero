# Get-User 
## Grab user information, select properties, filter, modify AD attributes

```powershell
$UserList = ('userA, userB, userC')

foreach ($Username in $UserList){
   
   Write-Host("Username: " + $Username)
    Get-ADUser -Identity $Username -Properties * | Select -Property manager,managedBy,mailNickname,msExchHideFromAddressLists,enabled,description,msExchRecipientDisplayType,msExchRecipientTypeDetails,msExchRemoteRecipientType | ft
    Get-ADPrincipalGroupMembership -Identity $Username | ft
         
               
}
```


```powershell
$DLList=@('enterDLListsHere')

foreach ($dl in $DLList) { #For each element ($dl) in the list above ($DLList) You can substitute the $DLList to Import-CSV & import many more files. See: Import-CSV
    Write-Host "
    DL Name:"$dl 
    "
    DL Members: "
    

    Get-DistributionGroupMember -identity $dl | Select-Object PrimarySMTPAddress,Alias | ft
    

```

### Note this is declared as a function & does not need to be. 
### Use Import-CSV if a .csv contains the members required. 

```powershell
Function Get-UserDLMembers{

    $DLList = Import-CSV -path C:\Scripts\ScriptInputs\DLMEMBERLIST.CSV
    foreach ($PRIMARY_EMAIL in $DLList){
   
    Get-DistributionGroupMember -Identity $PRIMARY_EMAIL.PRIMARY_EMAIL | Select-Object name,Alias,PrimarySMTPAddress,$PRIMARY_EMAIL.GroupName | Out-File -Append -filepath 'C:\Scripts\ScriptOutputs\output.csv'
    }

}

```