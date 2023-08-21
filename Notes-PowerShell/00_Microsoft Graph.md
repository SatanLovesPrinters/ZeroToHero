

<summary>
MICROSOFT GRAPH:
https://learn.microsoft.com/en-us/powershell/microsoftgraph/installation?view=graph-powershell-1.0 (INSTALL)
https://learn.microsoft.com/en-us/powershell/microsoftgraph/get-started?view=graph-powershell-1.0 (GET STARTED)


Creating Microsoft Graph Profiles: 
https://www.sharepointdiary.com/2022/04/office-365-find-last-login-date-using-powershell.html#ixzz893oyRdcZ

</summary>

<summary>
#Set the Graph Profile
Select-MgProfile auditProfile
 
#Properties to Retrieve
$Properties = @(
    'Id','DisplayName','Mail','UserPrincipalName','UserType', 'AccountEnabled', 'SignInActivity'   
)
 
#Get All users along with the properties
$AllUsers = Get-MgUser -All -Property $Properties | Select-Object $Properties
 
$SigninLogs = @()
ForEach ($User in $AllUsers)
{
    $SigninLogs += [PSCustomObject][ordered]@{
            LoginName       = $User.UserPrincipalName
            Email           = $User.Mail
            DisplayName     = $User.DisplayName
            UserType        = $User.UserType
            AccountEnabled  = $User.AccountEnabled
            LastSignIn      = $User.SignInActivity.LastSignInDateTime
    }
}
 
$SigninLogs
 
#Export Data to CSV
$SigninLogs | Export-Csv -Path "C:\Temp\SigninLogs.csv" -NoTypeInformation
</summary>
