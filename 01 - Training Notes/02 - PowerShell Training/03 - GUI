### Example of integrating PowerShell to Server Processes (AD)

```powershell
<#
Goal: Mix a on-prem to exchange online.
----Server 1
Export-LHADUser
Import-LHADUser
New-LHADUser
New-LHADExec
----Server 2
Enable-LHUserMailbox
Enable-LHExecMailbox
Delete-LHMailbox 

Script Example: Holding pre-generated scripts in a library before deploying outward. 
Import-Module functionA
Import-Module functionB
Write-Host $responseValues
#>

## Example:  Account creation by nontechnical staff
# UI - Examples
# Think of the flow of your application. 
#Import Modules that contain on-prem user and mailbox function
#Gather Information - FirstName, LastName, Username, JobTitle, EmployeeID
#Create the user account with gathered info into AD
#Create the user account with gathered info into O365
#Write-Host "The user account and mailbox were successfully created"

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$FormObjectA = New-Object System.Windows.Forms.Form
    $FormObjectA.Text = "Create a new account"
    $FormObjectA.Size = New-Object System.Drawing.Size(300,300)
    $FormObjectA.MaximizeBox = $false
    $FormObjectA.MinimizeBox = $false
    $FormObjectA.ControlBox = $true

$FormObject_FName = New-Object System.Windows.Forms.TextBox
    $FormObject_FName.location = New-Object System.Drawing.Size(25,40)
    $FormObject_FName.Size = New-Object System.drawing.size (250,20)
    $FormObject_FName.Text = "First Name"
    $FormObjectA.Controls.Add($FormObject_FName)

$FormObject_LName = New-Object System.Windows.Forms.TextBox
    $FormObject_LName.location = New-Object System.Drawing.Size(25,70)
    $FormObject_LName.Size = New-Object System.drawing.size (250,20)
    $FormObject_LName.Text = "Last Name"
    $FormObjectA.Controls.Add($FormObject_LName)

$FormObject_Username = New-Object System.Windows.Forms.TextBox
    $FormObject_Username.location = New-Object System.Drawing.Size(25,100)
    $FormObject_Username.Size = New-Object System.drawing.size (250,20)
    $FormObject_Username.Text = "Username"
    $FormObjectA.Controls.Add($FormObject_Username)

$FormObject_JobTitle = New-Object System.Windows.Forms.TextBox
    $FormObject_JobTitle.location = New-Object System.Drawing.Size(25,130)
    $FormObject_JobTitle.Size = New-Object System.Drawing.Size (250,20)
    $FormObject_JobTitle.Text = "Job Title"
    $FormObjectA.Controls.Add($FormObject_JobTitle)

$FormObject_Button_Close = new-object System.Windows.Forms.Button
    $FormObject_Button_Close.location = new-object system.drawing.size (25,200)
    $FormObject_Button_Close.Size = new-object system.drawing.size (120,25)
    $FormObject_Button_Close.TextAlign = "MiddleCenter"
    $FormObject_Button_Close.Text = "Create User Account"
    $FormObject_Button_Close.Add_Click({$FormObjectA.Close()})
    $FormObjectA.Controls.Add($FormObject_Button_Close)

$FormObjectA.Add_Shown({$FormObjectA.Activate()})
[Void] $FormObjectA.ShowDialog()

$NewUser = [ordered]@{FirstName=($FormObject_FName).text;LastName=($FormObject_LName).Text;Username=($FormObject_Username).text;JobTitle=($FormObject_JobTitle).Text;}
Return $NewUser

```